# كود للتحقق من وجود عنصر داخل قائمة وطباعة رسالة مخصصة
fruits = ["apple", "banana", "cherry"]
user_fruit = input("Enter a fruit to check: ").lower()

if user_fruit in fruits:
    print(f"Yes, {user_fruit} is in the list!")
else:
    print(f"No, {user_fruit} is not there.")
