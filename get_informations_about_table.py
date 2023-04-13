import psycopg2
import json
from extract_credentials import return_credentials
host, database, user, password = return_credentials()


def get_table_properties(table_name):
    


    # Connect to the database
    conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)
    cursor = conn.cursor()

    # Execute a SQL query to get the properties of the table
    cursor.execute(f"""
        SELECT column_name, data_type
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_name = '{table_name}';
    """)

    # Fetch and print the properties
    rows = cursor.fetchall()
    print(f"Properties of the '{table_name}' table:")
    for row in rows:
        print(f"Column Name: {row[0]}, Data Type: {row[1]}")

    # Close the connection
    cursor.close()
    conn.close()



def get_distinct_genres():

    # Connect to the database
    conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)
    cursor = conn.cursor()

    # Execute a SQL query to get all distinct genres
    cursor.execute("SELECT DISTINCT genre FROM movies;")

    # Fetch and print the distinct genres
    rows = cursor.fetchall()
    print("Distinct genres:")
    
    list_genre = []
    for row in rows:
        row_splited = row[0].split(',')
        for genre in row_splited:
            
            if genre not in list_genre:
                list_genre.append(genre)
    cursor.close()
    conn.close()
    return list_genre


a = get_distinct_genres()

print(a)
# get_table_properties("movies")