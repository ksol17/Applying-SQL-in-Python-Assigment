import mysql.connector
from mysql.connector import Error

def connect_database():
    """ Connect to the MySQL database and return the connection object """
    # Database connection parameters
    db_name = "fitness_center_DB"
    user = "root"
    password = "Preciosa2016!"
    host = "localhost"

    try:
        # Atterming to establish a connection
        conn = mysql.connector.connect(
            database=db_name, 
            user=user,
            password=password,
            host=host
        )

        # Check if the connection is successful
        print("Connected to MySQL database successfully")
        return conn
    
    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
        return None