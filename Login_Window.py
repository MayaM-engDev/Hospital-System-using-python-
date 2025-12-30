from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from patient import Patient
from Patient_Window import open_patient

from doctor import Doctor
from Doctor_Window import open_doctor

from staff import Staff


bg_color = "#D3D3D3"
fg_color = "#0026FF"


def staff_login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    # current_patient = Patient.login(username, password)
    # if current_patient == None:
    #     messagebox.showerror(title="Login Failed",
    #                          message="❌ Invalid username or password"
    #                          )
    # else:
    #     messagebox.showinfo(title="Login Success",
    #                         message="✔ Login successful!"
    #                         )
    messagebox.showerror(title="Staff",
                         message="❌ Staff"
                        )
def doctor_login(doc_id_entry):
    doctor_id = int(doc_id_entry.get())
    current_user = Doctor.login(doctor_id)
    if current_user == None:
        messagebox.showerror(title="Login Failed",
                             message="❌ Invalid Doctor ID"
                             )
    else:
        messagebox.showinfo(title="Login Success",
                            message="✔ Login successful!"
                            )
        login_window.destroy()
        open_doctor(doctor_id)

def patient_login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    current_patient = Patient.login(username, password)
    if current_patient == None:
        messagebox.showerror(title="Login Failed",
                             message="❌ Invalid username or password"
                             )
    else:
        messagebox.showinfo(title="Login Success",
                            message="✔ Login successful!"
                            )
        login_window.destroy()
        open_patient(username,password)

def doctor_login_f():
    login_frame = Frame(doctor_tab,
                    bg=bg_color
                    )
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    login_label = Label(login_frame,
                    text="Doctor Login",
                    bg=bg_color,
                    fg=fg_color,
                    font=("times new roman", 50,'bold')
                    )
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

    doc_id_label = Label(login_frame,
                       text="Doctor ID",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    doc_id_label.grid(row=1, column=0)

    doc_id_entry = Entry(login_frame,
                       font=("times new roman", 25)
                       )
    doc_id_entry.grid(row=1, column=1, pady=20)

    login_button = Button(login_frame,
                      text="Login",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: doctor_login(doc_id_entry)
                      )
    login_button.grid(row=2, column=0, columnspan=2, pady=30)
    
    return doc_id_entry


def page(tab,fun):
    login_frame = Frame(tab,
                    bg=bg_color
                    )
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    login_label = Label(login_frame,
                    text="Login",
                    bg=bg_color,
                    fg=fg_color,
                    font=("times new roman", 50,'bold')
                    )
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

    username_label = Label(login_frame,
                       text="Username",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    username_label.grid(row=1, column=0)

    username_entry = Entry(login_frame,
                       font=("times new roman", 25)
                       )
    username_entry.grid(row=1, column=1, pady=20)

    password_label = Label(login_frame,
                       text="Password",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    password_label.grid(row=2, column=0)

    password_entry = Entry(login_frame,
                       show="*",
                       font=("times new roman", 25)
                       )
    password_entry.grid(row=2, column=1, pady=20)



    login_button = Button(login_frame,
                      text="Login",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: fun(username_entry, password_entry)
                      )
    login_button.grid(row=3, column=0, columnspan=2, pady=30)
    
    return username_entry, password_entry

def open_login():
    global login_window
    global doctor_tab
    login_window = Tk()
    login_window.title("Log-In Page")
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    login_window.geometry(f"{screen_width}x{screen_height}+0+0")
    login_window.state("zoomed")
    login_window.configure(bg= bg_color)


    login_tabs = ttk.Notebook(login_window) 

    staff_tab = Frame(login_tabs,
                    bg= bg_color,
                    )
    doctor_tab = Frame(login_tabs,
                    bg= bg_color
                    )
    patient_tab = Frame(login_tabs,
                    bg= bg_color
                    )

    login_tabs.add(staff_tab,
                text="Staff",
                )
    login_tabs.add(doctor_tab,
                text="Doctor",
                )
    login_tabs.add(patient_tab,
                text="Patient",
                )

    login_tabs.pack(expand=True,
                    fill="both"
                )
    
    page(staff_tab,staff_login)
    doctor_login_f()
    page(patient_tab,patient_login)

    login_window.mainloop()