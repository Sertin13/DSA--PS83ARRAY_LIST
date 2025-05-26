class Student:
    def __init__(self, student_id, name, college_course, college, academic_year, class_section):
        self.student_id = student_id
        self.name = name
        self.college_course = college_course
        self.college = college
        self.academic_year = academic_year
        self.class_section = class_section
        self.subject_list = []

    def enroll_subject(self, subject):
        self.subject_list.append(subject)

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.college_course}")
        print(f"College: {self.college}")
        print(f"Academic Year: {self.academic_year}")
        print(f"Class Section: {self.class_section}")
        print("\n| Subject Code | Subject Name            | Units | Schedule      |")
        print("|--------------|-------------------------|-------|---------------|")
        for subject in self.subject_list:
            print(f"| {subject.code:<13}| {subject.name:<24}| {subject.units:<6}| {subject.schedule:<14}|")