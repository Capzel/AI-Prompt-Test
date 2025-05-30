To execute a SQL query safely in Python, particularly if the query is constructed from user inputs, it's crucial to prevent SQL injection. Here’s how to handle this using parameterized queries with the `sqlite3` library. While only `sqlite3` is shown here due to its inclusion in the standard library, other database libraries, such as `psycopg2` for PostgreSQL or `mysql.connector` for MySQL, also support parameterized queries.

import sqlite3

def execute_safe_query(user_query: str, db_connection: sqlite3.Connection, params: tuple):
    """
    Execute a SQL query safely by using parameterized queries to prevent SQL injection.
    
    :param user_query: The query string with placeholders (e.g., 'SELECT * FROM users WHERE id = ?')
    :param db_connection: An established SQLite database connection
    :param params: A tuple containing the parameters to securely insert into the query
    """
    try:
        cursor = db_connection.cursor()
        cursor.execute(user_query, params)
        results = cursor.fetchall()
        cursor.close()
        
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        raise

db_conn = sqlite3.connect('example.db')  # Open database connection
query = 'SELECT * FROM users WHERE id = ?'
params = (42,)  # Ensure params is a tuple
results = execute_safe_query(query, db_conn, params)


- **Parameterized Queries**: Use placeholders (`?`) in the query string and provide a tuple of parameters (`params`) to ensure that inputs are automatically escaped properly, effectively preventing SQL injection.
  
- **Error Handling**: Wrap operations in a `try-except` block to catch and log exceptions properly, providing clear feedback and avoiding logging sensitive data.

- **Resource Management**: Always close the cursor after operations, even if exceptions occur, to free up resources in the database connection handle.

This method ensures that SQL interactions remain secure, even with dynamic inputs from users.