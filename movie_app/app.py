from flask import Flask, render_template, request, redirect, url_for
import psycopg2


from extract_credentials import return_credentials
from get_image_imdb import get_movie_image, open_file

from translation_natural_language_sql_gpt4 import Convert_to_sql_gpt4
sql_convertor_gtp4 = Convert_to_sql_gpt4()

api_key_path = "C:\\Users\\PUECH Axel\\Documents\\POC GPT\\api_key_omdb.txt"

app = Flask(__name__)

def get_connection():

    host, database, user, password = return_credentials()

    conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        response = sql_convertor_gtp4.generate_response(query)
        sql_query = response["choices"][0]["message"]["content"]
        call = True
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        movies = cursor.fetchall()
        
        print("===== MOVIES =====",movies)
        cursor.close()
        conn.close()

        return render_template("index.html", movies=movies, sql_query=sql_query, call=call)

    return render_template("index.html", movies=None, sql_query=None, call=False)

@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    # Retrieve movie image URL here
    print(movie_id)
    movie_image_url = get_movie_image(movie_id,open_file(api_key_path))
    print(movie_image_url)
    
    # movie_image_url = "https://example.com/path/to/movie/image.jpg"
    return render_template('movie_details.html', movie_image_url=movie_image_url)

if __name__ == "__main__":
    app.run(debug=True)