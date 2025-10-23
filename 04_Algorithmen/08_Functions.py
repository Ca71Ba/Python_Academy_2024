def greet(name, age=12):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)
greet("Klaus")
greet(name="Horst", age=45)
greet(age=22, name="Heinz")


# greet(5)

books = []

def add_book(title):
    books.append(title)

add_book("1984")
add_book("Brave New World")
print(books)


