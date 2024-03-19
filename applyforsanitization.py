import subprocess
from tkinter import *
import sqlite3
from tkinter import messagebox
import re
import tkinter as tk

from PIL import ImageTk, Image

import mysql.connector

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
cursor.execute("CREATE TABLE IF NOT EXISTS sanitizationapply ("
               "id INT AUTO_INCREMENT PRIMARY KEY, "
               "name VARCHAR(255), "
               "email VARCHAR(255), "
               "contact VARCHAR(15), "
               "address VARCHAR(255), "
               "city VARCHAR(50), "
               "pincode INT(6), "
               "concern VARCHAR(50)"
               ")")

# Function to insert a new volunteer into the database
def insert_sanitizationapply(name, email, contact, address, city, pincode, concern ):
    sql_Q = "INSERT INTO sanitizationapply (name, email, contact, address, city, pincode, concern) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val_Q = (name, email, contact, address, city, pincode, concern)
    cursor.execute(sql_Q, val_Q)
    db.commit()

    print(cursor.rowcount, "record inserted.")

#GUI
   
win = Tk()
win.geometry("1000x700")
win.title("Apply for Sanitization")                        
win["bg"] = "light blue"  

frame = Frame(win, width=400, height=400)
frame.pack()
frame.place(x=0,y=130)

image = Image.open("applyForSanitization.jpg")
 
# Resize the image using resize() method
resize_image = image.resize((400,400))
 
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


 #validate all field at submit time
def validations():
    x =y = 0
    if name.get() == "":
        messagebox.showinfo("Alert","Enter your name first")
    elif email.get() =="":
        messagebox.showinfo("Alert","Enter Email")
    elif contact.get() == "" or len(contact.get())!=10:
        messagebox.showinfo("Alert","Enter valid Contact ")
    elif address.get() =="" :
        messagebox.showinfo("Alert","Enter Address")
    elif city.get() == "": 
        messagebox.showinfo("Alert","Enter your city ")
    elif pincode.get() == 0:
        messagebox.showinfo("Alert","Enter pincode")
    elif concern.get() == "":
        messagebox.showinfo("Alert","Enter your concern")
        # checkemail(email.get())
    
   
    else:
        Name=name.get()
        Email=email.get()
        Contact=contact.get()
        Address=address.get()
        City=city.get()
        Pincode=pincode.get()
        Concern = concern.get()
        insert_sanitizationapply(Name,Email, Contact,Address, City, Pincode, Concern)
        
        messagebox.showinfo("Success", "You have successfully applied for sanitization in your area!")
              
                                                               
         
#creating data selection variable on gui
name  = StringVar()
email = StringVar()
contact =StringVar()
address = StringVar()
city = StringVar()
pincode = IntVar()
concern = StringVar()

#Form Title
label_title = Label(win,text ="Apply for Sanitization",fg='black',bg='light blue',width = 18,font = ("bold",20)).place(x=520,y=50)


#Create fields
label_name = Label(win,text = "Name :",fg='black',bg='light blue',width = 15).place(x = 490,y = 130)
entry_name = Entry(win,width = 25,textvariable = name)
entry_name.place(x = 670,y = 130)

label_email = Label(win,text = "Email :",fg='black',bg='light blue',width = 15).place(x = 490,y = 180)
entry_email = Entry(win,textvariable =email,width = 25)
entry_email.place(x = 670,y = 180)


label_contact = Label(win,text ="Contact no :",fg='black',bg='light blue',width = 15).place(x = 490,y = 230)
entry_contact = Entry(win,textvariable = contact,width = 25)
entry_contact.place(x = 670,y = 230)


label_address = Label(win,text ="address :",fg='black',bg='light blue',width = 15).place(x = 490,y = 280)
entry_address = Entry(win,textvariable = address,width = 25)
entry_address.place(x = 670,y = 280)

label_city = Label(win,text = "City :",fg='black',bg='light blue',width = 15).place(x = 490,y = 330)
entry_city = Entry(win,textvariable = city,width = 25)
entry_city.place(x = 670,y = 330)

label_pincode = Label(win,text = "Pincode :",fg='black',bg='light blue',width = 15).place(x = 490,y = 380)
entry_pincode = Entry(win,textvariable = pincode,width = 25)
entry_pincode.place(x = 670,y = 380)

label_concern = Label(win,text = "Concern :",fg='black',bg='light blue',width = 15).place(x = 490,y = 430)
entry_concern = Entry(win,textvariable = concern,width = 25)
entry_concern.place(x = 670,y = 430)

# def go_to_next_page():
#     win.destroy()
#     import main

# from tkinter import *
import subprocess

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
#     elif concern.get() == "":
#         messagebox.showinfo("Alert","Enter your concern")
#     else:
#         messagebox.showinfo("Form submitted successfully")

def Submit():
    # Call the script that notifies the selected volunteers
    subprocess.call(["python", "notify_selected_volunteers.py"])

def both_commands():
    validations()
    Submit()

Button(win, text='Submit',width=10,bg='light grey',fg='black', command=both_commands).place(x=520,y=500)

import tkinter as tk




# def validate_form():
#     name = entry_name.get()
#     email = entry_email.get()
#     phone = entry_contact.get()
#     phone = entry_city.get()
#     phone = entry_pincode.get()
#     phone = entry_concern.get()

#     if not name or not email or not phone:
#         # display error message if any required fields are empty
#         error_label.config(text="Please fill in all the required fields", fg="red")
#     else:
# print("Form submitted successfully")

    
# button = tk.Button(win, text="Execute both commands", command=both_commands)
# button.pack()


# Create a button or a menu item
# button = Button(frame, text="Notify Volunteers", command=Submit)
# button.pack()



def go_to_next_page():
    win.destroy()
    import main
Button(win, text='Back',width=10,bg='light grey',fg='black', command=go_to_next_page).place(x=750,y=500)

win.mainloop()


