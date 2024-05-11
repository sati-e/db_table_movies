import mysql.connector

# create connection to mysql
connection = mysql.connector.connect(
    user='root',   # your user
    password='',   # your password
    host='localhost',  # your host name
    database='db_movies'
)

# creating cursor to execute the code
cursor = connection.cursor()

# select all columns
select_sql = '''select * from tb_movies'''
cursor.execute(select_sql)

# register tuples and print
l_registers = cursor.fetchall()
print("List of tuples: ")

# print vertical
for record in l_registers:
    print(record)

# Select the number of records in the tb_movies table
count_sql = '''SELECT COUNT(*) FROM tb_movies'''
cursor.execute(count_sql)

# Get the count result
count_result = cursor.fetchone()[0]

# Check if the table is empty
if count_result == 0:
    print("The tb_movies table is empty.")
else:
    print(f"The tb_movies table has {count_result} records.")

# select names
select_sql_name = '''select title from tb_movies'''
cursor.execute(select_sql_name)

# register tuples and print
l_registers = cursor.fetchall()
print("List of tuples: ")

# print vertical
for record in l_registers:
    print(record)

# commit changes
connection.commit()

# close connection
cursor.close()
connection.close()
print("connection closed")
