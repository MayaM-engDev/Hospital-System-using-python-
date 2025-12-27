from models.doctor import Doctor
class Prescription(Doctor):
    allPrescriptions = {}

    def __init__(self, prescription_id, patient_name, patient_age, medications):
        self.prescription_id = prescription_id
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.medications = medications    
    
    def add_Prescription(self):
        self.patient_name = input("Enter patient's name: ")
        self.patient_age = None
        while not isinstance(self.patient_age, int):
            try:
                self.patient_age = int(input("Enter patient's age: "))
            except ValueError:
                return "Invalid input for patient's age. Please enter a number."
            
        self.medications = input("Enter medications (comma-separated): ").split(',')
        self.prescription_id = len(Prescription.allPrescriptions) + 1
        Prescription.allPrescriptions[self.prescription_id] = {
            "patient_name": self.patient_name,
            "patient_age": self.patient_age,
            "doctor_name": self.doctor_name,
            "medications": [med.strip() for med in self.medications]
        }

    def show_all_prescriptions_for_patient(self, patient_name):
        result = []
        for prescription_id in Prescription.allPrescriptions:
            if Prescription.allPrescriptions[prescription_id]["patient_name"].lower() == patient_name.lower():
                result.append({
                    "prescription_id": prescription_id,
                    "patient_name": Prescription.allPrescriptions[prescription_id]["patient_name"],
                    "patient_age": Prescription.allPrescriptions[prescription_id]["patient_age"],
                    "medications": Prescription.allPrescriptions[prescription_id]["medications"]
                })
        return result
        
    
    def search_prescription_by_patient_name(self, patient_name):
        result = []
        for prescription_id in Prescription.allPrescriptions:
            if Prescription.allPrescriptions[prescription_id]["patient_name"].lower() == patient_name.lower():
                result.append({
                    "prescription_id": prescription_id,
                    "patient_name": Prescription.allPrescriptions[prescription_id]["patient_name"],
                    "patient_age": Prescription.allPrescriptions[prescription_id]["patient_age"],
                    "medications": Prescription.allPrescriptions[prescription_id]["medications"]
                })
        return result
    
    def search_prescription_by_id(self, prescription_id):
        if prescription_id in Prescription.allPrescriptions:
            prescription = Prescription.allPrescriptions[prescription_id]
            return {
                "prescription_id": prescription_id,
                "patient_name": prescription["patient_name"],
                "patient_age": prescription["patient_age"],
                "medications": prescription["medications"]
            }
        else:
            return "Prescription not found."
