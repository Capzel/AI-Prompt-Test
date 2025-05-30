To execute a SQL query safely, especially when dealing with user input, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's how you can do it using Python's `sqlite3` module as an example. This approach can be adapted to other database libraries like `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL, which also support parameterized queries.

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


- **Parameterized Queries**: Use placeholders (`?` for SQLite, `%s` for PostgreSQL/MySQL) in the SQL query and pass the actual values as a tuple in the `params` argument. This prevents SQL injection by ensuring that user input is treated as data, not executable code.
- **Error Handling**: Use try-except blocks to handle potential database errors gracefully.
- **Resource Management**: Always close the cursor to free up database resources. Use `finally` to ensure the cursor is closed even if an error occurs.
- **Commit Transactions**: For data-modifying queries (INSERT, UPDATE, DELETE), ensure changes are committed to the database.