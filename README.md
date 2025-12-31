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
