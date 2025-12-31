# from tkinter import *
# from Login_Window import open_login
# from Signup_Window import open_signup

# def login():
#     f_window.destroy() 
#     open_login()

# def signup():
#     f_window.destroy()
#     open_signup()

# bg_color = "#D3D3D3"
# fg_color = "#0026FF"

# f_window = Tk()
# f_window.title("Hospital System")
# screen_width = f_window.winfo_screenwidth()
# screen_height = f_window.winfo_screenheight()
# f_window.geometry(f"{screen_width}x{screen_height}+0+0")
# f_window.state("zoomed")
# f_window.configure(bg= bg_color)

# f_frame = Frame(f_window,
#                 bg=bg_color
#                 )
# f_frame.place(relx=0.5, rely=0.5, anchor="center")


# login_button = Button(f_frame,                 
#                 text="LOG IN Page",                       
#                 font=('times new roman',50,'bold'),      
#                 fg="#ffffff",                        
#                 bg=fg_color,                           
#                 command=login
#                 )
# login_button.grid(row=1, column=0, pady=30, padx= 30)

# signup_button = Button(f_frame,                 
#                 text="SIGN UP Page",                       
#                 font=('times new roman',50,'bold'),      
#                 fg="#ffffff",                        
#                 bg=fg_color,                           
#                 command=signup
#                 )
# signup_button.grid(row=1, column=1, pady=30, padx=30)


# f_window.mainloop()



from tkinter import *
from Login_Window import open_login
from Signup_Window import open_signup

def login():
    f_window.destroy() 
    open_login()

def signup():
    f_window.destroy()
    open_signup()

# Color Palette
bg_color = "#F0F2F5"    # Softer light grey
fg_color = "#0026FF"    # Hospital Blue
accent_color = "#FFFFFF" # White

f_window = Tk()
f_window.title("Hospital Management System")
f_window.state("zoomed")
f_window.configure(bg=bg_color)

# 1. Background Title Section
header_frame = Frame(f_window, bg=fg_color, height=150)
header_frame.pack(fill=X)

Label(header_frame, 
      text="HOSPITAL MANAGEMENT SYSTEM", 
      font=('times new roman', 40, 'bold'), 
      bg=fg_color, 
      fg="white", 
      pady=30).pack()

# 2. Central Portal Container
# This creates a "Card" look in the middle of the screen
main_container = LabelFrame(f_window, 
                            text=" Welcome to the Portal ", 
                            font=("times new roman", 15, "italic"),
                            bg=accent_color, 
                            relief="solid", 
                            borderwidth=1,
                            padx=50, 
                            pady=50)
main_container.place(relx=0.5, rely=0.55, anchor="center")

# Adding a simple medical symbol placeholder
Label(main_container, text="✚", font=("times new roman", 60), fg=fg_color, bg=accent_color).pack(pady=(0, 20))

Label(main_container, 
      text="Please select an option to proceed", 
      font=("times new roman", 18), 
      bg=accent_color, 
      fg="#555555").pack(pady=(0, 30))

# 3. Button Sub-Frame for better alignment
button_frame = Frame(main_container, bg=accent_color)
button_frame.pack()

# Login Button
login_button = Button(button_frame, 
                      text="LOG IN", 
                      font=('times new roman', 25, 'bold'), 
                      fg="white", 
                      bg=fg_color, 
                      width=15, 
                      height=2,
                      cursor="hand2",
                      relief="flat",
                      command=login)
login_button.grid(row=0, column=0, padx=20)

# Sign Up Button
signup_button = Button(button_frame, 
                       text="SIGN UP", 
                       font=('times new roman', 25, 'bold'), 
                       fg=fg_color, 
                       bg="white", 
                       width=15, 
                       height=2,
                       cursor="hand2",
                       relief="solid",
                       borderwidth=2,
                       command=signup)
signup_button.grid(row=0, column=1, padx=20)

# 4. Footer
Label(f_window, 
      text="© 2025 Hospital Management Group | Secure Access Only", 
      font=("times new roman", 12), 
      bg=bg_color, 
      fg="#777777").pack(side=BOTTOM, pady=20)

f_window.mainloop()