To execute a SQL query safely, especially when dealing with user input, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's a secure way to execute a query using Python's `sqlite3` module as an example. This approach can be adapted to other database libraries that support parameterized queries.

import sqlite3

def execute_safe_query(db_connection, user_query, params):
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


- **Parameterized Queries**: Use placeholders (`?` for SQLite) in the query and pass the actual values as a tuple in the `params` argument. This prevents SQL injection.
- **Error Handling**: Use try-except blocks to handle database errors gracefully.
- **Resource Management**: Always close the cursor in a `finally` block to ensure resources are released properly.
- **Commit Transactions**: Explicitly commit changes for data-modifying queries to ensure data integrity.