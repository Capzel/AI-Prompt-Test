import sqlite3

def query_database(user_input):
    conn = sqlite3.connect('example.db')  # Replace with your database
    cursor = conn.cursor()
    
    query = f"SELECT * FROM your_table WHERE your_column = ?"
    cursor.execute(query, (user_input,))
    
    results = cursor.fetchall()
    conn.close()
    
    return results

user_input = input("Enter your query parameter: ")
results = query_database(user_input)
for row in results:
    print(row)