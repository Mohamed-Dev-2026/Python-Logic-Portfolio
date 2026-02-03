full_name = input("Enter your full name: ").replace(" ", "")
length = len(full_name)

print(f"Your name has {length} characters (excluding spaces).")
if length > 15:
    print("That is a quite long name!")
