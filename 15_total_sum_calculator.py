# كود يقوم بجمع الأرقام من 1 إلى الرقم الذي يدخله المستخدم
limit = int(input("Enter a number to sum up to: "))
total = 0

for number in range(1, limit + 1):
    total += number

print(f"The total sum from 1 to {limit} is: {total}")
