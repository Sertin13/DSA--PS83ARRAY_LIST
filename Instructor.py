class Instructor:
    def __init__(self, name, username, password):
        self.name     = name
        self.username = username
        self.password = password
        self.sections = []

    def assign_section(self, section):
        self.sections.append(section)

    def display_classes(self, course_to_college, sections_per_course, detail_level=0):
        # Build map: college_name → [Section, ...]
        college_to_sections = {}
        for course, secs in sections_per_course.items():
            college = course_to_college.get(course, "Unknown College")
            for sec in secs:
                if sec in self.sections:
                    college_to_sections.setdefault(college, []).append(sec)

        print(f"\nClasses for {self.name}:\n")
        if not college_to_sections:
            print("No sections assigned.\n")
            return

        for college, secs in college_to_sections.items():
            print(f"--- {college} ---")
            for sec in secs:
                # Always display section name
                print(f"  Section {sec.name}")

                # Only show students (and subjects) if detail_level ≥ 1
                if detail_level >= 1:
                    if not sec.students:
                        print("    (no students)")
                    else:
                        for student in sec.students:
                            print(f"    - {student.name} (ID: {student.student_id})")
                            # List each subject
                            if student.subject_list:
                                for subj in student.subject_list:
                                    print(f"       * {subj.code} – {subj.name}"
                                        f" ({subj.units} units, {subj.schedule})")
                            else:
                                print("       (no subjects)")
            print()  # blank line between colleges
