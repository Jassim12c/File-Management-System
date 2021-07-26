import string
import tkinter as tk

from tkinter import filedialog
from ctypes import windll
from PIL import ImageTk, Image


def get_drives() -> list:
    """ This function gets all the drives on this device """
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives


# TODO: add back button
# TODO: add breadcrumbs
# TODO: add minor instructions

class FileManagerInterface:

    def __init__(self, master):
        self.master = master
        self.mainframe = tk.Frame(self.master, background="black")
        self.mainframe.pack(fill=tk.BOTH, expand=True)

        # Calling Methods
        self.build_grid()
        self.build_banner()
        self.add_image()

        self.get_all_drives_buttons()
        self.build_instruction()
        self.create_drive_buttons()

    def build_grid(self):
        """Builds the essential grid"""
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=2)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.rowconfigure(0, weight=2)
        self.mainframe.rowconfigure(1, weight=2)

    def add_image(self):
        """Opening, rendering and displaying logo"""
        open_image = Image.open('logo_file.png')
        open_image = open_image.resize((20, 40), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(open_image)
        img = tk.Label(self.mainframe, image=render, bg="black")
        img.image = render
        img.grid(row=0, column=0, sticky="nw")

    def build_banner(self):
        """Builds banner logo_file.png"""
        banner = tk.Label(
            self.mainframe,
            text="File Management",
            bg="black",
            fg="white",
            font=("Courier", 24, "bold")
        )
        banner.grid(
            row=0, column=1,
            padx=10, pady=10,
        )

    # TODO: Move the user inside the drive when they choose the drive
    def get_all_drives_buttons(self):
        """Gets all drives on the device and creates buttons for each one"""

        drive_dict = {}

        for drive in get_drives():
            drive_button = tk.Button(
                self.mainframe,
                text=drive,
                bg="black",
                fg="white",
                font=('Helvetica', 18, 'bold'),
            )

            drive_dict[drive] = drive_button

        return drive_dict

    def create_drive_buttons(self):
        """Puts each drive in its respective row and assigns the button command property to drive_btn_click()"""
        drive_dict = self.get_all_drives_buttons()

        row = 0
        for key, value in drive_dict.items():
            row += 1
            self.mainframe.rowconfigure(row, weight=1)
            btn = drive_dict[key]
            btn['command'] = lambda k=key: self.drive_btn_click(k)
            btn.grid(
                row=row, column=1,
                padx=10, pady=10,
            )

    def drive_btn_click(self, key_id):
        """Navigates inside the clicked on drive and opens a new window"""
        if key_id in get_drives():
            self.master.destroy()
            self.master = tk.Tk()
            self.app = InsideDrive(self.master)
            self.master.mainloop()

    def build_instruction(self):
        """Instructions for using the software"""
        instruction = tk.Label(
            self.mainframe,
            text="* Choose one of the drives:",
            fg="linen",
            bg="black",
            font=('Times', 13, "italic")
        )

        instruction.grid(
            row=1, column=0,
            sticky="N",
        )

class InsideDrive(FileManagerInterface):
    def __init__(self, master):
        super().__init__(master)

        self.get_all_drives_buttons()
        self.build_instruction()
        self.create_drive_buttons()

    # Override
    def get_all_drives_buttons(self):
        pass

    # Override
    def build_instruction(self):
        instruction = tk.Label(
            self.mainframe,
            text="* Choose one of the Operations then/or \n* Choose one of the files",
            fg="linen",
            bg="black",
            font=('Times', 13, "italic")
        )

        instruction.grid(
            row=1, column=0,
            sticky="N",
        )

    # Override 
    def create_drive_buttons(self):
        pass


if __name__ == "__main__":
    # Main Window
    root = tk.Tk()
    root.title("File Management")
    FileManagerInterface(root)
    root.mainloop()
