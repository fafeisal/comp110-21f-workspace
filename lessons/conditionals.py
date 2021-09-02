"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day! :)")

else: 
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else: 
        print("You guessed too low!")
    guess = int(input("What is your second guess? "))
    if guess == SECRET:
        print("Nice job, that's right!")
    else:
        print("RIP, you're wrong again.")

print("Game over.")