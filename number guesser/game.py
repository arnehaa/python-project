import random

number = random.randint(0,100)

finish = False
attempts = 0

print("Guess a number between 0 and 100")

while finish != True:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print(f"You guessed correct in {attempts} attempts")
        finish = True
    else:
        attempts += 1
        if guess > number:
            print("Too high")
        else:
            print("Too low")
