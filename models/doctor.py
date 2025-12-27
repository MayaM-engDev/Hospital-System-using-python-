class Doctor():
    allDoctors = {}
    id_counter = 0
    
    def __init__(self, doctor_id = None, name = None, specialty = None, time_slots = None, time_slot_counter = None):

        self.specialty = specialty
        self.doctor_id = doctor_id
        self.name = name
        self.time_slots = time_slots
        self.time_slot_counter = time_slot_counter

    def sign_up(self):
        Doctor.id_counter += 1
        self.doctor_id = Doctor.id_counter
        self.name = input("Enter doctor's name: ")
        self.specialty = input("Enter doctor's specialty: ")
        self.time_slot_counter = None

        while not isinstance(self.time_slot_counter, int):
            try:
                self.time_slot_counter = int(input("Enter doctor's time slot counter: "))
            except ValueError:
                print("Invalid input for time slot counter. Please enter a number.")

        self.time_slots = []
        for i in range(self.time_slot_counter):
            days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            day = input(f"Enter day for time slot {i+1} (e.g., 'Monday'): ").lower()

            while day not in days:
                print("Invalid day entered. Please enter a valid day of the week.")
                day = input(f"Enter day for time slot {i+1} (e.g., 'Monday'): ")
            
            time1_hours = input(f"Enter time for time slot {i+1} (e.g., '10'): ")
            while not (0 <= time1_hours <= 23):
                print("Invalid time entered. Please enter a valid hour (0-23).")
                time1_hours = input(f"Enter time for time slot {i+1} (e.g., '10'): ")

            time1_minutes = input(f"Enter minutes for time slot {i+1} (e.g., '30'): ")
            while not (0 <= time1_minutes <= 59):
                print("Invalid minutes entered. Please enter valid minutes (0-59).")
                time1_minutes = input(f"Enter minutes for time slot {i+1} (e.g., '30'): ")
   
            time2_hours = input(f"Enter time for time slot {i+1} (e.g., '10'): ")
            while not (0 <= time2_hours <= 23):
                print("Invalid time entered. Please enter a valid hour (0-23).")
                time2_hours = input(f"Enter time for time slot {i+1} (e.g., '10'): ")

            time2_minutes = input(f"Enter minutes for time slot {i+1} (e.g., '30'): ")
            while not (0 <= time2_minutes <= 59):
                print("Invalid minutes entered. Please enter valid minutes (0-59).")
                time2_minutes = input(f"Enter minutes for time slot {i+1} (e.g., '30'): ")   
  
            self.time_slots.append({"day": day, "from": f"{time1_hours}:{time1_minutes}", "to": f"{time2_hours}:{time2_minutes}"})

        Doctor.allDoctors[self.doctor_id] = {
            "name": self.name,
            "specialty": self.specialty,
            "time_slots": self.time_slots
        }

        return f"you have added Dr.{self.name} with ID {self.doctor_id} in {self.specialty} successfully"  
    
    def search_doctor_by_specialty(self, specialty):
        result = []
        for doctor_id in Doctor.allDoctors:
            if Doctor.allDoctors[doctor_id]["specialty"].lower() == specialty.lower():
                result.append({
                    "doctor_id": doctor_id,
                    "name": Doctor.allDoctors[doctor_id]["name"],
                    "specialty": Doctor.allDoctors[doctor_id]["specialty"],
                    "time_slots": Doctor.allDoctors[doctor_id]["time_slots"]
                })
        return result    
    
    def search_doctor_by_name(self, name):
        result = []
        for doctor_id in Doctor.allDoctors:
            if Doctor.allDoctors[doctor_id]["name"].lower() == name.lower():
                result.append({
                    "doctor_id": doctor_id, 
                    "\n name": Doctor.allDoctors[doctor_id]["name"],
                    "\n specialty": Doctor.allDoctors[doctor_id]["specialty"],
                    "\n time_slots": Doctor.allDoctors[doctor_id]["time_slots"]
                })
        return result
    
