To execute a SQL query safely, it's crucial to prevent SQL injection by using parameterized queries. This involves using placeholders in the SQL statement and passing the actual values separately. Here's how you can do it using Python's `sqlite3` module as an example, but the concept applies to other database libraries like `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL.

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


- **Parameterized Queries**: Use placeholders (`?` for SQLite, `%s` for PostgreSQL/MySQL) in the SQL statement and pass the actual values as a separate tuple or list. This approach prevents SQL injection.
- **Error Handling**: Always handle exceptions to catch and log database errors.
- **Resource Management**: Use `finally` to ensure that resources like cursors are closed properly, even if an error occurs.
- **Commit Transactions**: Explicitly commit changes for data-modifying queries to ensure data integrity.