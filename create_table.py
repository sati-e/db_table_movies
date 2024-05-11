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

# create table
table_sql = '''CREATE TABLE tb_movies (
            title VARCHAR(45) NULL,
            date DATE NULL,
            price DECIMAL NOT NULL,
            id INT NOT NULL AUTO_INCREMENT,
            PRIMARY KEY (id)
            ) '''

cursor.execute(table_sql)
# close connection
cursor.close()
connection.close()
print("connection closed")
