class Subject:
    def __init__(self, code, name, units, schedule):
        self.code = code
        self.name = name
        self.units = units
        self.schedule = schedule
    

def view_all_students():
    print("\n--- All Enrolled Students ---")
    if not students:
        print("No students enrolled yet.")
        return
    for idx, student in enumerate(students, 1):
        print(f"{idx}. {student.name} ({student.student_id}) - Section {student.section}") 

def main_menu():
    while True:
        print("\n===== Enrollment System Main Menu =====")
        print("[1] Student Enrollment")
        print("[2] Instructor Login")
        print("[3] View All Students")
        print("[4] Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            student_enrollment()
        elif choice == '2':
            instructor_login()
        elif choice == '3':
            view_all_students()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")