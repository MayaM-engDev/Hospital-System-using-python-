import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("hospital.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # --- Patients ---
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patients(
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                gender TEXT,
                problem TEXT
            )
        """)

        # --- Doctors ---
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Doctors(
                id INTEGER PRIMARY KEY,
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

        # --- Prescriptions ---
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Prescriptions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                doctor_id INTEGER,
                medicine TEXT,
                dosage TEXT,
                price REAL
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
    def add_patient(self, id, name, age, gender, problem=None):
        self.cursor.execute("SELECT * FROM Patients WHERE id=?", (id,))
        if self.cursor.fetchone():
            print(f"Patient with ID {id} already exists.")
            return
        self.cursor.execute("""
            INSERT INTO Patients (id, name, age, gender, problem)
            VALUES (?, ?, ?, ?, ?)
        """, (id, name, age, gender, problem))
        self.conn.commit()

    def get_patient(self, patient_id):
        self.cursor.execute("SELECT * FROM Patients WHERE id=?", (patient_id,))
        return self.cursor.fetchone()

    # ===== Doctors =====
    def add_doctor(self, id, name, specialty):
        self.cursor.execute("SELECT * FROM Doctors WHERE id=?", (id,))
        if self.cursor.fetchone():
            return
        self.cursor.execute("""
            INSERT INTO Doctors (id, name, specialty)
            VALUES (?, ?, ?)
        """, (id, name, specialty))
        self.conn.commit()

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

    # ===== Bills =====
    def add_bill(self, appointment_id, patient_id, total_cost):
        self.cursor.execute("""
            INSERT INTO Bills(appointment_id, patient_id, total_cost, payment_status)
            VALUES (?, ?, ?, 'pending')
        """, (appointment_id, patient_id, total_cost))
        self.conn.commit()

    def update_bill_status(self, appointment_id, status):
        self.cursor.execute("""
            UPDATE Bills SET payment_status=? WHERE appointment_id=?
        """, (status, appointment_id))
        self.conn.commit()

    def get_bill(self, appointment_id):
        self.cursor.execute("SELECT * FROM Bills WHERE appointment_id=?", (appointment_id,))
        return self.cursor.fetchone()
