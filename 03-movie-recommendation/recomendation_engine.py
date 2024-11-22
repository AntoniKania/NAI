import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances


# Load data
# Assume `data` is a DataFrame where rows are users and columns are movies
# Example: Use pandas to reshape the provided CSV data into such a structure

# Sample preprocessing: Creating a user-movie matrix
def preprocess_data(data):
    user_movie_matrix = data.pivot(index="User", columns="Movie", values="Rating")
    user_movie_matrix = user_movie_matrix.fillna(0)  # Replace NaN with 0
    return user_movie_matrix


# Clustering with KMeans
def cluster_users(user_movie_matrix, n_clusters=5, metric="euclidean"):
    if metric != "euclidean":
        # Calculate custom distance matrix
        dist_matrix = pairwise_distances(user_movie_matrix, metric=metric)
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, precompute_distances=False)
        kmeans.fit(dist_matrix)
    else:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(user_movie_matrix)
    return kmeans


# Generate recommendations and anti-recommendations
def recommend_movies(user_movie_matrix, kmeans, user_id, top_n=5):
    cluster = kmeans.labels_[user_id]
    cluster_users = user_movie_matrix[kmeans.labels_ == cluster]

    avg_ratings = cluster_users.mean(axis=0)
    user_ratings = user_movie_matrix.iloc[user_id]

    # Movies the user hasn't seen
    unseen_movies = avg_ratings[user_ratings == 0]

    # Top-N recommendations and anti-recommendations
    recommendations = unseen_movies.sort_values(ascending=False).head(top_n).index.tolist()
    anti_recommendations = unseen_movies.sort_values(ascending=True).head(top_n).index.tolist()
    return recommendations, anti_recommendations


def getRecomendations(user_id=0):

    # Assuming `data` is your loaded and reshaped DataFrame:
    data = pd.read_csv("resources/questionary_list.csv", header=None)
    count = data.shape[0]
    long_data = []

    # Iterate over each row to parse user and movie-rating pairs
    for _, row in data.iterrows():
        user = row.iloc[0]  # The second column contains the user's name
        pairs = row.iloc[1:]  # Skip the first two columns for movie-rating pairs

        #Process movie-rating pairs
        for i in range(count - 1, len(pairs), 2):  # Step by 2 to get movie-rating pairs
            movie = pairs[i]
            rating = pairs[i + 1]

            if pd.notna(movie) and pd.notna(rating):  # Skip if either is NaN
                long_data.append({"User": user, "Movie": movie, "Rating": float(rating)})

    df = pd.DataFrame(long_data)
    ddf = df.drop_duplicates()
    user_movie_matrix = preprocess_data(pd.DataFrame(long_data))

    # Cluster users
    kmeans = cluster_users(user_movie_matrix, n_clusters=5)

    # Recommend for a specific user (e.g., user_id=0)
    # user_id = 0  # Change as needed
    recommendations, anti_recommendations = recommend_movies(user_movie_matrix, kmeans, user_id)

    return {
        "recomendations": recommendations,
        "anti-recommendations": anti_recommendations
    }
