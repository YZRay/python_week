import random
import hangman_art
import hangman_words

print(hangman_art.logo)


word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
lives = 6 
blank_list= []
for i in range(len(chosen_word)):
    blank_list.append("_")


end_of_game = False
while not end_of_game: 
    guess = input("Guess a letter: ").lower()
    
    if guess in blank_list:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            blank_list[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    
    
    if "_" not in blank_list:
        end_of_game = True
        print("You Win!")
    print(blank_list)
    print(hangman_art.stages[lives])    
