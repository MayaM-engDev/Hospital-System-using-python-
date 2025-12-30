from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from patient import Patient
from doctor import Doctor
from Login_Window import open_login

bg_color = "#D3D3D3"
fg_color = "#0026FF"


def doctor_signup(name_entry, specialty_entry, age_entry):
    name = name_entry.get()
    specialty = specialty_entry.get()
    age = age_entry.get()
    current_user = Doctor.sign_up(name, specialty, age)
    if current_user == None:
        messagebox.showerror(title="Sign_UP Failed",
                             message="❌ Invalid Data"
                             )
    else:
        messagebox.showinfo(title="Sign_UP Success",
                            message="✔ signup successful! \n Dr.{current_user.name} added successfully with ID: {current_user.doctor_id}"
                            )
        signup_window.destroy()
        open_login()

        

def patient_signup(name_entry, age_entry, gender_entry, username_entry, password_entry):
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    current_patient = Patient.signup(name, age, gender, username, password)
    if current_patient == None:
        messagebox.showerror(title="Sign_UP Failed",
                             message="❌ Invalid  Data"
                             )
    else:
        messagebox.showinfo(title="Sign_UP Success",
                            message="✔ Sign_UP successful! \n Dr.{current_patient.name} added successfully with Username: {current_patient.username} "
                            )
        signup_window.destroy()
        open_login()


def doctor_signup_f():
    signup_frame = Frame(doctor_tab,
                    bg=bg_color
                    )
    signup_frame.place(relx=0.5, rely=0.5, anchor="center")

    signup_label = Label(signup_frame,
                    text="Doctor Sign Up",
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

    specialty_label = Label(signup_frame,
                       text="Specialty",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    specialty_label.grid(row=2, column=0)
    specialty_entry = Entry(signup_frame,
                       font=("times new roman", 25)
                       )
    specialty_entry.grid(row=2, column=1, pady=20)

    age_label = Label(signup_frame,
                       text="Age",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    age_label.grid(row=3, column=0)
    age_entry = Entry(signup_frame,
                       font=("times new roman", 25)
                       )
    age_entry.grid(row=3, column=1, pady=20)

    signup_button = Button(signup_frame,
                      text="Sign-UP",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: doctor_signup(name_entry,specialty_entry ,age_entry)
                      )
    signup_button.grid(row=6, column=0, columnspan=2, pady=30)
    
    return name_entry, specialty_entry ,age_entry



def patient_signup_f():
    signup_frame = Frame(patient_tab,
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
                      text="Sign-UP",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: patient_signup(name_entry, age_entry, gender_entry, username_entry, password_entry)
                      )
    signup_button.grid(row=6, column=0, columnspan=2, pady=30)
    
    return name_entry, age_entry, gender_entry, username_entry, password_entry


def open_signup():
    global signup_window
    global doctor_tab
    global patient_tab
    signup_window = Tk()
    signup_window.title("Sign-Up Page")
    screen_width = signup_window.winfo_screenwidth()
    screen_height = signup_window.winfo_screenheight()
    signup_window.geometry(f"{screen_width}x{screen_height}+0+0")
    signup_window.state("zoomed")
    signup_window.configure(bg= bg_color)


    signup_tabs = ttk.Notebook(signup_window) 


    doctor_tab = Frame(signup_tabs,bg= bg_color)
    patient_tab = Frame(signup_tabs,bg= bg_color)


    signup_tabs.add(doctor_tab,text="Doctor",)
    signup_tabs.add(patient_tab,text="Patient",)

    signup_tabs.pack(expand=True,fill="both")

    doctor_signup_f()
    patient_signup_f()

    signup_window.mainloop()