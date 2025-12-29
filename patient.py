from database import Database
from bill import Bill

db = Database()

class Patient:
    def __init__(self, id, name, age, gender, username, password, problem=None, assigned_doctor=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.username = username
        self.password = password
        self.problem = problem
        self.assigned_doctor = assigned_doctor

    @staticmethod
    def signup(name, age, gender, username, password):
        patient_id = db.add_patient(name, age, gender, username, password)
        if patient_id:
            print(f"✔ Signup successful! Your Patient ID: {patient_id}")
            return Patient(patient_id, name, age, gender, username, password)
        return None

    @staticmethod
    def login(username, password):
        record = db.get_patient_by_username(username)
        if record and record[5] == password:
            print("✔ Login successful!")
            return Patient(*record)
        print("❌ Invalid username or password")
        return None

    def view_doctors(self):
        return db.get_doctors_by_specialty()

    def view_doctor_schedule(self, doctor_id):
        # يمكن ربطها بجدول حقيقي لاحقًا
        return {"Sunday": ["10:00", "11:00"], "Tuesday": ["12:00", "13:00"]}

    def book_appointment(self, doctor_id, day, time, problem):
        self.problem = problem
        self.assigned_doctor = doctor_id
        db.execute(
            "UPDATE Patients SET problem=?, assigned_doctor=? WHERE id=?",
            (problem, doctor_id, self.id)
        )
        full_date = f"{day} - {time}"
        appointment_id = db.add_appointment(self.id, doctor_id, full_date, problem)
        Bill(self.id, appointment_id)
        return appointment_id

    def view_appointments(self):
        return db.get_patient_appointments(self.id)

    def edit_appointment(self, appointment_id, new_date=None, new_notes=None):
        db.edit_appointment(appointment_id, new_date, new_notes)

    def delete_appointment(self, appointment_id):
        db.delete_appointment(appointment_id)

    def view_bill(self, appointment_id):
        return db.get_bill(appointment_id)

    def pay_bill(self, appointment_id):
        bill = db.get_bill(appointment_id)
        if bill:
            db.update_bill_status(appointment_id, "paid")
            return "✔ Payment successful!"
        return "❌ Bill not found"
