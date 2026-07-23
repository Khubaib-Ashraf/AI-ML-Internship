# Task 3: Inheritance (Person -> Student, Teacher)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)
        self.student_id = student_id

    def study(self):
        print(self.name, "is studying.")
        print("Student ID:", self.student_id)


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

    def teach(self):
        print(self.name, "is teaching", self.subject)


# Main Program
student = Student("Ali", 20, "AI123")
teacher = Teacher("Ahmed", 40, "Python")
student2 = Student("Zain", 18, "AI122")
teacher2 = Teacher("Hassan", 30, "C++")
student3 = Student("Ahmed", 20, "AI123")
teacher3 = Teacher("Omer", 40, "Java")
student.introduce()
student.study()
student2.introduce()
student2.study()
student3.introduce()
student3.study()
print()
teacher.introduce()
teacher.teach()
teacher2.introduce()
teacher2.teach()
teacher3.introduce()
teacher3.teach()
