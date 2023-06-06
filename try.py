# user_age = int(input("please input your age: "))
# months = user_age * 12
# print(f"Your age {user_age} in months is {months} ")



# #LAMBDA function
# add = lambda x, y : x + y

# #LIST comprehension
# def double(x):
#     return x * 2
# sequence = [1, 3, 5, 7, 9]
# doubled = [double (x) for x in sequence]

# #MAP function 
# doubled = map(double, sequence)
# #map doesn't return a list to you need to wrap it with a list


# #DICTIONARY comprehension
# mapping = {item[1] : item for item in array}
# #the item[1] becomes the key and the others the value

# #OBject oriented proramming
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def average_grades(self):
#         return sum(self.grades) / len(self.grades)

# student1 = Student("Bob", (17, 75, 62, 86))
# student2 = Student("Rolf", (37, 79, 82, 46))
# st1 = (student1.name, student1.grades, student1.average_grades())
# st2 = (student2.name, student2.grades, student2.average_grades())
# print(st1, st2)
# # print (student1.name)
# # print (student2.name)
# # print (student1.grades)
# # print (student2.grades)
# # print(student1.average_grades())
# # print(student2.average_grades())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     #the str is to print the string representation of the object
#     def __str__(self):
#         return f"The person called {self.name} is {self.age} years old."
#     #the repr is actually used as a debugger
#     def __repr__(self):
#         return f"<Person('{self.name}', {self.age})>"

# bob = Person("Bob", 35)
# print(bob)

# static methods and class method
# class ClassTest:
#     """ instance method which requires an object to cal it"""
#     def instance_method(self):
#         print(f"called instance method of {self}")

#     """ class method """
#     @classmethod
#     def class_method(cls):
#         print(f"Called class method of {cls}")

#     """ static method doesn't use the instance"""
#     @staticmethod
#     def static_method():
#         print("Called static method.")

# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)

# ClassTest.class_method()

# ClassTest.static_method()


# class Book:
#     TYPES = ("hardcover", "paperback")

#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight

#     def __repr__(self):
#         return f"<Book {self.name}, {self.book_type} weighing {self.weight}grams>"

#     def __str__(self):
#         return f"Book {self.name}, {self.book_type} weighing {self.weight}grams."

#     @classmethod
#     def hardcover(cls, name, page_weight):
#         return cls(name, Book.TYPES[0], page_weight + 100)

#     @classmethod
#     def paperback(cls, name, page_weight):
#         return cls(name, Book.TYPES[1], page_weight + 10)
 
# book1 = Book.hardcover("Harry Potter", 1500)
# book2 = Book.paperback("Harry Potter", 1500)
# print(book1, book2)

# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True

#     def __str__(self):
#         return f"Device {self.name!r} ({self.connected_by})"

#     def disconnect(self):
#         self.connected = False
#         print("Disconnected.")


# # printer = Device("Printer", "USB")
# # print(printer)
# # printer.disconnect()

# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.remaining_pages =capacity

#     def __str__(self):
#         return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

#     def print(self, pages):
#         if not self.connected:
#             print("your printer is not connected.")
#             return 
#         print(f"Printing {pages} pages.")
#         self.remaining_pages -= pages

# printer = Printer("Printer", "USB", 500)
# printer.print(20)
# print(printer)

# printer.disconnect()
# printer.print(30)


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book():
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book1 = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book1, book2)

print(shelf)

""" Type hinting is a method of defining 
values before they are created or used as 
done in line 152"""

""" First class function"""
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError (f"Could not find an element with {expected}.")

friends = [
    {"name" : "Rolf Smith", "age" : 29},
    {"name" : "Ayo Mark", "age" :45},
    {"name" : "Tolu Grace", "age" : 61},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Rolf Smith", get_friend_name))


"""Python decorators"""
""" mutability in python"""