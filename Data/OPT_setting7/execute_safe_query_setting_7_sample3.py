To execute a SQL query safely, especially when dealing with user input, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's how you can do it using Python's `sqlite3` module as an example. If you're using a different database, the approach will be similar, but you might need to adjust the connection and cursor methods accordingly.

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
    finally:
        cursor.close()


1. **Parameterized Queries**: Use placeholders (`?` for SQLite) in the SQL query and pass the actual values as a tuple in the `params` argument. This prevents SQL injection by separating SQL code from data.
2. **Error Handling**: Use try-except blocks to catch and handle any database errors gracefully.
3. **Resource Management**: Ensure that the cursor is closed after the operation to free up resources.
4. **Commit Changes**: Explicitly commit changes for non-SELECT queries to ensure data integrity.

This approach ensures that your SQL execution is secure and robust against common vulnerabilities.