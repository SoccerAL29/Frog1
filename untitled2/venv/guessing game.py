import random
n=random.randint(1,99)
guess=int(input("enter a number between 1 and 99"))
while n !=guess:
    if guess < n:
        print("guess is too low")
        guess = int(input("enter a number between 1 and 99"))
    elif guess > n:
        print("guess is too high")
        guess = int(input("enter a number between 1 and 99"))
    else:
        print("you guessed  it")






