-- 1. Joins 
-- a. List all books with their authors 

use library;
select books.title as book_title, authors.name as author_name 
from books 
join authors on books.authorID=authors.authorID;

-- b. Show all books borrowed along with the member’s name
select books.Title, Members.Name as MemberName
from borrowing
join books on borrowing.BookId = books.BookId
join Members on borrowing.MemberId = Members.MemberId;

-- c. Find members who have borrowed Fantasy books
select distinct Members.Name as MemberName
from borrowing
join books on borrowing.BookId = books.BookId
join Members on borrowing.memberId = Members.MemberId
where books.category = 'Fantasy';

-- 2. Indexing for Optimization
-- a. Create an index on AuthorID in Books
create index Author_index on books(AuthorID);

-- b. Create an index on BookID in Borrowing
create index book_index on borrowing(BookId);

-- 3. Views
-- a. Create a view to display borrowed books and their members
create view BorrowedBooks as
select books.Title, Members.Name as Member, borrowing.BorrowDate, Borrowing.ReturnDate
from Borrowing
join books on borrowing.BookId = books.BookId
join Members on Borrowing.MemberId = Members.MemberId;

-- b. Query the view
select * from BorrowedBooks;

-- 4. Stored Procedure
-- a. Create a stored procedure to list books by category
Delimiter $$
create procedure GetBooksByCategory(In category_name varchar(50))
begin
	select Title from Books where Category = Category_name;
end $$
delimiter ; 

-- Calling the procedure
call GetBooksByCategory('Fantasy');

-- 5. User-defined functions
-- a. Create a function to calculate late fine (₹5 per day after 7 days)
Delimiter $$
create function CalculateFine(return_date Date, borrow_date date) RETURNS INT DETERMINISTIC
begin
	declare days_late int;
    declare fine int;
    set days_late = datediff(return_date, borrow_date) -7;
    set fine = If(days_late > 0, days_late * 5, 0);
    return fine;
end $$
delimiter ;

-- 6. Triggers
-- a. Create a trigger to update fine when a book is returned late
create table Fines (
	FineID int primary key auto_increment,
    MemberId int,
    BookId int,
    FineAmount int,
    foreign key(MemberId) references Members(MemberId),
    foreign key(BookId) references Books(BookId)
);
delimiter $$
create Trigger UpdateFineOnReturn
after update on borrowing
for each row
begin
	if New.ReturnDate is not null then
		insert into Fines(MemberId, BookId, FineAmount)
        values(New.MemberId, New.BookId, CalculateFine(New.ReturnDate, New.BorrowDate));
	end if;
end $$
delimiter ;

-- Testing the trigger
Update Borrowing set ReturnDate = '2025-03-10' where BorrowId = 1;


