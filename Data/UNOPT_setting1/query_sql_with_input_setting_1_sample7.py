import sqlite3

def query_database(user_input):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM your_table WHERE column_name = ?"
    cursor.execute(query, (user_input,))
    
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    conn.close()

user_input = input("Enter your query value: ")
query_database(user_input)