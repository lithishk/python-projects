import random


# Variable Initialization
user_points = 0
computer_points = 0

print("----Welcome to Rock Paper Scissors!----")


#Function to choose rock paper or scissor
def get_choice_name(choice):
    choices = {0: "Rock", 1: "Paper", 2: "Scissors"}
    return choices[choice]


#Function to get player name
def player_details():
    while True:
        player_name = input("Enter your name: ")
        if len(player_name) < 3:
            print("Please enter a valid name")
            continue

        if not all(c.isalpha() or c == ' ' for c in player_name):
            print("Invalid! Please enter a valid name.")
            continue
        break
    return player_name



#Function to choose number of rounds
def round_details():
    while True:
        try:
            rounds = int(input("Enter number of rounds: "))
            if rounds <= 0:
                print("Invalid input! Enter a number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
    print(f"You are selected to play {rounds} rounds.")
    return rounds


name = player_details()
num_rounds = round_details()


#Code for the game
def game_process():
    global user_points
    global computer_points
    computer_choice = random.randint(0, 2)
    while True:
        try:
            user_choice = int(input("\nEnter 0-Rock  1-Paper  2-Scissors: "))
            if user_choice < 0 or user_choice > 2:
                print("Enter 0, 1, or 2 only!")
                continue
            break
        except ValueError:
            print("Enter 0, 1, or 2 only!.")
            continue

    print(f"You chose: {get_choice_name(user_choice)}")
    print(f"Computer chose: {get_choice_name(computer_choice)}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win! ")
        user_points += 1
    else:
        print("You lose! ")
        computer_points += 1

    print(f"\nScore → {name}: {user_points} | Computer: {computer_points}")



for i in range(num_rounds):
    print(f"\nRound {i + 1}")
    if __name__== "__main__":
        game_process()



print(f"\nFinal Score → {name}: {user_points} | Computer: {computer_points}")

if user_points > computer_points:
    print(f"Congratulations! {name} you won the game! ")
elif user_points < computer_points:
    print(f"Computer won the game! Better luck next time {name}! ")
else:
    print("Overall it's a draw! ")




