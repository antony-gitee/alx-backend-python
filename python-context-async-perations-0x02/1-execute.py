#!/usr/bin/env python3
import sqlite3

# ✅ Reusable context manager to execute a query with parameters
class ExecuteQuery:
    def __init__(self, query, params=None):
        self.query = query
        self.params = params or ()
        self.conn = None
        self.results = None

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

# ✅ Usage
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(query, params) as results:
    print(results)
