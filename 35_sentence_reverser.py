text = input("Enter a sentence: ")
words = text.split()
reversed_text = " ".join(reversed(words))

print(f"Original: {text}")
print(f"Reversed: {reversed_text}")
