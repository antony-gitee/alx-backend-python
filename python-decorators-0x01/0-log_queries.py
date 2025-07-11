#!/usr/bin/env python3
import sqlite3
import functools
from datetime import datetime  # ✅ Required for timestamp

# ✅ Decorator that logs the SQL query before execution
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = args[0] if args else kwargs.get('query', '')
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] Executing SQL Query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# ✅ Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")

