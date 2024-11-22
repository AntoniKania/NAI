from recomendation_engine import getRecomendations
from data_fetcher import get_movie_object, get_movie_genres

data = getRecomendations(6)

def showRecomended(data):
    print("Filmy rekomendowane: \n")
    for title in data:
        metadata = get_movie_object(title)
        genres = get_movie_genres(metadata['id'], metadata['media_type'])
        print(title)
        print("Gatunki: " + ','.join(genres))
        print("Opis: " + metadata['overview'])
        print()

def showNotRecomended(data):
    print("Filmy odradzane: \n")
    print(', '.join(data))

showRecomended(data['recomendations'])
showNotRecomended(data['anti-recommendations'])
