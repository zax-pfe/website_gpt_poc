import json
import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))


credentials_path = os.path.join(parent_dir,"credentials.json")


def return_credentials(json_path = credentials_path):
    # Load credentials from the JSON file
    with open(json_path, "r") as file:
        credentials = json.load(file)

    # Access the credentials in the Python script
    host = credentials["host"]
    database = credentials["database"]
    user = credentials["user"]
    password = credentials["password"]
    
    return host, database, user, password