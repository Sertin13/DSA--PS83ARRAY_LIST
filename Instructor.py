class Instructor:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.sections = []

    def assign_section(self, section):
        self.sections.append(section)


    def display_classes(self, course_to_college, sections_per_course, detail_level=0):
        print(f"\nClasses for {self.name}:\n")
        if not course_to_college or not sections_per_course:
            print("Error: Course-to-college or sections-per-course data is missing.")
            return

        college_to_sections = {}
        for course, college in course_to_college.items():
            college_to_sections.setdefault(college, []).extend(sections_per_course.get(course, []))

        for college, sections in college_to_sections.items():
            print(f"\n{college:<30}")
            any_students_in_college = False  # Flag to check if any students are in this college
            for section in sections:
                print(f"  Section {section.name:<15}")
                if section.students:
                    any_students_in_college = True
                    for student in section.students:
                        print(f"    - {student.name:<25} ({student.student_id})")
                        if detail_level >= 1:
                            for subject in student.subjects:
                                print(f"       * {subject.code:<8} {subject.name:<25} ({subject.units} units, {subject.schedule})")
            if not any_students_in_college:
                print("  No students enrolled in any sections in this college.")