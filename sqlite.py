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
cursor.execute('''insert into STUDENT values('Student6', 'Machine Learning', 'ML')''')
cursor.execute('''insert into STUDENT values('Student7', 'Data Science', 'DS')''')
cursor.execute('''insert into STUDENT values('Student8', 'Natural Language', 'NLP')''')
cursor.execute('''insert into STUDENT values('Student9', 'Artificial Intelligence', 'AI')''')
cursor.execute('''insert into STUDENT values('Student10', 'Computer Vision', 'CV')''')
cursor.execute('''insert into STUDENT values('Student11', 'Cyber Security', 'CY')''')
cursor.execute('''insert into STUDENT values('Student12', 'Big Data', 'BD')''')
cursor.execute('''insert into STUDENT values('Student13', 'Cloud Computing', 'CC')''')
cursor.execute('''insert into STUDENT values('Student14', 'Machine Learning', 'ML')''')
cursor.execute('''insert into STUDENT values('Student15', 'Data Science', 'DS')''')
cursor.execute('''insert into STUDENT values('Student16', 'Natural Language', 'NLP')''')
cursor.execute('''insert into STUDENT values('Student17', 'Artificial Intelligence', 'AI')''')
cursor.execute('''insert into STUDENT values('Student18', 'Computer Vision', 'CV')''')
cursor.execute('''insert into STUDENT values('Student19', 'Cyber Security', 'CY')''')
cursor.execute('''insert into STUDENT values('Student20', 'Big Data', 'BD')''')
cursor.execute('''insert into STUDENT values('Student21', 'Cloud Computing', 'CC')''')
cursor.execute('''insert into STUDENT values('Student22', 'Machine Learning', 'ML')''')
cursor.execute('''insert into STUDENT values('Student23', 'Data Science', 'DS')''')
cursor.execute('''insert into STUDENT values('Student24', 'Natural Language', 'NLP')''')
cursor.execute('''insert into STUDENT values('Student25', 'Artificial Intelligence', 'AI')''')
cursor.execute('''insert into STUDENT values('Student26', 'Computer Vision', 'CV')''')
cursor.execute('''insert into STUDENT values('Student27', 'Cyber Security', 'CY')''')
cursor.execute('''insert into STUDENT values('Student28', 'Big Data', 'BD')''')
cursor.execute('''insert into STUDENT values('Student29', 'Cloud Computing', 'CC')''')
cursor.execute('''insert into STUDENT values('Student30', 'Machine Learning', 'ML')''')
cursor.execute('''insert into STUDENT values('Student31', 'Data Science', 'DS')''')
cursor.execute('''insert into STUDENT values('Student32', 'Natural Language', 'NLP')''')
cursor.execute('''insert into STUDENT values('Student33', 'Artificial Intelligence', 'AI')''')
cursor.execute('''insert into STUDENT values('Student34', 'Computer Vision', 'CV')''')
cursor.execute('''insert into STUDENT values('Student35', 'Cyber Security', 'CY')''')
cursor.execute('''insert into STUDENT values('Student36', 'Big Data', 'BD')''')
cursor.execute('''insert into STUDENT values('Student37', 'Cloud Computing', 'CC')''')
cursor.execute('''insert into STUDENT values('Student38', 'Machine Learning', 'ML')''')
cursor.execute('''insert into STUDENT values('Student39', 'Data Science', 'DS')''')
cursor.execute('''insert into STUDENT values('Student40', 'Natural Language', 'NLP')''')
cursor.execute('''insert into STUDENT values('Student41', 'Artificial Intelligence', 'AI')''')
cursor.execute('''insert into STUDENT values('Student42', 'Computer Vision', 'CV')''')
cursor.execute('''insert into STUDENT values('Student43', 'Cyber Security', 'CY')''')
cursor.execute('''insert into STUDENT values('Student44', 'Big Data', 'BD')''')
cursor.execute('''insert into STUDENT values('Student45', 'Cloud Computing', 'CC')''')
cursor.execute('''insert into STUDENT values('Student46', 'Machine Learning', 'ML')''')
cursor.execute('''insert into STUDENT values('Student47', 'Data Science', 'DS')''')
cursor.execute('''insert into STUDENT values('Student48', 'Natural Language', 'NLP')''')
cursor.execute('''insert into STUDENT values('Student49', 'Artificial Intelligence', 'AI')''')
cursor.execute('''insert into STUDENT values('Student50', 'Computer Vision', 'CV')''')
cursor.execute('''insert into STUDENT values('Student51', 'Cyber Security', 'CY')''')
cursor.execute('''insert into STUDENT values('Student52', 'Big Data', 'BD')''')
cursor.execute('''insert into STUDENT values('Student53', 'Cloud Computing', 'CC')''')
cursor.execute('''insert into STUDENT values('Student54', 'Machine Learning', 'ML')''')
cursor.execute('''insert into STUDENT values('Student55', 'Data Science', 'DS')''')

# Displaying the inserted records
print("The inserted records are: ")
data = cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)