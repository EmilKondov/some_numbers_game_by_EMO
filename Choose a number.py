import random
small_counter = 0
big_counter = 0
computer_number = int(random.randint(1, 100))


while True:
    is_found = False
    small_counter += 1
    player_input = input("Guess the  number between (1 and 100) that the computer has chosen: ")
    if small_counter > 2:
        print("""
        You have only three tries!
        Now you should try again!
        Sorry :) :) :) :) :) :) :) 
        """)
        small_counter = 0
        continue
    if not player_input.isdigit() or int(player_input) < 0 or int(player_input) > 100:
        print("Invalid input please try again ")
        small_counter = 0
        continue
    else:
        player_input = int(player_input)
        computer_number = int(computer_number)
        if player_input == computer_number:
            print("Congratulations! You gessued the number")
            is_found = True
            break
        elif player_input < computer_number:
            print("Too Low!")
        elif player_input > computer_number:
            print("Too High!")

if is_found:
    print("You won!")