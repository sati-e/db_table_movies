import mysql.connector

# create connection to mysql
connection = mysql.connector.connect(
    user='root',   # your user
    password='',   # your password
    host='localhost',  # your host name
    database='db_movies'
)

# create cursor
cursor = connection.cursor()

# creating objects
# insert name
title = input("Title: ")

# insert date
date = input("Date: ")

# insert price
price = float(input("Price: "))

insert_sql = f'''INSERT INTO tb_movies 
            (title, date, price) values 
            ('{title}', '{date}', '{price}')'''

# executar comando
cursor.execute(insert_sql)

# commit changes
connection.commit()

# close connection
cursor.close()
connection.close()
print("connection closed")

