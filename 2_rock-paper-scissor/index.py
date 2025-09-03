# Ask the user to make choice
# If choice is not valid
# print Error
# Let the computer to make a choice
# Print choices (emojis)
# Determine the winner
# ASk the user if they want to continue
# if not
# Terminate


import random


emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices = ('r', 'p', 's')

while True:
    user_choice = input("Rock, Paper, Or scissors?  (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choices")
        continue

    computer_choice = random.choice(choices)

    print(f"You choose {emojis[user_choice]}")  
    print(f"Computer choose {emojis[computer_choice]}")   

    if user_choice == computer_choice:
        print("Tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's')or
        (user_choice == 's' and computer_choice == 'p')or
        (user_choice == 'p' and computer_choice == 'r')):
        print('You Win')
    else:
        print("You Lose")    

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break