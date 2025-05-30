To execute an SQL query safely, you would typically use parameterized queries or prepared statements, which help protect against SQL injection attacks. Here's an example employing Python's `sqlite3` module in a way that ensures the necessary security precautions:

import sqlite3

def execute_safe_query(user_query, params, db_connection):
    """
    Safe execution of an SQL query with parameters.
    
    :param user_query: SQL query string with placeholders for parameters.
    :param params: A tuple of parameters to safely pass into the SQL query.
    :param db_connection: The database connection object.
    """
    with db_connection:
        cursor = db_connection.cursor()
        
        try:
            cursor.execute(user_query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            raise

query = "SELECT * FROM users WHERE username = ?"
parameters = ('john_doe',)  # parameterized to prevent SQL injection
results = execute_safe_query(query, parameters, db_connection)

print(results)

**Explanation:**
- Uses parameterized queries to prevent SQL injection. Here, placeholders `?` are used in the query string, and actual values are passed through the `params` tuple.
- A `with` statement is used to automatically handle cursor closure, promoting better resource management.
- Exceptions during execution are caught, allowing for error handling or logging. You can customize this further to raise exceptions or adjust error handling based on your application's needs.

Remember, using parameterized queries or prepared statements is vital when working with user-generated inputs, as it severely mitigates the risk of SQL injection attacks.