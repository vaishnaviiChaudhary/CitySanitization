import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
import re
from tkinter.tix import IMAGETEXT

from PIL import ImageTk, Image
from PIL import Image


import mysql.connector
import smtplib
from email.mime.text import MIMEText


msg = "Hello, you have successfully registered for our event!\n regards\n CleanHire"

subject = "Registration Confirmation"

# Create the message object and set the message and subject
message = MIMEText(msg)
message['Subject'] = subject

# Set the sender and recipient of the email
sender = "CleanHire04@gmail.com"
recipient = "kanak.pendse14@gmail.com"

# Connect to the SMTP server and send the message
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login("CleanHire04@gmail.com", "fsewlzhnbjyhbixz")
    server.sendmail(sender, recipient, message.as_string())

print("Email sent successfully!")

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@1234",
    database="citysanitizationdb"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Create a table for the volunteers
cursor.execute("CREATE TABLE IF NOT EXISTS volunteers ("
               "id INT AUTO_INCREMENT PRIMARY KEY, "
               "name VARCHAR(255), "
               "email VARCHAR(255), "
               "contact VARCHAR(15), "
               "address VARCHAR(255), "
               "city VARCHAR(50), "
               "pincode INT(6), "
               "education VARCHAR(255),"
               "age VARCHAR(45)"
               ")")

# Function to insert a new volunteer into the database
def insert_volunteer(name, email, contact, address, city, pincode, education, age):
    sql = "INSERT INTO volunteers (name, email, contact, address, city, pincode, education, age) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
    val = (name, email, contact, address, city, pincode, education,age)
    cursor.execute(sql, val)
    db.commit()

    print(cursor.rowcount, "record inserted.")


# GUI
win = Tk()
win.geometry("2010x2000")
win.title("Apply As a non-volunteer")
win["bg"] = "light blue"

frame = Frame(win, width=700, height=2000)
frame.pack()
frame.place(x=0, y=0)


image = Image.open("applyForSanitization.jpg")

# Resize the image using resize() method
resize_image = image.resize((700,900))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(frame,image=img)
label1.image = img
label1.pack()
label1.place(x=0,y=0)


def checkemail(email):
        if len(email)>7:
                if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                    return True
                    
                
                else:
                    messagebox.showwarning("Alert","Invalid E-mail enter by user")
                    return False
        else:
            messagebox.showwarning("Alert","Email length is too small")

def validations():
    if name.get() == "":
        messagebox.showinfo("Alert","Enter your name first")
    elif email.get() == "":
        messagebox.showinfo("Alert","Enter Email")
    elif not checkemail(email.get()):
        pass
    elif contact.get() == "" or len(contact.get())!=10:
        messagebox.showinfo("Alert","Enter valid Contact ")
    elif address.get() == "":
        messagebox.showinfo("Alert","Enter Address")
    elif city.get() == "": 
        messagebox.showinfo("Alert","Enter your city ")
    elif pincode.get() == 0:
        messagebox.showinfo("Alert","Enter pincode")
    elif education.get() == "":
        messagebox.showinfo("Alert","Enter your education details")
    # elif Age.get() == "":
    #     messagebox.showinfo("Alart,Enter your correct age")
    elif int(Age.get()) <= 17:
        messagebox.showerror("Error", "You must be over 18 years old to apply as a volunteer")
    else:
        Name = name.get()
        Email = email.get()
        Contact = contact.get()
        Address = address.get()
        City = city.get()
        Pincode = pincode.get()
        Education = education.get()
        age = Age.get()

        insert_volunteer(Name, Email, Contact, Address, City, Pincode, Education, age)

        msg = "Hello, you have successfully registered for our event!\n regards\n CleanHire"

        subject = "Registration Confirmation"

        # Create the message object and set the message and subject
        message = MIMEText(msg)
        message['Subject'] = subject

        # Set the sender and recipient of the email
        sender = "CleanHire04@gmail.com"
        recipient = Email

        # Connect to the SMTP server and send the message
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login("CleanHire04@gmail.com", "fsewlzhnbjyhbixz")
            server.sendmail(sender, recipient, message.as_string())

        print("Email sent successfully!")


        messagebox.showinfo("Success", "You have successfully registered as a volunteer!")


# creating data selection variable on gui
name = StringVar()
address = StringVar()
contact = StringVar()
email = StringVar()
city = StringVar()
pincode = IntVar()
education = StringVar()
Age = StringVar()

# Form Title
label_title = Label(win, text="Apply As Non-Volunteer", width=18,background='light blue', font=("bold", 30)).place(x=850, y=50)

#Create fields
label_name = Label(win,text = "Name:",width = 15,bg='light blue',font=('bold',20)).place(x = 775,y = 130)
entry_name = Entry(win,width = 30,textvariable = name)
entry_name.place(x = 1000,y = 140)

label_email = Label(win,text = "Email:",width = 15,bg='light blue',font=('bold',20)).place(x = 800,y = 180)
entry_email = Entry(win,textvariable =email,width = 30)
entry_email.place(x = 1000,y = 190)


label_contact = Label(win,text =" Contact no:",width = 15,bg='light blue',font=('bold',20)).place(x = 800,y = 230)
entry_contact = Entry(win,textvariable = contact,width = 30)
entry_contact.place(x = 1000,y = 240)


label_address = Label(win,text ="Address:",width = 15,bg='light blue',font=('bold',20)).place(x = 800,y = 280)
entry_address = Entry(win,textvariable = address,width = 30)
entry_address.place(x = 1000,y = 290)

label_city = Label(win,text = "City:",width = 15,bg='light blue',font=('bold',20)).place(x = 800,y = 330)
entry_city = Entry(win,textvariable = city,width = 30)
entry_city.place(x = 1000,y = 340)

label_pincode = Label(win,text = "Pincode:",width = 15,bg='light blue',font=('bold',20)).place(x = 800,y = 380)
entry_pincode = Entry(win,textvariable = pincode,width = 30)
entry_pincode.place(x = 1000,y = 390)

label_education = Label(win,text = "Education:",width = 15,bg='light blue',font=('bold',20)).place(x = 800,y = 430)
entry_education = Entry(win,textvariable = education,width = 30)
entry_education.place(x = 1000,y = 440)


label_age = Label(win,text = "Age:",width = 15,bg='light blue',font=('bold',20)).place(x = 800,y = 480)
entry_age = Entry(win,textvariable = Age ,width = 30)
entry_age.place(x = 1000,y = 490)

def go_to_next_page():
    win.destroy()
    import main
Button(win, text='Submit',width=10,bg='light grey',fg='black', command= validations).place(x=800,y=600)

def go_to_next_page():
    win.destroy()
    import jobOptions
Button(win, text='Back',width=10,bg='light grey',fg='black', command= go_to_next_page).place(x=1000,y=600)
win.mainloop()







