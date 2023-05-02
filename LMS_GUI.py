from tkinter import *
import sqlite3
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta, datetime


# 1. User checks out a book, add it to Book_Loan, the number of copies needs to be updated in the
# Book_Copies table. Show the output of the updated Book_Copies. [5 points]
# 2. Add information about a new Borrower. Do not provide the CardNo in your query. Output the card
# number as if you are giving a new library card. Submit your editable SQL query that your code
# executes. [3 points]
# 3. Add a new Book with publisher (use can use a publisher that already exists) and author information to
# all 5 branches with 5 copies for each branch. Submit your editable SQL query that your code
# executes. 
# 4. Given a book title list the number of copies loaned out per branch. 
# Given any due date range list the Book_Loans that were returned late and how many days they were
# late. Submit your editable SQL queries that your code executes.
# Given any due date range list the Book_Loans that were returned late and how many days they were
# late. Submit your editable SQL queries that your code executes. 

# cancel button to close the window
def cancel(Window):
    Window.destroy()

# create a font
ourFont = ("Helvetica", 14)

# function to check out a book
# User checks_out a book, add it to Book_Loan, the number of copies needs to be updated in the
# Book_Copies table.
def checkout_book():

    # create variables to hold the dates
    branch_id = StringVar()
    book_id = StringVar()
    card_no = StringVar()
    date_out = StringVar()
    due_date = StringVar()




    print("Checking out a book")
    #create a window
    w1 = Tk()
    w1.title("Check out a book")
    w1.geometry("600x500")

    #create a label
    text = Label(w1, text="Check out a book", font=ourFont)
    text.grid(row=0, column=1, padx = 10, pady=10, sticky='we')


    
    #create a label for the branch id
    branch_id_label = Label(w1, text="Branch Id", font=ourFont)
    branch_id_label.grid(row=1, column=0, padx = 10, pady=10, sticky='we')

    #create a text field for the branch id and assign it to branch_id
    branch_id_entry = Entry(w1, textvariable=branch_id, font=ourFont)
    branch_id_entry.grid(row=1, column=1, padx = 10, pady=10, sticky='we')



    #create a label for the book id
    book_id_label = Label(w1, text="Book Id", font=ourFont)
    book_id_label.grid(row=2, column=0, padx = 10, pady=10, sticky='we')

    #create a text field for the book id and assign it to book_id
    book_id_entry = Entry(w1, textvariable=book_id, font=ourFont)
    book_id_entry.grid(row=2, column=1, padx = 10, pady=10, sticky='we')




    #create a label for the card number
    card_no_label = Label(w1, text="Card No", font=ourFont)
    card_no_label.grid(row=3, column=0, padx = 10, pady=10, sticky='we')

    #create a text field for the card number and assign it to card_no
    card_no_entry = Entry(w1, textvariable=card_no, font=ourFont)
    card_no_entry.grid(row=3, column=1, padx = 10, pady=10, sticky='we')




    #create a label for the date out
    date_out_label = Label(w1, text="Date Out", font=ourFont)
    date_out_label.grid(row=4, column=0, padx = 10, pady=10, sticky='we')

    #display today's date using the datetime function, put it as a label ,assign it to date_out
    today = date.today()
    date_out = today.strftime("%Y-%m-%d")
    Date_out_label = Label(w1, text=date_out, font=ourFont)
    Date_out_label.grid(row=4, column=1, padx = 10, pady=10, sticky='we')
    



    #create a label for the due date
    due_date_label = Label(w1, text="Due Date", font=ourFont)
    due_date_label.grid(row=5, column=0, padx = 10, pady=10, sticky='we')
    
    #display due date(date + 1month) and assign it to due_date in the format mm/dd/yyyy
    #check if the month is december, if it is, add 1 to the year and set the month to january
    due_date = today + relativedelta(months=+1)
    if due_date.month == 12:
        due_date = due_date.replace(year=due_date.year+1, month=1)
    else:
        Due_date_label = Label(w1, text=due_date, font=ourFont)
    Due_date_label.grid(row=5, column=1, padx = 10, pady=10, sticky='we')
    
    #create a button to submit the information
    #keep submit button disabled until all fields are filled
    submit_button = Button(w1, text="Submit", command=lambda: CB_results(book_id_entry.get(), branch_id_entry.get(), card_no_entry.get(), date_out, due_date))
    submit_button.grid(row=6, column=1, padx = 10, pady=10, sticky='we')
    submit_button.config(state="disabled")
    #checks if all fields are filled
    def check_fields():
        if book_id_entry.get() != "" and branch_id_entry.get() != "" and card_no_entry.get() != "":
            submit_button.config(state="normal")
        else:
            submit_button.config(state="disabled")

    # check if all fields are filled every time a field is filled
    branch_id_entry.bind("<KeyRelease>", lambda e: check_fields())
    card_no_entry.bind("<KeyRelease>", lambda e: check_fields())
    book_id_entry.bind("<KeyRelease>", lambda e: check_fields())

    #create a button to cancel the window
    cancel_button = Button(w1, text="Cancel", command=lambda: cancel(w1))
    cancel_button.grid(row=7, column=1, padx = 10, pady=10, sticky='we')

    # execute my window
    w1.mainloop()

    return


# function to add a new borrower
def add_borrower():
    print("Adding a new borrower")

    #create a window
    w3 = Tk()
    w3.title("Add a new borrower")

    #create a label
    text = Label(w3, text="Add a new borrower", font=ourFont)
    text.grid(row=0, column=1, padx = 10, pady=10, sticky='we')

    #create a label for the name
    name_label = Label(w3, text="Name", font=ourFont)
    name_label.grid(row=1, column=0, padx = 10, pady=10, sticky='we')

    #create a text field for the name and assign it to name
    name = StringVar()
    name_entry = Entry(w3, textvariable=name, font=ourFont)
    name_entry.grid(row=1, column=1, padx = 10, pady=10, sticky='we')

    #create a label for the address
    address_label = Label(w3, text="Address", font=ourFont)
    address_label.grid(row=2, column=0, padx = 10, pady=10, sticky='we')

    #create a text field for the address and assign it to address
    address = StringVar()
    address_entry = Entry(w3, textvariable=address, font=ourFont)
    address_entry.grid(row=2, column=1, padx = 10, pady=10, sticky='we')

    #create a label for the phone
    phone_label = Label(w3, text="Phone", font=ourFont)
    phone_label.grid(row=3, column=0, padx = 10, pady=10, sticky='we')

    #create a text field for the phone and assign it to phone
    phone = StringVar()
    phone_entry = Entry(w3, textvariable=phone, font=ourFont)
    phone_entry.grid(row=3, column=1, padx = 10, pady=10, sticky='we')

    #create a button to submit the information
    submit_button = Button(w3, text="Submit", command=lambda: AB_results(name_entry.get(), address_entry.get(), phone_entry.get()))
    submit_button.grid(row=4, column=1, padx = 10, pady=10, sticky='we')

    #execute my window
    w3.mainloop()
    
    return


# function to add a new book
def add_book():
    print("Adding a new book")  

# function to list the number of copies loaned out per branch
def list_copies():
    print("Listing the number of copies loaned out per branch")

# function to list the Book_Loans that were returned late and how many days they were late
def list_late():
    print("Listing the Book_Loans that were returned late and how many days they were late")




# Show the output of the updated Book_Copies. 
def CB_results(book_id, branch_id, card_no, date_out, due_date):
    print("Checking out a book")

    #create a window
    w2 = Tk()

    #create a label
    text = Label(w2, text="Check out a book", font=ourFont)
    text.grid(row=0, column=1, padx = 10, pady=10, sticky='we')

   
    submit_conn = sqlite3.connect('LMS.sqlite3')
    submit_cur = submit_conn.cursor() 


    # add it to Book_Loan
    submit_cur.execute("INSERT INTO BOOK_LOANS(Book_Id, Branch_Id, Card_no, Date_Out, Due_Date) VALUES (:book_id, :branch_id, :card_no, :date_out, :due_date)",
    {
        'book_id': book_id,
        'branch_id': branch_id,
        'card_no': card_no,
        'date_out': date_out,
        'due_date': due_date,
    })
    print("Book_Loan updated")
    
   

    # the number of copies needs to be updated in the Book_Copies table.
    submit_cur.execute("UPDATE BOOK_COPIES SET No_Of_Copies = No_Of_Copies - 1 WHERE Book_Id = :book_id AND Branch_Id = :branch_id",
        {
            'book_id': book_id,
            'branch_id': branch_id,
        })
    print("Book_Copies updated")

    # Show the output of the updated Book_Copies.
    submit_cur.execute("SELECT * FROM BOOK_COPIES")
    print("Book_Copies output")
    records = submit_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    #create lebels for headers
    book_id_label = Label(w2, text="(Book_Id, Branch_Id, # of copies)", font=ourFont)
    book_id_label.grid(row=1, column=1, padx = 10, pady=10, sticky='we')

    
    query_label = Label(w2, text=print_records, font=ourFont)
    query_label.grid(row=2, column=1, padx = 10, pady=10, sticky='we')

    #create a button to cancel the window
    cancel_button = Button(w2, text="Close", command=lambda: cancel(w2))
    cancel_button.grid(row=3, column=1, padx = 10, pady=10, sticky='we')



    #closing the connection
    submit_conn.commit()
    submit_conn.close()
    return



# Add information about a new Borrower. Do not provide the CardNo in your query. Output the card
# number as if you are giving a new library card. Submit your editable SQL query that your code
# executes.
def AB_results(name, address, phone):

    #close the window


    #create a window
    w4 = Tk()
    w4.title("Add a new borrower")
    w4.geometry("400x200")

    #connect to the database
    submit_conn = sqlite3.connect('LMS.sqlite3')
    submit_cur = submit_conn.cursor()

    #add the new borrower to the database
    submit_cur.execute("INSERT INTO BORROWER(Name, Address, Phone) VALUES (:name, :address, :phone)",
    {
        'name': name,
        'address': address,
        'phone': phone,
    })

    #get the card number of the new borrower
    submit_cur.execute("SELECT Card_no FROM BORROWER WHERE Name = :name AND Address = :address AND Phone = :phone",
    {
        'name': name,
        'address': address,
        'phone': phone,
    })

    #display the card number
    records = submit_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    #create a label for the card number
    card_no_label = Label(w4, text="Card Number", font=ourFont)
    card_no_label.grid(row=0, column=1, padx = 10, pady=10, sticky='we')

    #create a label for the card number
    query_label = Label(w4, text=print_records, font=ourFont)
    query_label.grid(row=1, column=1, padx = 10, pady=10, sticky='we')

    #create a button to cancel the window
    cancel_button = Button(w4, text="Close", command=lambda: cancel(w4))

    #closing the connection
    submit_conn.commit()
    submit_conn.close()

    #execute my window
    w4.mainloop()

    return

# add tkinter window
root = Tk()
root.title("Library Management System")
root.geometry("600x500")

# create a database or connect to one
conn = sqlite3.connect('LMS.sqlite3')

# create cursor
cur = conn.cursor()

# add some text and horizontally center it
text = Label(root, text="GUI CSE3330", font=ourFont)
text.grid(row=0, column=1, padx = 190, pady=10, sticky='we')

# create a button to check out a book
checkout_button = Button(root, text="Check out a book", command=checkout_book)
checkout_button.grid(row=1, column=1, padx = 190, pady=10, sticky='we')

#create a button to add a new borrower
add_borrower_button = Button(root, text="Add a new borrower", command=add_borrower)
add_borrower_button.grid(row=2, column=1,padx = 190, pady=10, sticky='we')

#create a button to add a new book
add_book_button = Button(root, text="Add a new book", command=add_book)
add_book_button.grid(row=3, column=1, padx = 190, pady=10, sticky='we')

#create a button to list the number of copies loaned out per branch
list_copies_button = Button(root, text="List number of copies loaned out per branch", command=list_copies)
list_copies_button.grid(row=4, column=1,padx = 190, pady=10, sticky='we')

#create a button to list the Book_Loans that were returned late and how many days they were late
list_late_button = Button(root, text="List late Book_Loans and days overdue", command=list_late)
list_late_button.grid(row=5, column=1,padx = 190, pady=10, sticky='we')




# execute my window
root.mainloop()


# querry from the database
# insert values into the database
