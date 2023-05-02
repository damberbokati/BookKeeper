from tkinter import *
import sqlite3
from datetime import date, timedelta


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
def checkout_book():

    # create variables to hold the values
    book_title = StringVar()
    branch_id =  StringVar()
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
    branch_id_entry = Entry(w1, textvariable=branch_id)
    branch_id_entry.grid(row=1, column=1, padx = 10, pady=10, sticky='we')
    branch_id = branch_id_entry.get()



    #create a label for the book title
    book_title_label = Label(w1, text="Book Title", font=ourFont)
    book_title_label.grid(row=2, column=0, padx = 10, pady=10, sticky='we')

    #create a text field for the book title and assign it to book_title
    book_title_entry = Entry(w1, textvariable=book_title)
    book_title_entry.grid(row=2, column=1, padx = 10, pady=10, sticky='we')
    book_title = book_title_entry.get()



    #create a label for the card number
    card_no_label = Label(w1, text="Card No", font=ourFont)
    card_no_label.grid(row=3, column=0, padx = 10, pady=10, sticky='we')

    #create a text field for the card number and assign it to card_no
    card_no_entry = Entry(w1, textvariable=card_no)
    card_no_entry.grid(row=3, column=1, padx = 10, pady=10, sticky='we')
    card_no = card_no_entry.get()



    #create a label for the date out
    date_out_label = Label(w1, text="Date Out", font=ourFont)
    date_out_label.grid(row=4, column=0, padx = 10, pady=10, sticky='we')

    #display today's date using the datetime function, put it as a label ,assign it to date_out
    today = date.today()
    date_out = today.strftime("%m/%d/%Y")
    Date_out_label = Label(w1, text=date_out, font=ourFont)
    Date_out_label.grid(row=4, column=1, padx = 10, pady=10, sticky='we')


    #create a label for the due date
    due_date_label = Label(w1, text="Due Date", font=ourFont)
    due_date_label.grid(row=5, column=0, padx = 10, pady=10, sticky='we')
    
    #display due date(date_out + 30) and assign it to due_date
    due_date = today.strftime("%m/%d/%Y") + timedelta(days=30)
    Due_date_label = Label(w1, text=due_date, font=ourFont)
    Due_date_label.grid(row=5, column=1, padx = 10, pady=10, sticky='we')


    # execute my window
    w1.mainloop()
    
    return


# function to add a new borrower
def add_borrower():

    add_borow = Toplevel()
    add_borow.title("Adding a new borrower")
    add_borow.geometry("600x500")
    #print("Adding a new borrower")


# function to add a new book
def add_book():
    add_book = Toplevel()
    add_book.title("Adding a new book")
    add_book.geometry("600x500")
    #print("Adding a new book")

# function to list the number of copies loaned out per branch
def list_copies():
    list_copies = Toplevel()
    list_copies.title("Adding a new book")
    list_copies.geometry("600x500")
    #print("Listing the number of copies loaned out per branch")

# function to list the Book_Loans that were returned late and how many days they were late
def list_late():
    list_late = Toplevel()
    list_late.title("Adding a new book")
    list_late.geometry("600x500")

    #print("Listing the Book_Loans that were returned late and how many days they were late")



#nothing new

# add tkinter window
root = Tk()
root.title("Library Management System")
root.geometry("600x500")

# create a database or connect to one
conn = sqlite3.connect('LMS.db')

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
