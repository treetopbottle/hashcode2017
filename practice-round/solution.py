#!/usr/bin/env python3

import fileinput

lines = fileinput.input()

rows, columns, min_ingredients, max_slices = next(lines).split(' ')

for line in lines:
    pass

slices = [[0,0,1,1]]


# Output

# The total number of slices to be cut
print(len(slices))

# The slices
string_slices = []
for slice_ in slices:
    string_slice = ' '.join([str(s) for s in slice_])
    string_slices.append(string_slice)
print('\n'.join(string_slices))
