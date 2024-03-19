
import tkinter as tk
from tkinter import *
import re
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root@1234",
 database="citysanitizationdb"
)

mycursor = mydb.cursor()

# Reconnect to the server if the connection is lost
def reconnect():
    global mydb
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root@1234",
      database="citysanitizationdb"
    )
    mycursor = mydb.cursor()

# create the main window
tkWindow = tk.Tk()  
tkWindow.geometry('850x450')  
tkWindow.configure(bg='#154c79')
tkWindow.title('City Sanitization')

frame2 = tk.Frame(tkWindow,width=700,height=300,bg='white')
frame2.place(x=75,y=75)

image = Image.open("signUp.png")

# Resize the image using resize() method
resize_image = image.resize((300,300))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(frame2,image=img)
label1.image = img
label1.pack()
label1.place(x=0,y=0)

label_title = Label(frame2,text ="Register now !",fg='black',bg='white',width = 12,font = ("bold",20)).place(x=420,y=10)

def checkpassword(password):
    if len(password)>=5:
        print(password)
        if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])", password):
            return True
        else:
            messagebox.showwarning("Invalid","Enter valid password")
            return False
    else:
        messagebox.showwarning("Invalid","Length try to exceed")
        return False

def checkemail(email):
    if len(email)>7:
        if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
            return True
        else:
            messagebox.showwarning("Alert","Invalid E-mail enter by user")
            return False
    else:
        messagebox.showwarning("Alert","Email length is too small")

def register():
    x =y = 0
    print(password.get())
    if name.get() == "":
        messagebox.showinfo("Alert","Enter your name first")
    elif email.get() =="":
        messagebox.showinfo("Alert","Enter Email")
    elif password.get() == "" or len(password.get())<=5:
        messagebox.showinfo("Alert","Enter valid Hello Password ")
    else:
        # Validate email and password
        x = checkemail(email.get())
        y = checkpassword(password.get())

        # If both email and password are valid, register the user
        if (x == True) and (y == True):
            Name = name.get()
            Password = password.get()
            Email = email.get()

            # Check if 'id' column already has a primary key constraint
            mycursor.execute("""
                SELECT COUNT(*)
                FROM information_schema.KEY_COLUMN_USAGE
                WHERE
                    TABLE_SCHEMA = 'citysanitizationdb' AND
                    TABLE_NAME = 'loginpage' AND
                    COLUMN_NAME = 'id' AND
                    CONSTRAINT_NAME = 'PRIMARY'
            """)
            result = mycursor.fetchone()[0]

            # If 'id' doesn't already have a primary key constraint, add one
            if result == 0:
                mycursor.execute("ALTER TABLE loginpage MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL")
                mydb.commit()
                

            # Insert the user's information into the database
            sql = "INSERT INTO loginpage (name, password, email) VALUES (%s, %s, %s)"
            val = (Name, Password, Email)
            mycursor.execute(sql, val)
            mydb.commit()

            # Display a message box to indicate successful registration
            messagebox.showinfo("Registration Successful", "Your registration has been completed successfully!")



label_title = Label(frame2,text ="Register now !",fg='black',bg='white',width = 12,font = ("bold",20)).place(x=420,y=10)


name = StringVar()
label_name = Label(frame2,text = "Name :",fg='black',bg='white',width = 10).place(x = 400,y = 80)
entry_name = Entry(frame2,width = 20,textvariable = name)
entry_name.place(x = 500,y = 80)

password = StringVar()
label_password = Label(frame2,text = "Password :",fg='black',bg='white',width = 10).place(x = 400,y = 120)
entry_password = Entry(frame2,width = 20,textvariable = password,show="*")
entry_password.place(x = 500,y = 120)

email = StringVar()
label_email = Label(frame2,text = "Email :",fg='black',bg='white',width = 10).place(x = 400,y = 160)
entry_email = Entry(frame2,width = 20,textvariable = email)
entry_email.place(x = 500,y = 160)




Button(tkWindow, text='Register',width=10,bg='light grey',fg='black',command  = register).place(x=580,y=320)

tkWindow.mainloop()

# Close the database connection
#mycursor.close()
#mydb.close()




