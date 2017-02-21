#!/usr/bin/env python3

import fileinput

lines = fileinput.input()

rows, columns, min_ingredients, max_slices = next(lines).split(' ')

for line in lines:
    pass

slices = []

print(len(slices))
print('\n'.join(slices))
