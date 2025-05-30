To execute a SQL query safely, you should avoid directly incorporating user input into your SQL commands to prevent SQL injection attacks. Instead, use parameterized queries. Here’s how you can safely execute a query using the `sqlite3` library in Python, which supports parameterized queries:

import sqlite3

def execute_safe_query(db_connection, user_query, params):
    try:
        cursor = db_connection.cursor()
        cursor.execute(user_query, params)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

db_connection = sqlite3.connect('example.db')
user_query = "SELECT * FROM users WHERE username = ?"
params = ('example_user',)
results = execute_safe_query(db_connection, user_query, params)
print(results)
db_connection.close()

- **Parameterized Queries**: The `?` placeholder is used for parameterized queries, which helps prevent SQL injection by separating SQL code from data.
- **Error Handling**: Always include error handling to manage database exceptions.
- **Resource Management**: Use `finally` to ensure the cursor is closed properly, preventing resource leaks.