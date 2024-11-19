import pandas as pd

movies_df = pd.read_csv('resources/movies_with_genres.csv')

def load_movies_from_csv():
    """
        Loads list of movies 

        Reads a CSV file containing movie data and extracts the titles into
        a list. This function assumes the CSV file has a column named title
        that contains the movie titles.

        Returns:
            list of str: A list of movie titles extracted from the title
            column of the CSV file.
        
        Example:
            If file resources/movies_with_genres.csv exists and contains this data:

            title,rate,genres
            Whiplash,10,"Dramat, Muzyczny"
            Dziennik Bridget Jones,1,"Komedia, Romans, Dramat"

            >>> load_movies_from_csv()
            ["Whiplash", "Dziennik Bridget Jones"]

    """
    movies = []
    movies_df = pd.read_csv('resources/movies_with_genres.csv')
    movies_df['title'].apply(lambda title: movies.append(title))
    return movies

def print_selection(movies):
    """
        Display movies Questionnaire to user

        Enumerates over movies and print them to standard output with index
        number used in selection process

        Args:
            movies (list of str): A list of movie titles

        Returns:
            none

        Example:
        >>> print_selection(["Whiplash", "Dziennik Bridget Jones"])

        Will print on standard output:

        --- Movie Questionnaire ---
        1. Whiplash
        2. Dziennik Bridget Jones

        Enter the numbers corresponding to the movies you've watched, separated by commas (e.g., 1,3,5):

    """
    print("\n--- Movie Questionnaire ---")
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie}")
    print("\nEnter the numbers corresponding to the movies you've watched, separated by commas (e.g., 1,3,5):")

def is_valid_selection(selection, movies):
    """
        Checks if movie index is valid

        Parses selection into number, and if is it, check if is in movies index
        range (from 1 to length of movies list)

        Args:
            selection (str): Selected movie (as index number, not parsed)
            movies (list of str): A list of movie titles

        Returns:
            bool: `True` if index is valid, `False` otherwise

        Example:
            >>> is_valid_selection(1, ["Whiplash", "Dziennik Bridget Jones"])
            true
            >>> is_valid_selection(3, ["Whiplash", "Dziennik Bridget Jones"])
            false
    """
    selection_without_whitespaces = selection.strip()
    return selection_without_whitespaces.isdigit() and 1 <= int(selection_without_whitespaces) <= len(movies)

def get_selected_movies(movies):
    """
        Gets watched movies from standard input

        Gahter indexes of watched movies from standard input, and based on it
        filters movie list. In case of parsing errors - it prints errors on
        standard output

        Args:
            movies (list of str): A list of all avaliable movie titles

        Returns:
            list of str: A list of selected movie titles
        
        Example:
            >>> get_selected_movies(["Whiplash", "Dziennik Bridget Jones", "Samurai Champloo"])
            >>> 1,2
            ["Whiplash", "Dziennik Bridget Jones"]
    """
    watched_movies = []
    try:
        selections = input("> ").split(",")
        for selection in selections:
            if is_valid_selection(selection, movies):
                watched_movies.append(movies[int(selection) - 1])
            else:
                print(f"Invalid selection: {selection}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return watched_movies

def generate_questionnaire(movies):
    """
        Generates questionnaire

        Displays questionnaire and handles selection of movies by user

        Args:
            movies (list of str): A list of all avaliable movie titles

        Returns:
            list of str: A list of selected movie titles
        
        Example:
            >>> generate_questionnaire(["Whiplash", "Dziennik Bridget Jones"])

            Will print on standard output:

            --- Movie Questionnaire ---
            1. Whiplash
            2. Dziennik Bridget Jones

            Enter the numbers corresponding to the movies you've watched, separated by commas (e.g., 1,3,5):
            >>> 1,2
            ["Whiplash", "Dziennik Bridget Jones"]
        
    """
    print_selection(movies)
    return get_selected_movies(movies)

def display_results(watched_movies):
    """
        Displays list of strings

        Prints on standard output formated list of strings using end of line and
        dash as a bullet point with aditionall description at the begining of
        list

        Args:
            watched_movies (list of str): A list of movie titles
        
        Returns:
            none

        Example:
            >>> display_results(["Whiplash", "Dziennik Bridget Jones"])

            Will display on standard output:

            You have watched the following movies:
            - Whiplash
            - Dziennik Bridget Jones
    """
    if watched_movies:
        print("\nYou have watched the following movies:")
        for movie in watched_movies:
            print(f"- {movie}")
    else:
        print("\nYou didn't select any movies as watched.")

movies = load_movies_from_csv()
watched_movies = generate_questionnaire(movies)
display_results(watched_movies)
