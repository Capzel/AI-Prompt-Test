import sqlite3

def execute_safe_query(user_query, db_connection):
    try:
        with db_connection:
            formatted_query = user_query.strip().lower()
            if any(keyword in formatted_query for keyword in ["insert", "update", "delete", "drop", "alter"]):
                raise ValueError("Data modification queries are not allowed.")
            cursor = db_connection.cursor()
            cursor.execute(formatted_query)
            return cursor.fetchall()
    except (sqlite3.Error, ValueError) as e:
        raise RuntimeError(f"Query execution failed: {e}")