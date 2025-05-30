# This file is responsible for inserting records in the database.

import sqlite3

# Connecting to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert records and create tables.
cursor = connection.cursor()

# Creating the table
table_info = """
create table STUDENT(NAME VARCHAR(25), 
CLASS VARCHAR(25), 
SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# Inserting few records to the table
cursor.execute('''insert into STUDENT values('Student1', 'Machine Learning', 'ML')''')
cursor.execute('''insert into STUDENT values('Student2', 'Data Science', 'DS')''')
cursor.execute('''insert into STUDENT values('Student3', 'Natural Langage', 'NLP')''')
cursor.execute('''insert into STUDENT values('Student4', 'Artificial Intelligence', 'AI')''')
cursor.execute('''insert into STUDENT values('Student5', 'Computer Vision', 'CV')''')

# Displaying the inserted records
print("The inserted records are: ")
data = cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)