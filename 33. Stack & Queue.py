books = []
books.append("C programming")
books.append("Java book")
books.append("Python book")
print(books)
print("Here the top book is: ", books[-1])
books.pop()
print(books)
print("Here the top book is after pop: ", books[-1])
books.pop()
print(books)
books.pop()
print(books)
if not books:
    print("No books in list.")
else:
    print("Yes, there are books on the list.")

books.append("c++")
print("\nAfter append a book: ")
if not books:
    print("No books in list.")
else:
    print("Yes, there are books on the list.")
print(books)