class Book():
    def __init__(self, title, author, ISBN):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self._availability=True
    
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
                return {
                    'user_id':self.user_id, 
                    'book_title': book_obj.title, 
                    'action':'borrowed'
                    }
            else:
                print('you aleady borrowed this book')
        else:
            print('this book doesn\'t exist in a library')
        
    def return_books(self, book_obj):
        if isinstance(book_obj, Book):
            if book_obj._availability==False:
                self.books_borrowed.remove(book_obj)
                book_obj.available(True)
                return {
                    'user_id':self.user_id, 
                    'book_title': book_obj.title, 
                    'action':'returned'
                    }
            else:
                print('you haven\'t borrowed this book')
        else:
            print('this book doesn\'t exist in a library')
        

class Transaction:
    def __init__ (self, obj):
        self.user_id=obj['user_id']
        self.book_title=obj['book_title']
        self.action=obj['action']
        
        pass
   
    
    #getting confused about the transaction part
    
class Library:
    def __init__(self):
        self.users=[]
        self.books=[]
        self.transactions=[]
    
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
                return 
            else:
                print('this book was aleady added before')
        else:
            print('this book is not an instance of the class Book')
       
    def borrow_book(self, user_obj, book_obj ):
        transaction=Transaction(
            user_obj.borrow_books(book_obj)
        )
        self.transactions.append(transaction)
    
    def return_book(self, user_obj, book_obj):
        transaction=Transaction(
            user_obj.return_books(book_obj)
        )
        self.transactions.append(transaction)
    
    def display_books(self):
        for book in self.books:
            if book._availability:
                print(f'{book.title}\n')
    
    def transaction_report(self):
        for transaction in self.transactions:
            print(f'{transaction.user_id} {transaction.action} {transaction.book_title}')
    


       
book1 = Book("Python Programming", "John Doe", "978-0134853987")
book2 = Book("Data Structures and Algorithms", "Jane Smith", "978-0262033848")

# Create users
user1 = User(1, "Alice")
user2 = User(2, "Bob")

# Create library
library = Library()

# Add books to the library
library.add_books(book1)
library.add_books(book2)

# Register users
library.register_user(user1)
library.register_user(user2)

# User borrows a book
library.borrow_book(user1, book1)

# Display available books
library.display_books()

# User returns a book
library.return_book(user1, book1)

# Generate transaction report
library.transaction_report()