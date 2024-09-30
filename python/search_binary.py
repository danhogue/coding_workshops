from typing import TypeVar, List, Callable
from math import floor

T = TypeVar('T')

def _comp(a: T, b: T):
    if a < b:
        return 'lt'
    elif a > b:
        return 'gt'
    else:
        'eq'

def _binary_search(haystack: List[T], needle: T, comp: Callable[[T, T], str], start_range: int, end_range: int) -> int:
    if start_range > end_range:
        return -1

    middle_index = floor((start_range + end_range) / 2)
    middle_value = haystack[middle_index]
    comp_value = comp(needle, middle_value)
    if comp_value == 'lt':
        return _binary_search(haystack, needle, comp, start_range, middle_index - 1)
    elif comp_value == 'gt':
        return _binary_search(haystack, needle, comp, middle_index + 1, end_range)
    else:
        return middle_index


def binary_search(haystack: List[T], needle: T, comp: Callable[[T, T], str] = _comp) -> int:
    return _binary_search(haystack, needle, comp, 0, len(haystack) - 1)


if __name__ == '__main__':
    haystack = ['a','b','c', 'd']
    def comp(a, b):
        if a < b:
            return 'lt'
        elif a > b:
            return 'gt'
        else:
            'eq'
    print(binary_search(haystack, 'z', comp))
