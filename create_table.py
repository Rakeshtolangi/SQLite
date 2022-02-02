import sqlite3

# Connection to database hello.db
con = sqlite3.connect('database.db')

cur = con.cursor()

#creating table in SQLite
cur.execute("CREATE TABLE Product(p_id INTEGER PRIMARY KEY AUTOINCREMENT, p_name TEXT NOT NULL,price REAL,quantity INTEGER)");


#if sqlite3 connect successfully then print
print("Table created!!!")
con.close()
