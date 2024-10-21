import mysql.connector
from mysql.connector import Error

# Database connection parameters
db_name = "fitness_center_DB"
user = "root"
password = "Preciosa2016!"
host = "localhost"

try:
    conn = mysql.connector.connect(
        database = db_name,
        user = user,
        password = password,
        host = host
    )

    if conn.is_connected():
        print("Connected to MySQL database succesfully")

except Error as e: 
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("MySQL connection is closed.")