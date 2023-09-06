from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from constants.constants import VICTORY

BACKGROUND_COLOR = "gold"


def winner_window_yellow():
    win = Tk()
    # Set the geometry and title of tkinter Main window
    win.geometry("750x350")

    def close_win():
        win.destroy()

    label_main = Label(
        win, text="Yellow WON", bg=BACKGROUND_COLOR, font=("Helvetica 15", 40)
    )
    label_main.pack(pady=20)
    win.configure(background=BACKGROUND_COLOR)
    img = PhotoImage(file=VICTORY)
    limg = Label(win, i=img).pack()

    win.title("Yellow_Winner")
    win.mainloop()
