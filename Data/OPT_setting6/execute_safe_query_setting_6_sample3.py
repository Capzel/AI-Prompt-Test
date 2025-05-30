To execute a SQL query safely, it is crucial to prevent SQL injection attacks by using parameterized queries instead of directly interpolating user input into the SQL statement. Here's how you can do it using Python's `sqlite3` module, which supports parameterized queries out of the box:

import sqlite3

def execute_safe_query(db_connection, user_query, params=()):
    try:
        with db_connection:
            cursor = db_connection.cursor()
            cursor.execute(user_query, params)
            results = cursor.fetchall()
            return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


- **Parameterized Queries**: Use placeholders (`?` in SQLite) in the SQL statement and pass the actual values as a tuple `params`. This prevents SQL injection by treating the parameters as data, not executable code.
- **Error Handling**: Wrap the execution in a try-except block to handle any database errors gracefully.
- **Resource Management**: Use context management (`with db_connection`) to ensure that the connection and cursor are properly managed, and resources are released back to the system.

This approach ensures that your application is resistant to SQL injection attacks and handles potential database errors gracefully.