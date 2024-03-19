from functools import partial
from tkinter import *
import mysql.connector
from tkinter import messagebox

# def validateLogin(username, password):
def validateLogin():
    # validate if username and password are entered
    
    # establish a database connection
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root@1234',
        database='citysanitizationdb'
    )
    # create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # execute a SQL query to select the user with the given username and password
    query = 'SELECT * FROM loginpage WHERE name = %s AND password = %s'
    cursor.execute(query, (username.get(), password.get()))
    # u_name = username.get()
    if not username.get() or not password.get():
        print("User not present")
        return messagebox.showerror('Error', 'Please enter both username and password')
    # fetch the result of the query
    result = cursor.fetchone()
    # close the database connection and cursor
    cursor.close()
    conn.close()
    # check if the result is None (i.e. no user was found)
    if result is None:
        messagebox.showerror('Error', 'Invalid username or password')
    else:
        messagebox.showinfo('Success', 'Login successful')
        return go_to_next_page()

# create the main window
tkWindow = Tk()  
tkWindow.geometry('925x500+300+200')  
tkWindow.configure(bg='white')
tkWindow.title('City Sanitization')

# create the frame to hold the image and other widgets
frame = Frame(tkWindow, width=800, height=400, bg='white')
frame.place(relx=0.5, rely=0.5, anchor="center")


# create the heading label
heading = Label(frame, text='Login',fg='#57a1f8',bg='white', font=('Microsoft JhengHei UI Light', 26, 'bold'))
heading.grid(row=1, column=1, pady=10)

# create the image label
img = PhotoImage(file='Loginpage.png')
img = img.subsample(2) # resize the image by half
image_label = Label(frame, image=img, bg='white')
image_label.grid(row=1, column=0, pady=10)

# create the username label and entry box
username_label = Label(frame, text="User Name",fg='#57a1f8',bg='white', font=('Microsoft JhengHei UI Light', 18))
username_label.grid(row=2, column=0, pady=10)
username = StringVar()
username_entry = Entry(frame, textvariable=username, font=('Microsoft JhengHei UI Light', 14))
username_entry.grid(row=2, column=1, pady=10)

# create the password label and entry box
password_label = Label(frame, text="Password",fg='#57a1f8',bg='white', font=('Microsoft JhengHei UI Light', 18))
password_label.grid(row=3, column=0, pady=10)
password = StringVar()
password_entry = Entry(frame, textvariable=password, show='*', font=('Microsoft JhengHei UI Light', 14))
password_entry.grid(row=3, column=1, pady=10)


def go_to_next_page():
    tkWindow.destroy()
    import main

# create the login button
login_button = Button(frame, text="Login",fg='#57a1f8',bg='white',command= validateLogin , font=('Microsoft JhengHei UI Light', 14))
login_button.grid(row=4, column=0, columnspan=2, pady=10)

# create the "don't have an account? Sign in" label and button

signup_label = Label(frame, text="Don't have an account?",fg="blue",bg='white', font=('Microsoft JhengHei UI Light',12))
signup_label.grid(row=5, column=0, pady=10)

def open_new_page1(event):
    tkWindow.destroy()
    import signinpage

signup_link = Label(frame, text="Sign in", fg="blue",bg='white', font=('Microsoft JhengHei UI Light',12))
signup_link.grid(row=5, column=1, pady=10)
signup_link.bind("<Button-1>", lambda e: print("Sign up button clicked!"))
signup_link.bind("<Button-1>", open_new_page1)


# pack the frame into the main window
frame.pack()


tkWindow.mainloop()
