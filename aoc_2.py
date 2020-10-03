'''
input: 1,9,10,3,2,3,11,0,99,30,40,50

output:
3500,9,10,70,
2,3,11,0,
99,
30,40,50
'''
from typing import Optional, List, Tuple

# n = 4
#
# with open('aoc2.txt', 'r') as f:
#     raw_data = [item for item in f.readlines()]
#
# raw_data = raw_data[0].split(',')
# raw_data = [int(item) for item in raw_data]
#
#
# # start with the example
# raw_data = ['1,9,10,3,2,3,11,0,99,30,40,50']
# raw_data = raw_data[0].split(',')
# raw_data = [int(item) for item in raw_data]
# #data = [raw_data[i:i+n] for i in range(0, len(raw_data), n)]
#
# def apply_opcode(code: int, num1: int, num2: int) -> Optional[int]:
#     if code == 99:
#         return None
#     elif code == 1:
#         return num1 + num2
#     elif code == 2:
#         return num1 * num2
#     else:
#         print('Something went wrong, invalid opcode')
#         return None
#
# def get_blocks(input: List[int], n: int) -> List[List[int]]:
#     '''
#     n = number of elements in block
#     Returns list of lists with [opcode, num1_index, num2_index, output_index]
#     '''
#     return [input[i:i+n] for i in range(0, len(input), n)]
#
# get_blocks(raw_data, 4)
# # TODO: make it a class
# def process_data(input_data: List[int], n: int) -> Optional[List[int]]:
#     input = input_data.copy()
#     blocks = get_blocks(input, n)
#     for sub_list in blocks:
#         if sub_list[0] == 99:
#             print('99 opcode detected!')
#             return input
#         else:
#             input[sub_list[-1]] = apply_opcode(sub_list[0], input[sub_list[1]],
#                                                input[sub_list[2]])
#     return input
#
# assert process_data(raw_data, 4) == [3500,9,10,70,2,3,11,0,99,30,40,50]
#
#
# # our case
# with open('aoc2.txt', 'r') as f:
#     raw_data = [item for item in f.readlines()]
#
# raw_data = raw_data[0].split(',')
# raw_data = [int(item) for item in raw_data]
# raw_data[1] = 12
# raw_data[2] = 2
#
# ans = process_data(raw_data, 4)
# ans[0]

'''
Part 2
'''
class IntCode:
    def __init__(self, raw_data: str, elements_per_block: int = 4) -> None:
        self._raw_data = raw_data
        self._data: List[int] = []
        self.prep_data: List[int] = []
        self._n = elements_per_block    # number of elements in one block

    def preprocess(self) -> None:
        self.prep_data = self._raw_data[0].split(',')
        self.prep_data = [int(item) for item in self.prep_data]
        self._data = self.prep_data.copy()     # potential bottleneck

    @staticmethod
    def _apply_opcode(code: int, num1: int, num2: int) -> Optional[int]:
        if code == 99:
            return None
        elif code == 1:
            return num1 + num2
        elif code == 2:
            return num1 * num2
        else:
            print('Something went wrong, invalid opcode')
            return None

    @staticmethod
    def _get_blocks(input: List[int], n: int) -> List[List[int]]:
        '''
        n = number of elements in block
        Returns list of lists with [opcode, num1_index, num2_index, output_index]
        '''
        return [input[i:i + n] for i in range(0, len(input), n)]

    def get_output(self, noun: Optional[int] = None, verb: Optional[int] = None)\
            -> Optional[Tuple[int, int, int]]:
        '''
        Returns tuple(noun, verb, output).
        reset = True resets _data to prep_data
        '''
        self._data = self.prep_data.copy()
        if noun and verb:
            self._data[1] = noun
            self._data[2] = verb
        blocks = self._get_blocks(self._data, self._n)
        for sub_list in blocks:
            if sub_list[0] == 99:
                return self._data[1], self._data[2], self._data[0]
            else:
                self._data[sub_list[-1]] = self._apply_opcode(sub_list[0], self._data[sub_list[1]],
                                                   self._data[sub_list[2]])
        return self._data[1], self._data[2], self._data[0]



# testing
ic = IntCode(['1,9,10,3,2,3,11,0,99,30,40,50'])
assert ic.get_output() == (9, 10, 3500)

# test for reset
ic = IntCode(['1,9,10,3,2,3,11,0,99,30,40,50'])
ic.preprocess()
ic.get_output(3, 4)
assert ic._data == [1, 3, 4, 3, 2, 3, 11, 0, 99, 30, 40, 50]
ic.get_output()
assert ic._data == [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

# our case
with open('aoc2.txt', 'r') as f:
    input_data = [item for item in f.readlines()]

ic = IntCode(input_data)
ic.preprocess()
for noun in range(100):
    for verb in range(100):
        ans = ic.get_output(noun, verb)[2]
        if ans == 19690720:
            print(f'noun={noun}, verb={verb}')
            ans_noun = noun
            ans_verb = verb

final_answer = 100 * ans_noun + ans_verb
print(final_answer)