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

db_connection = sqlite3.connect('example.db')
user_query = "SELECT * FROM users WHERE username = ?"
params = ('john_doe',)
results = execute_safe_query(db_connection, user_query, params)
print(results)

- **Parameterized Queries**: Use placeholders (`?` for SQLite, `%s` for PostgreSQL/MySQL) in the SQL query and pass parameters separately to prevent SQL injection.
- **Error Handling**: Implement error handling to manage database errors gracefully.
- **Resource Management**: Ensure that database cursors are closed after use to prevent resource leaks.
- **Commit Transactions**: Explicitly commit transactions for data-modifying queries to ensure changes are saved.

This approach ensures that user input is safely handled and the application remains secure against SQL injection attacks.