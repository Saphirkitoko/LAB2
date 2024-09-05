# Part 1 and Part 2: Traditional Author class

class Author:
    def __init__(self, name):
        # Traditional class requires manually defining __init__ to initialize attributes
        self.name = name
        self.books = []

    def publish(self, title):
        # Check for duplicate book titles before adding
        if title in self.books:
            print(f"Error: '{title}' is already published by {self.name}.")
        else:
            self.books.append(title)

    def __str__(self):
        # Traditional class requires manually defining __str__ for string representation
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'No books'

        return f'Author Name: {self.name}\nPublished Books: {book_list}'


# Testing the Author class
author1 = Author('Sally Rooney')
author1.publish('Normal People')
author1.publish('Conversations with Friends')
author1.publish('Normal People')  # Testing duplicate book
print(author1)

author2 = Author('saphir kitoko')
print(author2)


# Part 3: Dataclass version of Student class
from dataclasses import dataclass

# The @dataclass decorator automatically generates __init__, __repr__, __eq__, and other methods
@dataclass
class Student:
    name: str
    school_id: str
    gpa: float


def main():
    # Creating instances of Student
    alex = Student('Alex', '1234', 3.5)
    sam = Student('Sam', '5678', 4.0)
    
    # Dataclasses automatically generate __repr__ for printing
    print(alex)
    print(sam)


if __name__ == '__main__':
    main()


    # Comments comparing the traditional class and dataclass:
 # 1. __init__ Method: # - Traditional classes like `Author` require manual creation of the __init__ method to initialize attributes. 
# - Dataclasses like `Student` automatically generate the __init__ method based on the fields provided. 
# 2. __str__ or __repr__ Method: # - In the traditional class, the __str__ method needs to be manually implemented to provide a custom string representation. # - Dataclasses automatically generate a __repr__ method that provides a readable string representation of the object. 
# 3. Code Length: # - Traditional classes involve more code to define the same functionality (e.g., manually defining __init__ and __str__). # - Dataclasses significantly reduce boilerplate code, making it easier and faster to define simple data structures. 
