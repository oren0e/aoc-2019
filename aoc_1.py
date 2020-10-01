from math import floor

from typing import Optional

'''
Part 1
'''
def calc_fuel(module: int) -> int:
    return floor(module / 3) - 2

assert calc_fuel(12) == 2
assert calc_fuel(14) == 2
assert calc_fuel(1969) == 654
assert calc_fuel(100756) == 33583

with open('aoc1.txt', 'r') as f:
    lines = f.readlines()
lines = [int(line.strip('\n')) for line in lines]
assert all(isinstance(item, int) for item in lines)

print(sum(calc_fuel(m) for m in lines))

'''
Part 2
'''
def calc_fuel2(module: int) -> Optional[int]:
    # base case
    fuel = floor(module / 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel2(fuel)

assert calc_fuel2(14) == 2
assert calc_fuel2(1969) == 966
assert calc_fuel2(100756) == 50346

print(sum(calc_fuel2(m) for m in lines))