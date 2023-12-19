#!/usr/bin/python3

'''Define the class Square'''


class Square:
    '''Represent the square'''

    def __init__(self, size=0):

        ''' Initialise The square
        Args:
            size (int): The size of the new square.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
