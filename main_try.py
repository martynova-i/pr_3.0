from tkinter import *

import stt
import tts
import main_AI
import commands

splash_root = Tk()
splash_root.geometry("500x500")
splash_root.overrideredirect(True)
splash_root.eval('tk::PlaceWindow . center')

img = PhotoImage(file="images/friday.png")
Label(splash_root, image=img).pack()
switch_value = True


def main_window():
    splash_root.destroy()
    root = Tk()

    root.title("Пятница")
    root.geometry("500x700")
    root.eval('tk::PlaceWindow . center')

    root.config(bg="white")
    light = PhotoImage(file="images/ligth.png")
    dark = PhotoImage(file="images/dark.png")

    def toggle():
        global switch_value
        if switch_value == True:
            switch.config(image=dark, bg="#26242f",
                          activebackground="#26242f")

            root.config(bg="#26242f")
            switch_value = False
        else:
            switch.config(image=light, bg="white",
                          activebackground="white")

            root.config(bg="white")
            switch_value = True

    switch = Button(root, image=light,
                    bd=0, bg="white",
                    activebackground="white",
                    command=toggle)
    switch.place(x=10, y=2)

    root.mainloop()


splash_root.after(1000, main_window)

mainloop()
