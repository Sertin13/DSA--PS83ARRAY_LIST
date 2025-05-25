class Instructor:
    def __init__(self, name, username, password):
        """
        Initialize an Instructor with basic credentials and an empty list of assigned sections.
        """
        self.name = name
        self.username = username
        self.password = password
        self.sections = []