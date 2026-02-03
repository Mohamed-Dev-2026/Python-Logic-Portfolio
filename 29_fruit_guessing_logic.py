import random

fruits = ["apple", "mango", "orange", "grape"]
secret = random.choice(fruits)

print("I'm thinking of a fruit...")
guess = input("Your guess: ").lower()

if guess == secret:
    print("Great job! You guessed it.")
else:
    print(f"Maybe next time! It was {secret}.")
