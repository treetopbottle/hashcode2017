#!/usr/bin/env python3

import fileinput
import sys

(header, *lines) = fileinput.input()

rows, columns, min_ingredients, max_slices = \
    [int(i) for i in header.strip().split(' ')]

#print('{rows} x {columns} with [{min_ingredients}-{max_slices}]'.format(**locals()))

def valid_slice(slice_):
    mushrooms = 0
    tomatos = 0
    for ingredient in slice_:
        if ingredient == 'M':
            mushrooms += 1
        elif ingredient == 'T':
            tomatos += 1
    return mushrooms >= min_ingredients and tomatos >= min_ingredients

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
