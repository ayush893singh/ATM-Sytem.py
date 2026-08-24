balance = 0
while True:
    print("\nATM Menu :- ")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Choose Option : ")
    if choice == "1":
        print("Balance :", balance)
    elif choice == "2":
        amount = int(input("Enter Amount : "))
        balance += amount
        print("Money Deposited")
    elif choice == "3":
        amount = int(input("Enter Amount : "))
        if amount <= balance:
            balance -= amount
            print("Money Withdrawn")
        else:
            print("Insufficient Balance")
    elif choice == "4":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")