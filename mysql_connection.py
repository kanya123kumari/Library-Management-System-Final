import mysql.connector

host = 'localhost'
user = 'root'
password = 'root'
database = 'library'
port = '3306'

# connection to MYSQL using keyword arguments

conn = mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
print(conn)
cursor = conn.cursor()

if conn:
    print("connection successfull")

else:
    print("Try again")

# Inserting data into the employee table(C - Create)

def add_books(bookID, title, authorID, category, price): 
    try:
        cursor1 = conn.cursor()
        conn.start_transaction()  # Begin transaction
        
        query = "INSERT INTO library.books(bookID, title, authorID, category, price) VALUES (%s, %s, %s, %s, %s)"
        cursor1.execute(query, (bookID, title, authorID, category, price))
        
        conn.commit()  # Commit transaction
        print("Book data added successfully")

    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of an error
        print("Transaction failed:", e)

    finally:
        cursor1.close()

# view the employees table(R - Read)
def get_books():
    try:
        cursor2 = conn.cursor()
        query = "select * from books"
        cursor2.execute(query)

        for row in cursor2.fetchall():
            print(row)

    except Exception as e:
        print("Data not visible: ",e)
    finally:
        cursor2.close()

# Update the employees record(U - update)

def update_books(bookID, title):
    print("--------update operation---------")

    try:
        cursor3 = conn.cursor()
        conn.start_transaction()
        
        query = "UPDATE books SET title = %s WHERE bookID = %s"
        cursor3.execute(query, (title, bookID))

        conn.commit()
        print("Data updated successfully")

    except Exception as e:
        conn.rollback()
        print("Update failed:", e)

    finally:
        cursor3.close()

# Delete a record from employees

def delete_books(bookID):
    print("-------Delete operation-------")

    try:
        cursor4 = conn.cursor()
        conn.start_transaction()
        query = "delete from books where bookID=%s"
        cursor4.execute(query,(bookID))
        conn.commit()
        print("Data deleted successfully")
        cursor4.close()

    except Exception as e:
        conn.rollback()
        print("Delete failed: ",e)
    finally:
        cursor4.close()

while True:
    print("Choose an operation: ")
    print("1 Add books")
    print("2 Update books title")
    print("3 Delete books")
    print("4 View books")
    print("5 Exit")

    userInput = int(input("Enter your choice: "))
    if userInput == 1:
        print("-------insert operation--------")
        bookID = input("Enter books id: ")
        title = input("Enter books title: ")
        authorID = input("Enter the Author id: ")
        category = input("Enter the book category: ")
        price = input("Enter the books price: ")
        add_books(bookID, title, authorID, category, price)
        break

    elif userInput ==2:
        print("----------Update employee salary----------")
        bookID =int(input("Enter the book id: "))
        title = (input("Enter books title:"))
        update_books(bookID, title)
        break

    elif userInput ==3:
        print("---------Delete operation----------")
        bookID = int(input("Enter the book id: "))
        delete_books(bookID)
        break

    elif userInput == 4:
        print("-------Read operation-----------")
        get_books()
        break

    elif userInput == 5:
        print("Exit from program...")
        break
    else:
        print("Wrong user input.")
        break

        conn.close()
        print("Database connection closed.")