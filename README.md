# ATM Program 
A simple ATM simulation program built in Python.

## Technologies Used
Python 3.x

## How It Works

1. Program starts with balance = 0
2. A menu is shown with 4 options
3. User selects an option by entering 1, 2, 3, or 4
4. **Check Balance** - Shows current balance
5. **Deposit Money** - Adds entered amount to balance
6. **Withdraw Money** - Deducts amount if sufficient balance exists
7. **Exit** - Ends the program
8. If wrong option is entered, it shows "Invalid Choice"

## Code
```python
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
```

## -----Output-----
```
ATM Menu :- 
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose Option : 2
Enter Amount : 5000
Money Deposited

ATM Menu :- 
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose Option : 1
Balance : 5000

ATM Menu :- 
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose Option : 3
Enter Amount : 2000
Money Withdrawn

ATM Menu :- 
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose Option : 4
Thank You!
```

## Author
[Ayush Singh
GitHub:@ayush893singh](https://github.com/ayush893singh)
