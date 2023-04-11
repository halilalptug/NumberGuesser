import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number: 
        guess = int(input(f'Guess a number 1 and {x}: '))
        if guess < random_number:
            print("Sorry pal, guess again. It's too low.")
        elif guess > random_number:
            print("Sorry bud, it's too high.")
    print(f'Yea boi! You got it right! It was {random_number} ')

guess(20)