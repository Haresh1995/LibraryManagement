class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks

    def displayAvailableBooks(self):
        print("The available books are : ")
        for book in self.books:
            print(book)


    def borrowBooks(self,bookName):
        if bookName in self.books:
            print(f"You have issued {bookName} and you have to return soon!")
            self.books.remove(bookName)
            return True
        else:
            print("This book is already issued")
            return False
    
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book")
    

class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow : ")
        return self.book
        
        

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return : ")
        return self.book

if __name__ == "__main__":
    centraLibrary = Library(['Physics','Chemistry','Biology','Maths','IT'])
    #centraLibrary.displayAvailableBooks()
    student = Student()
    while(True):
        WelcomeMsg = '''==========Welcome to the Library==========
Please select an option : 
1. Display All Books
2. Borrow a Book
3. Return a Book
4. Exit        
'''
        print(WelcomeMsg)

        a = int(input("Enter a choice : "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
            
        elif a == 2:
            centraLibrary.borrowBooks(student.requestBook())
            
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for using this library")
            exit()
        else:
            print("Enter a valid Choice")