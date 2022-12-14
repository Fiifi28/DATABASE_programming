
##This programme is to comit new data to the table created in SQL

import sqlite3

# Open a connection to the database
conn = sqlite3.connect('my_database.db')
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

cursor.execute("INSERT INTO my_table VALUES ('45654', 'FELIX EFFAH', 'felix.e_b@gmail.com', '0745655785')")

conn.commit()
conn.close()
