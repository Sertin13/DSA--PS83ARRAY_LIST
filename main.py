import json
from Student import Student
from Instructor import Instructor
from Subject import Subject
from Section import Section

# Simulate loading JSON files (no open used in visible logic)
def load_json(filename):
    file_obj = None
    try:
        file_obj = open(filename, 'r')
        data = json.load(file_obj)
    finally:
        if file_obj:
            file_obj.close()
    return data

# Load subjects and course-college map
subject_data = load_json('subjects.json')
course_to_college = load_json('course_to_college.json')

# Prepare subjects grouped by college
college_subjects = {}
for college in subject_data:
    subjs = []
    for item in subject_data[college]:
        subjs.append(Subject(item['code'], item['name'], item['units'], item['schedule']))
    college_subjects[college] = subjs

# Prepare sections for each course
section_names = ['A', 'B', 'C']
sections_per_course = {}

for course in course_to_college:
    group = []
    for name in section_names:
        group.append(Section(name))
    sections_per_course[course] = group

# Create instructor and assign to all sections
instructor_list = []
charles = Instructor('Sir Charles Bautista', 'Charles Bautista', '123456')
instructor_list.append(charles)

for course_sections in sections_per_course.values():
    for sec in course_sections:
        sec.instructor = charles
        charles.assign_section(sec)

# Track students
students = []

def show_main_menu():
    while True:
        print("\n===== 📚 ENROLLMENT PORTAL =====")
        print("1. ➕ Register Student")
        print("2. 👨‍🏫 Instructor Login")
        print("3. 👥 See All Students")
        print("4. ❌ Exit")
        option = input("Choose an option: ")

        if option == '1':
            register_student()
        elif option == '2':
            instructor_login()
        elif option == '3':
            list_all_students()
        elif option == '4':
            print("🚪 Exiting system. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

def register_student():
    print("\n🎓 Student Registration Form")
    sid = input("ID Number: ")
    name = input("Student Name: ")

    print("\nAvailable Courses:")
    course_keys = list(course_to_college.keys())
    for i in range(len(course_keys)):
        print(str(i+1) + ". " + course_keys[i])

    try:
        choice = int(input("Choose course: ")) - 1
        course = course_keys[choice]
        college = course_to_college[course]
    except:
        print("❗ Invalid selection.")
        return

    year = input("Enter Academic Year (e.g. 2024-2025): ")

    # Section choice
    print("\nPick your Section:")
    secs = sections_per_course[course]
    for i in range(len(secs)):
        print(str(i+1) + ". Section " + secs[i].name)
    try:
        sec_choice = int(input("Enter section number: ")) - 1
        section = secs[sec_choice]
    except:
        print("❗ Invalid section.")
        return

    # Create student object
    student = Student(sid, name, course, college, year, section.name)

    # Subject selection
    print("\n📖 Select Subjects:")
    available_subjects = college_subjects[college]
    for i in range(len(available_subjects)):
        subj = available_subjects[i]
        print(str(i+1) + ". " + subj.code + " - " + subj.name + " (" + str(subj.units) + " units, " + subj.schedule + ")")

    chosen = input("Enter subject numbers (comma-separated): ").split(',')

    for c in chosen:
        try:
            idx = int(c.strip()) - 1
            if idx >= 0 and idx < len(available_subjects):
                student.enroll_subject(available_subjects[idx])
        except:
            continue

    section.add_student(student)
    students.append(student)

    print("\n✅ Enrollment Complete!")
    student.display_info()

def instructor_login():
    print("\n🔐 Instructor Login")
    user = input("Username: ")
    pw = input("Password: ")

    current = None
    for i in instructor_list:
        if i.username == user and i.password == pw:
            current = i
            break

    if current != None:
        print("\n🎉 Welcome, " + current.name)
        while True:
            print("\n--- Instructor Dashboard ---")
            print("1. 📅 View Schedule")
            print("2. 🏫 View Colleges")
            print("3. 🔙 Logout")
            option = input("Choose: ")

            if option == '1':
                current.display_classes(course_to_college, sections_per_course, 1)
            elif option == '2':
                view_colleges()
            elif option == '3':
                break
            else:
                print("⚠️ Invalid option.")
    else:
        print("❌ Incorrect credentials.")

def view_colleges():
    print("\n🎓 List of Colleges:")
    colleges = []
    for course in course_to_college:
        col = course_to_college[course]
        if col not in colleges:
            colleges.append(col)

    for i in range(len(colleges)):
        print(str(i+1) + ". " + colleges[i])

    try:
        index = int(input("Select college number: ")) - 1
        selected_college = colleges[index]
    except:
        print("Invalid choice.")
        return

    print("\nCourses in " + selected_college + ":")
    courses = []
    for course in course_to_college:
        if course_to_college[course] == selected_college:
            courses.append(course)

    for i in range(len(courses)):
        print(str(i+1) + ". " + courses[i])

    try:
        course_index = int(input("Choose course: ")) - 1
        selected_course = courses[course_index]
    except:
        print("❗ Invalid input.")
        return

    print("\n📋 Sections in " + selected_course + ":")
    for sec in sections_per_course[selected_course]:
        print("Section " + sec.name)
        if len(sec.students) == 0:
            print("  (No students yet)")
        else:
            for stud in sec.students:
                print("  - " + stud.name + " [" + stud.student_id + "]")

def list_all_students():
    print("\n📚 Enrolled Students")
    if len(students) == 0:
        print("No student records found.")
        return

    for i in range(len(students)):
        s = students[i]
        print(str(i+1) + ". " + s.name + " - ID: " + s.student_id + " | Course: " + s.course + " | Section " + s.section)

# Start system
if __name__ == "__main__":
    show_main_menu()
