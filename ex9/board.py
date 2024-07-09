from typing import Tuple, List, Optional, Dict

from car import Car

Coordinates = Tuple[int, int]


class Board:
    """
    Manages the game board by providing a 7x7 grid with a designated target cell.
    Facilitates operations such as adding cars, moving them based on defined rules, and checking game state conditions.
    Supports functionalities like visualizing the board, identifying legal moves, and verifying position statuses.
    """

    def __init__(self) -> None:
        """
        Initializes a Board object with a fixed size and a target location.
        Also initializes an empty dictionary to store the cars on the board.
        """
        self.__size = 7  # Size of the board (7x7 grid)
        self.__target = (3, 7)  # Target location to be reached for victory
        self.__cars: Dict[str, Car] = {}  # Dictionary to store cars by their names

    @property
    def cars(self):
        return self.__cars

    def target_location(self) -> Coordinates:
        """
        This function returns the coordinates of the location that should be
        filled for victory.
        :return: (row, col) of the goal location.
        """
        return self.__target

    def initialize_board(self):
        """
        Initializes the board with the appropriate size and adds an extra cell to the specific row.
        It populates the board with the positions of the cars.
        :return: A list of lists representing the board.
        """
        board = [['_' for _ in range(self.__size)] for _ in range(self.__size)]

        # Adds an extra cell to the third row to accommodate the target location
        if self.__size > 2:  # Ensures the board has at least 3 rows
            board[3].append('_')

        # Fills the board with car names based on their coordinates.
        for car in self.__cars.values():
            for row, col in car.car_coordinates():
                if 0 <= row < len(board) and 0 <= col < len(board[row]):
                    board[row][col] = car.get_name()

        return board

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string representing the board.
        """
        board = self.initialize_board()

        # Top border
        board_str = '*' * (self.__size * 2 + 2) + '\n'

        # Side borders
        for row in range(len(board)):
            board_str += '*' + ' '.join(board[row]) + ' *\n'

        # Bottom border
        board_str += '*' * (self.__size * 2 + 2) + '\n'

        return board_str

    def cell_list(self) -> List[Coordinates]:
        """
        This function returns the coordinates of cells in this board.
        :return: list of coordinates.
        """
        cells = [(row, col) for row in range(self.__size) for col in range(self.__size)]
        cells.append(self.__target)
        return cells

    def possible_moves(self) -> List[Tuple[str, str, str]]:
        """
        This function returns the legal moves of all cars in this board.
        :return: list of tuples of the form (name, move_key, description)
                 representing legal moves. The description should briefly
                 explain what is the movement represented by move_key.
        """
        moves = []
        for car in self.__cars.values():
            for move_key, description in car.possible_moves().items():
                # Validates that all required cells for the move are free and within board limits
                if all(self.is_within_bounds([req]) and not self.is_occupied(req) for req in
                       car.movement_requirements(move_key)):
                    moves.append((car.get_name(), move_key, description))
        return moves

    def cell_content(self, coordinates: Coordinates) -> Optional[str]:
        """
        Checks if the given coordinates are empty.
        :param coordinates: tuple of (row, col) of the coordinates to check.
        :return: The name of the car in "coordinates", None if it's empty.
        """
        for car in self.__cars.values():
            # Checks if any part of the car occupies the given coordinates
            if coordinates in car.car_coordinates():
                return car.get_name()
        return None

    def add_car(self, car: Car) -> bool:
        """
        Adds a car to the game.
        :param car: car object to add.
        :return: True upon success, False if failed.
        """
        # Checks if any part of the new car's position conflicts with existing cars
        if any(self.is_occupied(coord) for coord in car.car_coordinates()):
            print("Car position is already occupied.")
            return False
        # Ensures the entire car fits within the board boundaries
        if not self.is_within_bounds(car.car_coordinates()):
            print("Car position is out of bounds.")
            return False
        self.__cars[car.get_name()] = car
        return True

    def move_car(self, name: str, move_key: str) -> bool:
        """
        Moves car one step in a given direction.
        :param name: name of the car to move.
        :param move_key: the key of the required move.
        :return: True upon success, False otherwise.
        """
        # Checks if the car exists on the board
        if name not in self.__cars:
            return False
        car = self.__cars[name]
        # Validates move direction against car's orientation (horizontal/vertical)
        if (car.orientation == 0 and move_key in ['l', 'r']) or (car.orientation == 1 and move_key in ['u', 'd']):
            return False
        # Checks move feasibility (path clearance and within bounds)
        if all(self.is_within_bounds([req]) and not self.is_occupied(req) for req in
               car.movement_requirements(move_key)):
            car.move(move_key)
            return True
        return False

    def is_within_bounds(self, coords: List[Coordinates]) -> bool:
        """
        Checks if the given coordinates are within the bounds of the board or the target cell.
        :param coords: A list of tuples representing the coordinates to check.
        :return: True if all coordinates are within bounds, False otherwise.
        """
        # Checks each coordinate pair to see if it lies within the playable area or is the target cell
        return all((0 <= row < self.__size and 0 <= col < self.__size) or (row, col) == self.__target for row, col in coords)

    def is_occupied(self, coord: Coordinates) -> bool:
        """
        Checks if a coordinate is occupied by any car.
        :param coord: The coordinate to check.
        :return: True if the coordinate is occupied, False otherwise.
        """
        return self.cell_content(coord) is not None
