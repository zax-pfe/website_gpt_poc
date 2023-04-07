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

# Save the cleaned dataset as a CSV file
movie_data.to_csv('cleaned_movie_data.csv', index=False)