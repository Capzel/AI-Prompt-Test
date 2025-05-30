To execute a SQL query safely, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's a secure way to execute a query using Python's `sqlite3` module as an example:

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

- **Parameterized Queries**: Use placeholders (`?`) in the query and pass parameters as a tuple to prevent SQL injection.
- **Error Handling**: Implement error handling to manage database errors gracefully.
- **Resource Management**: Ensure the cursor is closed after operations to free up resources.