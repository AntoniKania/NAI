import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('resources/movies_with_genres.csv')  # Przykładowy plik

tfidf = TfidfVectorizer(max_features=2000)
tfidf_matrix = tfidf.fit_transform(movies['genres'])

scaler = StandardScaler()
scaled_features = scaler.fit_transform(tfidf_matrix.toarray())

kmeans = KMeans(n_clusters=10, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

movies['cluster'] = clusters

def recommend(movie_title, max_number_of_recommendations=5):
    movie_idx = movies[movies['title'].str.contains(movie_title)].index[0]
    cluster = movies.iloc[movie_idx]['cluster']
    
    similar_movies = movies[movies['cluster'] == cluster].index

    #make sure that we do not take a larger sample than population 
    all_recomendations = similar_movies.size
    num_recommendations = max_number_of_recommendations if max_number_of_recommendations < all_recomendations else all_recomendations

    recommendations = movies.loc[similar_movies].sample(num_recommendations)    
    return recommendations[['title', 'rate', 'genres']]


print(recommend('Trainspotting', 2))
