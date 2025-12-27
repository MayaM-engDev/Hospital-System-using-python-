from database import Database

db = Database()

class Bill:
    def __init__(self, patient_id, appointment_id, total_cost=100):
        self.patient_id = patient_id
        self.appointment_id = appointment_id
        self.total_cost = total_cost
        self.payment_status = "pending"
        db.add_bill(appointment_id, patient_id, total_cost)

    def pay(self):
        self.payment_status = "paid"
        db.update_bill_status(self.appointment_id, "paid")
