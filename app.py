import string
import tkinter as tk
import os

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


# TODO: add breadcrumbs
# TODO: add minor instructions
# TODO: add CRUD + Move operations
# TODO: When user clicks on a drive,
#  open the file explorer.
#  Let them choose the file.
#  Then using the app they can choose the operation

class FileManagerInterface:

    def __init__(self, master):
        self.row = 0
        self.check_click = 1
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
        self.build_desktop_btn()

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

    # TODO: print all the files and operations
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

        for key, value in drive_dict.items():
            self.row += 1
            self.mainframe.rowconfigure(self.row, weight=1)
            btn = drive_dict[key]
            btn['command'] = lambda k=key: self.drive_btn_click(k)
            btn.grid(
                row=self.row, column=1,
                padx=10, pady=10,
            )

    def drive_btn_click(self, key_id):
        """Navigates inside the clicked on drive and opens a new window"""
        if key_id in get_drives():
            print(os.listdir("{}:/".format(key_id)))
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

    def build_desktop_btn(self):
        """Shortcut to desktop button"""
        desktop_btn = tk.Button(
            self.mainframe,
            text="Desktop",
            fg="tomato2",
            bg="black",
            font=('Roman', 15, "bold"),
            command=self.desktop_command
        )

        desktop_btn.grid(
            row=self.row + 1, column=0,
        )

    # TODO: CRUD operations and Moving files when clicked on
    def desktop_command(self):
        """Opens a file of choice from the user's desktop"""
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.file = tk.filedialog.askopenfile(initialdir=desktop, title="Select file", filetypes=(
            ('all files', '*.*'),
        ))
        self.master.destroy()
        self.master = tk.Tk()
<<<<<<< HEAD
        self.app = CRUDOperations(self.master, self.file.name)
        self.master.mainloop()
=======
        self.app = OpenedFile(self.master, file)
        self.master.mainloop()

>>>>>>> 82b6712ac0da262f9339640fcda357cc564643bc

class InsideDrive(FileManagerInterface):
    def __init__(self, master):
        super().__init__(master)

        self.get_all_drives_buttons()
        self.build_instruction()
        self.create_drive_buttons()
        self.create_back_button()

    # Override
    def get_all_drives_buttons(self):
        pass

    # Override
    def build_instruction(self):
        """Overrides the previous instructions and updates them to fit the current window's criteria"""
        instruction = tk.Label(
            self.mainframe,
            text=" * Choose a file \n* Choose one of the Operations",
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

    def create_back_button(self):
        """Creates back button design"""
        back_button = tk.Button(
            self.mainframe,
            text="Back",
            bg="black",
            fg="white",
            font=('Helvetica', 12, 'bold'),
            command=self.back_logic_button,
        )

        back_button.grid(
            row=0, column=0,
        )

    def back_logic_button(self):
        """Goes back to the main Window"""
        self.master.destroy()
        self.master = tk.Tk()
        self.app = FileManagerInterface(self.master)
        self.master.mainloop()


<<<<<<< HEAD
class CRUDOperations(FileManagerInterface):
    def __init__(self, master, main_file):
        super().__init__(master)
        print(main_file)
=======
class OpenedFile(FileManagerInterface):
    def __init__(self, master, file):
        super().__init__(master)
        self.file = file

        self.print_file()
        self.create_back_button()

        # Override
        self.get_all_drives_buttons()
        self.build_instruction()
        self.create_drive_buttons()

    # Override
    def build_desktop_btn(self):
        pass
>>>>>>> 82b6712ac0da262f9339640fcda357cc564643bc

    # Override
    def get_all_drives_buttons(self):
        pass

    # Override
    def build_instruction(self):
        """Overrides the previous instructions and updates them to fit the current window's criteria"""
        instruction = tk.Label(
            self.mainframe,
            text="* Choose one of the Operations",
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

<<<<<<< HEAD
    def build_desktop_btn(self):
        pass

    def desktop_command(self):
        pass
=======
    def create_back_button(self):
        back_button = tk.Button(
            self.mainframe,
            text="Back",
            bg="black",
            fg="white",
            font=('Helvetica', 12, 'bold'),
            command=self.back_logic_button,
        )

        back_button.grid(
            row=0, column=0,
        )

    def print_file(self):
        file_label = tk.Label(
            self.mainframe,
            text=self.file.name,
            fg="MistyRose4",
            bg="black",
            font=('Copperplate Gothic Light', 12),
        )

        file_label.grid(
            row=1, column=2,
        )

    def back_logic_button(self):
        """Command: Goes back to the main Window"""
        self.master.destroy()
        self.master = tk.Tk()
        self.app = FileManagerInterface(self.master)
        self.master.mainloop()
>>>>>>> 82b6712ac0da262f9339640fcda357cc564643bc


if __name__ == "__main__":
    # Main Window
    root = tk.Tk()
    root.title("File Management")
    FileManagerInterface(root)
    root.mainloop()
