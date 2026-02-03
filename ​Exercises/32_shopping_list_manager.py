# كود يجد أكبر رقم في قائمة دون استخدام دالة max الجاهزة
numbers = [23, 56, 12, 89, 44, 7]
max_num = numbers[0]

for n in numbers:
    if n > max_num:
        max_num = n

print(f"The largest number in the list is: {max_num}")

