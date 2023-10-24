#!/usr/bin/python3
"""Square class"""


class Square:
    """Define a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor .
        Args:
            size: size of the square.
            position (int, int): Tupple.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """property of a  square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property for position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of square."""
        return self.__size ** 2

    def my_print(self):
        """Print in stdout the square."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
