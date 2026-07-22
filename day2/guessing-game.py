import random
def guessing_game():
    target = random.randint(1, 50)
    attempts = 0
    print("Guess the number between 1 and 50!")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < target: print("Too low!")
        elif guess > target: print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

guessing_game()
