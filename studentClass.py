class Student:
    # Constructor to initialize the attributes
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
    
    # Function to display all the attributes and their values
    def display_student_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")

# Example usage
student1 = Student(1, "John Doe", "10th Grade")
student1.display_student_details()

student2 = Student(2, "Jane Smith", "11th Grade")
student2.display_student_details()
