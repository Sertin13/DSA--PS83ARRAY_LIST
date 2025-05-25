class Instructor:
    def __init__(self, full_name, user_name, user_password):
        self.full_name = full_name
        self.user_name = user_name
        self.user_password = user_password
        self.assigned_sections = []

    def assign_section(self, section):
        self.assigned_sections.append(section)

    def display_classes(self, course_college_map, course_sections_map, detail_level=0):
        print(f"\nClasses for {self.full_name}:\n")
        if not course_college_map or not course_sections_map:
            print("Error: Course-to-college or sections-per-course data is missing.")
            return
        
        college_sections_map = {}
        for course, college in course_college_map.items():
            college_sections_map.setdefault(college, []).extend(course_sections_map.get(course, []))

        for college, sections in college_sections_map.items():
            print(f"\n{college:<30}")
            students_found = False  # Flag to check if any students are in this college
            for section in sections:
                print(f"  Section {section.name:<15}")
                if section.students:
                    students_found = True
                    for student in section.students:
                        print(f"    - {student.full_name:<25} ({student.student_id})")
                        if detail_level >= 1:
                            for subject in student.subjects:
                                print(f"       * {subject.code:<8} {subject.name:<25} ({subject.units} units, {subject.schedule})")
            if not students_found:
                print("  No students enrolled in any sections in this college.")
