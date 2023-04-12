import psycopg2
from extract_credentials import return_credentials

from translation_natural_language_sql import Convert_to_sql

sql_convertor = Convert_to_sql()

# response = sql_convertor.generate_response("all the Dramas movies that are released after 2020")
# print("response: ", response)
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

# Prompt the user to enter a SQL query
# query = input("Enter a SQL query to search for movies (e.g., SELECT * FROM movies WHERE year_of_production > 2021):\n")

# Call the get_movies function with the user's query
a = get_movies("SELECT * FROM movies WHERE genre LIKE '%Sci-Fi%' AND year_of_production = 2003")
print(a)