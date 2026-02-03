import random
words = ["moh", "ikram", "chiama"]
random_word = random.choice(words)
guessed = input("please guess a letter: ").lower()

for letter in random_word:
    if guessed == letter:
        print("right")
    else:
        print("wrong")

