# seed.py
import csv
import uuid
import mysql.connector
from mysql.connector import Error

DB_NAME = "ALX_prodev"

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        print("Database created successfully")
    except Error as e:
        print(f"Error creating database: {e}")

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password",
            database=DB_NAME
        )
        return connection
    except Error as e:
        print(f"Error connecting to {DB_NAME}: {e}")
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        );
        """
        cursor.execute(query)
        connection.commit()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']

                cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
                if not cursor.fetchone():
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, name, email, age)
                    )
            connection.commit()
            print("Data inserted successfully")
    except Error as e:
        print(f"Error inserting data: {e}")

