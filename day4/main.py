from internship_system import InternshipSystem

system = InternshipSystem()

while True:

    print("\n========== AI Internship Dashboard ==========")

    print("1. Register Intern")

    print("2. Assign Task")

    print("3. Update Task Status")

    print("4. Search Intern")

    print("5. View Pending Tasks")

    print("6. View Completed Tasks")

    print("7. Top Performer")

    print("8. Save Data")

    print("9. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        system.register_intern()

    elif choice == "2":

        system.assign_task()

    elif choice == "3":

        system.update_task()

    elif choice == "4":

        system.search()

    elif choice == "5":

        system.pending_tasks()

    elif choice == "6":

        system.completed_tasks()

    elif choice == "7":

        system.top_performer()

    elif choice == "8":

        system.save_records()

    elif choice == "9":

        system.save_records()

        print("Good Bye")

        break

    else:

        print("Invalid Choice")
