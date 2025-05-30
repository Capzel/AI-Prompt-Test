To execute a SQL query string safely in Python, it's important to use parameterized queries to prevent SQL injection. Directly executing user-provided SQL queries can be very dangerous. However, if you must execute a raw SQL query (e.g., for administrative tasks), you should ensure the input is sanitized and validated before execution. Below is an example using parameterized queries with Python's `sqlite3` library. If you're using a different database system, the approach will be similar.

import sqlite3

def execute_safe_query(user_query, parameters, db_connection):
    try:
        cursor = db_connection.cursor()
        
        cursor.execute(user_query, parameters)
        
        if user_query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            return results
        
        db_connection.commit()
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

db_connection = sqlite3.connect('example.db')
query = "SELECT * FROM users WHERE id = ?"
parameters = (1,)  # Parameters should be a tuple
results = execute_safe_query(query, parameters, db_connection)

- **Parameterized Queries:** Always use parameterized queries to prevent SQL injection.
- **Error Handling:** Include error handling to manage database exceptions.
- **Resource Management:** Ensure that cursors and connections are properly closed using a `finally` block or context managers.
- **Validation:** Validate and sanitize user inputs before using them in queries.