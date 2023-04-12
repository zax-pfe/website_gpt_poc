import openai

class Convert_to_sql:
    def __init__(self,api_path='api_key.txt'):
        openai.api_key = self.open_file(api_path)
        
    def open_file(self,filepath):
        with open(filepath, 'r', encoding='utf-8') as infile:
            return infile.read()
        
    def generate_response(self, user_query):

        completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "the answer must be less than 100 words"},
                    {"role": "system", "content": "the user will prompt a query in natural language, the system has to convert it into sql query"},
                    {"role": "system", "content": "The databse is : Postgres SQL table, with their properties movies(id,name,genre, year_of_production,best_imdb_score,duration)"},
                    {"role": "system", "content": "the different genre are : Action', 'Adult', 'Adventure', 'Comedy', 'Crime', 'Drama', 'Horror', 'Western', 'Animation', 'Biography', 'Documentary', 'Family', 'Fantasy', 'History', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Short', 'Film-Noir', 'News', 'Reality-TV', 'Talk-Show', 'Game-Show'"},
                    {"role": "system", "content": "there can be multiple genre like that :'Drama, Action'"},
                    {"role": "user", "content": "all the sci fi movies that were releaser between 2005 and 2008"},
                    {"role": "assistant", "content": " * FROM movies WHERE genre = 'sci-fi' AND year_of_production BETWEEN 2005 AND 2008"},
            {"role": "user", "content": user_query}]
        )

        
        return completion

