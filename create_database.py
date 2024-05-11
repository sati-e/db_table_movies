import mysql.connector

# create connection to mysql
connection = mysql.connector.connect(
    user='root',   # your user
    password='',   # your password
    host='localhost'  # your host name
    # database = 'database name'
)

print("connection started")

# create cursor
cursor = connection.cursor()

# creating database
sql = "CREATE DATABASE if not exists db_movies"
cursor.execute(sql)
db_cinema = 'db_cinema'
db_mtheater = 'db_mtheater'
cursor.execute(f"ALTER DATABASE {db_cinema} RENAME TO {db_mtheater};")
connection.commit()

# close connection
cursor.close()
connection.close()
print("connection closed")