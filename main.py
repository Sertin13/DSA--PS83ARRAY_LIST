import json
from Student import Student
from Instructor import Instructor
from Subject import Subject
from Section import Section

# Load subjects from JSON file
with open('subjects.json', 'r') as f:
    subject_data = json.load(f)

# Convert JSON data to Subject objects, organized by college
college_subjects = {}
for college, subjects_list in subject_data.items():
    college_subjects[college] = [Subject(s['code'], s['name'], s['units'], s['schedule']) for s in subjects_list]

# Load course-to-college mapping
with open('course_to_college.json', 'r') as f:
    course_to_college = json.load(f)

# Create sections per course
section_names = ['A', 'B', 'C']
sections_per_course = {}
for course in course_to_college.keys():
    sections_per_course[course] = [Section(sec_name) for sec_name in section_names]

instructors = [
    Instructor('Sir Charles Bautista', 'Charles Bautista', '123456')
]

# Assign instructor to all sections for all courses
for course_sections in sections_per_course.values():
    for section in course_sections:
        section.instructor = instructors[0]
        instructors[0].assign_section(section)

students = []  # List of all enrolled students

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

def student_enrollment():
    print("\n--- Student Enrollment ---")
    student_id = input("Student ID: ")
    name = input("Name: ")
    # Load course-to-college mapping
    with open('course_to_college.json', 'r') as f:
        course_to_college = json.load(f)
    # Show available courses
    print("Select Course:")
    courses = list(course_to_college.keys())
    for idx, course_name in enumerate(courses, 1):
        print(f"[{idx}] {course_name}")
    try:
        course_choice = int(input("Enter course number: ")) - 1
        if course_choice < 0 or course_choice >= len(courses):
            print("Invalid course choice. Please try again.")
            return
        course = courses[course_choice]
        college = course_to_college[course]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    academic_year = input("Academic Year: ")
    # Let student select section for their course only
    course_sections = sections_per_course[course]
    print("Select Section:")
    for idx, sec in enumerate(course_sections, 1):
        print(f"[{idx}] Section {sec.name}")
    try:
        sec_choice = int(input("Enter section number: ")) - 1
        if sec_choice < 0 or sec_choice >= len(course_sections):
            print("Invalid section choice. Please try again.")
            return
        section = course_sections[sec_choice]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    student = Student(student_id, name, course, college, academic_year, section.name)
    print("Select subjects to enroll (comma separated numbers):")
    subjects = college_subjects[college]
    for idx, subj in enumerate(subjects, 1):
        print(f"[{idx}] {subj.code} - {subj.name} ({subj.units} units, {subj.schedule})")
    subj_choices = input("Enter choices: ").split(',')
    for c in subj_choices:
        try:
            student.enroll_subject(subjects[int(c.strip())-1])
        except:
            pass
    section.add_student(student)
    students.append(student)
    print("\n--- Enrollment Summary ---")
    student.display_info()

def instructor_login():
    print("\n--- Instructor Login ---")
    username = input("Username: ")
    password = input("Password: ")
    found = None
    for inst in instructors:
        if inst.username == username and inst.password == password:
            found = inst
            break
    if found:
        print(f"\nWelcome, {found.name}!")
        while True:
            print("\n[1] View Day Schedule (Table)")
            print("[2] Select College")
            print("[3] Logout")
            choice = input("Enter your choice: ")
            if choice == '1':
                found.display_classes(course_to_college, sections_per_course, detail_level=1) 
            elif choice == '2':
                # Show all colleges and prompt for selection
                colleges = list(set(course_to_college.values()))
                print("\nSelect a college:")
                for idx, college in enumerate(colleges, 1):
                    print(f"[{idx}] {college}")
                try:
                    sel = int(input("Enter college number: ")) - 1
                    if 0 <= sel < len(colleges):
                        selected_college = colleges[sel]
                        print(f"You selected: {selected_college}")
                        # Show courses for this college
                        courses = [course for course, col in course_to_college.items() if col == selected_college]
                        if not courses:
                            print("No courses for this college.")
                        else:
                            print("Select a course:")
                            for idx, course in enumerate(courses, 1):
                                print(f"[{idx}] {course}")
                            try:
                                course_sel = int(input("Enter course number: ")) - 1
                                if 0 <= course_sel < len(courses):
                                    selected_course = courses[course_sel]
                                    print(f"You selected: {selected_course}")
                                    # Show sections for this course
                                    sections = sections_per_course[selected_course]
                                    print("Sections and Enrolled Students:")
                                    for section in sections:
                                        print(f"- Section {section.name}")
                                        if section.students:
                                            for student in section.students:
                                                print(f"    - {student.name} ({student.student_id})")
                                        else:
                                            print("    No students enrolled.")
                                else:
                                    print("Invalid course selection.")
                            except ValueError:
                                print("Invalid input.")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input.")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid credentials.")

def view_all_students():
    print("\n--- All Enrolled Students ---")
    if not students:
        print("No students enrolled yet.")
        return
    for idx, student in enumerate(students, 1):
        print(f"{idx}. {student.name} ({student.student_id}) - Section {student.class_section} ({student.college})")

if __name__ == "__main__":
    main_menu()
