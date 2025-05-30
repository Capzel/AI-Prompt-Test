To execute a SQL query safely, especially when dealing with user input, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's how you can do it using Python's `sqlite3` module as an example. If you're using a different database, the approach will be similar, but the library might differ (e.g., `psycopg2` for PostgreSQL, `mysql-connector-python` for MySQL).

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
        db_connection.rollback()
    finally:
        cursor.close()


- **Parameterized Queries**: Use placeholders (`?` for SQLite) in the query and pass the actual values as a tuple in the `params` argument. This prevents SQL injection.
- **Error Handling**: Use try-except blocks to handle database errors gracefully and rollback transactions if needed.
- **Resource Management**: Always close the cursor to free up database resources. Use `finally` to ensure this happens even if an error occurs.