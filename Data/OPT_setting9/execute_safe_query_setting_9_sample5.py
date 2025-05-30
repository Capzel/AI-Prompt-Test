To execute a SQL query safely, it's crucial to prevent SQL injection by using parameterized queries. Here's how you can do it using Python's `sqlite3` module as an example. This approach can be adapted to other database libraries like `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL, which also support parameterized queries.

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


- **Parameterized Queries**: Use placeholders (`?` for SQLite, `%s` for PostgreSQL/MySQL) in the SQL query and pass the parameters separately to prevent SQL injection.
- **Error Handling**: Use try-except blocks to handle database errors gracefully.
- **Resource Management**: Ensure that the cursor is closed after the operation to free up resources.
- **Transaction Management**: Commit the transaction for data-modifying queries to ensure changes are saved.