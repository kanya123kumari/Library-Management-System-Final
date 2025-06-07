create database library;
show databases;
use library;
show tables;

create table authors (authorID int (10) primary key, name varchar (100), country varchar (50));

insert into authors(authorID, name, country)
values
(101, "Amit Chaudhuri", "India"),
(102, "Gita Mehta", "India"),
(103, "Jaswant Singh", "India");

select *from authors;

create table books (bookID int primary key, title varchar (50),
authorID int, category varchar (100), price decimal (10,2), foreign key (authorID) references authors (authorID));

insert into books(bookID, title, authorID, category, price)
values
(201, "Afternoon Raag ", 101, "Life history", 80.00),
(202, "The Lord of the Rings", 102, "Fantasy", 90.00),
(203, "To Kill a Mockingbird", 103, "Historical Fiction", 60.00); 

select *from books;


create table members (memberID int primary key auto_increment, name varchar (50), joinDate date);

insert into members (memberID, name, joinDate)
values
(301, "Alice", "2001-01-05"),
(302, "Bob", "2002-02-04"),
(303, "Madhu", "2000-01-10");

select * from members;

create table borrowing (borrowID int primary key auto_increment,
memberID int, bookID int, borrowDate date, returnDate date,
foreign key (memberID) references members (memberID),
foreign key (bookID) references books (bookID)
);

insert into borrowing (borrowID, memberID, bookID, borrowDate, returnDate)
values
(501, 301, 201, "2024-12-25", "2025-01-10"),
(502, 302, 202, "2024-11-15", "2025-01-02"),
(503, 303, 203, "2024-12-20", "2025-01-31");

select * from borrowing;

-- 1. List all books and their authors
select Books.Title,(select Authors.Name from Authors where Authors.AuthorID = Books.AuthorID) as Author from Books;

-- select name from authors modify name where name = 'Charlotte' to ; 
update Authors set Name = 'Alice' where AuthorID = 10;

update Members set Name = 'Alice' where MemberID = 10;
-- 2.Find all books brorowed by "Alice"
SELECT Title FROM Books WHERE BookID IN (SELECT BookID FROM Borrowing WHERE MemberID = (SELECT MemberID FROM Members WHERE Name = 'Alice'));

-- 3. Find all books that cost more than $20
select Title, price from books where price > 20 ;

-- Bonus
-- Add column fine in Borrowing table
alter table borrowing add fine decimal(10, 2);

UPDATE borrowing
SET fine = CASE
    WHEN DATEDIFF(ReturnDate, BorrowDate) > 7 THEN (DATEDIFF(ReturnDate, BorrowDate) - 7) * 2
    ELSE 0
END;
-- Find the most expensive book in the library.


-- Find the total number of book in each category 
select Category, count(*) as TotalBooks from books group by Category;
select * from Members;
select * from Books;
select * from Authors;
select * from Borrowing;




