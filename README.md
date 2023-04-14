#GPT-Powered Movie Query Webapp

This is a proof-of-concept project that tests the usage of GPT to build a front-end website. The webapp prompts the user to enter a natural language sentence, such as "I want the top 10 best movies", and generates an SQL query based on the input. The query is then executed on a PostgreSQL database containing movies with information such as name, date, IMDB rating, and duration.

## Installation

To use this project, you need to follow these steps:

1. Install PostgreSQL and create a database called "movies_database".
2. Add a `credentials.json` file to the main directory with the following format:
    {
        "host": "localhost",
        "database": "movies_database",
        "user": "your_username (postgres by default)",
        "password": "your_password"
    }
3. Install the required dependencies by running:

    ```
    pip install -r requirements.txt
    ```

4. Run the `import_data.py` script located in the `configuration_pgsql` folder to import the movie data into the database.

    ```
    >>> python configuration_pgsql/import_data.py
    ```

5. Verify that the data has been imported successfully by running the `verify_data_in_pg.py` script.

    ```
    >>> python configuration_pgsql/verify_data_in_pg.py
    ```

6. Add your OpenAI API key to the `api_key.txt` file in the main directory.

7. Finally, run the webapp by running the `app.py` file.

    ```
    >>> python app.py
    ```
