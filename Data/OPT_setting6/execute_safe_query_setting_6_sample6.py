To execute a SQL query safely, especially when dealing with user input, it is crucial to use parameterized queries to prevent SQL injection attacks. Here is a secure way to execute a query using Python's `sqlite3` module as an example:

import sqlite3

def execute_query_safely(db_connection, user_query, params=()):
    try:
        cursor = db_connection.cursor()
        
        cursor.execute(user_query, params)
        
        results = cursor.fetchall()
        
        db_connection.commit()
        
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        cursor.close()


- **Parameterized Queries**: Use placeholders (`?` for `sqlite3`) in the SQL query and pass user inputs as a tuple to prevent SQL injection.
- **Error Handling**: Catch and handle database errors to avoid crashing the application.
- **Resource Management**: Use `finally` to ensure the cursor is closed properly, freeing up resources.