from tkinter import *
from tkinter import messagebox
import re


# GUI

win = Tk()
win.geometry("1000x700")
win.title("Contact Us")
win["bg"] = "light blue"

frame = Frame(win, width=1000, height=700)
frame.pack()
frame.place(x=0, y=0)


# image = Image.open("applyForSanitization.jpg")

# Resize the image using resize() method
# resize_image = image.resize((400,700))

# img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
# label1 = Label(frame,image=img)
# label1.image = img
# label1.pack()
# label1.place(x=0,y=0)


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
    # elif message.get() == "" or len(message.get()) != 10:
    #     messagebox.showinfo("Alert", "Enter your message ")
    checkemail(email.get())

    if (x == True) and (y == True):
        Name = name.get()
        Email = email.get()
        # Message = message.get()


# creating data selection variable on gui
name = StringVar()
email = StringVar()
message = StringVar()

# Create fields
label_name = Label(win, text="Name :", width=15, font=("Arial", 12)).place(x=50, y=50)
entry_name = Entry(win, width=35, textvariable=name)
entry_name.place(x=150, y=50)

label_email = Label(win, text="Email :", width=15, font=("Arial", 12)).place(x=550, y=50)
entry_email = Entry(win, textvariable=email, width=35)
entry_email.place(x=670, y=50)

label_message = Label(win, text="Enter your message :", width=20, font=("Arial", 12)).place(x=400, y=230)
entry_message = Entry(win, textvariable=message, width=90)
entry_message.place(x=230, y=270)

def go_to_next_page():
    win.destroy()
    import main
Button(win, text='Submit', width=10, bg='light grey', fg='black', command=go_to_next_page).place(x=460, y=550)


def go_to_next_page():
    win.destroy()
    import aboutus
Button(win, text='Back', width=10, bg='light grey', fg='black', command=go_to_next_page).place(x=260, y=550)

win.mainloop()
