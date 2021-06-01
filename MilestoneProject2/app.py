from Utils.database import add_book, list_books, mark_book, delete_book

USER_CHOICE = """
 Enter:
 - 'a' to add a new book
 - 'l' to list all books
 - 'r' to mark a book as read
 - 'd' to delete a book
 - 'q' to quit
 
 Your choice:"""

user_options = {
    'a': add_book(),
    'l': list_books(),
    'r': mark_book(),
    'd': delete_book(),
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        pass

    # def prompt_add_book() ask for book name and author
    # def list_books() show all the books in our list
    # def prompt_read_book() ask for book name and change it to "read" in our list
    # def_prompt_delete_book() ask for book name and remove book from list
