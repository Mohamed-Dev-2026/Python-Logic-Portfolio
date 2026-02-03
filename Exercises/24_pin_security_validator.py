correct_pin = "0000"
attempts = 3

while attempts > 0:
    user_pin = input(f"Enter your PIN ({attempts} attempts left): ")
    if user_pin == correct_pin:
        print("PIN Verified. Entry allowed.")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")

if attempts == 0:
    print("Account Locked. Please contact support.")
