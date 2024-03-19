#main page
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
from PIL import Image, ImageTk
import tkinter.font as font
from tkinter import ttk
import tkinter as tk

window = tkinter.Tk()
window.title("Sanitisation")
window.geometry('2010x2000')

top_frame = tkinter.Frame(window)
top_frame.pack(fill="both", expand=True)

yep_frame = tkinter.Frame(window)
# yep_frame = tkinter.Frame(bg="black")
yep_frame.place(x=400, y=100, width=700, height=800)

logo_frame = tkinter.Frame(window)
# logo_frame = tkinter.Frame(bg="black")
logo_frame.place(x=60, y=20, width=70, height=70)

text_frame = tkinter.Frame(window)
# text_frame = tkinter.Frame(bg="black")
text_frame.place(x=400, y=200, width=1000, height=700)

label1 = tkinter.Label(top_frame, text="Cleaner city, Brighter future ❤️", bg="#576CBC", fg="white", height=3, font=("Courier", 15, "bold"))
label1.pack(fill="x")
# label1.place(x=10, y=30)

def go_to_next_page():
    window.destroy()
    import jobOptions

# btn.bind() video stamp 21.17
btn2 = tkinter.Button(yep_frame, text="Apply for job", bg="#916BBF", fg="white", font=("Helvetica", 12, "bold"), height=3, width=20, command=go_to_next_page)
btn2.place(x=400, y=5)


label4 = tkinter.Label(top_frame, text="", bg="#576CBC", width=30, font=("Helvetica", 12, "bold"))
label4.pack(side="left", fill="y")

def open_new_page1(event):
    window.destroy()
    import data1

def open_new_page2(event):
    window.destroy()
    import data2

def open_new_page3(event):
    window.destroy()
    import data3

def open_new_page4(event):
    window.destroy()
    import AboutUs

def open_new_page5(event):
    import statistical_data

# Create a label widget
label1 = tk.Label(top_frame, text="Why Sanitisation?",font=("Helvetica", 12, "bold"), cursor="hand2", bg="#576CBC")
label2 = tk.Label(top_frame, text="What are Sanitation products?",font=("Helvetica", 12, "bold"), cursor="hand2", bg="#576CBC")
label3 = tk.Label(top_frame, text="Sanitation & Hygiene",font=("Helvetica", 12, "bold"), cursor="hand2", bg="#576CBC")
label4 = tk.Label(top_frame, text="About Us",font=("Helvetica", 12, "bold"), cursor="hand2", bg="#576CBC")
label5 = tk.Label(top_frame, text="Statistical Data",font=("Helvetica", 12, "bold"), cursor="hand2", bg="#576CBC")

def go_to_next_page1():
    window.destroy()
    import ContactUs

contact_btn = tkinter.Button(top_frame, text="Contact us", bg="#0B2447", fg="white", font=("Helvetica", 12, "bold"), cursor="hand2", height=1, width=15, command=go_to_next_page1)
contact_btn.place(x=50, y=550)


# Bind the label to the open_new_page function
label1.bind("<Button-1>", open_new_page1)
label2.bind("<Button-1>", open_new_page2)
label3.bind("<Button-1>", open_new_page3)
label4.bind("<Button-1>", open_new_page4)
label5.bind("<Button-1>", open_new_page5)

# Pack the label widget
label1.place(x=50, y=300)
label2.place(x=50, y=360)
label3.place(x=50, y=420)
label4.place(x=50, y=480)
label5.place(x=50, y=480)
logo_img = ImageTk.PhotoImage(file="logo.png")
l1 = Label(logo_frame, image=logo_img).pack()

def go_to_next_page2():
    window.destroy()
    import applyforsanitization

btn1 = tkinter.Button(yep_frame, text="Register for Sanitisation", bg="#916BBF", fg="white", height=3, width=20, font=("Helvetica", 12, "bold"), command=go_to_next_page2)
btn1.place(x=2, y=5)


heading = tkinter.Label(text_frame, text="Cleaning Schedule", font=("georgia", 20, "bold", "underline"), fg="black")
heading.pack()


#to display table from database
import tkinter as tk
from tkinter import ttk
import pandas as pd
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', 
                              password='root@1234',
                              host='localhost',
                              database='citysanitizationdb')
cursor = cnx.cursor()

# Define the SQL query
query = "SELECT * FROM sanitizationapply"

# Create the Tkinter window and table widget
# root = tk.Tk()
table = ttk.Treeview(text_frame)
text_frame.place(x=350, y=200, width=1100, height=2000)

# Execute the query and create a data frame
df = pd.read_sql(query, cnx)

# Insert the data into the table widget
table["columns"] = list(df.columns)
table["show"] = "headings"
for column in table["columns"]:
    table.heading(column, text=column)
for index, row in df.iterrows():
    table.insert("", "end", values=list(row))

# Pack the table widget and start the Tkinter event loop
table.pack()


window.mainloop()