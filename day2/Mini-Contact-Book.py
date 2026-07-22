def contact_book():
    contacts = {}
    while True:
        print("\n1. Add | 2. Search | 3. Update | 4. Delete | 5. Exit")
        choice = input("Choice: ")
        if choice == '5': break
        
        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            contacts[name] = phone
        elif choice == '2':
            name = input("Search Name: ")
            print(f"Phone: {contacts.get(name, 'Not found')}")
        elif choice == '3':
            name = input("Name to update: ")
            if name in contacts:
                contacts[name] = input("New Phone: ")
        elif choice == '4':
            name = input("Name to delete: ")
            contacts.pop(name, None)

contact_book()
