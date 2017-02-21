#!/usr/bin/env python3

import fileinput
import sys

(header, *lines) = fileinput.input()
lines = [l.strip() for l in lines]

rows, columns, min_ingredients, max_cells = \
    [int(i) for i in header.strip().split(' ')]

#print('{rows} x {columns} with [{min_ingredients}-{max_cells}]'.format(**locals()))

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
        enum_line = enumerate(line)
        next_line = False
        for c,_ in enum_line:
            if next_line:
                break
            break_slice_size = False
            for slice_size in range(max_cells):
                if break_slice_size:
                    break
                slice_ = line[c:c+slice_size]
                if valid_slice(slice_):
                    slices.append([
                        r,
                        c,
                        r,
                        c+len(slice_)-1,
                    ])
                    if c+len(slice_) >= columns:
                        next_line = True
                        break
                    for _ in range(len(slice_)):
                        try:
                            next(enum_line)
                        except:
                            break_slice_size = True
                            break
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
