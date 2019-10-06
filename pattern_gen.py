"""
Mobile Lock Pattern each of the dots are represented by a number

    (1)   (2)   (3)

    (4)   (5)   (6)

    (7)   (8)   (9)

Patterns are a sequence of numbers. However have constraints.
Example, from 1 to go to 9 is not possible without 5 being in the pattern, that is,
if in a sequence 9 comes after 1, then 5 must occur before 9.
"""

"""
    Following defines the requirements.
    Example: from 1 to go to 3, 2 must already be visited. 
"""
pattern_requirements = {
    1: {3: 2, 7: 4, 9: 5},
    2: {8: 5},
    3: {1: 2, 7: 5, 9: 6},
    4: {6: 5},
    5: {},
    6: {4: 5},
    7: {1: 4, 3: 5, 9: 8},
    8: {2: 5},
    9: {1: 5, 3: 6, 7: 8},
}

from collections import Counter

""" Counts the possible patterns """
def count_patterns(counter=None, visited=None):
    if counter is None:
        counter = Counter()
    if visited is None:
        visited = []
        neighbours = list(range(1, 10))
    else:
        last = visited[-1]
        """ neighbours are all those nodes that satisfy the requirements and are not already visited. """
        neighbours = [
            dot for dot in range(1, 10)
            if not (
                dot in visited or
                (dot in pattern_requirements[last] and pattern_requirements[last][dot] not in visited)
            )
        ]
    counter[len(visited)] += 1
    for new in neighbours:
        count_patterns(counter, visited + [new])
    return counter

""" Get a specific pattern (ordering is definite) """
def get_pattern(pattern_size, pattern_index, counter=None, visited=None):
    """ pattern_size is the size of pattern [1, 9], pattern_index is the index of the pattern (> 1) """
    if counter is None:
        counter = Counter()
    if visited is None:
        visited = []
        neighbours = list(range(1, 10))
    else:
        last = visited[-1]
        """ neighbours are all those nodes that satisfy the requirements and are not already visited. """
        neighbours = [
            dot for dot in range(1, 10)
            if not (
                    dot in visited or
                    (dot in pattern_requirements[last] and pattern_requirements[last][dot] not in visited)
            )
        ]
    counter[len(visited)] += 1
    if  len(visited) == pattern_size and counter[len(visited)] == pattern_index:
        return visited

    for new in neighbours:
        pattern = get_pattern(pattern_size, pattern_index, counter, visited + [new])
        if pattern is not None:
            return pattern

if __name__ == "__main__":
    counted = count_patterns()
    print(counted)
    print(get_pattern(9, 10000))
