def simple_atm():
    balance = 1000.0
    while True:
        print(f"\nCurrent Balance: ${balance:.2f}")
        print("1. Check Balance | 2. Deposit | 3. Withdraw | 4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '4': break
        try:
            if choice == '1': continue
            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                balance += amount if amount > 0 else 0
            elif choice == '3':
                amount = float(input("Enter withdraw amount: "))
                if amount > balance: print("Insufficient funds!")
                else: balance -= amount
            else: print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")

simple_atm()
