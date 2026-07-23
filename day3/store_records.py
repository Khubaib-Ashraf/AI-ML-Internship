class Student:
    def add_record(self):
        file = open("students.txt", "a")
        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        department = input("Enter Department: ")
        file.write(name + "," + roll + "," + department + "\n")
        file.close()
        print("Record Added Successfully.")
student = Student()
while True:
    print("\n1. Add Record")
    print("2. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        student.add_record()
    elif choice == "2":
        print("Program Closed.")
        break
    else:
        print("Invalid Choice.")
