# 4-stream_ages.py

import mysql.connector
from mysql.connector import Error

def stream_user_ages():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password',  # 🔁 Replace with your password
            database='ALX_prodev'
        )

        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        for row in cursor:
            yield row[0]

        cursor.close()
        connection.close()

    except Error as e:
        print(f"Error: {e}")


def average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1

    if count > 0:
        avg = total_age / count
        print(f"Average age of users: {avg}")
    else:
        print("No users found.")
