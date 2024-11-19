import pandas as pd

movies_df = pd.read_csv('resources/movies_with_genres.csv')

def load_movies_from_csv():
    movies = []
    movies_df = pd.read_csv('resources/movies_with_genres.csv')
    movies_df['title'].apply(lambda title: movies.append(title))
    return movies

def generate_questionnaire(movies):
    print("\n--- Movie Questionnaire ---")
    watched_movies = []
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie}")
    print("\nEnter the numbers corresponding to the movies you've watched, separated by commas (e.g., 1,3,5):")
    try:
        selections = input("> ").split(",")
        for selection in selections:
            selection = selection.strip()
            if selection.isdigit() and 1 <= int(selection) <= len(movies):
                watched_movies.append(movies[int(selection) - 1])
            else:
                print(f"Invalid selection: {selection}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return watched_movies

def display_results(watched_movies):
    if watched_movies:
        print("\nYou have watched the following movies:")
        for movie in watched_movies:
            print(f"- {movie}")
    else:
        print("\nYou didn't select any movies as watched.")

movies = load_movies_from_csv()
watched_movies = generate_questionnaire(movies)
display_results(watched_movies)
