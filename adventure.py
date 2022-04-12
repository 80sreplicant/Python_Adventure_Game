print('Welcome to my game! ')
name = input('What is your name? ')
age = int(input('What is your age? '))

if age >= 18:
    print('You are old enough to play, enjoy!')

    wants_to_play = input('Do you want to play? ').lower()
    if wants_to_play == "yes":
        print("Let's play!")

        left_or_right = input("First choice.... Left or Right? (type left/right) ").lower()
        if left_or_right == "left":
            answer = input("Very well, you followed the path and reached the mountain entrance.... Do you go in or around? (type in/around) ")
        else:
             print("You tripped over a mine and killed yourself...")   

    else:
        print("Okay, have a nice day :D")

else:
    print("That is not a valid age to play this game.")

