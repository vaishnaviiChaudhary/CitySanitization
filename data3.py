import tkinter
from tkinter import *
from tkinter.tix import IMAGETEXT
from tkinter.ttk import *
import tkinter.font as font
import re
from PIL import Image, ImageTk


window = tkinter.Tk()
window.title("Why Sanitisation???")
window.geometry('2010x2000')

bottom_frame = tkinter.Frame(window)
bottom_frame = tkinter.Frame(bg="grey")
bottom_frame.place(x=0, y=250, width=1800, height=1500)

img2= ImageTk.PhotoImage(file="wash-face.png")
# l1 = Label(top_frame, image=img).pack(fill='x')
l1 = Label(window, image=img2).place(x=550, y=50)

img3= ImageTk.PhotoImage(file="safe.png")
# l1 = Label(top_frame, image=img).pack(fill='x')
l1 = Label(window, image=img3).place(x=700, y=50)

def go_to_next_page():
    window.destroy()
    import main

back_btn = tkinter.Button(window, text="back", bg="#0B2447", fg="white", font=("Helvetica", 12, "bold"), cursor="hand2", height=1, width=7, command=go_to_next_page)
back_btn.place(x=50, y=90)

# Create a Text widget and add some text
text = tkinter.Text(bottom_frame, wrap="word", font=("times", 20), bg="#EEEEEE", fg="black",width=100,height=16)
text.insert("2.0", "Sanitation and hygiene are critical to health, survival, and development. Many countries face challenges in providing adequate sanitation for their entire populations, leaving people at risk for diseases related to water, sanitation, and hygiene. Throughout the world, an estimated 1.7 billion people lack basic sanitation (about 21% of the world’s population).1, 2 Basic sanitation is defined as having access to facilities for the safe disposal of human waste (feces and urine), as well as having the ability to maintain hygienic conditions, through services such as garbage collection, industrial/hazardous waste management, and wastewater treatment and disposal. Around 2.3 billion people (about 29%) lack access to basic hygiene, which includes access to a handwashing station with soap and water at home.\n The world did not achieve the United Nations’ Millennium Development Goal (MDG) sanitation target to halve the proportion of people without sustainable access to basic sanitation by 2015. Now, the United Nations’ Sustainable Development goal (SDG) is for everyone to have “adequate and equitable” sanitation and basic hygiene for all by 2030.")

text.place(x=50, y=35)
window.mainloop()
