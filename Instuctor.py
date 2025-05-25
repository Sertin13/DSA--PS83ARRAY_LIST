class Instructor:
    def __init__(self, full_name, user_name, user_password):
        self.full_name = full_name
        self.user_name = user_name
        self.user_password = user_password
        self.assigned_sections = []

    def assign_section(self, section):
        self.assigned_sections.append(section)