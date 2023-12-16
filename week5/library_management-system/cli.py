from library import Book, User, Library

'''
command-line interface:
adding books, registering users, borrowing books, returning books, and viewing reports.
'''
def validated_input(question):
    answer=input(answer)
    if len(answer)<3:
        print('>too short try again')
        return validated_input(question)
    elif len(answer)>15:
        print('>too long try again')
        return validated_input(question)
    else:
        return answer
        

def add_book():
    #title, #author, #isbn
    print('adding new book to the library')
    title=validated_input('Enter the title of the book: ')
    author=validated_input('Enter the name of the author')
    isbn=validated_input('Enter the isbn number')


def register_user():
    #user_id, name
    print('registering new user')
    user_id=validated_input('Enter the user_id of the user: ')
    name=validated_input('Enter the name of the user')
    isbn=validated_input('Enter the isbn number')

def borrow_book():
    #user_obj, book_obj
    print('borrowing a book')
    user_id=validated_input('Enter the id of the borrower: ')
    book_title=validated_input('Enter the title of the book')

def return_book():
    #user_obj, book_obj
    print('returning borrowed book')
    user_id=validated_input('Enter the id of the borrower: ')
    book_title=validated_input('Enter the title of the book')


def view_report(library):
    return library.transaction_report()
