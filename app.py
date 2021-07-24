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
        self.build_drives_rows()
        self.build_instruction()
        self.add_image()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=2)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.rowconfigure(0, weight=2)
        self.mainframe.rowconfigure(1, weight=2)

    def add_image(self):
        open_image = Image.open('logo_file.png')
        open_image = open_image.resize((20, 40), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(open_image)
        img = tk.Label(self.mainframe, image=render, bg="black")
        img.image = render
        img.grid(row=0, column=0, sticky="nw")

    def build_banner(self):
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
    def choose_drive(self):
        pass

    def build_drives_rows(self):
        """Prints out all of the drives available"""

        row = 0

        for drive in get_drives():
            row += 1

            self.mainframe.rowconfigure(row, weight=1)

            text = tk.Button(
                self.mainframe,
                text=drive,
                bg="black",
                fg="white",
                font=('Helvetica', 18, 'bold'),
                command=self.choose_drive,
            )

            text.grid(
                row=row, column=1,
                padx=10, pady=10,
            )

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
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Management")
    FileManagerInterface(root)
    root.mainloop()
