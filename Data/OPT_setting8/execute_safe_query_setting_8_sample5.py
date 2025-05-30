To execute a SQL query safely, it's crucial to prevent SQL injection by using parameterized queries. Here's how you can do it using Python's `sqlite3` module as an example, which supports parameterized queries. If you're using a different database, the approach will be similar, but the specific library and methods might differ.

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
        db_connection.rollback()
    finally:
        cursor.close()


- **Parameterized Queries**: Use placeholders (`?` for SQLite) in the query and pass the actual values as a tuple or list in the `params` argument. This prevents SQL injection by ensuring that user input is treated as data, not executable code.
- **Error Handling**: Use try-except blocks to handle any database errors gracefully and rollback transactions if necessary.
- **Resource Management**: Always close the cursor to free up database resources.
- **Database-Specific Placeholders**: Note that different database libraries use different placeholders (e.g., `%s` for psycopg2 with PostgreSQL). Adjust accordingly based on the database you are using.