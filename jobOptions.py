import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.font as font

from PIL import Image, ImageTk


window = tkinter.Tk()
window.title("Sanitisation")
window.geometry('2010x2000')

right_frame = tkinter.Frame(window)
# right_frame = tkinter.Frame(bg="black")
right_frame.place(x=950, y=200, width=300, height=300)
left_img = ImageTk.PhotoImage(file="interview.png")
l1 = Label(window, image=left_img).place(x=150, y=100)


def go_to_next_page():
    window.destroy()
    import applyNonVolunteer

btn1 = tkinter.Button(right_frame, text="Non-Volunteer", bg="#916BBF", font=20, height=3, width=20,command=go_to_next_page)
btn1.place(x=2, y=1)

def go_to_next_page():
    window.destroy()
    import applyvolunteer
btn3 = tkinter.Button(right_frame, text="Volunteer", bg="#916BBF", font=20, height=3, width=20, command=go_to_next_page)
btn3.place(x=4, y=200)

def go_to_next_page():
    window.destroy()
    import main
back_btn = tkinter.Button(window, text="back", bg="#0B2447", fg="white", font=("Helvetica", 12, "bold"), cursor="hand2", height=1, width=5, command=go_to_next_page)
back_btn.place(x=50, y=50)


window.mainloop()
