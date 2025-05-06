def enroll_student():
    """Enrolls a student."""
    year_level = get_year_level()  # Function to get year level from user input
    if year_level == "Exit":
        return "Exit"
    fill_form()  # Function to handle form filling
    enroll_to_section(year_level)  # Function to enroll to a section

def enroll_to_section(year_level):
    """Enrolls student to a section."""
    section = choose_section(year_level) # Function to choose section
    if section == "Exit":
        return "Exit"
    save_data() # Function to save data


def get_year_level():
    """Gets the year level from the user."""
    print("Select Year Level:")
    #Show all year levels
    year_levels = ["Year 1", "Year 2", "Year 3", "Year 4"] #example
    for i, year in enumerate(year_levels):
        print(f"{i+1}. {year}")
    print("Exit")
    choice = input("Enter your choice: ")
    if choice == "Exit":
        return "Exit"
    try:
        return year_levels[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid input.")
        return get_year_level()


def choose_section(year_level):
    """Gets the section from the user."""
    print(f"Select Section for {year_level}:")
    # Show all sections in the selected year level
    sections = ["Section A", "Section B", "Section C"] #example
    for i, section in enumerate(sections):
        print(f"{i+1}. {section}")
    print("Exit")
    choice = input("Enter your choice: ")
    if choice == "Exit":
        return "Exit"
    try:
        return sections[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid input.")
        return choose_section(year_level)


def fill_form():
    """Handles the form filling process."""
    print("Fill up form...")
    # Add form filling logic here (get student details)


def view_students():
    """Views student data."""
    year_level = get_year_level()
    if year_level == "Exit":
        return "Exit"
    section = choose_section(year_level)
    if section == "Exit":
        return "Exit"
    #Show enrolled students in the selected section
    print(f"Enrolled students in {year_level}, {section}:")
    # Add logic to retrieve and display student data


def delete_student():
    """Deletes a student record."""
    year_level = get_year_level()
    if year_level == "Exit":
        return "Exit"
    section = choose_section(year_level)
    if section == "Exit":
        return "Exit"
    student = select_student(year_level, section) # Function to select student
    if student == "Exit" or student == "Cancel":
        return student
    confirm_deletion() # Function to confirm deletion
    save_data()


def select_student(year_level, section):
    """Selects a student to delete."""
    print(f"Select student to delete from {year_level}, {section}:")
    # Add logic to display students and get user selection
    # ... (Implementation to get student selection) ...
    print("Cancel")
    choice = input("Enter your choice: ")
    if choice == "Cancel":
        return "Cancel"
    elif choice == "Exit":
        return "Exit"
    # ... (Implementation to return selected student) ...


def confirm_deletion():
    """Confirms student deletion."""
    print("Confirm Deletion? (y/n)")
    choice = input()
    if choice.lower() != 'y':
        print("Deletion cancelled.")
        return "Cancel"


def save_data():
    """Saves data to storage."""
    print("Saving data...")
    # Add data saving logic here (save to file, database, etc.)


def main():
    """Main function to run the system."""
    while True:
        print("\nMain Menu:")
        print("1. Enroll")
        print("2. View")
        print("3. Delete/Unenroll")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            enroll_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()