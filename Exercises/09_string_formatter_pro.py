# كود يتحقق إذا كانت كلمة السر قوية كفاية من حيث الطول
password = input("Create a new password: ")

if len(password) < 8:
    print("Weak: Password must be at least 8 characters long.")
elif len(password) >= 8 and len(password) < 12:
    print("Medium: Good, but could be longer.")
else:
    print("Strong: Excellent password length!")
