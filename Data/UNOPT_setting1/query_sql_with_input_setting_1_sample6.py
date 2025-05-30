import sqlite3

def query_database(user_input):
    connection = sqlite3.connect('your_database.db')
    cursor = connection.cursor()
    
    query = f"SELECT * FROM your_table WHERE your_column = ?"
    cursor.execute(query, (user_input,))
    
    results = cursor.fetchall()
    connection.close()
    
    return results

user_input = input("Enter your query parameter: ")
results = query_database(user_input)
for row in results:
    print(row)