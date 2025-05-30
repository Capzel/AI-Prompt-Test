import sqlite3

def query_database(user_input):
    sanitized_input = user_input.replace("'", "''")
    query = f"SELECT * FROM my_table WHERE my_column = '{sanitized_input}';"
    
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    connection.close()
    
    return results

user_input = input("Enter your query parameter: ")
result_set = query_database(user_input)
print(result_set)