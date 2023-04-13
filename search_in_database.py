import psycopg2
from extract_credentials import return_credentials

from translation_natural_language_sql import Convert_to_sql
from translation_natural_language_sql_gpt4 import Convert_to_sql_gpt4

sql_convertor = Convert_to_sql()
sql_convertor_gtp4 = Convert_to_sql_gpt4()

def get_movies(query):
    # Replace these with your PostgreSQL credentials
    host, database, user, password = return_credentials()

    # Connect to the database
    conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)
    cursor = conn.cursor()

    # Execute the user's SQL query
    cursor.execute(query)

    # Fetch and print the rows returned by the query
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No movies found.")
        
    # Close the connection
    cursor.close()
    conn.close()
    return rows

query = input("Enter a SQL query to search for movies (e.g., SELECT * FROM movies WHERE year_of_production > 2021):\n")
response = sql_convertor_gtp4.generate_response(query)



sql_query = response["choices"][0]["message"]["content"]
print("response: ", sql_query)
# Call the get_movies function with the user's query
output = get_movies(sql_query)
print(output)