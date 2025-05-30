import sqlite3

def query_database(user_input):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    user_query = f"SELECT * FROM data WHERE column_name = ?"
    cursor.execute(user_query, (user_input,))

    results = cursor.fetchall()
    conn.close()
    return results

user_input = input("Enter your search term: ")
results = query_database(user_input)
for row in results:
    print(row)