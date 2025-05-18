import random

finish = False

#Create a new game
while finish != True:

    number = random.randint(0,100)
    round = False
    attempts = 0

    print("Guess a number between 0 and 100")

    #Guess the number
    while round != True:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print(f"You guessed correct in {attempts} attempts")
            round = True
            finish = True if input("Play another round? (y/n)") == 'n' else False
            if finish:
                break
        else:
            attempts += 1
            if guess > number:
                print("Too high")
            else:
                print("Too low")
print("Game exit")