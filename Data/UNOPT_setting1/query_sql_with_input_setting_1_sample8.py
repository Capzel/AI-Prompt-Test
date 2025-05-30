import sqlite3

def query_database(user_input):
    connection = sqlite3.connect('your_database.db')
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT * FROM your_table WHERE column_name = ?", (user_input,))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except sqlite3.Error as error:
        print("Error executing query:", error)
    finally:
        connection.close()

user_input = input("Enter your query parameter: ")
query_database(user_input)