print('Welcome to my game! ')
name = input('What is your name? ')
age = int(input('What is your age? '))

if age <= 12:
    print("Sorry you are too young to play.")
elif age >= 18:
    print('You are old enough to play, enjoy!')
else:
    print("That is not a valid age!")

