'''
1. Write a Manhatan distance function
2. Represent the wire with all its operations
3. Parse input
'''

from typing import NamedTuple, List, Tuple

# read input
def get_wire_plans(file: str) -> Tuple[List[str], List[str]]:
    raw_data: List[str] = []
    with open(file, 'r') as f:
        raw_data = f.readlines()

    wire1 = raw_data[0].strip()
    wire2 = raw_data[1].strip()

    wire1 = [item for item in wire1.split(',')]
    wire2 = [item for item in wire2.split(',')]

    return wire1, wire2

plan1, plan2 = get_wire_plans('test0')


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return repr(f'({self.x},{self.y})')

    def __str__(self) -> str:
        return repr(f'({self.x},{self.y})')

Plan = List[str]


class Path:
    def __init__(self, start: Point) -> None:
        self.origin = start
        self.data: List[Point] = []

    def add(self, new_point: Point) -> None:
        self.data.append(new_point)

    def __repr__(self) -> str:
        str_path = str(self.data[0])
        for item in self.data[1:]:
            str_path += f'-> {item} '
        return str_path

def get_current_position(start_point: Point, plan: Plan) -> Tuple[Point, Path]:
    path = Path(start_point)

    for instruction in plan:
        direction: str = instruction[0]
        steps: int = int(instruction[1:])

        if direction == 'L':
            start_point.x -= steps
            path.add(Point(start_point.x, start_point.y))
        elif direction == 'R':
            start_point.x += steps
            path.add(Point(start_point.x, start_point.y))
        elif direction == 'U':
            start_point.y += steps
            path.add(Point(start_point.x, start_point.y))
        elif direction == 'D':
            start_point.y -= steps
            path.add(Point(start_point.x, start_point.y))
        else:
            raise ValueError('Invalid direction')
    return start_point, path

position1, path1 = get_current_position(Point(0,0), plan1)     # plan1 = 'R8,U5,L5,D3'
position2, path2 = get_current_position(Point(0,0), plan2)     # plan1 = 'R8,U5,L5,D3'


# TODO:
#   1. take both plans, increment both wire positions by 1 always checking
#   if they are equal, if they are, append to list of equal positions

