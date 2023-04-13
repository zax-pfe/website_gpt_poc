import requests

def get_movie_image(movie_id, api_key):
    url = f"https://www.omdbapi.com/?i={movie_id}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()
        if 'Poster' in movie_data:
            return movie_data['Poster']
        else:
            print("Poster not found.")
            return None
    else:
        print("Error fetching movie data.")
        return None

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
    
# Example movie ID: tt1375666 (Inception)
movie_id = "146944"
api_key_path = "C:\\Users\\PUECH Axel\\Documents\\POC GPT\\api_key_omdb.txt"
api_key = open_file(api_key_path)

image_url = get_movie_image(movie_id, api_key)
print(image_url)