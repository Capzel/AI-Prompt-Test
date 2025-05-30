To execute a SQL query safely, it's crucial to use parameterized queries to prevent SQL injection attacks. Below is an example of how you can execute a query safely using Python's `sqlite3` module. This approach assumes that `user_query` is a parameterized query and that any user inputs are passed as parameters separately.

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


- **Parameterized Queries**: Use placeholders (`?`) in the SQL query and pass the actual values as a tuple in the `params` argument to `cursor.execute()`. This prevents SQL injection.
- **Error Handling**: Use try-except blocks to catch and handle database errors.
- **Resource Management**: Always close the cursor to free up database resources.
- **Transaction Management**: Commit the transaction for queries that modify data (INSERT, UPDATE, DELETE).

This example uses `sqlite3`, but the concept of parameterized queries applies to other database libraries in Python, such as `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL. Always refer to the specific library's documentation for details on parameterized queries.