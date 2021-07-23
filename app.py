import string
import tkinter as tk

from ctypes import windll


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

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=2)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.rowconfigure(0, weight=2)

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

        for driver in get_drives():
            row += 1

            self.mainframe.rowconfigure(row, weight=1)

            text = tk.Button(
                self.mainframe,
                text=driver,
                bg="black",
                fg="white",
                font=('Helvetica', 18, 'bold'),
                command=self.choose_drive,
            )

            text.grid(
                row=row, column=1,
                padx=10, pady=10,
            )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Management")
    root.resizable(False, False)
    FileManagerInterface(root)
    root.mainloop()
