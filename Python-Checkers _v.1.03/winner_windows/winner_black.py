from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from constants.constants import VICTORY

BACKGROUND_COLOR = "black"


def winner_window_black():
    win = Tk()
    # Set the geometry and title of tkinter Main window
    win.geometry("750x350")

    def close_win():
        win.destroy()

    label_main = Label(
        win, text="Black WON", bg="black", fg="white", font=("Helvetica 15", 40)
    )
    label_main.pack(pady=20)
    win.configure(background=BACKGROUND_COLOR)
    img = PhotoImage(file=VICTORY)
    limg = Label(win, i=img).pack()

    win.title("Winner")
    win.mainloop()
