import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to Our Number Guessing Game!")
    print("\nI have generated a number between 1 and 100.")
    
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_number()
