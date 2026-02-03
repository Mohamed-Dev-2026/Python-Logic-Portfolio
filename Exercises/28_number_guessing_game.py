# كود يأخذ نصاً ويقوم بتحويله لعدة صيغ (كبير، صغير، عنوان)
text = input("Enter any sentence: ")

print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title Case: {text.title()}")
print(f"Word Count: {len(text.split())}")
