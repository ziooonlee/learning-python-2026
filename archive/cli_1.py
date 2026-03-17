import random

secret_number = random.randint(1,100)
guess = None
attempts = 0

print("Step right up! Guess the number, Win a Prize!")
print ("1 to 100, try to guess the number I am thinking of!")

while guess != secret_number:
    
    guess_str = int(input("What's your guess? "))
    guess = int(guess_str)
    attempts += 1
    if guess < secret_number:
        print("Close, but think bigger.")
    elif guess > secret_number:
        print("Close, ground yourself a little.")
    else:
        print("Winner, Winner, Chicken Dinner!")