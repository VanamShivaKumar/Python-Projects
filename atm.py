balance = 5000
correct_pin = 1234
transactions = []
print("Welcome to ATM")
card = input("Insert your card (press enter): ")
print("1. English")
print("2. Telugu")
print("3. Hindi")
lang = int(input("Select language: "))
pin = int(input("Enter your PIN: "))
if pin == correct_pin:
    print("Login Successful")
    while True:
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit")
        print("4. Mini Statement")
        print("5. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            print("Your balance is:", balance)
        elif option == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                transactions.append(f"Withdraw: {amount}")
                print("Please collect your cash")
                print("Remaining balance:", balance)
            else:
                print("Insufficient Balance")
        elif option == 3:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            transactions.append(f"Deposit: {amount}")
            print("Amount deposited successfully")
            print("Updated balance:", balance)
        elif option == 4:
            print("Mini Statement")
            if transactions:
                for t in transactions:
                    print(t)
            else:
                print("No transactions yet")
        elif option == 5:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid option")
else:
    print("Incorrect PIN")
