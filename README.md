# ATM-System.py
balance = 10000
pin = "1234"

user_pin = input("Enter PIN: ")

if user_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            print("Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter amount: "))
            balance += amount
            print("Money deposited")

        elif choice == "3":
            amount = int(input("Enter amount: "))
            if amount <= balance:
                balance -= amount
                print("Money withdrawn")
            else:
                print("Insufficient balance")

        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice")
else:
    print("Wrong PIN!!!!!!!!!!")
