To execute a SQL query safely, especially when dealing with user input, it's crucial to use parameterized queries to prevent SQL injection attacks. Below is an example of how to safely execute a SQL query using Python's `sqlite3` module, which supports parameterized queries. This approach can be adapted to other database libraries like `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL.

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


- **Parameterized Queries**: Use placeholders (`?` for SQLite, `%s` for PostgreSQL/MySQL) in the SQL query and pass parameters as a separate tuple. This prevents SQL injection.
- **Error Handling**: Implement error handling to manage exceptions and ensure the application remains robust.
- **Resource Management**: Use `finally` to ensure resources like cursors are closed properly, preventing resource leaks.