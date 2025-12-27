import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("hospitalnew1.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # --- Patients ---
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patients(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                username TEXT UNIQUE,
                password TEXT,
                problem TEXT
            )
        """)

        # --- Doctors ---
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Doctors(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                specialty TEXT
            )
        """)

        # --- Appointments ---
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Appointments(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                doctor_id INTEGER,
                date TEXT,
                notes TEXT,
                payment_status TEXT
            )
        """)

        # --- Bills ---
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Bills(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                appointment_id INTEGER,
                patient_id INTEGER,
                total_cost REAL,
                payment_status TEXT
            )
        """)
        self.conn.commit()

    # ===== Patients =====
    def add_patient(self, name, age, gender, username, password, problem=None):
        self.cursor.execute("SELECT * FROM Patients WHERE username=?", (username,))
        if self.cursor.fetchone():
            print(f"Username '{username}' already exists!")
            return None
        self.cursor.execute("""
            INSERT INTO Patients (name, age, gender, username, password, problem)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, age, gender, username, password, problem))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_patient_by_username(self, username):
        self.cursor.execute("SELECT * FROM Patients WHERE username=?", (username,))
        return self.cursor.fetchone()

    # ===== Doctors =====
    def add_doctor(self, name, specialty):
        self.cursor.execute("INSERT INTO Doctors (name, specialty) VALUES (?, ?)", (name, specialty))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_doctors_by_specialty(self, specialty=""):
        if specialty:
            self.cursor.execute("SELECT * FROM Doctors WHERE specialty LIKE ?", ('%'+specialty+'%',))
        else:
            self.cursor.execute("SELECT * FROM Doctors")
        return self.cursor.fetchall()

    # ===== Appointments =====
    def add_appointment(self, patient_id, doctor_id, date, notes):
        self.cursor.execute("""
            INSERT INTO Appointments(patient_id, doctor_id, date, notes, payment_status)
            VALUES (?, ?, ?, ?, 'pending')
        """, (patient_id, doctor_id, date, notes))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_patient_appointments(self, patient_id):
        self.cursor.execute("SELECT * FROM Appointments WHERE patient_id=?", (patient_id,))
        return self.cursor.fetchall()

    def edit_appointment(self, appointment_id, new_date=None, new_notes=None):
        if new_date:
            self.cursor.execute("UPDATE Appointments SET date=? WHERE id=?", (new_date, appointment_id))
        if new_notes:
            self.cursor.execute("UPDATE Appointments SET notes=? WHERE id=?", (new_notes, appointment_id))
        self.conn.commit()

    def delete_appointment(self, appointment_id):
        self.cursor.execute("DELETE FROM Bills WHERE appointment_id=?", (appointment_id,))
        self.cursor.execute("DELETE FROM Appointments WHERE id=?", (appointment_id,))
        self.conn.commit()

    # ===== Bills =====
    def add_bill(self, appointment_id, patient_id, total_cost=100):
        self.cursor.execute("""
            INSERT INTO Bills(appointment_id, patient_id, total_cost, payment_status)
            VALUES (?, ?, ?, 'pending')
        """, (appointment_id, patient_id, total_cost))
        self.conn.commit()

    def update_bill_status(self, appointment_id, status):
        self.cursor.execute("UPDATE Bills SET payment_status=? WHERE appointment_id=?", (status, appointment_id))
        self.conn.commit()

    def get_bill(self, appointment_id):
        self.cursor.execute("SELECT * FROM Bills WHERE appointment_id=?", (appointment_id,))
        return self.cursor.fetchone()
