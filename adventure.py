print('Welcome to my game!')
name = input('What is your name? ')
age = int(input('What is your age? '))
health = 100

if age >= 18:
    print(f'Welcome {name}, You are old enough to play, enjoy!')
    print("You have a total of", health, " Good luck!")

    wants_to_play = input('Do you want to play? ').lower()
    if wants_to_play == "yes":
        print("Let's play!")

        left_or_right = input("First choice.... Left or Right? (type left/right) ").lower()
        if left_or_right == "left":
            answer = input("Very well, you followed the path and reached the mountain entrance.... Do you go in or around? (type in/around) ").lower()

            if answer == "in":
                print("You step into a dark mountain, you see nothing but markings on the floor")
                answer = input("You notice one of the marking on the floor is a different color than the rest, do you step on it or go around? (step on it / around) ").lower()
                if answer ==  "step on it":
                        print("Congrats!!! You deactivated the traps security and the hidden treasure is all yours!!!")
                else:
                    print(f"Sorry! you triggered a trap that set the alarm and activated auto turrets, you are dead!")
            elif answer == "around":
                health -= 50
                print("You attempt to go around the mountain, but you run into a pit of snakes, your health is now", health)
            
            

        elif left_or_right == 'right':
             print("You tripped over a mine and killed yourself...")   

    else:
        print("Okay, have a nice day :D")

else:
    print("That is not a valid age to play this game.")

