from typing import List
from math import floor

def _sort(input: List[int], start_range: int, end_range: int) -> List[int]:
    if len(input) < 2:
        return input

    print(input[start_range:end_range+1])

    if start_range >= end_range:
        return

    middle_index = floor((end_range + start_range) / 2)
    middle_value = input[middle_index]
    i = start_range
    j = end_range
    done = False
    while not done:
        while input[i] < middle_value and i < middle_index:
            i += 1
        while input[j] >= middle_value and j > middle_index:
            j -= 1
        if i > j:
            done = True
        

    _sort(input, start_range, middle_index - 1)
    _sort(input, middle_index + 1, end_range)

    return input


def sort(input: List[int]) -> List[int]:
    _sort(input, 0, len(input) - 1)
    return input


if __name__ == '__main__':
    print(sort([4,8,6,2,3,9]))

# [4,8,6,2,3,9]
# [4,8, 6 ,2,3,9]
# [4,3, 6 ,2,8,9]
# [4,3, 2 ,6,8,9]