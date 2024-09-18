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

    cursor.execute("INSERT INTO books (title, author, genre, price, stock) VALUES (%s, %s, %s, %s, %s)",
                   (title, author, genre, price, stock))
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

#testmessage
def search_books():
    keyword = input("Enter a keyword to search for books: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR genre LIKE %s",
                   ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
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


# To prevent interference from other branches
if __name__ == "__main__":
    create_books_table()
    print(
        "\nWELCOME TO S.H.E.L.F.I.E. \nS.H.E.L.F.I.E is a software program meticulously designed to streamline and enhance the management of your library's inventory with unparalleled efficiency. Leveraging a user-friendly interface and a robust set of commands, S.H.E.L.F.I.E empowers librarians and administrators to effortlessly oversee their collection and optimize operations. Here's a glimpse of its key features and commands")
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