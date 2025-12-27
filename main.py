from patient import Patient
from database import Database

db = Database()

# --- إضافة دكاترة (لو مش موجودين) ---
if not db.get_doctors_by_specialty():
    db.add_doctor("Dr. Ahmed", "Cardiology")
    db.add_doctor("Dr. Sara", "Dermatology")
    db.add_doctor("Dr. Soha", "Dermatology")

# ===== LOGIN / SIGNUP =====
current_patient = None
while not current_patient:
    print("\n--- Welcome to Hospital System ---")
    print("1) Login")
    print("2) Signup")
    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        current_patient = Patient.login(username, password)

    elif choice == "2":
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        username = input("Choose username: ")
        password = input("Choose password: ")
        current_patient = Patient.signup(name, age, gender, username, password)

    else:
        print("Invalid choice!")

# ===== MAIN MENU =====
while True:
    print("\n--- Menu ---")
    print("1) Show Doctors")
    print("2) Show Doctor Schedule")
    print("3) Book Appointment")
    print("4) Show My Appointments")
    print("5) Edit My Appointment")
    print("6) Delete My Appointment")
    print("7) Show My Bills")
    print("8) Pay Bill")
    print("9) Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        doctors = current_patient.view_doctors()
        print("\nDoctors:")
        for d in doctors:
            print(f"{d[0]}) {d[1]} - {d[2]}")

    elif choice == "2":
        doc_id = int(input("Enter Doctor ID to view schedule: "))
        schedule = current_patient.view_doctor_schedule(doc_id)
        print(f"\nDoctor {doc_id} Schedule:")
        for day, times in schedule.items():
            print(f"{day}: {', '.join(times)}")

    elif choice == "3":
        doctors = current_patient.view_doctors()
        print("\nDoctors:")
        for d in doctors:
            print(f"{d[0]}) {d[1]} - {d[2]}")
        doc_id = int(input("Enter Doctor ID to book: "))
        schedule = current_patient.view_doctor_schedule(doc_id)
        print("\nSchedule:")
        for day, times in schedule.items():
            print(f"{day}: {', '.join(times)}")
        day = input("Choose day: ")
        if day not in schedule:
            print("Invalid day!")
            continue
        time = input(f"Choose time ({', '.join(schedule[day])}): ")
        if time not in schedule[day]:
            print("Invalid time!")
            continue
        problem = input("Enter problem/notes: ")
        appointment_id = current_patient.book_appointment(doc_id, day, time, problem)
        print(f"✔ Appointment booked with ID: {appointment_id}")

    elif choice == "4":
        appointments = current_patient.view_appointments()
        if not appointments:
            print("No appointments yet.")
        else:
            print("\nMy Appointments:")
            for a in appointments:
                print(f"ID: {a[0]}, Doctor ID: {a[2]}, Date: {a[3]}, Notes: {a[4]}, Status: {a[5]}")

    elif choice == "5":
        appointments = current_patient.view_appointments()
        if not appointments:
            print("No appointments to edit.")
            continue
        print("\nAppointments:")
        for a in appointments:
            print(f"ID: {a[0]}, Doctor ID: {a[2]}, Date: {a[3]}, Notes: {a[4]}, Status: {a[5]}")
        app_id = int(input("Enter Appointment ID to edit: "))
        new_date = input("Enter new date (or leave empty to keep current): ")
        new_notes = input("Enter new notes (or leave empty to keep current): ")
        current_patient.edit_appointment(app_id, new_date if new_date else None, new_notes if new_notes else None)
        print("✔ Appointment updated!")

    elif choice == "6":
        appointments = current_patient.view_appointments()
        if not appointments:
            print("No appointments to delete.")
            continue
        print("\nAppointments:")
        for a in appointments:
            print(f"ID: {a[0]}, Doctor ID: {a[2]}, Date: {a[3]}, Notes: {a[4]}, Status: {a[5]}")
        app_id = int(input("Enter Appointment ID to delete: "))
        current_patient.delete_appointment(app_id)
        print("✔ Appointment deleted!")

    elif choice == "7":
        appointments = current_patient.view_appointments()
        if not appointments:
            print("No bills yet.")
            continue
        print("\nMy Bills:")
        for a in appointments:
            bill = current_patient.view_bill(a[0])
            print(f"Appointment ID: {bill[1]}, Total: {bill[3]}, Status: {bill[4]}")

    elif choice == "8":
        app_id = int(input("Enter Appointment ID to pay: "))
        result = current_patient.pay_bill(app_id)
        print(result)

    elif choice == "9":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
