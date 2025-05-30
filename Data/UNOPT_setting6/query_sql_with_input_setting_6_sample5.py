import sqlite3

def query_database():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    user_input = input("Enter your query: ")
    
    try:
        cursor.execute(user_input)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    conn.close()

query_database()