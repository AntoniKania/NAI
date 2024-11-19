import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.themoviedb.org/3'

def fetch_movie_genres(title):
    try:
        search_url = f"{BASE_URL}/search/multi"
        params = {
            'api_key': API_KEY,
            'query': title,
            'language': 'pl-PL'
        }
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        search_results = response.json()

        if search_results['results']:
            movie_id = search_results['results'][0]['id']

            media_type = search_results['results'][0]['media_type']

            details_url = f"{BASE_URL}/{media_type}/{movie_id}"
            details_params = {
                'api_key': API_KEY,
                'language': 'pl-PL'
            }
            details_response = requests.get(details_url, params=details_params)
            details_response.raise_for_status()
            movie_details = details_response.json()

            genres = [genre['name'] for genre in movie_details.get('genres', [])]
            return genres
        else:
            return []
    except Exception as e:
        print(f"Error fetching data for {title}: {e}")
        return []

def get_movie_genres():
    input_csv_path = 'resources/movies.csv'
    output_csv_path = 'resources/movies_with_genres.csv'
    movies_df = pd.read_csv(input_csv_path)
    if 'title' not in movies_df.columns:
        raise ValueError("The input CSV must have a 'Title' column.")
    movies_df['genres'] = movies_df['title'].apply(lambda title: ', '.join(fetch_movie_genres(title)))
    movies_df.to_csv(output_csv_path, index=False)
    print(f"Genres have been added. Output saved to {output_csv_path}.")

get_movie_genres()