To execute a SQL query safely, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's how you can do it using Python's `sqlite3` module as an example. If you're using a different database, the approach will be similar, but you might need to adjust the connection and cursor methods accordingly.

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

- **Parameterized Queries**: Use placeholders (`?` for SQLite) in the SQL query and pass the actual values as a tuple in the `params` argument. This prevents SQL injection.
- **Error Handling**: Use try-except blocks to handle potential database errors gracefully.
- **Resource Management**: Ensure that the cursor is closed after the operation to free up resources.
- **Database-Specific Placeholders**: Note that different databases use different placeholders (e.g., `%s` for PostgreSQL with `psycopg2`).

This approach ensures that your SQL execution is secure and resistant to injection attacks.