import random


def game_start():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(0, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

    is_game_play = True
    life = 0
    if difficulty == "easy":
        life = 10
    elif difficulty == 'hard':
        life = 5

    print(f"You have {life} attempts remaining to guess the number.")
    while is_game_play:

        guess = int(input("Make a guess: "))

        if guess == number:
            is_game_play = False
            print("You win!")
        elif guess > number:
            print("Too hight")
            life -= 1
            print(f"You have {life} attempts remaining to guess the number.")
        elif guess < number:
            print("Too low")
            life -= 1
            print(f"You have {life} attempts remaining to guess the number.")

        if life == 0:
            print("you lose")
            is_game_play = False


game_start()
