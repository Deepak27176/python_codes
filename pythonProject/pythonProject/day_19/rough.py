class Book:
    def __init__(self,id,book_name,author_name,type,price):
        self.id=id
        self.book_name=book_name
        self.author_name=author_name
        self.type=type
        self.price=price
    def percent(self,discount):
        self.price = (1-(discount/100))*self.price

class BookStore:
    booklist = []
    def books(self):
        no_books=int(input())
        for i in range(no_books):
            id = input()
            name = input()
            author = input()
            price = float(input())
            type = input()
            obj=Book(id,name,author,type,price)
            self.booklist.append(obj)


    author_rating={}
    def get_book_type(self, type1):
        for i in self.booklist:
            if i.type=="fiction":
                i.percent(20)
            else:
                i.percent(10)
            if i.type==type1:
                if self.author_rating[i.author_name]>4:
                    return i
                else:
                    return "None"
            else:
                return "None"

