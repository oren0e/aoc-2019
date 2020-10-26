from typing import Dict

raw_input: str = '235741-706948'
start: int = int(raw_input.split('-')[0])
end: int = int(raw_input.split('-')[1])

criteria = range(start, end + 1)

num_positives: int = 0


def is_six_digits(num: int) -> bool:
    if num % 1000000 == num:
        return True
    else:
        return False


def is_two_digits_same(num: int) -> bool:
    d: Dict[str, int] = {}
    counter = 0
    str_num = str(num)
    for num1, num2 in zip(str_num, str_num[1:]):
        if num1 == num2:
            counter += 1
            if num1 not in d:
                d[num1] = 2
            else:
                d[num1] += 1
    return any([True for v in d.values() if v == 2])
    # if counter >= 1:
    #     return True
    # else:
    #     return False


def is_non_decreasing(num: int) -> bool:
    res = [int(digit) for digit in str(num)]
    return res == sorted(res)


for num in criteria:
    if is_six_digits(num) and is_two_digits_same(num) and is_non_decreasing(num):
        num_positives += 1

print(num_positives)
