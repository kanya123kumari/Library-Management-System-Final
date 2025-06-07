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

def add_members(memberID, name, joinDate): 
    try:
        cursor1 = conn.cursor()
        conn.start_transaction()  # Begin transaction
        
        query = "insert into library.members(memberID, name, joinDate) values (%s, %s, %s)"
        cursor1.execute(query, (memberID, name, joinDate))
        
        conn.commit()  # Commit transaction
        print("members data added successfully")

    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of an error
        print("Transaction failed:", e)

    finally:
        cursor1.close()

# view the employees table(R - Read)
def get_members():
    try:
        cursor2 = conn.cursor()
        query = "select * from members"
        cursor2.execute(query)

        for row in cursor2.fetchall():
            print(row)

    except Exception as e:
        print("Data not visible: ",e)
    finally:
        cursor2.close()

# Update the employees record(U - update)

def update_members(memberID, name):
    print("--------update operation---------")

    try:
        cursor3 = conn.cursor()
        conn.start_transaction()
        
        query = "update members set name = %s where memberID = %s"
        cursor3.execute(query, (name, memberID))

        conn.commit()
        print("Data updated successfully")

    except Exception as e:
        conn.rollback()
        print("Update failed:", e)

    finally:
        cursor3.close()

# Delete a record from employees

def delete_members(memberID):
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
    print("1 Add Members ")
    print("2 Update members name")
    print("3 Delete member")
    print("4 View members")
    print("5 Exit")

    userInput = int(input("Enter your choice: "))
    if userInput == 1:
        print("-------insert operation--------")
        memberID = int(input("Enter members id: "))
        name = input("Enter members name: ")        
        joinDate = input("Enter the join date: ")
        add_members(memberID, name, joinDate)
        break

    elif userInput ==2:
        print("----------Update members name----------")
        memberID =int(input("Enter the members id: "))
        name = input("Enter members name:")
        update_members(memberID,name)
        break

    elif userInput ==3:
        print("---------Delete operation----------")
        memberID = int(input("Enter the member id: "))
        delete_members(memberID)
        break

    elif userInput == 4:
        print("-------Read operation-----------")
        get_members()
        break

    elif userInput == 5:
        print("Exit from program...")
        break
    else:
        print("Wrong user input.")
        break

        conn.close()
        print("Database connection closed.")