AIWin =0
UserWin =0
import random as rand
while True:

    AI = rand.choice(["Rock","Paper","Scissors"])
    User = input("Enter Rock Or Paper Or Scissors :-")

    print(f"AI Choice is: {AI}")
    print(f"User Choice is: {User}")
    if User == AI:
        print("It's A Tie")

    elif (AI == "Paper" and User == "Rock") or \
        (AI == "Rock" and User == "Scissors") or \
        (AI == "Scissors" and User == "Paper"):
        print("AI Wins")
        AIWin +=1
        if AIWin == 3:
            print("AI won The Game")
    

    else:
        print("User Wins")
        UserWin += 1
        if AIWin == 3:
            print("User won The Game")
print(f"Score -> AI: {AIWin}, User: {UserWin}\n")