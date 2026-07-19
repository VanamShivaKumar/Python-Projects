Num1 = int(input("Enter A Number:-"))
Result = Num1
Operation = ['+','-','*','/','%',"="]
print("Enter Your Operator From below List")
print("+ :- Addition")
print("- :- Subtraction")
print("* :- Multiplication")
print("/ :- Divide")
print("% :- Percentage")
print("= :- Final Result")
print("== -- > To Exit The Calculator")


while True:
    
    Option = input("Enter Your Operator:- ")
    if Option not in Operation:
        print("Invalid Input")
    elif Option in "=":
        print(f"Final Result is  {Result}")
        

    elif Option == "+":
            Num2 = int(input("Enter Value:"))
            Result = Num1+Num2
            print("Current Result is :-",Result)

    elif Option == "-":
            Num2 = int(input("Enter Value:"))
            Result = Num1-Num2
            print("Current Result is :-",Result)
    
    elif Option == "*":
            Num2 = int(input("Enter Value:"))
            Result = Num1*Num2
            print("Current Result is :-",Result)
    
    elif Option == "/":
            Num2 = int(input("Enter Value:"))
            Result = Num1/Num2
            if Num2 == 0:
                print("Number Can't Be Divided By Zero")
            else:
                print("Current Result is :-",Result)

    elif Option == "%":
            Num2 = int(input("Enter Value:"))
            Result =  (Num1/Num2)*100
            print("Current Result is :-",Result)
    elif Option == "==":
        print("Exiting The Calculator")
        break

        

    