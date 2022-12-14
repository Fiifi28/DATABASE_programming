
##Programme to add multiple rows to the table created in SQL

import sqlite3

with sqlite3.connect('my_database.db') as connection:

    c = connection.cursor()

    data = [
        ('23455', 'JOHN LEGGEND', 'john.leggend@gmail.com',  '345423454234'),
        ('4384', 'MICHEAL BLACKSON', 'blackson@uti.com', '743374346348'),
        ('4638749', 'ANTHONY JOSHUA', 'joshua.a@yujj.com', '54343436538'),
        ('2534', 'BRANDON FORD', 'ford@gmail.com', '4653828346') ]

    c.executemany('INSERT INTO my_table VALUES (?,?,?,?)', data) #the executemany() object permits the addition of many rows to the table created in SQL
