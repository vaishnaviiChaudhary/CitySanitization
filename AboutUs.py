import tkinter as tk

root = tk.Tk()
root.title("About Us")
root.geometry("1000x700")

# Company Name and Logo

about_us_text = ""

about_us_text_label = tk.Label(root, text=about_us_text, wraplength=400, justify="left")
about_us_text_label.pack(pady=10)

company_name_label = tk.Label(root, text="About Us")
company_name_label.config(font=("Arial", 24))
company_name_label.pack(pady=10)


about_us_text = ""

about_us_text_label = tk.Label(root, text=about_us_text, wraplength=400, justify="left")
about_us_text_label.pack(pady=10)

about_us_text = ""

about_us_text_label = tk.Label(root, text=about_us_text, wraplength=400, justify="left")
about_us_text_label.pack(pady=10)

about_us_text = ""

about_us_text_label = tk.Label(root, text=about_us_text, wraplength=400, justify="left")
about_us_text_label.pack(pady=10)


# About Us Text
about_us_label = tk.Label(root, text="In the critical phase of COVID-19; community transmission takes place. Hence, it is critical to sanitize public places that witness high number of footfalls (such as community/public toilets, parks, markets, tourist spots etc). Areas such as markets, which are accessible even during lockdown periods need to be sanitised during the lockdown period at regular intervals to contain the risk of further spreading the infection. In addition, common places where many people gather, such as cinema and marriage halls, cremation grounds, railway stations, bus stands, airports, restaurants and dining areas, art and other exhibition centres, conferences and commercial/market places and mandis; need to be sanitised regularly. Government has issued advisories to this effect which must be followed by all concerned establishments in the time to come.", wraplength=600, justify="left")
about_us_label.config(font=("Arial", 12))
about_us_label.pack(pady=10)

root.mainloop()
