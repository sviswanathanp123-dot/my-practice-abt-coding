print("WELCOME TO SIMPLE ATM")

pin = 1234
balance = 10000

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    print("\nLogin successful")

    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 3:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Amount deposited")
        print("Updated balance:", balance)

    else:
        print("Invalid choice")

else:
    print("Wrong PIN")

print("\nThank you for using ATM 😊")



