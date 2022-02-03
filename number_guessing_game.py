import random

print("guess a number between 1 to 100")
lives = 0
correct_choice = False
while not correct_choice:
    user_input = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if user_input == "easy":
        lives = 10
        correct_choice = True
    elif user_input == "hard":
        lives = 5
        correct_choice = True
    else:
        print("Please type in a valid input 'easy' or 'hard'")


random_choice = random.randint(1,100)

game_over = False
while not game_over:
    print(f"You have {lives} attempts remaining to guess the number.")
    if lives == 0:
        game_over = True
    else:
        user_guess = int(input("Make a guess: "))
        if user_guess > random_choice:
            lives -=1
            print("Too high")
        elif user_guess < random_choice:
            lives -=1
            print("Too low")
        else:
            game_over = True
            print(f"You got it! The answer was {user_guess}")
    if user_guess == random_choice:
        pass
    elif lives != 0: 
        print("guess again")        




