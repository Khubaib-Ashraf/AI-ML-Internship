# Create a Student Class with Attributes and Methods
class Student:
    def __init__(self, name, roll_number, department):
        self.name = name
        self.roll_number = roll_number
        self.department = department

    def display_info(self):
        return f"Name: {self.name}, Roll No: {self.roll_number}, Department: {self.department}"


if __name__ == "__main__":
    student1 = Student("Ali Akbar", "AI234455", "Artificial Intelligence")
    student2 = Student("Sami", "AI235732", "Artificial Intelligence")
    student3 = Student("Ali", "AI345677", "Artificial Intelligence")
    student4 = Student("Danish", "AI993344", "Artificial Intelligence")
    print(student1.display_info())
    print(student2.display_info())
    print(student3.display_info())
    print(student4.display_info())
