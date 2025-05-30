To execute a SQL query safely, especially when dealing with user-generated input, it's crucial to prevent SQL injection by using parameterized queries. Here's a secure way to handle this in Python, assuming you're using a library like `sqlite3` or `psycopg2`:

def execute_safe_query(user_query, db_connection, params):
    """
    Execute a parameterized SQL query safely.

    Args:
    - user_query: A SQL query string with placeholders for parameters.
    - db_connection: A database connection object.
    - params: A tuple of parameters to safely inject into the query.

    Returns:
    - The result of the query execution.
    """
    with db_connection.cursor() as cursor:
        cursor.execute(user_query, params)
        result = cursor.fetchall()
    return result


- **Parameterized Queries**: Use placeholders (`%s` for psycopg2 or `?` for sqlite3) in the SQL query and provide parameters separately. This prevents SQL injection by safely escaping inputs.
- **Cursor Context Manager**: Use a context manager (`with` statement) to ensure the cursor is properly closed after use, which also helps prevent resource leaks.
- **Avoid Direct String Interpolation**: Never directly interpolate user inputs into the SQL query string. Always use parameterized queries as shown.

This approach ensures that your application is resistant to SQL injection attacks and can safely execute SQL commands.