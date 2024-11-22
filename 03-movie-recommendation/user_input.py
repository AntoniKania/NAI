from data_fetcher import get_movie_object, get_movie_genres

def showRecomended(data):
    """
    Display a list of recommended movies with their genres and descriptions.

    This function takes a list of movie titles, retrieves additional metadata 
    for each movie, and displays the title, genres, and a brief overview.

    Args:
    data (list) : A list of recommended movie titles.
        
    """
    print("Filmy rekomendowane: \n")
    for title in data:
        metadata = get_movie_object(title)
        genres = get_movie_genres(metadata['id'], metadata['media_type'])
        print(title)
        print("Gatunki: " + ','.join(genres))
        print("Opis: " + metadata['overview'])
        print()

def showNotRecomended(data):
    """
    Display a list of anti-recommended movies.

    This function takes a list of movie titles that are not recommended for the user 
    and prints them as a comma-separated string.

    Args:
    data (list) : A list of not recommended movie titles.
    """
    print("Filmy odradzane: \n")
    print(', '.join(data))
    