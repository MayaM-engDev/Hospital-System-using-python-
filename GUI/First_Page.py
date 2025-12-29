from tkinter import *

count = 0
def login():
    f_window.destroy()
    import Login_Window_GUI

def signup():
    f_window.destroy()
    import Signup_Window_GUI

bg_color = "#D3D3D3"
fg_color = "#0026FF"

f_window = Tk()
f_window.title("Hospital System")
screen_width = f_window.winfo_screenwidth()
screen_height = f_window.winfo_screenheight()
f_window.geometry(f"{screen_width}x{screen_height}+0+0")
f_window.state("zoomed")
f_window.configure(bg= bg_color)

f_frame = Frame(f_window,
                bg=bg_color
                )
f_frame.place(relx=0.5, rely=0.5, anchor="center")


login_button = Button(f_frame,                 
                text="LOG IN Page",                       
                font=('times new roman',50,'bold'),      
                fg="#ffffff",                        
                bg=fg_color,                           
                command=login
                )
login_button.grid(row=1, column=0, pady=30, padx= 30)

signup_button = Button(f_frame,                 
                text="SIGN UP Page",                       
                font=('times new roman',50,'bold'),      
                fg="#ffffff",                        
                bg=fg_color,                           
                command=signup
                )
signup_button.grid(row=1, column=1, pady=30, padx=30)


# display window
f_window.mainloop()