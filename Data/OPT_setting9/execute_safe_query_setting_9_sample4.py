To execute a SQL query safely, especially when dealing with user input, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's a secure way to execute a query using Python's `sqlite3` module as an example. If you're using a different database, the concept remains the same, but the specific library might differ.

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


1. **Parameterized Queries**: Use placeholders (`?` for SQLite) in the query and pass parameters as a tuple to prevent SQL injection.
2. **Error Handling**: Use try-except blocks to handle database errors and ensure the connection is rolled back in case of an error.
3. **Resource Management**: Use `finally` to ensure the cursor is closed, preventing resource leaks.
4. **Commit Transactions**: Explicitly commit transactions for non-SELECT queries to ensure changes are saved.