favorite_title = input()
book_counter = 0
while True:
    title = input()

    if title == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break

    if title == favorite_title:
        print(f"You checked {book_counter} books and found it.")
        break
    book_counter += 1
