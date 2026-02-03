word = input("Enter a word: ").lower()
char_count = {}
for char in word:
    if char != " ":
        char_count[char] = char_count.get(char, 0) + 1
print("Character Frequency:", char_count)
