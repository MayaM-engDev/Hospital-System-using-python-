# Hospital Management System

## Project Overview
The **Hospital Management System** is a Python-based application designed to manage basic hospital operations using **Object-Oriented Programming (OOP)**, a **SQLite database**, and a **Graphical User Interface (GUI)** built with **Tkinter**.

The system supports multiple user roles (**Patient**, **Doctor**, and **Staff**) and allows appointment booking, billing management, and patient records handling in an organized and interactive way.

---

## Group Members
- Maya Maged — 120230241  
- Karen Labib — 120230259  
- Mairoun — 120230136  
- Kirolos Khairy — 120230237  

---

## Technologies Used
- **Programming Language:** Python  
- **GUI Framework:** Tkinter  
- **Database:** SQLite3  
- **Paradigm:** Object-Oriented Programming (OOP)  

---

##  Project Structure
Doctor.py
patient.py
staff.py
appointment.py
bill.py
database.py
main.py
GUI_main.py
GUI_tools.py
Signup_window.py
Login_window.py
Doctor_window.py
Patient_window.py
Staff_window.py

---

## Object-Oriented Design

### Main Classes
- Patient  
- Doctor  
- Staff  
- Appointment  
- Bill  

### Patient Attributes
- ID  
- Name  
- Age  
- Gender  
- Username  
- Password  
- Problem  
- Assigned Doctor  

### Doctor Attributes
- ID  
- Name  
- Age  
- Specialty  

### Staff Attributes
- ID  
- Name  
- Age  
- Gender  

### Appointment Attributes
- Patient ID  
- Doctor ID  
- Date  
- Notes  
- Payment Status  

### Bill Attributes
- Patient ID  
- Appointment ID  
- Total Cost  
- Payment Status  

---

## System Methods

### Patient Functions
- `signup()`  
- `login()`  
- `view_doctors()`  
- `book_appointment()`  
- `view_appointments()`  
- `pay_bill()`  

### Doctor Functions
- `view_assigned_patients()`  
- `view_appointments()`  
- `profile()`  

### Staff Functions
- `add_patient()`  
- `update_patient()`  
- `delete_patient()`  
- `register_patient_offline()`  
- `view_all_bills()`  

### Appointment Functions
- `add_patient_appointment()`  
- `get_patient_appointments()`  

### Bill Functions
- `view_all_bills()`  
- `view_paid_bills()`  
- `total_paid_amount()`  
- `mark_bill_as_paid()`  

---

## OOP Concepts Applied
- **Encapsulation:** Each class manages its own data and behavior  
- **Abstraction:** Only essential methods are exposed  
- **Inheritance:** Designed for future extension (User → Patient/Doctor/Staff)  
- **Polymorphism:** Similar methods behave differently across classes  

---

## Application Features

### Patient Features
- Sign up & login  
- View doctors  
- Book appointments  
- View, edit, and delete appointments  
- View and pay bills  

### Doctor Features
- View assigned patients  
- View appointments  
- View profile  

### Staff Features
- Add, update, and delete patients  
- View patients and doctors  
- Add appointments (offline registration)  
- View all bills  
- View paid bills  
- View total paid amount  

---

##  Database Structure

### Patients Table
(id, name, age, gender, problem, assigned_doctor)

### Doctors Table
(id, name, specialty)

### Appointments Table
(id, patient_id, doctor_id, date, notes, payment_status)

### Bills Table
(patient_id, appointment_id, total_cost, payment_status)

## implementation 
### how to run 
1. Install **Python 3**.
2. Open the project folder.
3. Run the following command:
```bash
python main.py
```
### screenshot
1)Program Execution and User Interaction

## implementation 
### how to run 
1. Install **Python 3**.
2. Open the project folder.
3. Run the following command:
```bash
python main.py
```
### screenshot
1. [Program Execution and User Interaction](https://github.com/user-attachments/assets/9f056f99-6165-4e09-806e-41569d81b570)
2. [Patient Menu – Viewing Doctors and Booking an Appointment ](https://github.com/user-attachments/assets/dba2c685-162f-48f9-993c-1120f7256492)
3. [Patient Appointment and Billing Execution](https://github.com/user-attachments/assets/218213dc-69f5-47b7-87fe-7e13514c6ddc)
4. [Doctor Login and Patient Management Execution](https://github.com/user-attachments/assets/92416a7a-705c-4865-9425-55a37ff20bcb)
5. [Staff login()and view_appointments()](https://github.com/user-attachments/assets/66052bd7-d485-40af-8abd-1ae72548ebf6)
6. [view_all_bills() and view_patients()](https://github.com/user-attachments/assets/1bf1d5c8-d9ca-4fb0-b9cc-036af495cc9f)












