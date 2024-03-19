# from tkinter import *
# import sqlite3
# from tkinter import messagebox
# import re

# from PIL import ImageTk, Image



# # Connect to MySQL database
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root@1234",
#     database="citysanitizationdb"
# )

# # Create a cursor object to execute SQL queries
# cursor = db.cursor()

# # Create a table for the volunteers
# cursor.execute("CREATE TABLE IF NOT EXISTS volunteers ("
#                "id INT AUTO_INCREMENT PRIMARY KEY, "
#                "name VARCHAR(255), "
#                "email VARCHAR(255), "
#                "contact VARCHAR(15), "
#                "address VARCHAR(255), "
#                "city VARCHAR(50), "
#                "pincode INT(6), "
#                "education VARCHAR(255)"
#                ")")

# # Function to insert a new volunteer into the database
# def insert_volunteer(name, email, contact, address, city, pincode, education):
#     sql = "INSERT INTO volunteers (name, email, contact, address, city, pincode, education) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#     val = (name, email, contact, address, city, pincode, education)
#     cursor.execute(sql, val)
#     db.commit()

#     print(cursor.rowcount, "record inserted.")

# #GUI   
# win = Tk()
# win.geometry("1000x700")
# win.title("Apply as Volunteer")                        
# win["bg"] = "light blue"  

# frame = Frame(win, width=400, height=400)
# frame.pack()
# frame.place(x=0,y=130)

# image = Image.open("applyForSanitization.jpg")
 
# # Resize the image using resize() method
# resize_image = image.resize((400,700))
 
# img = ImageTk.PhotoImage(resize_image)
 
# # create label and add resize image
# label1 = Label(frame,image=img)
# label1.image = img
# label1.pack()
# label1.place(x=0,y=0)


       
# def checkemail(email):
#         if len(email)>7:
#                 if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
#                     return True
                    
                
#                 else:
#                     messagebox.showwarning("Alert","Invalid E-mail enter by user")
#                     return False
#         else:
#             messagebox.showwarning("Alert","Email length is too small")

# def validations():
#     if name.get() == "":
#         messagebox.showinfo("Alert","Enter your name first")
#     elif email.get() == "":
#         messagebox.showinfo("Alert","Enter Email")
#     elif not checkemail(email.get()):
#         pass
#     elif contact.get() == "" or len(contact.get())!=10:
#         messagebox.showinfo("Alert","Enter valid Contact ")
#     elif address.get() == "":
#         messagebox.showinfo("Alert","Enter Address")
#     elif city.get() == "": 
#         messagebox.showinfo("Alert","Enter your city ")
#     elif pincode.get() == 0:
#         messagebox.showinfo("Alert","Enter pincode")
#     elif education.get() == "":
#         messagebox.showinfo("Alert","Enter your education details")
#     else:
#         Name = name.get()
#         Email = email.get()
#         Contact = contact.get()
#         Address = address.get()
#         City = city.get()
#         Pincode = pincode.get()
#         Education = education.get()
#         insert_volunteer(Name, Email, Contact, Address, City, Pincode, Education)

#         messagebox.showinfo("Success", "You have successfully registered as a fulltime job Applicant!")

              
                                                               
         
# #creating data selection variable on gui
# name  = StringVar()
# address = StringVar()
# contact =StringVar()
# email = StringVar()
# city = StringVar()
# pincode = IntVar()
# education = StringVar()

# #Form Title
# label_title = Label(win,text ="Apply as a full time",width = 18,font = ("bold",20)).place(x=520,y=50)


# #Create fields
# label_name = Label(win,text = "Name:",width = 15,bg='light blue',font='bold').place(x = 490,y = 130)
# entry_name = Entry(win,width = 25,textvariable = name)
# entry_name.place(x = 670,y = 130)

# label_email = Label(win,text = "Email:",width = 15,bg='light blue',font='bold').place(x = 490,y = 180)
# entry_email = Entry(win,textvariable =email,width = 25)
# entry_email.place(x = 670,y = 180)


# label_contact = Label(win,text ="Contact no:",width = 15,bg='light blue',font='bold').place(x = 490,y = 230)
# entry_contact = Entry(win,textvariable = contact,width = 25)
# entry_contact.place(x = 670,y = 230)


# label_address = Label(win,text ="Address:",width = 15,bg='light blue',font='bold').place(x = 490,y = 280)
# entry_address = Entry(win,textvariable = address,width = 25)
# entry_address.place(x = 670,y = 280)

# label_city = Label(win,text = "City:",width = 15,bg='light blue',font='bold').place(x = 490,y = 330)
# entry_city = Entry(win,textvariable = city,width = 25)
# entry_city.place(x = 670,y = 330)

# label_pincode = Label(win,text = "Pincode:",width = 15,bg='light blue',font='bold').place(x = 490,y = 380)
# entry_pincode = Entry(win,textvariable = pincode,width = 25)
# entry_pincode.place(x = 670,y = 380)

# label_education = Label(win,text = "Education:",width = 15,bg='light blue',font='bold').place(x = 490,y = 430)
# entry_education = Entry(win,textvariable = education,width = 25)
# entry_education.place(x = 670,y = 430)



# Button(win, text='Submit',width=10,bg='light grey',fg='black',command  = validations).place(x=620,y=500)


# win.mainloop()




# from tkinter import *
# import sqlite3
# from tkinter import messagebox
# import re
# from tkinter.tix import IMAGETEXT

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

# Assume that 'volunteer_email' is the email provided by the volunteer during registration
# 'msg' is the message you want to send to the volunteer
# 'subject' is the subject of the email you want to send

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
# GUI

win = Tk()
win.geometry("1000x700")
win.title("Apply Full-Time")
win["bg"] = "light blue"

frame = Frame(win, width=400, height=700)
frame.pack()
frame.place(x=0, y=0)


image = Image.open("applyForSanitization.jpg")

# Resize the image using resize() method
resize_image = image.resize((400,700))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(frame,image=img)
label1.image = img
label1.pack()
label1.place(x=0,y=0)


def checkemail(email):
    if len(email) > 7:
        if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email):
            return True


        else:
            messagebox.showwarning("Alert", "Invalid E-mail enter by user")
            return False
    else:
        messagebox.showwarning("Alert", "Email length is too small")


# validate all field at submit time
def validations():
    x = y = 0
    if name.get() == "":
        messagebox.showinfo("Alert", "Enter your name first")
    elif email.get() == "":
        messagebox.showinfo("Alert", "Enter Email")
    elif contact.get() == "" or len(contact.get()) != 10:
        messagebox.showinfo("Alert", "Enter valid Contact ")
    elif address.get() == "":
        messagebox.showinfo("Alert", "Enter Address")
    elif city.get() == "":
        messagebox.showinfo("Alert", "Enter your city ")
    elif pincode.get() == 0:
        messagebox.showinfo("Alert", "Enter pincode")
    elif feasibletime.get() == "":
        messagebox.showinfo("Alert", "Enter your feasible time")
    elif pastexperience.get() == "":
        messagebox.showinfo("Alert", "Enter your past experience")
    elif salaryexpections.get() == "":
        messagebox.showinfo("Alert", "Enter your salary expections")
    checkemail(email.get())

    if (x == True) and (y == True):
        Name = name.get()
        Email = email.get()
        Contact = contact.get()
        Address = address.get()
        City = city.get()
        Pincode = pincode.get()
        FeasibleTime = feasibletime.get()
        PastExperience = pastexperience.get()
        SalaryExpections = salaryexpections.get()


# creating data selection variable on gui
name = StringVar()
address = StringVar()
contact = StringVar()
email = StringVar()
city = StringVar()
pincode = IntVar()
feasibletime = StringVar()
pastexperience = StringVar()
salaryexpections = StringVar()

# Form Title
label_title = Label(win, text="Apply For Full-Time Job", width=18, font=("bold", 20)).place(x=550, y=50)

# Create fields
label_name = Label(win, text="Name :", width=15).place(x=490, y=130)
entry_name = Entry(win, width=35, textvariable=name)
entry_name.place(x=670, y=130)

label_email = Label(win, text="Email :", width=15).place(x=490, y=180)
entry_email = Entry(win, textvariable=email, width=35)
entry_email.place(x=670, y=180)

label_contact = Label(win, text="Contact no :", width=15).place(x=490, y=230)
entry_contact = Entry(win, textvariable=contact, width=35)
entry_contact.place(x=670, y=230)

label_address = Label(win, text="Address :", width=15).place(x=490, y=280)
entry_address = Entry(win, textvariable=address, width=35)
entry_address.place(x=670, y=280)

label_city = Label(win, text="City :", width=15).place(x=490, y=330)
entry_city = Entry(win, textvariable=city, width=35)
entry_city.place(x=670, y=330)

label_pincode = Label(win, text="Pincode :", width=15).place(x=490, y=380)
entry_pincode = Entry(win, textvariable=pincode, width=35)
entry_pincode.place(x=670, y=380)

# label_feasibletime = Label(win,text = "Feasible Time :",width = 15).place(x = 490,y = 430)
# entry_feasibletime = Entry(win,textvariable = feasibletime,width = 35)
# entry_feasibletime.place(x = 670,y = 430)

label_pastexperience = Label(win, text="Past Experience :", width=15).place(x=490, y=430)
entry_pastexperience = Entry(win, textvariable=pastexperience, width=35)
entry_pastexperience.place(x=670, y=430)

label_salaryexpections = Label(win, text="Salary Expections :", width=15).place(x=490, y=480)
entry_salaryexpections = Entry(win, textvariable=salaryexpections, width=35)
entry_salaryexpections.place(x=670, y=480)

Button(win, text='Submit', width=10, bg='light grey', fg='black', command=validations).place(x=650, y=550)

win.mainloop()







