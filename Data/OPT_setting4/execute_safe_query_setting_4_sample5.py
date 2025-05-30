To execute a SQL query safely, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's how you can do it using Python's `sqlite3` module as an example. This approach can be adapted to other database libraries like `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL, which also support parameterized queries.

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


- **Parameterized Queries**: Use placeholders (`?` for `sqlite3`, `%s` for `psycopg2`, etc.) in your SQL statements and pass parameters separately to prevent SQL injection.
- **Error Handling**: Implement error handling to manage database errors gracefully.
- **Resource Management**: Always close the cursor to free up database resources. Use `finally` to ensure cleanup occurs even if an error is raised.
- **Commit Transactions**: Explicitly commit transactions for data-modifying queries to ensure changes are saved.