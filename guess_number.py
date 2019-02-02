from random import randint
number = randint(1, 100)
#print(number)
guess = 0
while guess != number:
    guess = int(input("Input number from 1 to 100: "))
    if guess < number:
        print("That's too low")
    elif guess > number:
        print("That's too high")
    else:
        print("That's exactly right!")


