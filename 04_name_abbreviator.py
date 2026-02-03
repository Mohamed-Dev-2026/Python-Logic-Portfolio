names = input("Enter names separated by a comma: ").split(", ")
abbreviated_names = []

for name in names:
    name_parts = name.split()
    if len(name_parts) >= 2:
        # نأخذ الحرف الأول من الاسم الأول والحرف الأول من اللقب
        first_initial = name_parts[0][0]
        last_initial = name_parts[1][0]
        abbreviation = f"{first_initial}.{last_initial}."
        abbreviated_names.append(abbreviation)
    
for x in abbreviated_names:
    print(x)
