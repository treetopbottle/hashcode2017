#!/usr/bin/env python3

import fileinput
import sys

(header, *lines) = fileinput.input()
lines = [l.strip() for l in lines]

nr_videos, nr_endpoints, nr_request_descriptions, nr_cache_servers, capacity =\
    [int(i) for i in header.strip().split(' ')]

videos_mb = [int(i) for i in lines.pop(0).split(' ')]
print(videos_mb)

endpoints = []
for i in range(nr_endpoints):
    latency, nr_connected_cache_servers = [int(i) for i in lines.pop(0).split(' ')]
    connected_cache_servers = []
    for j in range(nr_connected_cache_servers):
        next_line = lines.pop(0)
        id_, latency = [int(i) for i in next_line.split(' ')]
        connected_cache_servers.append((id_, latency))
    endpoints.append((latency, connected_cache_servers))
print(endpoints[0])

for i in range(nr_request_descriptions):
    pass

# Output


print('---')

