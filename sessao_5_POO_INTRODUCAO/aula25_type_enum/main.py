# Exemplos de Enum, coisas para serem escolhidas.

from enum import Enum, auto

class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'


if __name__ == '__main__':
    # print(move('right'))
    # print(move('left'))
    # print(move('up'))
    # print(move('down'))

    print(move(Directions.right))
    print(move(Directions.left))

    print()

    for direction in Directions:
        print(direction, direction.name, direction.value)