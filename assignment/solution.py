#!/usr/bin/env python3

import fileinput
import sys

(header, *lines) = fileinput.input()
lines = [l.strip() for l in lines]

_, _ = \
    [int(i) for i in header.strip().split(' ')]



# Output

