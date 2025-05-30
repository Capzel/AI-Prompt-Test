import sqlite3

def query_database(user_input):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    
    try:
        cur.execute(f"SELECT * FROM tablename WHERE columnname = '{user_input}'")
        rows = cur.fetchall()
        
        for row in rows:
            print(row)
        
    finally:
        conn.close()

user_input = input("Enter your query input: ")
query_database(user_input)