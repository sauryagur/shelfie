# S.H.E.L.F.I.E.

**S.H.E.L.F.I.E: Simplified Handling for Electronic Library and Inventory Efficiency**

S.H.E.L.F.I.E is a comprehensive software program meticulously designed to streamline and enhance the management of your library's inventory with unparalleled efficiency. Leveraging a user-friendly interface and a robust set of commands, S.H.E.L.F.I.E empowers librarians and administrators to effortlessly oversee their collection and optimize operations. Here's a glimpse of its key features and commands:

**1. Register Book:** With S.H.E.L.F.I.E, registering new books into your library's inventory is a breeze. Enter book details such as title, author, genre, price, and initial stock quantity to ensure that your catalog stays up to date.

**2. List All Books:** Access a comprehensive and organized list of all the books in your library. This feature provides a clear overview of your collection, making it easy to find and retrieve information.

**3. Update Book Information:** Keep your catalog current and accurate by effortlessly updating book information as needed. Whether it's correcting errors or making changes to existing entries, S.H.E.L.F.I.E simplifies the process.

**4. Search for books:** The powerful search functionality in S.H.E.L.F.I.E allows you to find books quickly and efficiently. You can search by book title, author, genre, or even keywords, making it easier for patrons to discover the books they're looking for.

**5. Record Sale:** Manage book sales and transactions seamlessly. S.H.E.L.F.I.E’s integrated sales recording system ensures you can keep detailed records of all transactions, whether you're selling books to library members or for fundraising purposes.

S.H.E.L.F.I.E is designed with a minimalistic user-friendly keyboard based interface, ensuring that both experienced librarians and beginners can navigate the program with ease. Say goodbye to the complexities of traditional inventory management and embrace the modern, efficient approach with S.H.E.L.F.I.E. It offers a simple solution for electronic library and inventory management that can save you time and enhance your library's overall efficiency.

**Made by Saurya Gur (XII-E) for Computer Science.**

## Prerequisites

Run this in command prompt, making sure pip is installed.

```bash
pip install pymysql
```

Next, copy paste this script into MySQL command line client to make sure the database and tables are installed:

```sql
create database bookstore_db;
use bookstore_db;

drop table if exists books;

-- Create the 'books' table
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(50),
    price DECIMAL(10, 2),
    stock INT
);

-- Insert data into the 'books' table
INSERT INTO books (book_id, title, author, genre, price, stock)
VALUES
(1, 'The Iliad', 'Homer', 'Epic', 813.26, 50),
(2, 'The Odyssey', 'Homer', 'Epic', 961.26, 45),
(3, 'Brave New World', 'Aldous Huxley', 'Science Fiction', 1183.26, 30),
(4, 'Thus Spake Zarathustra', 'Friedrich Nietzsche', 'Philosophy', 739.26, 20),
(5, 'Solaris', 'Stanis?aw Lem', 'Science Fiction', 1109.26, 25),
(6, 'Brief Answers To The Big Questions', 'Stephen Hawking', 'Science', 887.26, 35),
(7, 'Surrounded By Idiots', 'Thomas Erikson', 'Psychology', 1035.26, 40),
(8, 'The Prince Of Milk', 'Exurb1a', 'Children''s Literature', 665.26, 15),
(9, 'The Brothers Karamazov', 'Fyodor Dostoevsky', 'Fiction', 924.26, 60),
(10, 'Autofac', 'Philip K. Dick', 'Science Fiction', 1109.26, 30),
(11, 'The Selfish Gene', 'Richard Dawkins', 'Science', 887.26, 25),
(12, 'The Way Of The Superior Man', 'David Deida', 'Self-Help', 739.26, 45),
(13, 'How to Win Friends and Influence People', 'Dale Carnegie', 'Self-Help', 813.26, 50),
(14, 'The Nine Billion Names Of God', 'Arthur C. Clarke', 'Science Fiction', 998.26, 30),
(15, 'Men Without Women', 'Haruki Murakami', 'Fiction', 961.26, 38),
(16, 'Ego Is The Enemy', 'Ryan Holiday', 'Self-Help', 813.26, 35),
(17, 'The Metamorphosis', 'Franz Kafka', 'Fiction', 765.00, 28),
(18, '1984', 'George Orwell', 'Dystopian', 975.50, 15),
(19, 'Meditations', 'Marcus Aurelius', 'Philosophy', 689.99, 10),
(20, 'The Psychology of Money', 'Morgan Housel', 'Finance', 1150.00, 22),
(21, 'Essentialism: The Disciplined Pursuit Of Less', 'Greg McKeown', 'Self-Help', 899.99, 18),
(22, 'I don''t know Timmy, Being God is a Big Responsibility', 'qntm', 'Humor', 599.95, 7),
(23, 'Randomize', 'Andy Weir', 'Science Fiction', 1250.00, 12),
(24, 'The Egg', 'Andy Weir', 'Short Story', 299.99, 5);
```

![Untitled](S%20H%20E%20L%20F%20I%20E%20041f3d3bff81465d98978c496bfb1048/Untitled.png)

# Code

[main.py](S%20H%20E%20L%20F%20I%20E%20041f3d3bff81465d98978c496bfb1048/main.py)

```python
import pymysql

# Database connection
connection = pymysql.connect(host='localhost', user='root', password='amity', db='bookstore_db')
cursor = connection.cursor()

def create_books_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                      book_id INT AUTO_INCREMENT PRIMARY KEY,
                      title VARCHAR(255),
                      author VARCHAR(255),
                      genre VARCHAR(50),
                      price DECIMAL(10, 2),
                      stock INT)''')
    connection.commit()

def register_book():
    title = input("Enter book title: ")
    author = input("Enter author's name: ")
    genre = input("Enter book genre: ")
    price = float(input("Enter book price: "))
    stock = int(input("Enter initial stock quantity: "))

    cursor.execute("INSERT INTO books (title, author, genre, price, stock) VALUES (%s, %s, %s, %s, %s)", (title, author, genre, price, stock))
    connection.commit()
    print("Book registered successfully!")

def list_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    
    print("\nList of Books:")
    for book in books:
        print(f"Book ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Genre: {book[3]}")
        print(f"Price: ₹{book[4]:.2f}")
        print(f"Stock: {book[5]}\n")

def update_book():
    book_id = int(input("Enter the book ID to update: "))
    
    edit = input("Enter information to update\n1. Title\n2. Author\n3. Genre\n4. Price\n5. Stock\n\nEnter selection: ")
    print("\n")
    if str(edit).lower() in ["1", "title", "name"]:
        nam = str(input("Enter new name: "))
        cursor.execute("UPDATE books SET title = %s WHERE book_id = %s", (nam, book_id))

    if str(edit).lower() in ["2", "author", "author name"]:
        nam = str(input("New author's name: "))
        cursor.execute("UPDATE books SET author = %s WHERE book_id = %s", (nam, book_id))
    
    if str(edit).lower() in ["3", "genre", "type"]:
        nam = str(input("Updated genre: "))
        cursor.execute("UPDATE books SET genre = %s WHERE book_id = %s", (nam, book_id))
    
    if str(edit).lower() in ["4", "price", "cost"]:
        nam = int(input("Enter new price: "))
        cursor.execute("UPDATE books SET price = %s WHERE book_id = %s", (nam, book_id))

    if str(edit).lower() in ["5", "stock", "sale"]:
        stock = int(input("Enter the new stock quantity: "))
        cursor.execute("UPDATE books SET stock = %s WHERE book_id = %s", (stock, book_id))

    connection.commit()
    print("Data updated successfully!")

def search_books():
    keyword = input("Enter a keyword to search for books: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR genre LIKE %s", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()

    if books:
        print("\nSearch Results:")
        for book in books:
            print(f"Book ID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(f"Genre: {book[3]}")
            print(f"Price: ₹{book[4]:.2f}")
            print(f"Stock: {book[5]}\n")
    else:
        print("No matching books found.")

def record_sale():
    book_id = int(input("Enter the book ID sold: "))
    quantity = int(input("Enter the quantity sold: "))
    cursor.execute("SELECT stock FROM books WHERE book_id = %s", (book_id,))
    current_stock = cursor.fetchone()[0]

    if current_stock >= quantity:
        cursor.execute("UPDATE books SET stock = stock - %s WHERE book_id = %s", (quantity, book_id))
        connection.commit()
        print("Sale recorded successfully!")
    else:
        print("Insufficient stock to complete the sale.")
#To prevent interference from other branches
if __name__ == "__main__":
    create_books_table()
    print("\nWELCOME TO S.H.E.L.F.I.E. \nS.H.E.L.F.I.E is a software program meticulously designed to streamline and enhance the management of your library's inventory with unparalleled efficiency. Leveraging a user-friendly interface and a robust set of commands, S.H.E.L.F.I.E empowers librarians and administrators to effortlessly oversee their collection and optimize operations. Here's a glimpse of its key features and commands") 
    while True:
        print("\n1. Register Book")
        print("2. List All Books")
        print("3. Update Book Information")
        print("4. Search for Books")
        print("5. Record Sale")
        print("6. Exit")
        choice = input("\n\nEnter your choice: ")

        if choice == '1':
            register_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            update_book()
        elif choice == '4':
            search_books()
        elif choice == '5':
            record_sale()
        elif choice == '6':
            break
        else:
            print('Please enter a valid command.')

    cursor.close()
    connection.close()
```

![Untitled](S%20H%20E%20L%20F%20I%20E%20041f3d3bff81465d98978c496bfb1048/Untitled%201.png)

![Untitled](S%20H%20E%20L%20F%20I%20E%20041f3d3bff81465d98978c496bfb1048/Untitled%202.png)

# Additional Versions

[tabularshelfie.py](S%20H%20E%20L%20F%20I%20E%20041f3d3bff81465d98978c496bfb1048/tabularshelfie.py)

**T.H.E.L.F.I.E: Tabular Handling for Electronic Library and Inventory Efficiency.**

This is the same as **S.H.E.L.F.I.E,** except the data is displayed in a much more aesthetic tabular form using tabulate module with a filter command. Use the following prerequisite before running the code.

```jsx
pip install tabulate
```

### Code:

```jsx
import pymysql
from tabulate import tabulate

# Database connection
connection = pymysql.connect(host='localhost', user='root', password='amity', db='bookstore_db')
cursor = connection.cursor()

def create_books_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                      book_id INT AUTO_INCREMENT PRIMARY KEY,
                      title VARCHAR(255),
                      author VARCHAR(255),
                      genre VARCHAR(50),
                      price DECIMAL(10, 2),
                      stock INT)''')
    connection.commit()

def register_book():
    title = input("Enter book title: ")
    author = input("Enter author's name: ")
    genre = input("Enter book genre: ")
    price = float(input("Enter book price: "))
    stock = int(input("Enter initial stock quantity: "))

    cursor.execute("INSERT INTO books (title, author, genre, price, stock) VALUES (%s, %s, %s, %s, %s)", (title, author, genre, price, stock))
    connection.commit()
    print("Book registered successfully!")

def list_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if not books:
        print("No books found.")
    else:
        headers = ["Book ID", "Title", "Author", "Genre", "Price", "Stock"]
        book_data = []

        for book in books:
            book_data.append([book[0], book[1], book[2], book[3], f"₹{book[4]:.2f}", book[5]])

        print(tabulate(book_data, headers, tablefmt="pretty"))

def update_book():
    book_id = int(input("Enter the book ID to update: "))
    
    edit = input("Enter information to update\n1. Title\n2. Author\n3. Genre\n4. Price\n5. Stock\n\nEnter selection: ")
    print("\n")
    if str(edit).lower() in ["1", "title", "name"]:
        nam = str(input("Enter new name: "))
        cursor.execute("UPDATE books SET title = %s WHERE book_id = %s", (nam, book_id))

    if str(edit).lower() in ["2", "author", "author name"]:
        nam = str(input("New author's name: "))
        cursor.execute("UPDATE books SET author = %s WHERE book_id = %s", (nam, book_id))
    
    if str(edit).lower() in ["3", "genre", "type"]:
        nam = str(input("Updated genre: "))
        cursor.execute("UPDATE books SET genre = %s WHERE book_id = %s", (nam, book_id))
    
    if str(edit).lower() in ["4", "price", "cost"]:
        nam = int(input("Enter new price: "))
        cursor.execute("UPDATE books SET price = %s WHERE book_id = %s", (nam, book_id))

    if str(edit).lower() in ["5", "stock", "sale"]:
        stock = int(input("Enter the new stock quantity: "))
        cursor.execute("UPDATE books SET stock = %s WHERE book_id = %s", (stock, book_id))

    connection.commit()
    print("Data updated successfully!")

def search_books():
    keyword = input("Enter a keyword to search for books: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR genre LIKE %s", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()

    if books:
        print("\nSearch Results:")
        for book in books:
            print(f"Book ID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(f"Genre: {book[3]}")
            print(f"Price: ₹{book[4]:.2f}")
            print(f"Stock: {book[5]}\n")
    else:
        print("No matching books found.")

def filter_books():
    keyword = input("Enter a keyword to filter books: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR genre LIKE %s", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()

    if books:
        headers = ["Book ID", "Title", "Author", "Genre", "Price", "Stock"]
        book_data = []

        for book in books:
            book_data.append([book[0], book[1], book[2], book[3], f"₹{book[4]:.2f}", book[5]])

        print(tabulate(book_data, headers, tablefmt="pretty"))
    else:
        print("No matching books found.")

def record_sale():
    book_id = int(input("Enter the book ID sold: "))
    cursor.execute("SELECT title FROM books WHERE book_id = %s", (book_id,))
    print("Book name: ",cursor.fetchone()[0])
    quantity = int(input("Enter the quantity sold: "))
    cursor.execute("SELECT stock FROM books WHERE book_id = %s", (book_id,))
    current_stock = cursor.fetchone()[0]

    if current_stock >= quantity:
        cursor.execute("UPDATE books SET stock = stock - %s WHERE book_id = %s", (quantity, book_id))
        connection.commit()
        print("Sale recorded successfully!")
        print("Remaining stock: ", current_stock-quantity)
    else:
        print("Insufficient stock to complete the sale.")

create_books_table()

print("\nWelcome to S.H.E.L.F.I.E.")
print("S.H.E.L.F.I.E is a comprehensive software program meticulously designed to streamline and enhance the management of your library's inventory with unparalleled efficiency.")
print("Leveraging a user-friendly interface and a robust set of commands, S.H.E.L.F.I.E empowers librarians and administrators to effortlessly oversee their collection and optimize operations.")
print("Here are all the commands:")

while True:
    print("1. Register Book")
    print("2. List All Books")
    print("3. Update Book Information")
    print("4. Search for Books")
    print("5. Record Sale")
    print("6. Filter Books")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        register_book()
    elif choice == '2':
        list_books()
    elif choice == '3':
        update_book()
    elif choice == '4':
        search_books()
    elif choice == '5':
        record_sale()
    elif choice == '6':
        filter_books()
    elif choice == '':
        print('Invalid input. Please enter a valid choice.')
    elif choice == '7':
        break

cursor.close()
connection.close()
```

# **In case you need to reset/reinstall the database:**

```sql
drop database if exists bookstore_db;
create database bookstore_db;
use bookstore_db;

drop table if exists books;

-- Create the 'books' table
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(50),
    price DECIMAL(10, 2),
    stock INT
);

-- Insert data into the 'books' table
INSERT INTO books (book_id, title, author, genre, price, stock)
VALUES
(1, 'The Iliad', 'Homer', 'Epic', 813.26, 50),
(2, 'The Odyssey', 'Homer', 'Epic', 961.26, 45),
(3, 'Brave New World', 'Aldous Huxley', 'Science Fiction', 1183.26, 30),
(4, 'Thus Spake Zarathustra', 'Friedrich Nietzsche', 'Philosophy', 739.26, 20),
(5, 'Solaris', 'Stanis?aw Lem', 'Science Fiction', 1109.26, 25),
(6, 'Brief Answers To The Big Questions', 'Stephen Hawking', 'Science', 887.26, 35),
(7, 'Surrounded By Idiots', 'Thomas Erikson', 'Psychology', 1035.26, 40),
(8, 'The Prince Of Milk', 'Exurb1a', 'Children''s Literature', 665.26, 15),
(9, 'The Brothers Karamazov', 'Fyodor Dostoevsky', 'Fiction', 924.26, 60),
(10, 'Autofac', 'Philip K. Dick', 'Science Fiction', 1109.26, 30),
(11, 'The Selfish Gene', 'Richard Dawkins', 'Science', 887.26, 25),
(12, 'The Way Of The Superior Man', 'David Deida', 'Self-Help', 739.26, 45),
(13, 'How to Win Friends and Influence People', 'Dale Carnegie', 'Self-Help', 813.26, 50),
(14, 'The Nine Billion Names Of God', 'Arthur C. Clarke', 'Science Fiction', 998.26, 30),
(15, 'Men Without Women', 'Haruki Murakami', 'Fiction', 961.26, 38),
(16, 'Ego Is The Enemy', 'Ryan Holiday', 'Self-Help', 813.26, 35),
(17, 'The Metamorphosis', 'Franz Kafka', 'Fiction', 765.00, 28),
(18, '1984', 'George Orwell', 'Dystopian', 975.50, 15),
(19, 'Meditations', 'Marcus Aurelius', 'Philosophy', 689.99, 10),
(20, 'The Psychology of Money', 'Morgan Housel', 'Finance', 1150.00, 22),
(21, 'Essentialism: The Disciplined Pursuit Of Less', 'Greg McKeown', 'Self-Help', 899.99, 18),
(22, 'I don''t know Timmy, Being God is a Big Responsibility', 'qntm', 'Humor', 599.95, 7),
(23, 'Randomize', 'Andy Weir', 'Science Fiction', 1250.00, 12),
(24, 'The Egg', 'Andy Weir', 'Short Story', 299.99, 5);
```

WARNING: This will reset the database.
