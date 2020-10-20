'''
1. Write a Manhatan distance function
2. Represent the wire with all its operations
3. Parse input
'''

from typing import List, Tuple, Dict, Set, NamedTuple

from itertools import zip_longest

# read input
def get_wire_plans(file: str) -> Tuple[List[str], List[str]]:
    with open(file, 'r') as f:
        raw_data = f.readlines()

    wire1 = raw_data[0].strip()
    wire2 = raw_data[1].strip()

    wire1 = [item for item in wire1.split(',')]
    wire2 = [item for item in wire2.split(',')]

    return wire1, wire2




# class Point:
#     def __init__(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other) -> bool:
#         return (self.x == other.x) and (self.y == other.y)
#
#     def __repr__(self) -> str:
#         return repr(f'({self.x},{self.y})')
#
#     def __str__(self) -> str:
#         return f'({self.x},{self.y})'

class Point(NamedTuple):
    x: int
    y: int


Plan = List[str]


def manhattan_distance(point1: Point, point2: Point) -> float:
    xdist = abs(point2.x - point1.x)
    ydist = abs(point2.y - point1.y)
    return xdist + ydist


def get_positions(start_point: Point,
                         plan: Plan) -> Set[Tuple[int, int]]:

    x = start_point.x
    y = start_point.y
    set_of_points: Set[Tuple[int, int]] = set()

    for instruction in plan:
        direction: str = instruction[0]
        steps: int = int(instruction[1:])
        while steps > 0:
            if direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            else:
                raise ValueError(f'Wrong direction {direction}')

            set_of_points.add(Point(x, y))
            steps -= 1
    return set_of_points

plan1, plan2 = get_wire_plans('aoc3')
start_position = Point(0, 0)
points1 = get_positions(start_position, plan1)
points2 = get_positions(start_position, plan2)
crossings = points1.intersection(points2)


min(manhattan_distance(start_position, p) for p in crossings)