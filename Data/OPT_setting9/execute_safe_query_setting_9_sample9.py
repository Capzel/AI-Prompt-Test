To execute a SQL query safely, it's crucial to prevent SQL injection by using parameterized queries. Here's how you can do it using Python's `sqlite3` module as an example. This approach can be adapted to other database libraries like `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL, which also support parameterized queries.

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

db_connection = sqlite3.connect('example.db')
user_query = "SELECT * FROM users WHERE username = ?"
params = ('example_user',)
results = execute_safe_query(db_connection, user_query, params)
print(results)

- **Parameterized Queries**: Use placeholders (`?` for SQLite, `%s` for PostgreSQL/MySQL) in your SQL statements and pass parameters separately to prevent SQL injection.
- **Error Handling**: Always handle exceptions to manage database errors gracefully.
- **Resource Management**: Ensure that database cursors are closed after use to free up resources. Use `finally` to guarantee cleanup even if an error occurs.
- **Commit Transactions**: Explicitly commit changes for data-modifying queries to ensure data integrity.