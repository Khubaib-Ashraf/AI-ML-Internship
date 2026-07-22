def calculate_grade():
    while True:
        try:
            marks = int(input("Enter student's marks (0-100): "))

            if marks < 0 or marks > 100:
                print("Invalid input! Marks must be between 0 and 100.")
                continue

            if 90 <= marks <= 100:
                grade = 'A'
            elif 80 <= marks < 90:
                grade = 'B'
            elif 70 <= marks < 80:
                grade = 'C'
            elif 60 <= marks < 70:
                grade = 'D'
            else:
                grade = 'F'

            print(f"Marks: {marks} | Grade: {grade}")
            break   # Exit after valid input

        except ValueError:
            print("Invalid input. Please enter a number.")

calculate_grade()
