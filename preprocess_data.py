import pandas as pd


# Load and clean the title.basics.tsv.gz file
title_basics = pd.read_csv('title.basics.tsv.gz', delimiter='\t', low_memory=False)
title_basics = title_basics[title_basics['titleType'] == 'movie']  # Filter only movies
title_basics = title_basics[['tconst', 'primaryTitle', 'startYear', 'runtimeMinutes', 'genres']]
title_basics = title_basics.rename(columns={
    'tconst': 'id',
    'primaryTitle': 'name',
    'startYear': 'year_of_production',
    'runtimeMinutes': 'duration',
    'genres': 'genre'
})

# Load and clean the title.ratings.tsv.gz file
title_ratings = pd.read_csv('title.ratings.tsv.gz', delimiter='\t', low_memory=False)
title_ratings = title_ratings[['tconst', 'averageRating']]
title_ratings = title_ratings.rename(columns={
    'tconst': 'id',
    'averageRating': 'best_imdb_score'
})

# Merge the two DataFrames
movie_data = title_basics.merge(title_ratings, on='id')

# Calculate the number of rows before removing '\N' values
rows_before = len(movie_data)

# Remove rows with '\N' values
movie_data = movie_data[(movie_data != '\\N').all(axis=1)]

# Calculate the number of rows after removing '\N' values
rows_after = len(movie_data)

# Calculate the number of rows deleted
rows_deleted = rows_before - rows_after

# Print the number of rows deleted
print(f"Deleted {rows_deleted} rows containing '\\N' values.")

# Save the cleaned dataset as a CSV file
movie_data.to_csv('cleaned_movie_data.csv', index=False)