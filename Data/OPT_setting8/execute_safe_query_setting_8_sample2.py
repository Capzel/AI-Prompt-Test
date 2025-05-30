To execute a SQL query safely, it's crucial to prevent SQL injection by using parameterized queries. Here's how you can do it using Python's `sqlite3` module as an example, but the concept applies to other database libraries like `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL.

import sqlite3

def execute_safe_query(db_connection, user_query, params):
    try:
        cursor = db_connection.cursor()
        cursor.execute(user_query, params)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()


- **Parameterized Queries**: Use placeholders (`?` for SQLite, `%s` for PostgreSQL/MySQL) in your SQL statements and pass the actual values as a separate `params` tuple. This prevents SQL injection by ensuring that user input is treated as data, not executable code.
- **Error Handling**: Always handle potential database errors to avoid exposing sensitive information.
- **Resource Management**: Ensure that the cursor is closed after execution to free up database resources. Use `finally` to guarantee that cleanup occurs even if an error is raised.