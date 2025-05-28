
class Subject:
    def __init__(self, code, name, units, schedule):
        self.code = code
        self.name = name
        self.units = units
        self.schedule = schedule
    

def view_all_students():
    print("\n--- All Enrolled Students ---")
    if not student:
        print("No students enrolled yet.")
        return
    for idx, student in enumerate(student, 1):
        print(f"{idx}. {student.name} ({student.student_id}) - Section {student.section}") 

