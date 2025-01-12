import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissor"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit\t:").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_num = random.randint(0,2)
    #0=Rock, 1= Paper, 2= Scissors
    computer_pick = options[random_num]
    print("Computer picked",computer_pick+".")
    if user_input == "rock" and computer_pick == "scissors":
        print("YOu won!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == computer_pick:
        print("Tie!")
        continue
    else:
        print("Computer won!")
        computer_wins += 1
        continue 
print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")
print("Goodbye!")
    
    
