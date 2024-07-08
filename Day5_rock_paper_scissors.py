import random

cpu = ['rock', 'paper', 'scissors']

welcome = input("Welcome to rock-paper-scissors, do you want to play? y/n: ").strip().lower()
if welcome == "y":
    user = input("Rock, Paper, Scissors. Choose one: ").strip().lower()
    answer = random.choice(cpu)
    if user not in cpu:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    else:
        if user == answer:
            print(f"It was a draw. CPU also chose {answer}.")
        elif (user == "rock" and answer == "paper") or \
             (user == "paper" and answer == "scissors") or \
             (user == 'scissors' and answer == "rock"):
            print(f"You lose. CPU chose {answer}.")
        else:
            print(f"You win! CPU chose {answer}.")
elif welcome == "n":
    print("Thank you for playing.")
else:
    print("Invalid input. Please enter 'y' to play or 'n' to exit.")
