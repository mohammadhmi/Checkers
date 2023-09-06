# Import tkinter library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


# Create an instance of tkinter frame
def winner_window_yellow():
    win = Tk()
    # Set the geometry and title of tkinter Main window
    win.geometry("750x350")

    def close_win():
        win.destroy()

    label_main = Label(win, text="Yellow WON", bg="gold", font=("Helvetica 15", 40))
    label_main.pack(pady=20)
    win.configure(background="gold")
    img = PhotoImage(file="assets/victory-resize.png")
    limg = Label(win, i=img).pack()

    win.title("Yellow_Winner")
    win.mainloop()


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
    win.configure(background="black")
    img = PhotoImage(file="assets/victory-resize.png")
    limg = Label(win, i=img).pack()

    win.title("Winner")
    win.mainloop()


winner_window_black()
winner_window_yellow()
