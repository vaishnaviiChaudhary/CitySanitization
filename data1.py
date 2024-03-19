import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("Why Sanitisation???")
window.geometry('2010x2000')

top_frame = tkinter.Frame(window)
# top_frame = tkinter.Frame(bg="black")
top_frame.place(x=200, y=100, width=800, height=500)

bottom_frame = tkinter.Frame(window)
bottom_frame = tkinter.Frame(bg="skyblue")
bottom_frame.place(x=0, y=300, width=1800, height=1500)

img= ImageTk.PhotoImage(file="spray.png")
# l1 = Label(top_frame, image=img).pack(fill='x')
l1 = Label(window, image=img).place(x=580, y=3)

def go_to_next_page():
    window.destroy()
    import main

back_btn = tkinter.Button(window, text="back", bg="#0B2447", fg="white", font=("Helvetica", 12, "bold"), cursor="hand2", height=1, width=7, command=go_to_next_page)
back_btn.place(x=50, y=75)

# Create a Text widget and add some text
text = tkinter.Text(bottom_frame, wrap="word", font=("times", 15), bg="#EEEEEE", fg="black",width=142,height=20)
#text_widget = tk.Text(root, width=50, height=10)
text.insert("2.0", "City sanitization is an important process that involves cleaning and disinfecting public places and surfaces to prevent the spread of diseases and infections. Here are some reasons why city sanitization is necessary:\n\n\n1) Disease Prevention: Sanitizing cities helps prevent the spread of diseases, especially those that are easily transmitted through contact with contaminated surfaces. Sanitization can reduce the risk of diseases like COVID-19, flu, and other infections.\n\n2) Public Health: City sanitization is crucial for maintaining public health and safety. Regular cleaning and disinfecting of public spaces such as parks, streets, and public transportation can help prevent the spread of diseases and ensure that people are safe while moving around the city.\n\n3) Environmental Health: Sanitization of cities also helps in maintaining environmental health. Cleaning and disinfecting public spaces help reduce the amount of waste and pollutants that accumulate in the environment, thus reducing the risk of environmental contamination.\n\n4) Image of the City: A clean and well-sanitized city creates a positive image of the city and attracts more tourists and investors. It shows that the city takes public health and safety seriously, which is an essential factor for economic growth.\n\nOverall, city sanitization is a critical process that helps prevent the spread of diseases, ensures public health and safety, and maintains environmental health. Regular cleaning and disinfecting of public spaces are necessary to keep the city safe and healthy.")
text.place(x=50, y=35)

window.mainloop()