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