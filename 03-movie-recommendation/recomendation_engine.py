import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances
import sys

def preprocess_data(data):
    """
    Preprocess raw user-movie rating data into a matrix suitable for clustering.

    This function takes a dataset with user, movie, and rating information, 
    converts it into a user-movie matrix where rows correspond to users and 
    columns correspond to movies, and fills any missing values with 0. In that
    case not popular movies will be less often recommended that more popular
    one. Using it is debatable, and we want to talk it through - in contruary,
    filling it with average is also a option (it will benefits less popular
    movies).

    Args:
        data (pandas.DataFrame)
        A DataFrame containing user, movie, and rating information. It should 
        have the following columns:
        - "User": Identifier for each user (e.g., user IDs).
        - "Movie": Identifier for each movie (e.g., movie titles or IDs).
        - "Rating": The rating a user has given to a movie.

    Returns:
        user_movie_matrix (pandas.DataFrame)
        A pivot table where rows correspond to users, columns correspond to 
        movies, and the values are the ratings. Missing ratings are replaced 
        with 0.
    """
    user_movie_matrix = data.pivot(index="User", columns="Movie", values="Rating")
    user_movie_matrix = user_movie_matrix.fillna(0)
    return user_movie_matrix


# Clustering with KMeans
def cluster_users(user_movie_matrix, n_clusters=5, metric="euclidean"):
    """
    Cluster users based on their movie preferences using the k-means algorithm.

    Args:
    user_movie_matrix : array-like or sparse matrix, shape (n_users, n_movies)
        A matrix where each row represents a user, and each column represents 
        a movie. The values indicate user preferences or interactions with 
        the corresponding movies (e.g., ratings or binary indicators).

    n_clusters : int, default=5
        The number of clusters to form.

    metric : str, default="euclidean"
        The distance metric to use for clustering. If "euclidean", the k-means 
        algorithm operates directly on the `user_movie_matrix`. For other metrics, 
        a pairwise distance matrix is computed, and clustering is performed on 
        this matrix. Supported metrics include "manhattan", "cosine", etc.

    Returns:
        sklearn.cluster.KMeans : A fitted k-means clustering model. The `labels_`
        attribute of the model contains the cluster assignments for each user.
    """
    if metric != "euclidean":
        dist_matrix = pairwise_distances(user_movie_matrix, metric=metric)
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(dist_matrix)
    else:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(user_movie_matrix)
    return kmeans

def recommend_movies(user_movie_matrix, kmeans, user_id, top_n=5):
    """
    Generate personalized movie recommendations and anti-recommendations for a user.

    This function identifies movies that a user has not seen and recommends the 
    most liked movies among their cluster, while also identifying the least liked 
    movies as anti-recommendations.

    Args:
    user_movie_matrix (pandas.DataFrame) : A user-movie matrix where rows
        represent users, columns represent movies, and values represent the
        ratings given by users to movies. A value of 0 indicates the user has
        not rated (or seen) the movie.

    kmeans (sklearn.cluster.KMeans) : A fitted k-means clustering model where
        each user is assigned to a cluster 
        based on their preferences.

    user_id (int) : The index of the user in the `user_movie_matrix` for whom
        recommendations are to be generated.

    top_n (int, default=5): The number of top recommendations and
        anti-recommendations to return.

    Returns:
        recommendations (list) : A list of the top `top_n` recommended movie
        titles (column names in the `user_movie_matrix`) for the user.

        anti_recommendations (list) : A list of the top `top_n` least
        recommended movie titles for the user.

    """
    cluster = kmeans.labels_[user_id]
    cluster_users = user_movie_matrix[kmeans.labels_ == cluster]

    avg_ratings = cluster_users.mean(axis=0)
    user_ratings = user_movie_matrix.iloc[user_id]
    unseen_movies = avg_ratings[user_ratings == 0]

    recommendations = unseen_movies.sort_values(ascending=False).head(top_n).index.tolist()
    anti_recommendations = unseen_movies.sort_values(ascending=True).head(top_n).index.tolist()
    return recommendations, anti_recommendations

def parseData(data):
    """
    Parse a DataFrame containing user and movie-rating pairs into a structured list.

    This function processes a DataFrame where each row represents a user, followed by 
    alternating movie titles and their corresponding ratings. It extracts this information 
    and returns it as a list of dictionaries, where each dictionary contains a user, 
    a movie, and the associated rating.

    Args:
        data (pandas.DataFrame): A DataFrame where:
        - The first column contains user identifiers.
        - Subsequent columns contain alternating movie names and ratings (e.g., 
          Movie1, Rating1, Movie2, Rating2, etc.).
        Missing values (NaN) in either movie or rating columns are ignored.

    Returns:
        list of dict: A list of dictionaries where each dictionary has the following keys:
        - "User": The user identifier.
        - "Movie": The movie name.
        - "Rating": The movie rating (as a float).
    """
    count = data.shape[0]
    parsedData = []

    for _, row in data.iterrows():
        user_name = row.iloc[0]
        movie_rating_pairs = row.iloc[1:]  # Skip the first two columns - username/NaN pair

        for i in range(count - 1, len(movie_rating_pairs), 2):
            movie = movie_rating_pairs[i]
            rating = movie_rating_pairs[i + 1]

            if pd.notna(movie) and pd.notna(rating):
                parsedData.append({"User": user_name, "Movie": movie, "Rating": float(rating)})
    return parsedData
    

def getRecomendations(user_id = 0):
    """
    Generate movie recommendations and anti-recommendations for a given user.

    This function processes a dataset containing user-movie-rating data, clusters 
    users into groups based on their preferences, and provides personalized 
    recommendations and anti-recommendations for a specified user.

    Args:
        user_id (int, default=0): The identifier of the user for whom
        recommendations and anti-recommendations are generated. The `user_id`
        should correspond to a row index in the user-movie matrix.

    Returns:
        dict: A dictionary containing:
        - "recommendations": A list of recommended movies for the user.
        - "anti-recommendations": A list of movies not recommended for the user.

    """
    data = pd.read_csv("resources/questionary_list.csv", header=None)
    parsed_data = parseData(data)
    user_movie_matrix = preprocess_data(pd.DataFrame(parsed_data))
    metric = "euclidean"
    if len(sys.argv) > 1:
        metric = sys.argv[1]
        print(f"Using: {metric} metric")
    else:
        print("No metric provided, using euclidean")

    kmeans = cluster_users(user_movie_matrix, 5, metric)

    recommendations, anti_recommendations = recommend_movies(user_movie_matrix, kmeans, user_id)

    return {
        "recomendations": recommendations,
        "anti-recommendations": anti_recommendations
    }
