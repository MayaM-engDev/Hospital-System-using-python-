from tkinter import *
from tkinter import ttk
from GUI_Tools import create_scrollable_tab
from tkinter import messagebox
from staff import Staff 

bg_color = "#D3D3D3"
fg_color = "#0026FF"

def update(current_staff,patient_id_entry, new_name_entry, new_age_entry,new_gender_entry,new_problem_entry):
    pid = int(patient_id_entry.get())
    name = new_name_entry.get()
    age = int(new_age_entry.get())
    gender = new_gender_entry.get()
    problem = new_problem_entry.get()
    current_staff.update_patient(pid, name, age, gender, problem)
    messagebox.showinfo(title="update_patient Apointment Success",
                        message=f"✔ Patient {pid} updated"
                        )
    patient_list_frame.destroy()
    bill_frame.destroy()
    paid_bill_frame.destroy()
    total_paid_frame.destroy()
    patient_list_f(current_staff)
    bill_f(current_staff)
    paid_bill_f(current_staff)
    total_paid_f(current_staff)

def delete(current_staff,patient_idd_entry):
    pid = int(patient_idd_entry.get())
    current_staff.delete_patient(pid)
    print("✔ Appointment Deleted!")
    messagebox.showinfo(title="Delete Patient Success",
                        message=f"✔ Patient {pid} and related appointments deleted"
                        )
    patient_list_frame.destroy()
    bill_frame.destroy()
    paid_bill_frame.destroy()
    total_paid_frame.destroy()
    patient_list_f(current_staff)
    bill_f(current_staff)
    paid_bill_f(current_staff)
    total_paid_f(current_staff)

def book(current_staff,patient_id_entry ,doc_id_entry, date_entry, note_entry):
    patient_id = int(patient_id_entry.get())
    doctor_id = int(doc_id_entry.get())
    date = date_entry.get()
    notes = note_entry.get()
    appointment_id = current_staff.add_appointment(patient_id, doctor_id, date, notes)

    messagebox.showinfo(title="Book Apointment Success",
                        message=f"✔ Appointment booked with ID: {appointment_id}"
                        )
    patient_list_frame.destroy()
    bill_frame.destroy()
    paid_bill_frame.destroy()
    total_paid_frame.destroy()
    patient_list_f(current_staff)
    bill_f(current_staff)
    paid_bill_f(current_staff)
    total_paid_f(current_staff)

def view(current_staff,patient_iddd_entry):
     appointment_list_frame.destroy()
     appointment_list_f(current_staff,int(patient_iddd_entry.get()))



def profile_f(current_staff):
    profile_frame = Frame(staff_window,
                          bg=bg_color
                          )
    profile_frame.pack()


    name = Label(profile_frame,
                 text=f"Name: {current_staff.name}",
                 bg=bg_color,
                 fg=fg_color,
                 font=("times new roman", 50,'bold')
                 )
    name.grid(row=0, column=0)

    id = Label(profile_frame,
               text=f"ID: {current_staff.id}",
               bg=bg_color,
               fg=fg_color,
               font=("times new roman", 50,'bold')
               )
    id.grid(row=0, column=1)

    role = Label(profile_frame,
                text=f"Role: {current_staff.role}",
                bg=bg_color,
                fg=fg_color,
                font=("times new roman", 50,'bold')
                )
    role.grid(row=1, column=0)

    gender = Label(profile_frame,
                   text=f"Gender: {current_staff.gender}",
                   bg=bg_color,
                   fg=fg_color,
                   font=("times new roman", 50,'bold')
                   )
    gender.grid(row=1, column=1)

def patient_list_f(current_staff):
    global patient_list_frame
    patient_list_frame = Frame(patient_tab,
                              bg=bg_color
                             )
    patient_list_frame.grid(row=0,column=0,padx= 20)

    i = 0
    patients = current_staff.view_patients()
    for p in patients:
        staff_label = Label(patient_list_frame,
                              text=f"ID: {p[0]} \n Name: {p[1]} \n Age: {p[2]} \n Gender: {p[3]} \n Problem: {p[6]}",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 30,'bold')
                              )
        staff_label.grid(row=i, column=0, pady=20, padx= 20)
        i += 1

def update_patient_f(current_staff):
    update_patient_frame = Frame(patient_tab,
                                 bg=bg_color
                                )
    update_patient_frame.grid(row=0,column=1,padx= 20)
    
    patient_id_label = Label(update_patient_frame,
                       text="Patient ID",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    patient_id_label.grid(row=0, column=0)
    patient_id_entry = Entry(update_patient_frame,
                       font=("times new roman", 25)
                       )
    patient_id_entry.grid(row=0, column=1, pady=20)

    new_name_label = Label(update_patient_frame,
                       text="New Name",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    new_name_label.grid(row=1, column=0)
    new_name_entry = Entry(update_patient_frame,
                       font=("times new roman", 25)
                       )
    new_name_entry.grid(row=1, column=1, pady=20)

    new_age_label = Label(update_patient_frame,
                       text="New Age",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    new_age_label.grid(row=2, column=0)
    new_age_entry = Entry(update_patient_frame,
                       font=("times new roman", 25)
                       )
    new_age_entry.grid(row=2, column=1, pady=20)

    new_gender_label = Label(update_patient_frame,
                       text="New Gender",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    new_gender_label.grid(row=3, column=0)
    new_gender_entry = Entry(update_patient_frame,
                       font=("times new roman", 25)
                       )
    new_gender_entry.grid(row=3, column=1, pady=20)

    new_problem_label = Label(update_patient_frame,
                       text="New Problem",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    new_problem_label.grid(row=4, column=0)
    new_problem_entry = Entry(update_patient_frame,
                       font=("times new roman", 25)
                       )
    new_problem_entry.grid(row=4, column=1, pady=20)

    update_patient_button = Button(update_patient_frame,
                      text="Update",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: update(current_staff,patient_id_entry, new_name_entry, new_age_entry,new_gender_entry,new_problem_entry)
                      )
    update_patient_button.grid(row=5, column=0, columnspan=2, pady=30)

def delete_f(current_staff):
    delete_frame = Frame(patient_tab,
                         bg=bg_color
                        )
    delete_frame.grid(row=0,column=2,padx= 20)

    patient_idd_label = Label(delete_frame,
                       text="Patient ID",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    patient_idd_label.grid(row=0, column=0)
    patient_idd_entry = Entry(delete_frame,
                       font=("times new roman", 25)
                       )
    patient_idd_entry.grid(row=0, column=1, pady=20)

    delete_button = Button(delete_frame,
                      text="Delete",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: delete(current_staff,patient_idd_entry)
                      )
    delete_button.grid(row=1, column=0, columnspan=2, pady=30)

def doctor_list_f(current_staff):
    doctor_list_frame = Frame(doctor_tab,
                                   bg=bg_color
                                  )
    doctor_list_frame.grid(row=0,column=0,sticky='w',padx= 20)

    ii = 0
    doctors = current_staff.view_doctors()
    for d in doctors:
        doctor_label = Label(doctor_list_frame,
                              text=f"ID: {d[0]} \n Name: {d[1]} \n Specialty: {d[2]}\n",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 10,'bold')
                              )
        doctor_label.grid(row=ii, column=0, pady=40, padx= 20)
        ii += 1


def book_f(current_staff):
    book_frame = Frame(doctor_tab,
                       bg=bg_color
                      )
    book_frame.grid(row=0,column=1,padx= 20)

    patient_id_label = Label(book_frame,
                       text="Patient ID",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    patient_id_label.grid(row=0, column=0)
    patient_id_entry = Entry(book_frame,
                       font=("times new roman", 25)
                       )
    patient_id_entry.grid(row=0, column=1, pady=20)

    doc_id_label = Label(book_frame,
                       text="Doctor ID",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    doc_id_label.grid(row=1, column=0)
    doc_id_entry = Entry(book_frame,
                       font=("times new roman", 25)
                       )
    doc_id_entry.grid(row=1, column=1, pady=20)

    date_label = Label(book_frame,
                       text="Date",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    date_label.grid(row=2, column=0)
    date_entry = Entry(book_frame,
                       font=("times new roman", 25)
                       )
    date_entry.grid(row=2, column=1, pady=20)

    note_label = Label(book_frame,
                       text="Notes",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    note_label.grid(row=3, column=0)
    note_entry = Entry(book_frame,
                       font=("times new roman", 25)
                       )
    note_entry.grid(row=3, column=1, pady=20)

    book_button = Button(book_frame,
                      text="Book Appointment",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: book(current_staff,patient_id_entry ,doc_id_entry, date_entry, note_entry)
                      )
    book_button.grid(row=4, column=0, columnspan=2, pady=30)

def view_f(current_staff):
    view_frame = Frame(appointment_tab,
                         bg=bg_color
                        )
    view_frame.grid(row=0,column=0,padx= 20)

    patient_iddd_label = Label(view_frame,
                       text="Patient ID",
                       bg=bg_color,
                       fg=fg_color,
                       font=("times new roman", 25,'bold')
                       )
    patient_iddd_label.grid(row=0, column=0)
    patient_iddd_entry = Entry(view_frame,
                       font=("times new roman", 25)
                       )
    patient_iddd_entry.grid(row=0, column=1, pady=20)

    view_button = Button(view_frame,
                      text="View Appointment",
                      bg=fg_color,
                      fg="#FFFFFF",
                      font=("times new roman", 25,'bold'),
                      command=lambda: view(current_staff,patient_iddd_entry)
                      )
    view_button.grid(row=1, column=0, columnspan=2, pady=30)

def appointment_list_f(current_staff,pid):
    global appointment_list_frame
    appointment_list_frame = Frame(appointment_tab,
                                   bg=bg_color
                                  )
    appointment_list_frame.grid(row=0,column=1,sticky='w',padx= 20)

    iii = 0
    appointments = current_staff.view_appointments(pid)
    for a in appointments:
        appointment_label = Label(appointment_list_frame,
                              text=f"ID: {a[0]} \n Doctor ID: {a[2]} \n Date: {a[3]} \n Notes: {a[4]} \n Status: {a[5]}\n",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 10,'bold')
                              )
        appointment_label.grid(row=iii, column=0, pady=40, padx= 20)
        iii += 1

def bill_f(current_staff):
    global bill_frame
    bill_frame = Frame(bill_tab,
                       bg=bg_color
                      )
    bill_frame.grid(row=0,column=0,padx= 20)
    
    iiii = 0
    bills = current_staff.view_all_bills()
    for b in bills:
        bill_label = Label(bill_frame,
                              text=f"Bill ID: {b['bill_id']}, Appointment ID: {b['appointment_id']} \n Patient ID: {b['patient_id']}, Patient Name: {b['patient_name']} \n Appointment Date: {b['appointment_date']}, Total: {b['total_cost']}, Status: {b['payment_status']}\n",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 10,'bold')
                              )
        bill_label.grid(row=iiii, column=0, pady=40, padx= 20)
        iiii += 1

def paid_bill_f(current_staff):
    global paid_bill_frame
    paid_bill_frame = Frame(bill_tab,
                       bg=bg_color
                      )
    paid_bill_frame.grid(row=0,column=1,padx= 20)
    
    iiiii = 0
    paid_bills = current_staff.view_paid_bills()
    for b in paid_bills:
        paid_bill_label = Label(paid_bill_frame,
                              text=f"paid_bill ID: {b['paid_bill_id']}, Appointment ID: {b['appointment_id']} \n Patient ID: {b['patient_id']}, Patient Name: {b['patient_name']} \n Appointment Date: {b['appointment_date']}, Total: {b['total_cost']}, Status: {b['payment_status']}\n",
                              bg=bg_color,
                              fg='red',
                              font=("times new roman", 10,'bold')
                              )
        paid_bill_label.grid(row=iiiii, column=0, pady=40, padx= 20)
        iiiii += 1

def total_paid_f(current_staff):
    global total_paid_frame
    total_paid_frame = Frame(bill_tab,
                       bg=bg_color
                      )
    total_paid_frame.grid(row=0,column=2,padx= 20)
    
    total_paid = current_staff.total_paid_amount()
    total_paid_label = Label(total_paid_frame,
                              text="Total Paid Amount",
                              bg=bg_color,
                              fg='Blue',
                              font=("times new roman", 20,'bold')
                              )
    total_paid_label.grid(row=0, column=0, pady=40, padx= 20)

    amount_label = Label(total_paid_frame,
                              text=total_paid,
                              bg=bg_color,
                              fg='black',
                              font=("times new roman", 20)
                              )
    amount_label.grid(row=0, column=1, pady=40, padx= 20)

def open_staff(username,password):
    global staff_window
    global patient_tab
    global doctor_tab
    global appointment_tab
    global bill_tab
    global appointment_list_frame
    current_staff = Staff.login(username,password)
    staff_window = Tk()
    staff_window.title("Staff Page")
    screen_width = staff_window.winfo_screenwidth()
    screen_height = staff_window.winfo_screenheight()
    staff_window.geometry(f"{screen_width}x{screen_height}+0+0")
    staff_window.state("zoomed")
    staff_window.configure(bg= bg_color)

    profile_f(current_staff)

    staff_tabs = ttk.Notebook(staff_window)
    staff_tabs.pack(expand=True,fill="both")  

    patient_tab = create_scrollable_tab(staff_tabs,"Patients")
    doctor_tab =  create_scrollable_tab(staff_tabs,"Doctors")
    appointment_tab =  create_scrollable_tab(staff_tabs,"Appointments")
    bill_tab =  create_scrollable_tab(staff_tabs,"Bills")

    # patient_tab = Frame(staff_tabs,bg= bg_color,)
    # doctor_tab = Frame(staff_tabs,bg= bg_color)
    # appointment_tab = Frame(staff_tabs,bg= bg_color)
    # bill_tab = Frame(staff_tabs,bg= bg_color)

    # staff_tabs.add(patient_tab,text="Patients")
    # staff_tabs.add(doctor_tab,text="My Doctors")
    # staff_tabs.add(appointment_tab,text="Appointments")
    # staff_tabs.add(bill_tab,text="Bills")

    patient_list_f(current_staff)
    update_patient_f(current_staff)
    delete_f(current_staff)
    doctor_list_f(current_staff)
    book_f(current_staff)
    view_f(current_staff)
    appointment_list_frame = Frame(appointment_tab,
                                   bg=bg_color
                                  )
    appointment_list_frame.grid(row=0,column=1,sticky='w',padx= 20)

    bill_f(current_staff)
    paid_bill_f(current_staff)
    total_paid_f(current_staff)


    staff_window.mainloop()


