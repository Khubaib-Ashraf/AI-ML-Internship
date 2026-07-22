
# Global list to store student dictionaries
students_db = []
next_id = 1

def add_student():
    global next_id
    print("\n--- Add New Student ---")
    name = input("Enter Name: ").strip()
    try:
        age = int(input("Enter Age: "))
        grade = input("Enter Grade (e.g., A, B, C): ").strip().upper()
    except ValueError:
        print("Error: Age must be a number. Student not added.")
        return

    student = {
        "id": next_id,
        "name": name,
        "age": age,
        "grade": grade
    }
    students_db.append(student)
    next_id += 1
    print(f"Success: {name} added with ID {student['id']}.")

def view_students():
    print("\n--- All Students ---")
    if not students_db:
        print("No students found.")
        return
    
    print(f"{'ID':<5} | {'Name':<15} | {'Age':<5} | {'Grade':<5}")
    print("-" * 35)
    for s in students_db:
        print(f"{s['id']:<5} | {s['name']:<15} | {s['age']:<5} | {s['grade']:<5}")

def search_student():
    print("\n--- Search Student ---")
    try:
        search_id = int(input("Enter Student ID to search: "))
    except ValueError:
        print("Error: ID must be a number.")
        return

    for s in students_db:
        if s["id"] == search_id:
            print(f"Found: ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
            return
    print("Student not found.")

def update_student():
    print("\n--- Update Student ---")
    try:
        update_id = int(input("Enter Student ID to update: "))
    except ValueError:
        print("Error: ID must be a number.")
        return

    for s in students_db:
        if s["id"] == update_id:
            print(f"Updating record for {s['name']}")
            s["name"] = input(f"New Name ({s['name']}): ").strip() or s["name"]
            try:
                age_input = input(f"New Age ({s['age']}): ")
                s["age"] = int(age_input) if age_input else s["age"]
            except ValueError:
                print("Invalid age. Keeping old age.")
                
            s["grade"] = input(f"New Grade ({s['grade']}): ").strip().upper() or s["grade"]
            print("Record updated successfully!")
            return
    print("Student ID not found.")

def delete_student():
    print("\n--- Delete Student ---")
    try:
        delete_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Error: ID must be a number.")
        return

    for i, s in enumerate(students_db):
        if s["id"] == delete_id:
            removed = students_db.pop(i)
            print(f"Successfully deleted {removed['name']}.")
            return
    print("Student ID not found.")

def main():
    """Main loop to run the Student Management System."""
    print("Welcome to the Student Management System!")
    while True:
        print("\n1. Add Student | 2. View All | 3. Search | 4. Update | 5. Delete | 6. Exit")
        choice = input("Select an option (1-6): ").strip()

        if choice == '1': add_student()
        elif choice == '2': view_students()
        elif choice == '3': search_student()
        elif choice == '4': update_student()
        elif choice == '5': delete_student()
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()
