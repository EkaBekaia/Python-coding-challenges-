class Student:
    def __init__(self, name, roll_number, grade):
        # Initialize student information (name, roll_number, grade)
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def __str__(self):
        # Return string with student's details
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        # Empty list of students
        self.students = []

    def add_student(self):
        # Asking user for student details
        name = input("Enter student's name: ").strip()

        # Validate roll number input
        roll_number = input("Enter roll number (3 digits): ").strip()

        # Check if roll number has exactly 3 digits
        while not (roll_number.isdigit() and len(roll_number) == 3):  # Ensure it's 3 digits
            print("Invalid roll number. Please enter a valid 3-digit roll number from your student card")
            roll_number = input("Enter roll number: ").strip()

        # Check if roll number already exists (uniqueness check)
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Roll number {roll_number} is already taken. Please enter a unique roll number")
                return

        # Validate grade input (A, B, C, D, F)
        grade = input("Enter student's grade (A, B, C, D, F): ").strip().upper() 
        while grade not in ['A', 'B', 'C', 'D', 'F']: 
            print("Invalid grade. Please enter a valid grade (A, B, C, D, F).")
            grade = input("Enter student's grade (A, B, C, D, F): ").strip().upper()

        # Create new student object and add it to the students list
        new_student = Student(name, roll_number, grade)
        self.students.append(new_student)
        print("Student added successfully.")

    def view_all_students(self):
        # Notify user if no student exists
        if not self.students:
            print("No students to display.")
            return
        
        # Display details of all students
        for student in self.students:
            print(student)

    def search_student(self):
        # Ask for roll number to search for a student
        roll_number = input("Enter roll number to search (exactly 3 digits): ").strip()

        # Validate the roll number to ensure it's exactly 3 digits
        while not (roll_number.isdigit() and len(roll_number) == 3):  
            print("Invalid roll number. Please enter a valid 3-digit roll number.")
            roll_number = input("Enter roll number to search (exactly 3 digits): ").strip()
        
        found = False
        # Search for the student by roll number
        for student in self.students:
            if student.roll_number == roll_number:
                print(student)  
                found = True
                break

        if not found:
            print(f"Student with roll number {roll_number} does not exist.")
            add_student = input("Would you like to add this student to the list? (yes/no): ").strip().lower()
            if add_student == "yes":
                self.add_student()  
            else:
                print("Student not added")

    def update_student_grade(self):
        # Ask for roll number to update grade
        roll_number = input("Enter roll number to update grade (exactly 3 digits): ").strip()

        # Validate the roll number to ensure it's exactly 3 digits
        while not (roll_number.isdigit() and len(roll_number) == 3):
            print("Invalid roll number. Please enter a valid 3-digit roll number.")
            roll_number = input("Enter roll number to update grade (exactly 3 digits): ").strip()

        found = False
        # Search for the student by roll number
        for student in self.students:
            if student.roll_number == roll_number:
                grade = input("Enter new grade (A, B, C, D, F): ").strip().upper()
                while grade not in ['A', 'B', 'C', 'D', 'F']:  
                    print("Invalid grade. Please enter a valid grade (A, B, C, D, F).")
                    grade = input("Enter new grade (A, B, C, D, F): ").strip().upper()
                student.grade = grade 
                print("Grade updated successfully.")
                found = True
                break

        if not found:
            print("Student not found. Please enter a valid roll number.")

    def menu(self):
        # User Menu 
        while True:
            print("\nStudent Management System")
            print("1. Add new student")
            print("2. View all students")
            print("3. Search student by roll number")
            print("4. Update student grade")
            print("5. Exit")

            choice = input("Enter choice: ").strip()

            # Menu options
            if choice == "1":
                self.add_student()  # Add a new student
            elif choice == "2":
                self.view_all_students()  # View all students
            elif choice == "3":
                self.search_student()  # Search student by roll number
            elif choice == "4":
                self.update_student_grade()  # Update student grade
            elif choice == "5":
                print("Exiting the system.")  # Exit the program
                break
            else:
                print("Invalid choice. Please try again.")  # Invalid option entered

system = StudentManagementSystem()
system.menu()
