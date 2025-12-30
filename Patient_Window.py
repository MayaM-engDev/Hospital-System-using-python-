from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from GUI_Tools import create_scrollable_tab
from patient import Patient 

bg_color = "#D3D3D3"
fg_color = "#0026FF"

def book(current_patient,doc_id_entry, day_entry, time_entry, problem_entry):
    doc_id = int(doc_id_entry.get())
    day = day_entry.get()
    time = time_entry.get()
    problem = problem_entry.get() 
    appointment_id = current_patient.book_appointment(doc_id, day, time, problem)
    print(f"✔ Appointment booked with ID: {appointment_id}")
    messagebox.showinfo(title="Book Apointment Success",
                        message=f"✔ Appointment booked with ID: {appointment_id}"
                        )
    view_appointment_frame.destroy()
    bill_frame.destroy()
    view_f(current_patient)
    bill_f(current_patient)


def edit(current_patient,app_id_entry, new_date_entry, new_notes_entry):
    app_id = int(app_id_entry.get())
    new_date = new_date_entry.get()
    new_notes = new_notes_entry.get()
    current_patient.edit_appointment(app_id, new_date if new_date else None, new_notes if new_notes else None)
    print("✔ Appointment updated!")
    messagebox.showinfo(title="Edit Apointment Success",
                        message="✔ Appointment updated!"
                        )
    view_appointment_frame.destroy()
    bill_frame.destroy()
    view_f(current_patient)
    bill_f(current_patient)
    


def delete(current_patient,app_idd_entry):
    app_idd = int(app_idd_entry.get())
    current_patient.delete_appointment(app_idd)
    print("✔ Appointment Deleted!")
    messagebox.showinfo(title="Delete Apointment Success",
                        message="✔ Appointment Deleted!"
                        )
    view_appointment_frame.destroy()
    bill_frame.destroy()
    view_f(current_patient)
    bill_f(current_patient)
    
def pay(current_patient,app_iddd_entry):
    app_iddd = int(app_iddd_entry.get())
    result = current_patient.pay_bill(app_iddd)
    print(result)
    messagebox.showinfo(title="Pay A Bill Success",
                        message=result
                        )
    bill_frame.destroy()
    bill_f(current_patient)


def profile_f(current_patient):
    profile_frame = Frame(patient_window,
                          bg=bg_color
                          )
    profile_frame.pack()

    name = Label(profile_frame,
                 text=f"Name: {current_patient.name}",
                 bg=bg_color,
                 fg=fg_color,
                 font=("times new roman", 50,'bold')
                 )
    name.grid(row=0, column=0)

    id = Label(profile_frame,
               text=f"ID: {current_patient.id}",
               bg=bg_color,
               fg=fg_color,
               font=("times new roman", 50,'bold')
               )
    id.grid(row=0, column=1)

    age = Label(profile_frame,
                text=f"Age: {current_patient.age}",
                bg=bg_color,
                fg=fg_color,
                font=("times new roman", 50,'bold')
                )
    age.grid(row=1, column=0)

    gender = Label(profile_frame,
                   text=f"Gender: {current_patient.gender}",
                   bg=bg_color,
                   fg=fg_color,
                   font=("times new roman", 50,'bold')
                   )
    gender.grid(row=1, column=1)

def doctor_list_f(current_patient):
    doctor_list_frame = Frame(doctor_list_tab,
                              bg=bg_color
                             )
    doctor_list_frame.grid(row=0,column=0,padx= 20)

    doctors = current_patient.view_doctors()
    i = 0
    for d in doctors:
        patient_label = Label(doctor_list_frame,
                              text=f"{d[0]}) {d[1]} - {d[2]}",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 30,'bold')
                              )
        patient_label.grid(row=i, column=0, pady=20, padx= 20)
        i += 1

def book_f(current_patient):
    book_frame = Frame(doctor_list_tab,
                       bg=bg_color
                      )
    book_frame.grid(row=0,column=1,padx= 20)

    doc_id_label = Label(book_frame,
                       text="Doctor ID",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    doc_id_label.grid(row=0, column=0)
    doc_id_entry = Entry(book_frame,
                       font=("times new roman", 25)
                       )
    doc_id_entry.grid(row=0, column=1, pady=20)

    day_label = Label(book_frame,
                       text="Day",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    day_label.grid(row=1, column=0)
    day_entry = Entry(book_frame,
                       font=("times new roman", 25)
                       )
    day_entry.grid(row=1, column=1, pady=20)

    time_label = Label(book_frame,
                       text="Time",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    time_label.grid(row=2, column=0)
    time_entry = Entry(book_frame,
                       font=("times new roman", 25)
                       )
    time_entry.grid(row=2, column=1, pady=20)

    problem_label = Label(book_frame,
                       text="Problem",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    problem_label.grid(row=3, column=0)
    problem_entry = Entry(book_frame,
                       font=("times new roman", 25)
                       )
    problem_entry.grid(row=3, column=1, pady=20)

    book_button = Button(book_frame,
                      text="Book Appointment",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: book(current_patient,doc_id_entry, day_entry, time_entry, problem_entry)
                      )
    book_button.grid(row=4, column=0, columnspan=2, pady=30)

def view_f(current_patient):
    global view_appointment_frame
    view_appointment_frame = Frame(view_appointment_tab,
                                   bg=bg_color
                                  )
    view_appointment_frame.grid(row=0,column=0,sticky='w',padx= 20)
    
    ii = 0
    appointments = current_patient.view_appointments()
    for a in appointments:
        patient_label = Label(view_appointment_frame,
                              text=f"ID: {a[0]} \n Doctor ID: {a[2]}\n Date: {a[3]}\n Notes: {a[4]}\n Status: {a[5]}\n",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 10,'bold')
                              )
        patient_label.grid(row=ii, column=0, pady=40, padx= 20)
        ii += 1

def edit_f(current_patient):
    edit_frame = Frame(view_appointment_tab,
                       bg=bg_color
                      )
    edit_frame.grid(row=0,column=1,padx= 20)

    app_id_label = Label(edit_frame,
                       text="Appointment ID",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    app_id_label.grid(row=0, column=0)
    app_id_entry = Entry(edit_frame,
                       font=("times new roman", 25)
                       )
    app_id_entry.grid(row=0, column=1, pady=20)

    new_date_label = Label(edit_frame,
                       text="New Date",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    new_date_label.grid(row=1, column=0)
    new_date_entry = Entry(edit_frame,
                       font=("times new roman", 25)
                       )
    new_date_entry.grid(row=1, column=1, pady=20)

    new_notes_label = Label(edit_frame,
                       text="New Notes",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    new_notes_label.grid(row=2, column=0)
    new_notes_entry = Entry(edit_frame,
                       font=("times new roman", 25)
                       )
    new_notes_entry.grid(row=2, column=1, pady=20)

    edit_button = Button(edit_frame,
                      text="Edit Appointment",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: edit(current_patient,app_id_entry, new_date_entry, new_notes_entry)
                      )
    edit_button.grid(row=3, column=0, columnspan=2, pady=30)


def delete_f(current_patient):
    delete_frame = Frame(view_appointment_tab,
                         bg=bg_color
                        )
    delete_frame.grid(row=0,column=2,padx= 20)

    app_idd_label = Label(delete_frame,
                       text="Appointment ID",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    app_idd_label.grid(row=0, column=0)
    app_idd_entry = Entry(delete_frame,
                       font=("times new roman", 25)
                       )
    app_idd_entry.grid(row=0, column=1, pady=20)

    delete_button = Button(delete_frame,
                      text="Delete Appointment",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: delete(current_patient,app_idd_entry)
                      )
    delete_button.grid(row=1, column=0, columnspan=2, pady=30)

def bill_f(current_patient):
    global bill_frame
    bill_frame = Frame(bill_tab,
                       bg=bg_color
                      )
    bill_frame.grid(row=0,column=0,padx= 20)
    
    iii = 0
    appointments = current_patient.view_appointments()
    for a in appointments:
        bill = current_patient.view_bill(a[0])
        if bill:
            patient_label = Label(bill_frame,
                              text=f"Appointment ID: {bill[1]}\n Patient ID: {bill[2]}\nTotal: {bill[3]}\nStatus: {bill[4]}\n",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 10,'bold')
                              )
            patient_label.grid(row=iii, column=0, pady=40, padx= 20)
            iii += 1

def pay_f(current_patient):
    pay_frame = Frame(bill_tab,
                      bg=bg_color
                     )
    pay_frame.grid(row=0,column=1,padx=20)

    app_iddd_label = Label(pay_frame,
                           text="Appointment ID",
                           bg=bg_color,
                           fg=fg_color,
                           font=("times new roman", 25,'bold')
                          )
    app_iddd_label.grid(row=0, column=0)
    app_iddd_entry = Entry(pay_frame,
                           font=("times new roman", 25)
                          )
    app_iddd_entry.grid(row=0, column=1, pady=20)

    pay_button = Button(pay_frame,
                      text="Pay Bill",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: pay(current_patient,app_iddd_entry)
                      )
    pay_button.grid(row=1, column=0, columnspan=2, pady=30)


def open_patient(username,password):
    global patient_window
    global doctor_list_tab
    global view_appointment_tab
    global bill_tab
    current_patient = Patient.login(username,password)
    patient_window = Tk()
    patient_window.title("Patient Page")
    screen_width = patient_window.winfo_screenwidth()
    screen_height = patient_window.winfo_screenheight()
    patient_window.geometry(f"{screen_width}x{screen_height}+0+0")
    patient_window.state("zoomed")
    patient_window.configure(bg= bg_color)

    profile_f(current_patient)

    patient_tabs = ttk.Notebook(patient_window) 
    patient_tabs.pack(expand=True,fill="both")  

    doctor_list_tab = create_scrollable_tab(patient_tabs,"Doctors List")
    view_appointment_tab = create_scrollable_tab(patient_tabs,"My Appointment")
    bill_tab = create_scrollable_tab(patient_tabs,"Bills")

    # doctor_list_tab = Frame(patient_tabs,bg= bg_color,)
    # view_appointment_tab = Frame(patient_tabs,bg= bg_color)
    # bill_tab = Frame(patient_tabs,bg= bg_color)

    # patient_tabs.add(doctor_list_tab,text="Doctors List")
    # patient_tabs.add(view_appointment_tab,text="My Appointment")
    # patient_tabs.add(bill_tab,text="Patient")

    doctor_list_f(current_patient)
    book_f(current_patient)
    view_f(current_patient)
    edit_f(current_patient)
    delete_f(current_patient)
    bill_f(current_patient)
    pay_f(current_patient)


    patient_window.mainloop()


