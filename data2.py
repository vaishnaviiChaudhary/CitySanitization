import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("Why Sanitisation???")
window.geometry('2010x2000')

# top_frame = tkinter.Frame(window)
# top_frame = tkinter.Frame(bg="black")
# top_frame.place(x=200, y=100, width=800, height=500)

bottom_frame = tkinter.Frame(window)
bottom_frame = tkinter.Frame(bg="lightgreen")
bottom_frame.place(x=0, y=200, width=1800, height=1500)

img1= ImageTk.PhotoImage(file="cleaning-products.png")
# # l1 = Label(top_frame, image=img).pack(fill='x')
l1 = Label(window, image=img1).place(x=480, y=50)
#
img2= ImageTk.PhotoImage(file="hand-sanitizer.png")
# # l1 = Label(top_frame, image=img).pack(fill='x')
l1 = Label(window, image=img2).place(x=630, y=50)
#
img3= ImageTk.PhotoImage(file="basket.png")
# # l1 = Label(top_frame, image=img).pack(fill='x')
l1 = Label(window, image=img3).place(x=780, y=50)

def go_to_next_page():
    window.destroy()
    import main
back_btn = tkinter.Button(window, text="Back", bg="#0B2447", fg="white", font=("Helvetica", 12, "bold"), cursor="hand2", height=1, width=7, command=go_to_next_page)
back_btn.place(x=50, y=70)

# Create a Text widget and add some text
text = tkinter.Text(bottom_frame, wrap="word", font=("times", 20), bg="#EEEEEE", fg="black",width=100,height=18)

text.insert("2.0", "Sanitization products are products that are designed to kill or eliminate harmful bacteria, viruses, and other microorganisms that can cause disease or infection. These products are commonly used in homes, hospitals, schools, restaurants, and other public places to prevent the spread of infections. \n \n Sanitization products come in various forms, including liquids, sprays, wipes, and gels. Some common types of sanitization products include: \n \n \n Hand sanitizers: These are alcohol-based gels or sprays that are used to clean hands when soap and water are not available. \n Surface sanitizers: These are products used to clean and disinfect surfaces such as countertops, doorknobs, and other high-touch areas.\n Air sanitizers: These are products that are used to purify the air and remove harmful particles and microorganisms from indoor environments.\n \n Sanitization products typically contain active ingredients such as alcohol, hydrogen peroxide, or quaternary ammonium compounds, which work to kill or neutralize harmful microorganisms. It is important to use these products as directed, and to choose products that are effective against the specific microorganisms that you are trying to eliminate.")

text.place(x=50, y=35)

window.mainloop()