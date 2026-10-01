import sqlite3

connect = sqlite3.connect('Homework.db')
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TXT,
        author TXT,
        date INTEGER,
        price INTEGER 
    )
""")
def CreateBook(name, author, date, price):
    cursor.execute("""
        INSERT INTO Books (name, author, date, price) VALUES (?, ?, ?, ?)

    """, (name, author, date, price))
CreateBook('It_basic_patterns', 'Nothing', 2022, 400)

CreateBook('MathBook', 'Einstain', 1935, 200)

CreateBook('EnglisgBook', 'School', 2020, 220)


cursor.execute("""
    UPDATE Books SET author = ? WHERE book_id = ?
""", ('School', 2))
cursor.execute("""
    DELETE FROM Books WHERE book_id = ?
""", (3, ))



cursor = connect.execute("SELECT * FROM Books")
for i in cursor:
    print(i)
connect.commit()
connect.close()