class Book():
    def __init__(self, title, author, ISBN, availability):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self._availability=availability
    
    def display_details(self):
        print(f'''title: {self.title}\nauthor: {self.author}\nISBN: {self.ISBN}\navailability: {self._availability}''')
        
    def available(self, bool):
        self._availability=bool
    
class User():
    def __init__(self, user_id, name):
        self.user_id=user_id
        self.name=name
        self.books_borrowed=[]
        
    def display_details(self):
        #use a one liner to loop through all books you borrowed
        print(f'''user_id: {self.user_id}\nname: {self.name}\nbooks_borrowed: {self.books_borrowed}''')
        
    def borrow_books(self, book_obj):
        if isinstance(book_obj, Book):
            if book_obj._availability==True:
                book_obj.available(False)
                self.books_borrowed.append(book_obj)
            else:
                print('you aleady borrowed this book')
        else:
            print('this book doesn\'t exist in a library')
        
    def return_books(self, book_obj):
        if isinstance(book_obj, Book):
            if book_obj._availability==False:
                self.books_borrowed.remove(book_obj)
                book_obj.available(True)
            else:
                print('you haven\'t borrowed this book')
        else:
            print('this book doesn\'t exist in a library')
        

class Transactions:
    def __init__(self):
        self.transactions=[]
        
    #getting confused about the transaction part
    
class Library:
    def __init__(self):
        self.users=[]
        self.books=[]
    
    def register_user(self, user_obj):
        if isinstance(user_obj, User):
            if user_obj not in self.users:
                self.users.append(user_obj)
            else:
                print('user aleady registered')
        else:
            print('this person doesn\'t exist on paper')
        
    def add_books(self, book_obj):
        if isinstance(book_obj, Book):
            if book_obj not in self.books:
                self.books.append(book_obj)
            else:
                print('this book was aleady added before')
        else:
            print('this book is not an instance of the class Book')
        
    
        
