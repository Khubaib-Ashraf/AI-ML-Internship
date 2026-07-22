def basic_student_records():
    records = []
    records.append({"name": "Alice", "age": 20, "major": "CS"})
    records.append({"name": "Bob", "age": 22, "major": "Math"})
    records.append({"name": "Ali", "age": 23, "major": "AI"})
    records.append({"name": "Zain", "age": 19, "major": "SSC"})
    # Search
    search_name = input("Search student: ").lower()
    for student in records:
        if student["name"].lower() == search_name:
            print(f"Found: {student}")
            break
    else:
        print("Student not found.")

basic_student_records()
