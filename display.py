import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()


print("p_id \t p_name \t  price \t quantity \n")
cursor = cur.execute("SELECT * FROM Product");

for row in cursor:
    print(row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\n")

con.close()