import sqlite3

def execute_safe_query(user_query, db_connection):
    cursor = db_connection.cursor()
    try:
        cursor.execute(user_query)
        db_connection.commit()
        return cursor.fetchall()
    except sqlite3.Error as e:
        db_connection.rollback()
        raise e
    finally:
        cursor.close()
