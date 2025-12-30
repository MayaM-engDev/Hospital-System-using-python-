from tkinter import *
from tkinter import ttk
from GUI_Tools import create_scrollable_tab
from doctor import Doctor 

bg_color = "#D3D3D3"
fg_color = "#0026FF"


def profile_f(current_doctor):
    profile_frame = Frame(doctor_window,
                          bg=bg_color
                          )
    profile_frame.pack()

    name = Label(profile_frame,
                 text=f"Name: {current_doctor.name}",
                 bg=bg_color,
                 fg=fg_color,
                 font=("times new roman", 50,'bold')
                 )
    name.grid(row=0, column=0)

    id = Label(profile_frame,
               text=f"ID: {current_doctor.id}",
               bg=bg_color,
               fg=fg_color,
               font=("times new roman", 50,'bold')
               )
    id.grid(row=0, column=1)

    age = Label(profile_frame,
                text=f"Age: {current_doctor.age}",
                bg=bg_color,
                fg=fg_color,
                font=("times new roman", 50,'bold')
                )
    age.grid(row=1, column=0)

    specialty = Label(profile_frame,
                   text=f"Specialty: {current_doctor.specialty}",
                   bg=bg_color,
                   fg=fg_color,
                   font=("times new roman", 50,'bold')
                   )
    specialty.grid(row=1, column=1)

def patient_list_f(current_doctor):
    doctor_list_frame = Frame(patient_list_tab,
                              bg=bg_color
                             )
    doctor_list_frame.grid(row=0,column=0,padx= 20)
    
    i = 0
    patients = current_doctor.view_assigned_patients()
    for p in patients:
        patient_label = Label(doctor_list_frame,
                              text=f"ID: {p[0]} \n Name: {p[1]} \n Age: {p[2]} \n Gender: {p[3]} \n Problem: {p[4]}",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 30,'bold')
                              )
        patient_label.grid(row=i, column=0, pady=20, padx= 20)
        i += 1


def view_f(current_doctor):
    global view_appointment_frame
    view_appointment_frame = Frame(view_appointment_tab,
                                   bg=bg_color
                                  )
    view_appointment_frame.grid(row=0,column=0,sticky='w',padx= 20)
    
    ii = 0
    appointments = current_doctor.view_appointments()
    for a in appointments:
        appointment_label = Label(view_appointment_frame,
                              text=f"ID: {a[0]} \n Patient ID: {a[1]} \n Date: {a[3]} \n Notes: {a[4]} \n Status: {a[5]}",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 10,'bold')
                              )
        appointment_label.grid(row=ii, column=0, pady=40, padx= 20)
        ii += 1


def open_doctor(doctor_id):
    global doctor_window
    global patient_list_tab
    global view_appointment_tab
    current_doctor = Doctor.login(doctor_id)
    doctor_window = Tk()
    doctor_window.title("Doctor Page")
    screen_width = doctor_window.winfo_screenwidth()
    screen_height = doctor_window.winfo_screenheight()
    doctor_window.geometry(f"{screen_width}x{screen_height}+0+0")
    doctor_window.state("zoomed")
    doctor_window.configure(bg= bg_color)

    profile_f(current_doctor)

    doctor_tabs = ttk.Notebook(doctor_window) 
    doctor_tabs.pack(expand=True,fill="both")  

    patient_list_tab = create_scrollable_tab(doctor_tabs,"Assigned Patients List")
    view_appointment_tab = create_scrollable_tab(doctor_tabs,"Appointments")

    # patient_list_tab = Frame(doctor_tabs,bg= bg_color,)
    # view_appointment_tab = Frame(doctor_tabs,bg= bg_color)

    # doctor_tabs.add(patient_list_tab,text="Assigned Patients List")
    # doctor_tabs.add(view_appointment_tab,text="Appointments")

    patient_list_f(current_doctor)
    view_f(current_doctor)

    doctor_window.mainloop()


