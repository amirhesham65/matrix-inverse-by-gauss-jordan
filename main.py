# An implementation for the gauss-jordan elimination algorithm in Python
# Author: Amir Hesham K.
from matrix import Matrix

if __name__ == '__main__':
    example = [
        [2, 4],
        [-4, 10]
    ]

    matrix = Matrix(example)
    matrix.inverse()
    matrix.print()
