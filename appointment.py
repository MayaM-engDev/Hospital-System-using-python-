from database import Database

db = Database()

class Appointment:
    def __init__(self, patient_id, doctor_id, date, notes=""):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.notes = notes
        self.payment_status = "pending"
        self.id = db.add_appointment(patient_id, doctor_id, date, notes)

    def update(self, new_date=None, new_notes=None):
        if new_date:
            self.date = new_date
        if new_notes:
            self.notes = new_notes
        db.edit_appointment(self.id, new_date, new_notes)

    def delete(self):
        db.delete_appointment(self.id)
