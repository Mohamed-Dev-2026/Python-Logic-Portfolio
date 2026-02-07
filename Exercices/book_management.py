my_books={}
for i in range(3):
    print("\n....Entry{i+1}....")
    book_id=input("Enter book ID: ")
    title=input("Enter Title: ")
    author=input("Enter Author ")
    year=input("Enter Publication Year: ")
    my_books[book_id] = {
        "title": title,
        "author":author,
        "year":year,
    }
print("\nfinally library")
print(my_books)
