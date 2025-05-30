import sqlite3

def query_database(user_query):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    try:
        cursor.execute(user_query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
    finally:
        conn.close()

user_input = input("Enter your SQL query: ")
query_database(user_input)