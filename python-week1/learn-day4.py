# import random

# random_integer = random.randint(1,50)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# city_of_taiwan = ["Taipei","Taitung","Tainan"]
# # city_of_taiwan.append("Pingtung")

# city_of_taiwan.extend(["Pingtung","Hualian"]) 
# print(city_of_taiwan)

# import random
# names= ["Taipei","Taitung","Tainan"] 
# random_name = random.choice(names)
# print(random_name)
import random
paper ="📄"
scissors = "✂"
rock ="🌑"

game_img =[rock, paper, scissors]

user_choice = int(input("Waht do you choose? Type 0 for Rock, 1 for Paper or  2 for Scissors.\n"))
if user_choice >=3 or user_choice <0:
    print("You typed an invalid number.")
else:
    print(game_img[user_choice])


    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_img[computer_choice])


    if user_choice == 0 and computer_choice ==2:
        print("YOu win!")
    elif computer_choice ==0 and user_choice ==2:
        print("You lose")
    elif computer_choice >user_choice:
        print("You lose")
    elif user_choice >computer_choice:
        print("You win!")
    elif computer_choice == user_choice :
        print("It's a draw")
