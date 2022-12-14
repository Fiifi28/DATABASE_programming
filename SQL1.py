##Programme to create a table in SQL

import sqlite3

# Open a connection to the database
conn = sqlite3.connect('my_database.db')
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the SQL query to create the table
query = '''
CREATE TABLE my_table (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT
)
'''

# Execute the query to create the table
cursor.execute(query)

# Save the changes to the database
conn.commit()

# Close the connection to the database
conn.close()
