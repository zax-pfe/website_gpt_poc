import pandas as pd
import psycopg2
from psycopg2 import sql

# Replace these with your PostgreSQL credentials

from extract_credentials import return_credentials

host, database, user, password = return_credentials()


# host = "localhost"
# database = "movie_database"
# user = "postgres"
# password = "Axelfalco5859"
# Connect to the database


conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)
cursor = conn.cursor()

# Drop the movies table if it exists
cursor.execute("DROP TABLE IF EXISTS movies;")
conn.commit()

# Create the movies table
cursor.execute("""
    CREATE TABLE movies (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        genre VARCHAR(255),
        year_of_production INTEGER,
        best_imdb_score FLOAT,
        duration INTEGER
    );
""")
conn.commit()

# Load the cleaned_movie_data.csv
movie_data = pd.read_csv('cleaned_movie_data.csv')

# Insert data into the movies table
for index, row in movie_data.iterrows():
    cursor.execute(
        "INSERT INTO movies (name, genre, year_of_production, best_imdb_score, duration) VALUES (%s, %s, %s, %s, %s)",
        (row['name'], row['genre'], row['year_of_production'], row['best_imdb_score'], row['duration'])
    )
conn.commit()

# Close the connection
cursor.close()
conn.close()