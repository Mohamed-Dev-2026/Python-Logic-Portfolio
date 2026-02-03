grades = input("Enter grades separated by space: ").split()
grades = [float(g) for g in grades]
if grades:
    average = sum(grades) / len(grades)
    print(f"Your average grade is: {average:.2f}")
