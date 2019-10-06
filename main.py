from pattern_draw import draw_pattern
from pattern_gen import count_patterns, get_pattern
from math import ceil
from random import random

counter = count_patterns()
print(counter)
print('Generate Random Mobile Patterns')

pattern_size = int(input('Enter a pattern size:'))
pattern_index = ceil(random() * counter[pattern_size])
pattern = get_pattern(pattern_size, pattern_index)

draw_pattern(pattern)