#!/usr/bin/env python3

import fileinput
import sys

lines = fileinput.input()

rows, columns, min_ingredients, max_slices = \
    [int(i) for i in next(lines).strip().split(' ')]

#print('{rows} x {columns} with [{min_ingredients}-{max_slices}]'.format(**locals()))

def valid_slice(slice_):
    return True

def get_slices():
    slices = []
    for r,line in enumerate(lines):
        for c,_ in enumerate(line):
            slice_ = line[c:max_slices]
            if valid_slice(slice_):
                slices.append([
                    r,
                    c,
                    r,
                    c+len(slice_),
                ])
                return slices
    return slices

slices = get_slices()


# Output

# The total number of slices to be cut
print(len(slices))

# The slices
string_slices = []
for slice_ in slices:
    string_slice = ' '.join([str(s) for s in slice_])
    string_slices.append(string_slice)
print('\n'.join(string_slices))
