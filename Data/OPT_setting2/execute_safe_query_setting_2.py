import sqlite3

def execute_safe_query(user_query, db_connection):
    try:
        with db_connection:
            cursor = db_connection.cursor()
            cursor.execute(user_query)
            results = cursor.fetchall()
            return results
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
