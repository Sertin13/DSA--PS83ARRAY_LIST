class Instructor:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.sections = []

    def assign_section(self, section):
        self.sections.append(section)

    def display_classes(self, course_to_college, sections_per_course, detail_level=1):
        print(f"\n--- Classes for Instructor: {self.name} ---")
        for course, sections in sections_per_course.items():
            for section in sections:
                if section.instructor == self:
                    print(f"\nCourse: {course} ({course_to_college.get(course, 'Unknown College')}) - Section {section.name}")
                    if detail_level > 0:
                        if not hasattr(section, 'students') or not section.students:
                            print("  No students enrolled.")
                        else:
                            for student in section.students:
                                print(f"  Student: {student.name} ({student.student_id})")
                                if student.subject_list:
                                    print("    Enrolled Subjects:")
                                    for subj in student.subject_list:
                                        print(f"      - {subj.code}: {subj.name} ({subj.units} units, {subj.schedule})")
                                else:
                                    print("    No subjects enrolled.")