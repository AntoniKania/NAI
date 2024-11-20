import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering

movies = pd.read_csv('resources/movies_with_genres.csv')
movies_hca = movies.copy(deep=True)

tfidf = TfidfVectorizer(max_features=2000)
tfidf_matrix = tfidf.fit_transform(movies['genres'])

scaler = StandardScaler()
scaled_features = scaler.fit_transform(tfidf_matrix.toarray())

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

hca = AgglomerativeClustering(n_clusters=3, linkage='ward')
clusters_hca = hca.fit_predict(scaled_features)

movies['cluster'] = clusters
movies_hca['cluster'] = clusters_hca

def recommend(movie_titles, max_number_of_recommendations=5, type='kmeans', worst=False):
    if type == 'hca':
        movies['cluster'] = movies_hca['cluster']
    movie_ids = []
    for movie_title in movie_titles:
        movie_idx = movies[movies['title'].str.contains(movie_title)].index[0]
        movie_ids.append(movie_idx)
    
    clusters = movies.iloc[movie_ids]['cluster'].unique()
        
    similar_movies = movies[movies['cluster'].isin(clusters)].index
    similar_movies = similar_movies.difference(movie_ids)

    recommend_movies = movies.loc[similar_movies]

    if worst:
        filtered_recommend_movies = recommend_movies[recommend_movies['rate'] <= 7]
    else:
        filtered_recommend_movies = recommend_movies[recommend_movies['rate'] > 7]
    
    limit_df = filtered_recommend_movies.head(max_number_of_recommendations)
    return limit_df

test_array = ['Django', 'Cowboy Bebop', 'Powrót do przyszłości']
number_of_recomendations = 10
print("K-means recommended movies:")
print(recommend(test_array, number_of_recomendations, 'kmeans'))
print("K-means not recommended movies:")
print(recommend(test_array, number_of_recomendations, 'kmeans', True))
print("Hierarchical Clustering Algorithm recommended movies:")
print(recommend(test_array, number_of_recomendations, 'hca'))
print("Hierarchical Clustering Algorithm not recommended movies:")
print(recommend(test_array, number_of_recomendations, 'hca', True))
