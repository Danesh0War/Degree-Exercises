import sys
from typing import Any, Dict, List, Union

import helper
from board import Board
from car import Car

JsonCoordinates = List[int]
CarConfiguration = List[Union[int, JsonCoordinates]]


class Game:
    """
    Represents a game session of 'Rush Hour', a puzzle game where players move cars on a grid to clear a path for the
    escape vehicle. This class manages game initialization, user interactions, and the game loop until completion.
    """

    def __init__(self, board: Board) -> None:
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board
        # Controls the continuation of the game loop.
        self.__continue_game = True

    @staticmethod
    def load_configuration(config_file: str) -> Dict[str, CarConfiguration]:
        """
        Loads the car configuration from a JSON file to set up the game board.
        :param config_file: The path to the configuration file.
        :return: A dictionary containing the configuration.
        """
        return helper.load_json(config_file)

    def setup_board(self, config: Dict[str, Any]) -> None:
        """
        This method initializes the board state before the game starts. Function iterates through each car
        configuration provided, creates a Car object, and attempts to place it on the board. If placement fails
        it outputs an error message and continues to place the rest of remaining cars. It also checks
        if the initial board setup results in a victory condition.
        """
        for name, config in config.items():
            length, location, orientation = config
            location_tuple = tuple(location)
            car = Car(name, length, location_tuple, orientation)
            if not self.__board.add_car(car):
                print(f"Failed to add car: {name}")
        if self.check_victory():
            print(self.__board)
            print("Victory! The car has reached the target location immediately after loading the configuration.")
            self.__continue_game = False

    def __single_turn(self):
        """
        Executes a single turn in the game. This method handles user input, validates it, executes moves, and checks
        for game victory.

        During a turn:
        1. The current state of the board is displayed.
        2. The user is prompted to enter a command to move a car or quit the game.
        3. Input is parsed and validated for correct format and feasibility of the requested move.
        4. If the input is valid, the move is executed on the board, and the board's state is updated.
        5. After the move, the game checks for a victory condition to determine if the game should end.
        """

        print(self.__board)
        user_input = input("Enter the car name and direction (e.g., Y,d) or '!' to quit: ").strip()

        if user_input == '!':
            print("Exiting the game.")
            self.__continue_game = False
            return

        if ',' not in user_input or len(user_input.split(',')) != 2:
            print("Invalid input format. Please use the format 'car_name,direction' (e.g., Y,d).")
            return

        car_name, direction = user_input.split(',')
        car_name = car_name.strip().upper()
        direction = direction.strip().lower()

        if car_name not in self.__board.cars:
            print(f"No car found with the name {car_name}.")
            return

        if direction not in ['u', 'd', 'l', 'r']:
            print("Invalid direction. Use 'u' for up, 'd' for down, 'l' for left, 'r' for right.")
            return

        if not self.__board.move_car(car_name, direction):
            print(f"Move '{direction}' for car '{car_name}' is not valid.")
        else:
            if self.check_victory():
                print(self.__board)
                print("Congratulations! You've won the game.")
                self.__continue_game = False

    def play(self) -> None:
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while self.__continue_game:
            self.__single_turn()

    def check_victory(self) -> bool:
        """
        Determines if the victory condition for the game has been met.
        :return: True if the car has reached the target location, False otherwise.

        If any car's coordinates include the target location, returns True, indicating the game has been won.
        """
        for car in self.__board.cars.values():
            coordinates = car.car_coordinates()
            if self.__board.target_location() in coordinates:
                return True
        return False


if __name__ == "__main__":
    # If config proved form command line
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
    else:
        # Prompts the user to enter the configuration file path if not provided as a command line argument.
        config_file = input("Enter the path to the JSON configuration file: ").strip().strip('"')

    # Attempts to load the configuration, handling any errors that occur due to file access issues.

    # Initializes the game board.
    board = Board()
    # Creates a game instance with the initialized board.
    game = Game(board)
    try:
        # Loads the game configuration from the specified file.
        config = game.load_configuration(config_file)
        # Sets up the game board with cars from the loaded configuration.
        game.setup_board(config)
    except FileNotFoundError:
        print(f"Error: File '{config_file}' does not exist or could not be accessed.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

    # If ok,starts the game loop.
    game.play()
