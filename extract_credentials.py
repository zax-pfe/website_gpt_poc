import json
import os
current_dir = os.getcwd() 
json_path = os.path.join(current_dir,"credentials.json" )
print("json_path", json_path)


def return_credentials(json_path = json_path):
    # Load credentials from the JSON file
    with open(json_path, "r") as file:
        credentials = json.load(file)

    # Access the credentials in the Python script
    host = credentials["host"]
    database = credentials["database"]
    user = credentials["user"]
    password = credentials["password"]
    
    return host, database, user, password