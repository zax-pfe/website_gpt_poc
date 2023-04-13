from flask import Flask, render_template, request, redirect, url_for
import psycopg2


from extract_credentials import return_credentials

from translation_natural_language_sql_gpt4 import Convert_to_sql_gpt4
sql_convertor_gtp4 = Convert_to_sql_gpt4()


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
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        movies = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template("index.html", movies=movies, sql_query=sql_query)

    return render_template("index.html", movies=None, sql_query=None)

if __name__ == "__main__":
    app.run(debug=True)