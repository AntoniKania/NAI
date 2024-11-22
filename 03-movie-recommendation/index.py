from recomendation_engine import getRecomendations
from user_input import showRecomended, showNotRecomended

if __name__ == "__main__":
    """
    Main script entry point for generating movie recommendations and anti-recommendations.

    This script prompts the user for their ID, retrieves movie recommendations 
    and anti-recommendations based on users in database viewing history,
    and displays them.

    It uses argv parameters that let select metric by user that is used in
    recommendation engine

    1. The script runs in a loop, asking the user to input their user ID.
    2. If the input is not a valid integer, it displays an error message and prompts again.
    3. Once a valid user ID is provided:
        - Calls the `getRecomendations` function to retrieve recommendations 
          and anti-recommendations for the specified user.
        - Calls `showRecomended` to display the recommended movies.
        - Calls `showNotRecomended` to display the anti-recommended movies.
    4. The script terminates after successfully displaying the results.
    """
    user_id = int(input("Podaj swoje id w bazie obejrzanych filmów: "))
    data = getRecomendations(user_id)
    showRecomended(data['recomendations'])
    showNotRecomended(data['anti-recommendations'])
