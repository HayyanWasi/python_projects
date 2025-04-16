import json


library = []
FILE_NAME = "library.json"

def add_book(library):
            title = input("title: ")
            author = input("author: ")
            year = int(input("publication year: "))
            genre = input("genre: ")
            book_readed_status = input("book read yes/no: ")
            read_status = book_readed_status == "yes"

            book = {
                "title" : title,
                "author" : author,
                "publication" : year,
                "genre" : genre,
                "book_read" : read_status  
            }
            library.append(book)
            print(f"Book {title} sucessfully added!")


def remove_books(library):
    title = input("Enter book to remove: ").strip().lower()
    for book in library:
         if book['title'] == title.lower():
              library.remove(book)
              print(f"removed {title}")
              return
    print(f"Book {title} removed ")

def search_book(library):
    search_option = input("Search book").strip().lower()
    for book in library:
        if search_option.lower().strip() == book["title"].lower():
            print(book)
            print(f"sucessfully searched {book['title']}")
            return    
        else:
             print("invalid book name")  

def display_stats(library):
    total_books = len(library)
    print(f"total books is {total_books}")
    
    counter = 0

    if total_books == 0:
        print("no books found")
        return

    read_count = 0
    for book in library:
         if book['book_read']:
              read_count += 1

    percentage = (read_count / total_books) * 100
    print(f"{percentage}% read")

while True:
    print("enter Add or 1 , remove or 2, search for book or 3, display stats or 4, exit or 5")
    user = input("").lower().strip()

    if user in ("add", "1"):
        print("----book adding----")
        add_book(library)
    elif user in ("remove book", "2"):
        print("book removed")
        remove_books(library)
    elif user in ("search", "3"):
        search_book(library)
    elif user in ("display stats", "4"):
        display_stats(library)
    elif user in ("exit", "5"):
        print("thanks for our services")
        break
    else:
        print("invalid ")


    