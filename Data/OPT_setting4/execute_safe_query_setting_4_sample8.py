To execute a SQL query safely, especially when dealing with user input, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's a secure way to execute a query using Python's `sqlite3` module as an example:

import sqlite3

def execute_safe_query(db_connection, user_query, params=()):
    try:
        cursor = db_connection.cursor()
        
        cursor.execute(user_query, params)
        
        if user_query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            return results
        
        db_connection.commit()
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        db_connection.rollback()
        
    finally:
        cursor.close()


- **Parameterized Queries**: Use placeholders (`?` for SQLite) and pass parameters as a tuple to avoid SQL injection.
- **Error Handling**: Implement error handling to manage exceptions and rollback transactions if necessary.
- **Resource Management**: Ensure that database cursors are closed properly to avoid resource leaks.