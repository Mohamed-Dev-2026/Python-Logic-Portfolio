text = input("Enter a word: ").lower()
if text == text[::-1]:
    print("Yes, it is a Palindrome!")
else:
    print("No, it is not.")
