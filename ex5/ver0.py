import sys
import os
from collections import defaultdict

#  GLOBAL CONSTANTS
# All the defined search directions accordingly to documentation
VALID_DIRECTIONS = {'u', 'd', 'r', 'l', 'w', 'x', 'y', 'z'}
# Dictionary matching to each direction a vector (tuple representing the change in row (x) and column (y)):
# (1 For down, -1 for up, 0 if not moving, 1 For right , -1 for left, 0 if not moving)
DIRECTION_VECTORS = {
    'r': (0, 1), 'l': (0, -1), 'u': (-1, 0), 'd': (1, 0),
    'w': (-1, 1), 'x': (-1, -1), 'y': (1, 1), 'z': (1, -1)
}


def find_file_recursively(filename, search_path='.'):
    """
      Search for a file recursively in the directory tree starting from the search_path.

      Args:
          filename (str): The name of the file to search for.
          search_path (str): The starting directory for the search (by default current directory).

      Returns:
          str: The full path to the file if found, otherwise None.
      """
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None


def read_wordlist(filename):
    """
    Read a list of words from a file, traversing each line, removing \n escape sequences and appending to a list (thus
    saving the words order).

       Args:
           filename (str): The name of the file containing the word list.

       Returns:
           list: A list of words.

       Exits:
           If the file is not found or cannot be opened, the program exits with an appropriate error message.
       """
    # trying to find the full location of the desired file
    filepath = find_file_recursively(filename)
    # if not found, terminate the program and print informative message
    if not filepath:
        print(f"Word file {filename} not found.")
        sys.exit(1)
    # if found, only then declare return container
    list_of_words = []  # declaring return list
    # try to open the desiree file
    try:
        # with for safe closing process.
        with open(filepath, 'r') as f:
            line = f.readline()
            while line:
                list_of_words.append(line.strip())
                line = f.readline()
        return list_of_words
    # if we couldn't open file, also terminate the program with appropriate error type
    except PermissionError:
        print(f"Error while opening the file {filename}.")
        sys.exit(1)


def read_matrix(filename):
    """
       Read a matrix of letters from a file.

       Args:
           filename (str): The name of the file containing the matrix.

       Returns:
           list: A list of lists representing the matrix.

       Exits:
           If the file is not found or cannot be opened, the program exits with an error message.
       """

    # trying to find the full location of the desired file
    filepath = find_file_recursively(filename)
    # if not found, terminate the program and print informative message
    if not filepath:
        print(f"matrix file {filename} not found.")
        sys.exit(1)

    # if found, only then declare return container
    letter_matrix = []
    try:
        # with for safe closing process.
        with open(filepath, 'r') as f:
            for line in f:
                # split all letters based on comma between them and add the line of letters as a row to letter_matrix
                matrix_row = line.strip().split(',')
                letter_matrix.append(matrix_row)

        return letter_matrix

    # if we couldn't open file, also terminate the program with appropriate error type
    except PermissionError:
        print(f"Error while opening the file {filename}.")
        sys.exit(1)


def convert_matrix_to_dict(matrix):
    """
    Convert a matrix of letters into a dictionary. Key - letter, value - position in matrix [row_num, num_in_row] -
    in this way we will bind all the locations to the desired character The points for this task are also given for
    efficiency, so I tried to find out creative solution to not traverse again and again blindly to find the
    beginning letter of each word. In O(1) we will point for the first letter for each word, then perform
    validations for the possible next letter from the current position and only then continue traversing (We already
    studied dictionaries).

        Args:
            matrix (list): A list of lists representing the matrix.

        Returns:
            dict: A dictionary where keys are characters and values are lists of (row, col) positions.
        """
    # Create a defaultdict with a list as the default value for position values
    char_positions = defaultdict(list)
    # Iterate over each row in the matrix
    for row_index, row in enumerate(matrix):
        # Iterate over each character in the row
        for col_index, char in enumerate(row):
            # Append the position (row, col) to the list of positions for the character
            char_positions[char].append((row_index, col_index))

    return char_positions


def validate_directions(directions):
    """
      Validate the provided directions (str) against the set of the valid ones.

      Args:
          directions (str): A string of directions to validate.

      Exits:
          If any invalid direction is found, the program exits with an error message.
      """
    # convert to set to ensure uniqueness
    provided_directions = set(directions)
    # If not subset of valid directions - there are one or more invalid characters in the input.
    if not provided_directions.issubset(VALID_DIRECTIONS):
        print(f"Invalid directions provided. Directions must be a combination of:", {VALID_DIRECTIONS})
        sys.exit(1)


def write_output(results, filename):
    """
       Write the search results to an output file.

       Args:
           results (list): A list of tuples  (words, their counts).
           filename (str): The name of the output file.
       """
    # With ensures safe proces closure. W mode to crete if not exists, and if exists - to override
    with open(filename, 'w') as f:
        for word, count in results:
            f.write(f"{word},{count}\n")


def is_valid_position(x, y, num_rows, num_cols):
    """
        Check if the position is valid within the matrix boundaries.

        Args:
            x (int): The row index.
            y (int): The column index.
            num_rows (int): The number of rows in the matrix.
            num_cols (int): The number of columns in the matrix.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
    return 0 <= x < num_rows and 0 <= y < num_cols


def is_word_in_direction(word, matrix, start_x, start_y, delta_x, delta_y):
    """
    Check if the word can be found in the specific direction starting from the potential position (first letter of
    the word) which we mapped as dictionary values

    Args:
        word (str): The word to search for.
        matrix (list): The matrix of letters.
        start_x (int): The starting row index of the letter.
        start_y (int): The starting column index of the letter.
        delta_x (int): The change in the row index for the direction.
        delta_y (int): The change in the column index for the direction.

    Returns:
        bool: True if the word is found, False otherwise.
    """
    word_len = len(word)
    for k in range(word_len):
        # Calculate the new position based on the current position and the direction (in which we're
        # currently traversing the matrix)
        new_x, new_y = start_x + k * delta_x, start_y + k * delta_y
        # Fast check if the new (next) position is valid and matches the next character in the word
        if not is_valid_position(new_x, new_y, len(matrix), len(matrix[0])) or matrix[new_x][new_y] != word[k]:
            return False
    # We found the word from the starting position! (The current word can be fitted within the boundaries and each
    # next character is part of the word)
    return True


def count_word_matches(word, matrix, positions, directions):
    """
       Count times word from the list is presented in matrix for each mapped position and for each chosen direction.

       Args:
           word (str): The word to search for.
           matrix (list): The matrix of letters.
           positions (dict): Dictionary values contain a list of suitable (row, col) positions to start the search from.
           directions (str): The directions to search in.

       Returns:
           int: The count of occurrences of the word.
       """
    count = 0
    # Traverse through all suitable positions
    for start_x, start_y in positions:
        # In all directions for each position
        for direction in directions:
            # For critical case when constant valid directions will not correspond to constant vectors (preventing
            # unexpected result)
            if direction in DIRECTION_VECTORS:
                delta_x, delta_y = DIRECTION_VECTORS[direction]
                # for each position and vector, if found match update counter
                if is_word_in_direction(word, matrix, start_x, start_y, delta_x, delta_y):
                    count += 1
    return count


def find_words(word_list, matrix, char_positions, directions):
    """
    Collective function which utilizes previous blocks to find all words in the word list within the matrix based on
    the provided directions.

        Args:
            word_list (list): A list of words to search for.
            matrix (list): The matrix of letters.
            char_positions (dict): A dictionary of character positions.
            directions (str): The directions to search in.

        Returns:
            list: A list of tuples containing words and their counts.
        """
    # Declare container for the results (tuples word, count)
    results = []

    for word in word_list:
        # Fast check to decide whether word exists in matrix (by first char).
        if word[0] in char_positions:
            # Point from whole matrix some positions to check for to all the necessary directions
            start_positions = char_positions[word[0]]
            # Count number of times the word appeared in the matrix
            word_count = count_word_matches(word, matrix, start_positions, directions)
            # Only if word appeared, at to results
            if word_count > 0:
                results.append((word, word_count))
    # If no word from the word_list appeared in matrix, return blank list (so later on we will return blank file
    # accordingly to requirements)
    return results


def main():
    # If the number of parameters isn't 4, message user and terminate program
    if len(sys.argv) != 5:
        print("Incorrect number of parameters.")
        sys.exit(1)
    # Assigning variables with parameters with values from command line input
    word_file = sys.argv[1]
    matrix_file = sys.argv[2]
    output_file = sys.argv[3]
    directions = sys.argv[4]

    # Attempting to pass to serving function str parameters from command line, if one of them is invalid we
    # will terminate the program immediately on him and print appropriate message
    word_list = read_wordlist(word_file)
    matrix = read_matrix(matrix_file)
    validate_directions(directions)

    # Map the characters
    char_positions = convert_matrix_to_dict(matrix)
    # Main function
    results = find_words(word_list, matrix, char_positions, directions)
    write_output(results, output_file)


if __name__ == '__main__':
    main()