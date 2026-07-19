import random as rand

AI = rand.randrange(1,101)
attempts = 0
#print(AI)

while True:

    user = int(input("Enter A Num To guess The AI :- "))

    if AI > user:
        print("AI Is Greater Than User")
    elif AI < user:
        print("AI is Lesser Than User")
    else:
        print("You Won")
        break

    attempts += 1
print(f"attempts Taken To Guess The AI is {attempts}")