import random
import string

print("welcome to the Password Generator!")
total_letters = int(input("enter the number of letters: "))
total_numbers = int(input("enter the number of numbers: "))
total_symbols = int(input("enter the number of symbols: "))

letters = string.ascii_letters 
numbers = string.digits
symbols = string.punctuation 

password_chars = (
    random.choices(letters, k=total_letters) +
    random.choices(numbers, k=total_numbers) +
    random.choices(symbols, k=total_symbols)
)
random.shuffle(password_chars)
password = "".join(password_chars)
print(f"Generated password: {password}")
