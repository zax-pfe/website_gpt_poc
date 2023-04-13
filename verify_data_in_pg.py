import psycopg2

from extract_credentials import return_credentials

host, database, user, password = return_credentials()

# Connect to the database
conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)
cursor = conn.cursor()

# Count the number of rows in the movies table
cursor.execute("SELECT COUNT(*) FROM movies;")
row_count = cursor.fetchone()[0]
print(f"Number of rows in the movies table: {row_count}")

# Fetch and print the first 10 rows from the movies table
cursor.execute("SELECT * FROM movies LIMIT 10;")
rows = cursor.fetchall()

print("\nFirst 10 rows in the movies table:")
for row in rows:
    print(row)

# Close the connection
cursor.close()
conn.close()