To execute a SQL query safely, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's a secure way to execute a query using Python's `sqlite3` module as an example:

import sqlite3

def execute_safe_query(db_connection, user_query, params):
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


- **Parameterized Queries**: Use placeholders (`?` for SQLite) in the SQL query and pass the actual values as a tuple via the `params` argument. This prevents SQL injection.
- **Error Handling**: Use try-except blocks to handle potential database errors gracefully.
- **Resource Management**: Ensure that the cursor is closed after the operation to free up resources.
- **Commit Transactions**: For data-modifying queries, ensure changes are committed to the database.