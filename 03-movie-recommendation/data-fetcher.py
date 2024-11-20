import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.themoviedb.org/3'

def get_movie_object(title):
    """
    Fetches the first movie or TV show object matching the given title 
    from the API and returns it.

    Sends a GET request to the themoviedb multi-search endpoint.
    It queries the API for the specified `title` in Polish (`pl-PL` language)
    and retrieves the search results. Returns first of search if avaliable.
    Authentication by API_KEY

    Args:
        title (str): The title of the movie or TV show to search for.

    Returns:
        dict or None: A dictionary containing details of the first matching movie or TV 
        show, or `None` if no match is found or if an error occurs.

    Exceptions:
        Prints an error message if the request fails or an exception occurs during the process.

    Example:
        >>> get_movie_object("Whiplash")
        {
            'backdrop_path': '/5h8VtV4oh2qkO8Iqz7gypIYJPAr.jpg',
            'id': 244786,
            'title': 'Whiplash',
            'original_title': 'Whiplash',
            'overview': "Andrew (Miles Teller) jest utalentowanym młodym
                        perkusistą, uczniem konserwatorium muzycznego na
                        Manhattanie. Chłopak marzy o wielkiej karierze.
                        Aby zrealizować plany, postanawia dołączyć do szkolnej
                        orkiestry jazzowej prowadzonej przez okrutnego
                        nauczyciela Terence'a Fletchera (J.K. Simmons), który
                        często wyładowuje swoje frustracje na uczniach. Pod
                        kierunkiem bezwzględnego Fletchera, Andrew zaczyna
                        dążyć do doskonałości za wszelką cenę - nawet własnego
                        człowieczeństwa.",
            'poster_path': '/4Twi6WFaiGHc0SrIhdtZRNt45xg.jpg', 
            'media_type': 'movie',
            'adult': False,
            'original_language': 'en',
            'genre_ids': [18, 10402],
            'popularity': 158.388,
            'release_date': '2014-10-10',
            'video': False,
            'vote_average': 8.38,
            'vote_count': 15071
        }
        
    """
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
            return search_results['results'][0]
        else:
            return None
    except Exception as e:
        print(f"Error fetching data for {title}: {e}")
        return None

def fetch_movie_genres(title):
    """
    Fetches genres of movie from themoviedb api.

    Sends GET requests to the themoviedb and fetches metadata of
    movie based on title. It queries the API for the specified `title` in
    Polish (`pl-PL` language) and retrieves the search results. Returns genres
    of movie if avaliable. Authentication by API_KEY

    Args:
        title (str): The title of the movie or TV show to search for.

    Returns:
        list of str: List containing each genre

    Exceptions:
        Prints an error message if the request fails or an exception occurs during the process.

    Example:
        >>> fetch_movie_genres("Whiplash")
        ["Dramat, Muzyczny"]
        
    """
    try:
        movie = get_movie_object(title)

        if movie:
            movie_id = movie['id']
            media_type = movie['media_type']
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
    """
    Add to movie dataset genre information and saves it.

    Reads a CSV file containing a list of movies, fetches the genres for each
    movie, and adds the genres as a new column. The extended dataset is then
    saved to a new CSV file.

    Input and output file paths are hardcoded:
    - Input file: 'resources/movies.csv'
    - Output file: 'resources/movies_with_genres.csv'

    Returns:
        None

    Raises:
        ValueError: If the input CSV does not contain a `title` column.

    Example:
        Given an input CSV with a `title` column:
        ```
        title,rate
        Whiplash,10
        Dziennik Bridget Jones,1
        ```

        The output CSV will include a `genres` column:
        ```
        title,rate,genres
        Whiplash,10,"Dramat, Muzyczny"
        Dziennik Bridget Jones,1,"Komedia, Romans, Dramat"
        ```

    Output:
        A new CSV file named 'resources/movies_with_genres.csv' with the
        updated data.
        String on standard output on success: "Genres have been added.
        Output saved to resources/movies_with_genres.csv"
    """

    input_csv_path = 'resources/movies.csv'
    output_csv_path = 'resources/movies_with_genres.csv'
    movies_df = pd.read_csv(input_csv_path)
    if 'title' not in movies_df.columns:
        raise ValueError("The input CSV must have a 'Title' column.")
    movies_df['genres'] = movies_df['title'].apply(lambda title: ', '.join(fetch_movie_genres(title)))
    movies_df.to_csv(output_csv_path, index=False)
    print(f"Genres have been added. Output saved to {output_csv_path}.")

get_movie_genres()