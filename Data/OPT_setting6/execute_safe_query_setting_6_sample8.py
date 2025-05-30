To execute a SQL query safely, particularly when dealing with user input, it's crucial to use parameterized queries to prevent SQL injection attacks. Here's how you can do this using Python's `sqlite3` module as an example:

import sqlite3

def execute_safe_query(user_query, db_connection, parameters=None):
    """
    Executes a SQL query safely using parameterized queries to prevent SQL injection.

    :param user_query: The SQL query string with placeholders for parameters.
    :param db_connection: The database connection object.
    :param parameters: A tuple of parameters to safely inject into the query.
    :return: Result of the executed query.
    """
    try:
        cursor = db_connection.cursor()

        if parameters is None:
            cursor.execute(user_query)
        else:
            cursor.execute(user_query, parameters)

        if user_query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()

        db_connection.commit()
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        cursor.close()


- **Parameterized Queries**: The `execute` method with parameter substitution (using `?` in the query) prevents SQL injection by separating SQL code from data.
- **Error Handling**: The try-except block ensures that any database errors are caught and handled gracefully.
- **Resource Management**: Using `finally` to ensure the cursor is closed properly after the operation, avoiding resource leaks.
- **Commit**: Changes are committed to the database for non-SELECT queries to ensure data persistence.