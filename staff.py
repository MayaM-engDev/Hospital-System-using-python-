from person import Person
from database import Database

class Staff(Person):
    def __init__(self, id, name, age, gender, role, access_level):
        super().__init__(id, name, age, gender)
        self.role = role
        self.access_level = access_level
        self.db = Database()

    #  ADD PATIENT 
    def add_patient(self, name, age, gender, problem, assigned_doctor):
        if self.access_level == 1 or self.access_level == 3:
            query = "INSERT INTO Patients (name, age, gender, problem, assigned_doctor) VALUES (?, ?, ?, ?, ?)"
            self.db.execute(query, (name, age, gender, problem, assigned_doctor))
        else:
            print("Access denied: You are not allowed to add patients.")

    # UPDATE PATIENT
    def update_patient(self, patient_id, name, age, gender, problem):
        if self.access_level == 3:
            query = "UPDATE Patients SET name=?, age=?, gender=?, problem=? WHERE id=?"
            self.db.execute(query, (name, age, gender, problem, patient_id))
        else:
            print("Access denied: Only admin can update patient data.")

    # DELETE PATIENT
    def delete_patient(self, patient_id):
        if self.access_level != 3:
            print("Access denied: Only admin can delete patient records.")
            return
        check_query = "SELECT * FROM Patients WHERE id=?"
        result = self.db.fetch(check_query, (patient_id,))
        if len(result) == 0:
            print("Delete failed: Patient does not exist.")
        else:
            delete_query = "DELETE FROM Patients WHERE id=?"
            self.db.execute(delete_query, (patient_id,))
            print("Patient deleted successfully due to incorrect or duplicated record.")

    # SEARCH RECORDS
    def search_records(self, table_name, keyword):
        if self.access_level != 3:
            print("Access denied: Only admin can search all records.")
            return []
        query = f"SELECT * FROM {table_name} WHERE id LIKE ?"
        return self.db.fetch(query, ('%' + str(keyword) + '%',))
