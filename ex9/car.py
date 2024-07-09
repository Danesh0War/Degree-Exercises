from typing import Tuple, List, Dict

Coordinates = Tuple[int, int]


class Car:
    """
    Represents a car in the Rush Hour game, maintaining attributes such as name, length, and orientation.
    Encapsulates car properties, enforcing valid configurations through property validations.
    Supports movement operations, checking legality based on orientation and predefined rules.
    """
    # Class constants
    __VALID_NAMES = {'Y', 'B', 'O', 'W', 'G', 'R'}
    __MAX_LENGTH = 4
    __MIN_LENGTH = 2
    __VERTICAL = 0
    __HORIZONTAL = 1

    def __init__(self, name: str, length: int, location: Coordinates,
                 orientation: int) -> None:
        """
        A constructor for a Car object.
        :param name: A string representing the car's name.
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head location (row,col).
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL).
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value not in self.__VALID_NAMES:
            raise ValueError(f"Invalid car name: {value}. Valid names are: {self.__VALID_NAMES}")
        self.__name = value

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, value: int) -> None:
        if not (self.__MIN_LENGTH <= value <= self.__MAX_LENGTH):
            raise ValueError(
                f"Invalid car length: {value}. Valid lengths are between {self.__MIN_LENGTH} and {self.__MAX_LENGTH}")
        self.__length = value

    @property
    def location(self) -> Coordinates:
        return self.__location

    @location.setter
    def location(self, value: Coordinates) -> None:
        if not (isinstance(value, tuple) and len(value) == 2 and all(isinstance(coord, int) for coord in value)):
            raise ValueError(f"Invalid location: {value}. Location must be a tuple of two integers.")
        self.__location = value

    @property
    def orientation(self) -> int:
        return self.__orientation

    @orientation.setter
    def orientation(self, value: int) -> None:
        if value not in (self.__VERTICAL, self.__HORIZONTAL):
            raise ValueError(
                f"Invalid orientation: {value}. Valid orientations are {self.__VERTICAL} for vertical and {self.__HORIZONTAL} for horizontal.")
        self.__orientation = value

    def car_coordinates(self) -> List[Coordinates]:
        """
        :return: A list of coordinates the car is in.
        """
        coordinates = []
        for i in range(self.__length):
            if self.__orientation == self.__VERTICAL:
                coordinates.append((self.__location[0] + i, self.__location[1]))
            else:
                coordinates.append((self.__location[0], self.__location[1] + i))
        return coordinates

    def possible_moves(self) -> Dict[str, str]:
        """
        :return: A dictionary of strings describing possible movements 
                 permitted by this car.
        """
        if self.__orientation == self.__VERTICAL:
            return {
                'u': "Move up",
                'd': "Move down"
            }
        else:
            return {
                'l': "Move left",
                'r': 'Move right'
            }

    def movement_requirements(self, move_key: str) -> List[Coordinates]:
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for 
                 this move to be legal.
        """
        if move_key == 'u':
            # The cell above the car's current head must be empty
            return [(self.__location[0] - 1, self.__location[1])]
        elif move_key == 'd':
            # The cell below the car's current tail must be empty
            return [(self.__location[0] + self.__length, self.__location[1])]
        elif move_key == 'l':
            # The cell to the left of the car's current head must be empty
            return [(self.__location[0], self.__location[1] - 1)]
        elif move_key == 'r':
            return [(self.__location[0], self.__location[1] + self.__length)]
        else:
            return []

    def move(self, move_key: str) -> bool:
        """ 
        This function moves the car.
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if move_key not in self.possible_moves():
            return False
        if move_key == 'u':
            self.__location = (self.__location[0] - 1, self.__location[1])
        elif move_key == 'd':
            self.__location = (self.__location[0] + 1, self.__location[1])
        elif move_key == 'l':
            self.__location = (self.__location[0], self.__location[1] - 1)
        elif move_key == 'r':
            self.__location = (self.__location[0], self.__location[1] + 1)

        return True

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.__name


