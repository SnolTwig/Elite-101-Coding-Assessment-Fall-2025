from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def view_Book():
    i = 0
    while i < len(library_books):
        if library_books[i]["available"] == True:
            print(f"Book title: {library_books[i]["title"]}")
            print(f"Author: {library_books[i]["author"]}")
            print(f"ID: {library_books[i]["id"]}")
            print("--------------------")
        i+= 1

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_Book():
    #gets 
    genre = input("What is the genre of the book you're looking for: ")
    genre = genre.lower()
    genre = genre.capitalize()
    match_Book = []
    i = 0
    while i < len(library_books):
        if library_books[i]["genre"] == genre:
            match_Book.append(library_books[i])
        i+=1
    i = 0
    while i < len(match_Book):
        print(f"Book title: {match_Book[i]["title"]}")
        print(f"Author: {match_Book[i]["author"]}")
        print(f"ID: {match_Book[i]["id"]}")
        print("--------------------") 
        i+=1
    if match_Book == []:
        print("That's not a vaild genre, please try again")
        search_Book()
    return(match_Book)
# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout(id):
    book_id=id
    book_id=book_id.capitalize()
    i = 0
    while i < len(library_books):
        if library_books[i]["id"] == book_id:
            if library_books[i]["available"] == True:
                library_books[i]["available"] = False
                library_books[i]["checkouts"]+=1
                #Credit for how to set the date Pablo Santa Cruz from stackoverflow
                dt = datetime.now()
                td = timedelta(days=14)
                my_date = dt + td
                my_date = str(my_date.date())
                library_books[i]["due_date"] = my_date
                print(f"Book {library_books[i]["title"]} has been checked out, enjoy!")
                break
            else:
                print("That book has been checkout")
        i+=1
# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_Book(id):
    book_id=id
    book_id=book_id.capitalize()
    i = 0
    while i < len(library_books):
        if library_books[i]["id"] == book_id:
            if library_books[i]["available"] == False:
                library_books[i]["available"] == True
                library_books[i]["due_date"] == None
                print("book has been returned!")
            else:
                print("that book had already been returned")
        i+=1

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def overdue_Books():
    test = datetime.now()
    test = str(test.date())
    overdue =[]
    i = 0
    while i < len(library_books):
        if library_books[i]["available"] == False and library_books[i]["due_date"]< test:
            overdue.append(library_books[i])
        i+=1
    i = 0
    while i < len(overdue):
        print(f"Book title: {overdue[i]["title"]}")
        print(f"Author: {overdue[i]["author"]}")
        print(f"ID: {overdue[i]["id"]}")
        print("--------------------") 
        i+=1

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!
def add_Book():
    id = input("Enter the book id: ")
    title = input("Enter the title: ")
    author = input("Enter the book's author: ")
    genre = input("Enter the book genre: ")
    available = True
    due_date = None
    checkouts = 0
    new_Book = {"id": id,
                "title": title,
                "author": author,
                "genre": genre,
                "available": available,
                "due_date": due_date,
                "checkouts": checkouts}
    library_books.append(new_Book)

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
