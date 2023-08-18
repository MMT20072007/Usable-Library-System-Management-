import sqlite3
import datetime

# ساخت دیتابیس و جداول
conn = sqlite3.connect('library.db') 

conn.execute('''CREATE TABLE users  
         (id INTEGER PRIMARY KEY, name TEXT, signup_date TEXT)''')

conn.execute('''CREATE TABLE books  
         (id INTEGER PRIMARY KEY, name TEXT, author TEXT)''')

conn.execute('''CREATE TABLE loans
         (id INTEGER PRIMARY KEY, user_id INTEGER, book_id INTEGER,
         loan_date TEXT, return_date TEXT)''')
         
# ثبت نام کاربر جدید         
def register_user():
    name = input("Please enter your name: ")
    signup_date = datetime.date.today()
    
    conn.execute('''INSERT INTO users (name, signup_date)
             VALUES (?, ?)''', (name, signup_date))
    print("Registration successful!")

# امانت دادن کتاب
def lend_book():
    user_id = int(input("Please enter your user id: "))
    book_id = int(input("Please enter book id: "))
    loan_date = datetime.date.today()

    conn.execute('''INSERT INTO loans (user_id, book_id, loan_date)  
             VALUES (?, ?, ?)''', (user_id, book_id, loan_date))
             
    print("Book loaned successfully!")

# صدا زدن توابع            
register_user() 
lend_book()

conn.close()