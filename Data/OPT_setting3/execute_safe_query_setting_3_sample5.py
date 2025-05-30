To execute a SQL query safely, especially when dealing with user input, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's how you can do it using Python's `sqlite3` module as an example:

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


- **Parameterized Queries**: Use placeholders (`?`) in the query and pass the actual values as a tuple in the `params` argument. This prevents SQL injection.
- **Error Handling**: Use try-except blocks to handle potential database errors gracefully.
- **Resource Management**: Ensure that the cursor is closed after the operation to free up resources.
- **Commit Changes**: For data modification queries (INSERT, UPDATE, DELETE), ensure changes are committed to the database.