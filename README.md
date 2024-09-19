# S.H.E.L.F.I.E.
## **Made by Saurya Gur for class 12th Computer Science.**
**S.H.E.L.F.I.E: Simplified Handling for Electronic Library and Inventory Efficiency**

S.H.E.L.F.I.E is a comprehensive software program meticulously designed to streamline and enhance the management of your library's inventory with unparalleled efficiency. Leveraging a user-friendly interface and a robust set of commands, S.H.E.L.F.I.E empowers librarians and administrators to effortlessly oversee their collection and optimize operations. Here's a glimpse of its key features and commands:

**1. Register Book:** With S.H.E.L.F.I.E, registering new books into your library's inventory is a breeze. Enter book details such as title, author, genre, price, and initial stock quantity to ensure that your catalog stays up to date.

**2. List All Books:** Access a comprehensive and organized list of all the books in your library. This feature provides a clear overview of your collection, making it easy to find and retrieve information.

**3. Update Book Information:** Keep your catalog current and accurate by effortlessly updating book information as needed. Whether it's correcting errors or making changes to existing entries, S.H.E.L.F.I.E simplifies the process.

**4. Search for books:** The powerful search functionality in S.H.E.L.F.I.E allows you to find books quickly and efficiently. You can search by book title, author, genre, or even keywords, making it easier for patrons to discover the books they're looking for.

**5. Record Sale:** Manage book sales and transactions seamlessly. S.H.E.L.F.I.E’s integrated sales recording system ensures you can keep detailed records of all transactions, whether you're selling books to library members or for fundraising purposes.

S.H.E.L.F.I.E is designed with a minimalistic user-friendly keyboard based interface, ensuring that both experienced librarians and beginners can navigate the program with ease. Say goodbye to the complexities of traditional inventory management and embrace the modern, efficient approach with S.H.E.L.F.I.E. It offers a simple solution for electronic library and inventory management that can save you time and enhance your library's overall efficiency.

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

# Additional Versions

[tabularshelfie.py](S%20H%20E%20L%20F%20I%20E%20041f3d3bff81465d98978c496bfb1048/tabularshelfie.py)

**T.H.E.L.F.I.E: Tabular Handling for Electronic Library and Inventory Efficiency.**

This is the same as **S.H.E.L.F.I.E,** except the data is displayed in a much more aesthetic tabular form using tabulate module with a filter command. Use the following prerequisite before running the code.

```jsx
pip install tabulate
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

WARNING: This will reset the database and rewrite the data with boilerplate values.
