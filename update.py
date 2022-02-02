import sqlite3

con = sqlite3.connect('database.db')

cur = con.cursor()

# update sqlite query
cur.execute("UPDATE Product SET quantity = quantity+1")

con.commit()

print("p_id \t P_name \t price \t quantity \n")
cursor = cur.execute("SELECT * FORM Product");

for row in cursor:
    print(row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\n")
con.close()