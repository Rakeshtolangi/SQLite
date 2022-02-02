import sqlite3

# Connection to database hello.db
con = sqlite3.connect('database.db')

cur = con.cursor()

#Insert Data in SQLite table
cur.execute("INSERT INTO Product(p_name,price, quantity) VALUES('Mobile ', 5000, 200)");
cur.execute("INSERT INTO Product(p_name,price, quantity) VALUES('Keyboard', 2000, 140)");
cur.execute("INSERT INTO Product(p_name,price, quantity) VALUES('Mouse   ', 1000, 170)");

#if data is inserted in sqlite3  successfully then print
print("Data Inserted!!")
con.commit()
con.close()



