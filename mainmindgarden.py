import pickle


class Book:
    def __init__(self, name, author, status, remarks, path):
        self.name = name
        self.author = author
        self.status = status
        self.remarks = remarks
        self.path = path
# books = []
# pickle_out = open('list.pickle', 'wb')
# pickle.dump(books, pickle_out)
# pickle_out.close()
def add():
    n = input("add book name:   ")
    a = input("add book author:   ")
    s = input("add book status:   ")
    r = input("add book remarks:   ")
    p = input("add book path:   ")

    book = Book(name=n if n != '' else 'Undefined',
                author=a if a != '' else 'Undefined',
                status=s if s != '' else 'Undefined',
                remarks=r if r != '' else 'Undefined',
                path=p if p != '' else 'Undefined')

    print(book.name, book.author, book.status, book.remarks, book.path)

    pickle_in = open('list.pickle', 'rb')
    pickle_list = pickle.load(pickle_in)
    pickle_list.append(book)

    pickle_out = open('list.pickle', 'wb')
    pickle.dump(pickle_list, pickle_out)
    pickle_out.close()
    return pickle_list

def remove(x):
    pickle_in = open('list.pickle', 'rb')
    pickle_list = pickle.load(pickle_in)

    for i, o in enumerate(pickle_list):
        if o.name == x:
            del pickle_list[i]
            break

    pickle_out = open('list.pickle', 'wb')
    pickle.dump(pickle_list, pickle_out)
    pickle_out.close()

def edit(e):
    pickle_in = open('list.pickle', 'rb')
    pickle_list = pickle.load(pickle_in)

    for i, o in enumerate(pickle_list):
        if o.name == e:
            o.name = input("add book name:   ")
            o.author = input("add book author:   ")
            o.status = input("add book status:   ")
            o.remarks = input("add book remarks:   ")
            o.path = input("add book path:   ")
        print(o.name, o.author, o.status, o.remarks, o.path)

    pickle_out = open('list.pickle', 'wb')
    pickle.dump(pickle_list, pickle_out)
    pickle_out.close()

def read():
    pickle_in = open('list.pickle', 'rb')
    new_loaded_list = pickle.load(pickle_in)
    if new_loaded_list:
        for i in new_loaded_list:
            print(i.name, i.author, i.status, i.remarks, i.path)
    else:
        print('No books')
#add()
#read()
#remove(input('type book name to remove:   '))

#edit(input('type book name to edit:   '))
#read()

