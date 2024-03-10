import sqlite3

def main():
    database = 'library.db'
    conn = sqlite3.connect('library.db')
   
    
    with conn:
        myItem = input("Enter the item you looking for: ")
        cursor = conn.cursor()
        print("Opened database sucessfully \n")
        findItem(conn, myItem)
        myBorrowItem = input("Enter the item you want to borrow: ")
        borrowItem(conn, myBorrowItem)
        myReturnedItem = input("Enter the item you want to return: ")
        returnedBorrowed(conn, myReturnedItem)
        myDonateItem = input("Enter the item you want to donate: ")
        donateItem(conn, myDonateItem)
        myEvent = input("Enter the event you looking for: ")
        findEvent(conn, myEvent)
        myRegEvent = input("Enter the event you want to register for: ")
        regEvent(conn, myRegEvent)
        myVolunteer = input("Enter your name to volunteer: ")
        volunteerLib(conn, myVolunteer)

    if conn:
        conn.close()
        print("Closed database successfully")





def returnedBorrowed(conn, itemBorrowed):
    cur = conn.cursor()

    myQuery = "SELECT ItemName FROM Items WHERE ItemName =:userItem"

    cur.execute(myQuery,{"userItem":itemBorrowed})

    rows=cur.fetchall()
    if rows:
        myQuery2 = "DELETE FROM Borrowed WHERE ItemBorrowed =:itemBorrowed"
        cur.execute(myQuery2,{"itemBorrowed":itemBorrowed})
        print("Item Returned!\n") 
    else:
        print("ERROR: There was a problem with item you entered")

    conn.commit()

  

def findItem(conn, item):
    
    cur = conn.cursor()

    myQuery = "SELECT ItemName FROM Items WHERE ItemName =:userItem"

    cur.execute(myQuery,{"userItem":item})

    rows=cur.fetchall()
    if rows:
        print("We do have your item!")
    else:
        print("We do not have your item")

    conn.commit()

def borrowItem(conn, item):
    cur = conn.cursor()

    myQuery = "SELECT ItemName FROM Items WHERE ItemName =:userItem"

    cur.execute(myQuery,{"userItem":item})

    rows=cur.fetchall()
    if rows:
        myQuery2 = "INSERT INTO Borrowed(DateBorrowed, Duedate, Fine, ItemBorrowed, BorrowExtensionDays) VALUES('2023-07-30', '2023-08-14', 00.00, :userItem2, 5)"
        cur.execute(myQuery2,{"userItem2":item})
        print("Item borrowed!\n")  
    else:
        print("ERROR: There was a problem with item you entered")
    
    conn.commit()    
    
def donateItem(conn, item):
    cur = conn.cursor()

    myQuery = "INSERT INTO Items(ItemName,ItemsCount,ItemCategory) VALUES(:userItem, 1, 'Video Games')"
    try:
        cur.execute(myQuery,{"userItem":item}) 
        print("Item Donated!\n")       
    except sqlite3.IntegrityError:
        print("ERROR: There was a problem with item you entered")

    
    conn.commit() 

def findEvent(conn, event):
    
    cur = conn.cursor()

    myQuery = "SELECT EventName FROM LibraryEvents WHERE EventName =:userEvent"

    cur.execute(myQuery,{"userEvent":event})

    rows=cur.fetchall()
    if rows:
        print("We do have the event you want!")
    else:
        print("We do not have the event you want")

    conn.commit()  

def regEvent(conn, event):
    
    cur = conn.cursor()

    myQuery = "SELECT EventName FROM LibraryEvents WHERE EventName =:userEvent"

    cur.execute(myQuery,{"userEvent":event})

    rows=cur.fetchall()
    if rows:
        myQuery2 = "UPDATE LibraryEvents SET NumRegistered = 1 WHERE EventName =:userEvent"
        cur.execute(myQuery2,{"userEvent":event})
        print("You have been registered!")
    else:
        print("ERROR: There was a problem with event you entered")

    conn.commit() 

def volunteerLib(conn, name):
    cur = conn.cursor()
    myQuery = "INSERT INTO Volunteers(FirstName,LastName, PhoneNumber, EmailAddress) VALUES(:userName, 'LastName', 'PhoneNumber', 'EmailAddress')"
    try:
        cur.execute(myQuery,{"userName":name}) 
        print("Thank you for volunteering!\n")       
    except sqlite3.IntegrityError:
        print("ERROR: There was a problem with item you entered")
    conn.commit()


if __name__ == '__main__':
    main()    