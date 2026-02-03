import random
numbers = set()
while len(numbers) < 5:
    numbers.add(random.randint(1, 50))
print(f"Your lucky numbers: {sorted(list(numbers))}")
