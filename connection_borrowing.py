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

def add_borrowing(borrowID, memberID, bookID, borrowDate, returnDate): 
    try:
        cursor1 = conn.cursor()
        conn.start_transaction()  # Begin transaction
        
        query = "insert into library.borrowing(borrowID, memberID, bookID, borrowDate, returnDate) values (%s, %s, %s, %s, %s)"
        cursor1.execute(query, (borrowID, memberID, bookID, borrowDate, returnDate))
        
        conn.commit()  # Commit transaction
        print("Borrowing data added successfully")

    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of an error
        print("Transaction failed:", e)

    finally:
        cursor1.close()

# view the employees table(R - Read)
def get_borrowing():
    try:
        cursor2 = conn.cursor()
        query = "select * from borrowing"
        cursor2.execute(query)

        for row in cursor2.fetchall():
            print(row)

    except Exception as e:
        print("Data not visible: ",e)
    finally:
        cursor2.close()

# Update the employees record(U - update)

def update_borrowing(borrowID, borrowDate):
    print("--------update operation---------")

    try:
        cursor3 = conn.cursor()
        conn.start_transaction()
        
        query = "update borrowing set borrowDate = %s where borrowID = %s"
        cursor3.execute(query, (borrowDate, borrowID))

        conn.commit()
        print("Data updated successfully")

    except Exception as e:
        conn.rollback()
        print("Update failed:", e)

    finally:
        cursor3.close()

# Delete a record from employees

def delete_borrowing(borrowID):
    print("-------Delete operation-------")

    try:
        cursor4 = conn.cursor()
        conn.start_transaction()
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
    print("1 Add borrower ")
    print("2 Update return date ")
    print("3 Delete borrow id ")
    print("4 View borrowing ")
    print("5 Exit ")

    userInput = int(input("Enter your choice: "))
    if userInput == 1:
        print("-------insert operation--------")
        borrowID = int(input("Enter borrow id: "))
        joinDate = input("Enter the join date: ")
        returnDate = input("Enter the return date: ")
        add_borrowing(borrowID, joinDate, returnDate)
        break

    elif userInput ==2:
        print("----------Update members name----------")
        borrowID =int(input("Enter the borrow id: "))
        borrowDate = input("Enter borrow date:")
        update_borrowing(borrowID, borrowDate)
        break

    elif userInput ==3:
        print("---------Delete operation----------")
        borrowID = int(input("Enter the borrow id: "))
        delete_borrowing(borrowID)
        break

    elif userInput == 4:
        print("-------Read operation-----------")
        get_borrowing()
        break

    elif userInput == 5:
        print("Exit from program...")
        break
    else:
        print("Wrong user input.")
        break

        conn.close()
        print("Database connection closed.")