import random

guess = random.randint(0, 10)

welcome = input("Welcome to the Number Guessing Game, do you want to play? y/n: ").strip().lower()
if welcome == "y":
    try:
        user_input = int(input("Guess a number between 0 to 10: ").strip())
        if user_input == guess:
            print("You have guessed the right number!")
        elif user_input > guess:
            print(f"Your guess was too high. The correct number was {guess}.")
        elif user_input < guess:
            print(f"Your guess was too low. The correct number was {guess}.")
    except ValueError:
        print("Please enter a valid number between 0 and 10.")
elif welcome == "n":
    print("Thanks for playing.")
else:
    print("Please enter 'y' or 'n'.")
