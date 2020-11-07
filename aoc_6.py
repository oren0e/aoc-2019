from typing import List, Set, Dict, Optional, Union

from collections import defaultdict, OrderedDict

all_objects: Set[str] = set()

file = 'day6_input'

# identify all unique objects
with open(file, 'r') as f:
    raw_data = f.readlines()
    for line in raw_data:
        for obj in line.strip().split(')'):
            if obj not in all_objects:
                all_objects.add(obj)

# Map objects to numbers
mapping_dict: Dict[str, int] = {}
for i, obj in enumerate(all_objects):
    mapping_dict[obj] = i

data: List[List[int]] = [[] for _ in range(len(all_objects))]
with open(file, 'r') as f:
    raw_data = f.readlines()
    for line in raw_data:
        row = line.strip().split(')')   # row[1] orbits row[0]
        data[mapping_dict[row[1]]].append(mapping_dict[row[0]])

# count number of orbits
orbits: Dict[int, List[int]] = defaultdict(list)

def count_orbits(data: List[List[int]], pos: int = 0) -> int:
    if not data[pos]:
        return 1
    orbits[data[pos][0]].append(count_orbits(data, pos=data[pos][0]))

for i, _ in enumerate(data):
    count_orbits(data, pos=i)

total = 0
for lst in orbits.values():
    total += len(lst)

# test case 0
# assert total == 42

print(total)

'''
Part 2
'''
class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.seen: bool = False

    def __repr__(self) -> str:
        return repr(self.value)


data_undirected: List[List[Node]] = [[] for _ in range(len(all_objects))]

with open(file, 'r') as f:
    raw_data = f.readlines()
    for line in raw_data:
        row = line.strip().split(')')
        node0 = Node(mapping_dict[row[0]])
        node1 = Node(mapping_dict[row[1]])
        data_undirected[mapping_dict[row[1]]].append(node0) # row[1] to row[0]
        data_undirected[mapping_dict[row[0]]].append(node1)  # row[0] to row[1]

my_pos = data[[value for key, value in mapping_dict.items() if key == 'YOU'][0]][0]
san_pos = data[[value for key, value in mapping_dict.items() if key == 'SAN'][0]][0]

orbits_to_san: Dict[int, List[int]] = defaultdict(list)
nodes: List[Union[int, str]] = []

def count_orbits_to_san(data: List[List[Node]], pos: int = my_pos) -> Optional[str]:
    current_node_value = pos
    for lst in data:
        for item in lst:
            if item.value == current_node_value:
                item.seen = True

    for node in data[pos]:
        if node.value == san_pos:
            nodes.append('found')
            return 'found santa'
        if not node.seen:
            nodes.append(node.value)
            orbits_to_san[node.value].append(count_orbits_to_san(data, pos=node.value))
            #orbits_to_santa.append(1)
            #count_orbits_to_san(data, pos=node.value)

count_orbits_to_san(data_undirected)
#nodes
#orbits_to_san

orbits_to_santa = 0
for k, v in orbits_to_san.items():
    if v[0] == 'found santa':
        break
    else:
        orbits_to_santa += 1

print(orbits_to_santa + 2)