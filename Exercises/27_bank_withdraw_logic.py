balance = 1000.0
amount = float(input(f"Current balance ${balance}. Withdraw: "))
if 0 < amount <= balance:
    balance -= amount
    print(f"Success! New balance: ${balance}")
else:
    print("Insufficient funds or invalid amount.")
