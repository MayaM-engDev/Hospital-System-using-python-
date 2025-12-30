from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from patient import Patient

bg_color = "#D3D3D3"
fg_color = "#0026FF"

signup_window = Tk()
signup_window.title("Sign-Up Page")
screen_width = signup_window.winfo_screenwidth()
screen_height = signup_window.winfo_screenheight()
signup_window.geometry(f"{screen_width}x{screen_height}+0+0")
signup_window.state("zoomed")
signup_window.configure(bg= bg_color)

def staff_signup(name_entry, age_entry, gender_entry, username_entry, password_entry):
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    # current_patient = Patient.signup(username, password)
    # if current_patient == None:
    #     messagebox.showerror(title="signup Failed",
    #                          message="❌ Invalid username or password"
    #                          )
    # else:
    #     messagebox.showinfo(title="signup Success",
    #                         message="✔ signup successful!"
    #                         )
    messagebox.showerror(title="Staff",
                         message="❌ Staff"
                        )
def doctor_signup(name_entry, age_entry, gender_entry, username_entry, password_entry):
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    # current_patient = Patient.signup(username, password)
    # if current_patient == None:
    #     messagebox.showerror(title="signup Failed",
    #                          message="❌ Invalid username or password"
    #                          )
    # else:
    #     messagebox.showinfo(title="signup Success",
    #                         message="✔ signup successful!"
    #                         )
    messagebox.showerror(title="Doctor",
                         message="❌ Doctor"
                        )
        

def patient_signup(name_entry, age_entry, gender_entry, username_entry, password_entry):
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    current_patient = Patient.signup(name, age, gender, username, password)
    if current_patient == None:
        messagebox.showerror(title="signup Failed",
                             message="❌ Invalid username or password"
                             )
    else:
        messagebox.showinfo(title="signup Success",
                            message="✔ signup successful!"
                            )
        signup_window.destroy()
        import Login_Window_GUI
        


signup_tabs = ttk.Notebook(signup_window) 

staff_tab = Frame(signup_tabs,
                  bg= bg_color,
                  )
doctor_tab = Frame(signup_tabs,
                   bg= bg_color
                   )
patient_tab = Frame(signup_tabs,
                   bg= bg_color
                   )

signup_tabs.add(staff_tab,
               text="Staff",
               )
signup_tabs.add(doctor_tab,
               text="Doctor",
               )
signup_tabs.add(patient_tab,
               text="Patient",
               )

signup_tabs.pack(expand=True,
                fill="both"
               )
  
def page(tab,fun):
    signup_frame = Frame(tab,
                    bg=bg_color
                    )
    signup_frame.place(relx=0.5, rely=0.5, anchor="center")

    signup_label = Label(signup_frame,
                    text="Sign Up",
                    bg=bg_color,
                    fg=fg_color,
                    font=("times new roman", 50,'bold')
                    )
    signup_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

    name_label = Label(signup_frame,
                       text="Name",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    name_label.grid(row=1, column=0)
    name_entry = Entry(signup_frame,
                       font=("times new roman", 25)
                       )
    name_entry.grid(row=1, column=1, pady=20)

    age_label = Label(signup_frame,
                       text="Age",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    age_label.grid(row=2, column=0)
    age_entry = Entry(signup_frame,
                       font=("times new roman", 25)
                       )
    age_entry.grid(row=2, column=1, pady=20)

    gender_label = Label(signup_frame,
                       text="Gender",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    gender_label.grid(row=3, column=0)
    gender_entry = Entry(signup_frame,
                       font=("times new roman", 25)
                       )
    gender_entry.grid(row=3, column=1, pady=20)

    username_label = Label(signup_frame,
                       text="Username",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    username_label.grid(row=4, column=0)
    username_entry = Entry(signup_frame,
                       font=("times new roman", 25)
                       )
    username_entry.grid(row=4, column=1, pady=20)

    password_label = Label(signup_frame,
                       text="Password",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    password_label.grid(row=5, column=0)

    password_entry = Entry(signup_frame,
                       show="*",
                       font=("times new roman", 25)
                       )
    password_entry.grid(row=5, column=1, pady=20)



    signup_button = Button(signup_frame,
                      text="signup",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: fun(name_entry, age_entry, gender_entry, username_entry, password_entry)
                      )
    signup_button.grid(row=6, column=0, columnspan=2, pady=30)
    
    return name_entry, age_entry, gender_entry, username_entry, password_entry


page(staff_tab,staff_signup)
page(doctor_tab,doctor_signup)
page(patient_tab,patient_signup)

signup_window.mainloop()