class Section:
    def __init__(self, name, instructor=None):
        self.name = name
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.students.sort(key=lambda s: s.name.lower())

    def display_section(self):
        print(f"Section: {self.name}")
        print(f"Instructor: {self.instructor.name if self.instructor else 'None'}")
        print("Enrolled Students:")
        for idx, student in enumerate(self.students, 1):
            print(f"{idx}. {student.name} ({student.student_id})")
