class BookNotFoundError(Exception):
    pass
class BookAlreadyExistsError(Exception):
    pass
class MemberLimitExceededError(Exception):
    pass
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def __str__(self):
        return f"title: {self.title} author: {self.author} ({'borrowed' if self.is_borrowed  else 'available'})"

class Member:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []
    def __str__(self):
        return f"name:{self.name} borrowed_books:{(book.title for book in self.borrowed_books)}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self,book):
        self.books.append(book)
    def add_member(self,member):
        self.members.append(member)
    def borrow_book(self,member_name,book_title):
        member = next((m for m in self.members if m.name == member_name),None)
        if not member:
            raise ValueError('Member not found')
        book = next((b for b in self.books if b.title==book_title),None)
        if not book:
            raise BookNotFoundError('Book not found')
        if book.is_borrowed:
            raise BookAlreadyExistsError('Book already borrowed')
        if len(book.borrowed_books) <= 3:
            raise MemberLimitExceededError('Member limit exceeded')
        book.is_borrowed = True
        book.borrowed_books.append(book)
    def return_book(self,member_name,book_title):
        member = next ((m for m in self.members if m.name==member_name),None)
        if not member:
            raise ValueError('Member not found')
        book = next((b for b in self.books if b.title==book_title),None)
        if not book:
            raise BookNotFoundError('Book not found')
        book.is_borrowed = False
        member.borrowed_books.append(book)
if __name__ == '__main__':
    library = Library()
    book1 = Book('book 1', author='<NAME>1')
    book2 = Book('book 2', author='<NAME>2')
    book3 = Book('book 3', author='<NAME>3')
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    member1 = Member('<NAME>1')
    member2 = Member('<NAME>2')
    library.add_member(member1)
    library.add_member(member2)
    try:
        library.borrow_book('Ali', 'book 1')
        library.borrow_book('Asad', 'book 2')
        library.borrow_book('Asad', 'book ')
    except Exception as e:
        print(f'Error:{e}')

    try:
        library.return_book('Asad', 'book 2')
    except Exception as e:
        print(f'Error:{e}')
    print(member1)
    print(member2)
    for book in library.books:
        print(book)



