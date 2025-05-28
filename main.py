import json
import re
import os
from Section import Section
from Subject import Subject
from Instructor import Instructor
from Student import Student

# Data loading
with open('subjects.json') as f:
    subjects_data = json.load(f)
with open('course_college.json') as f:
    course_college = json.load(f)

# Build in-memory Subject objects per college
subject_map = {
    college: [Subject(s['code'], s['name'], s['units'], s['schedule'])
            for s in subs]
    for college, subs in subjects_data.items()
}

# Build Section objects per course
sections_per_course = {
    course: [Section('A'), Section('B'), Section('C')]
    for course in course_college
}

#Instructor setup
instructor = Instructor('Sir Charles Bautista', 'cbautista', 'password123')
for secs in sections_per_course.values():
    for sec in secs:
        instructor.assign_section(sec)
instructors = [instructor]

class Arraylist:    #Arraylist
    def __init__(self):
        self.all_students=[]
    def append(self,data):
        self.all_students.append(data)

    def getAll(self):
        return self.all_students
    
all_students = Arraylist()
STORAGE_FILE = 'student_enroll.json'

def save_subjects():
    """Persist current subject_map back to subjects.json."""
    data = {
        college: [
            {'code': s.code, 'name': s.name, 'units': s.units, 'schedule': s.schedule}
            for s in subs
        ]
        for college, subs in subject_map.items()
    }
    with open('subjects.json', 'w') as f:
        json.dump(data, f, indent=2)

def load_students():
    """Load enrolled students from STORAGE_FILE into memory and Sections."""
    if not os.path.isfile(STORAGE_FILE):
        return
    with open(STORAGE_FILE) as f:
        data = json.load(f)
    for e in data:
        s = Student(
            e['student_id'], e['name'], e['college_course'],
            e['college'], e['academic_year'], e['class_section']
        )
        # restore subjects
        for code in e.get('subjects', []):
            for subj in subject_map.get(e['college'], []):
                if subj.code == code:
                    s.enroll_subject(subj)
                    break
        all_students.append(s)
        # reattach to Section
        for sec in sections_per_course.get(s.course, []):
            if sec.name == s.class_section:
                sec.add_student(s)
                break

def save_students():
    """Persist current all_students list to STORAGE_FILE."""
    out = []
    for s in all_students.getAll():
        out.append({
            'student_id'    : s.student_id,
            'name'          : s.name,
            'college_course': s.course,
            'college'       : s.college,
            'academic_year' : s.academic_year,
            'class_section' : s.class_section,
            'subjects'      : [sub.code for sub in s.subject_list]
        })
    with open(STORAGE_FILE, 'w') as f:
        json.dump(out, f, indent=2)

# Load existing enrollments on startup
load_students()

# Menu routines

def student_enrollment():
    print("\n=== Student Enrollment ===")
    # Name validation
    name = input("Enter name: ").strip()
    if not re.fullmatch(r"[A-Za-z ]+", name): #Pattern for text validation
        print("Error: letters and spaces only.\n"); return
    if any(s.name.lower() == name.lower() for s in all_students.getAll()):
        print(f"Error: '{name}' already enrolled.\n"); return

    # ID validation
    sid = input("Enter ID (digits only): ").strip()
    if not sid.isdigit():
        print("Error: numeric only.\n"); return

    # Course selection
    courses = list(course_college)
    for i, c in enumerate(courses, 1):
        print(f"  {i}. {c}")
    try:
        course = courses[int(input("Choice: ")) - 1]
    except:
        print("Invalid choice.\n"); return
    college = course_college[course]

    # Section selection
    secs = sections_per_course[course]
    for i, sec in enumerate(secs, 1):
        print(f"  {i}. Section {sec.name}")
    try:
        section = secs[int(input("Choice: ")) - 1]
    except:
        print("Invalid choice.\n"); return

    # Academic year
    year = input("Academic year (e.g. 1st Year): ").strip()

    # Create & register
    student = Student(sid, name, course, college, year, section.name)
    all_students.append(student)
    section.add_student(student)

    # Subject selection (3–8 distinct)
    subs = subject_map[college]
    while True:
        for i, sub in enumerate(subs, 1):
            print(f"  {i}. {sub.code} – {sub.name}")
        picks = input("Choose 3–8 subjects (comma-separated numbers): ").split(',')
        idxs = set()
        for p in picks:
            try:
                idx = int(p.strip()) - 1
                if 0 <= idx < len(subs):
                    idxs.add(idx)
            except:
                pass
        if len(idxs) < 3: # min
            print("Pick at least 3 subjects."); continue
        if len(idxs) > 8: # max
            print("Pick at most 8 subjects."); continue
        for idx in idxs:
            student.enroll_subject(subs[idx])
        break

    save_students()
    print("\n Enrollment successful.\n")
    student.display_info()
    print()

def instructor_login():
    print("\n=== Instructor Login ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    inst = next((i for i in instructors
                if i.username == username and i.password == password), None)
    if not inst:
        print("Login failed.\n"); return

    # Instructor submenu loop
    while True:
        print(f"\nWelcome, {inst.name}!")
        print("  1. View my classes (detailed)")
        print("  2. View classes by college only")
        print("  3. Logout")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            inst.display_classes(course_college, sections_per_course, detail_level=1)
        elif choice == '2':
            inst.display_classes(course_college, sections_per_course, detail_level=0)
        elif choice == '3':
            print("Logging out...\n")
            break
        else:
            print("Invalid option.\n")

def view_all_students():
    if not all_students.getAll():
        print("\nNo students enrolled.\n"); return
    print("\n=== All Enrolled Students ===")
    for s in all_students.getAll():
        print(f"• {s.name} (ID: {s.student_id}) — {s.course}, Section {s.class_section}")
    print()

def add_subject():
    print("\n=== Add New Subject ===")
    colleges = list(subject_map)
    for i, col in enumerate(colleges, 1):
        print(f"  {i}. {col}")
    try:
        college = colleges[int(input("Choose college number: ")) - 1]
    except:
        print("Invalid college choice.\n"); return

    code = input("Enter subject code: ").strip()
    name = input("Enter subject name: ").strip()
    while True:
        u = input("Enter units (integer): ").strip()
        if u.isdigit():
            units = int(u)
            break
        print("Units must be a number.")
    schedule = input("Enter schedule (e.g. MWF 8-9am): ").strip()

    new_sub = Subject(code, name, units, schedule)
    subject_map[college].append(new_sub)
    save_subjects()
    print(f"Added {code} – {name} to {college}.\n")

def main_menu():
    while True:
        print("1. Enroll Student")
        print("2. Instructor Login")
        print("3. View All Students")
        print("4. Add Subject")
        print("5. Exit")
        choice = input("Choice: ").strip()

        if choice == '1':
            student_enrollment()
        elif choice == '2':
            instructor_login()
        elif choice == '3':
            view_all_students()
        elif choice == '4':
            add_subject()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid.\n")

if __name__ == '__main__':
    main_menu()
