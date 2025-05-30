To execute a SQL query safely, it's crucial to prevent SQL injection by using parameterized queries. Below is an example using Python's `sqlite3` module, which is representative of how you would handle this with other database libraries like `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL.

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


- **Parameterized Queries**: Use placeholders (`?` for SQLite, `%s` for PostgreSQL/MySQL) in the query and pass parameters separately to prevent SQL injection.
- **Error Handling**: Use try-except blocks to handle potential database errors gracefully.
- **Resource Management**: Ensure that database cursors are closed properly using a `finally` block to avoid resource leaks.
- **Database-Specific Syntax**: Note that the placeholder syntax may vary depending on the database library used (e.g., `%s` for psycopg2). Always refer to the specific library's documentation for details.