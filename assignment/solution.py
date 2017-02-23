#!/usr/bin/env python3

import fileinput
import sys
import collections

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
        id_, latency = [int(i) for i in lines.pop(0).split(' ')]
        connected_cache_servers.append((id_, latency))
    endpoints.append((latency, connected_cache_servers))
print(endpoints[0])

request_descriptions = []
for i in range(nr_request_descriptions):
    video_id, endpoint_id, nr_requests = [int(i) for i in lines.pop(0).split(' ')]
    request_descriptions.append((video_id, endpoint_id, nr_requests))
print(request_descriptions)

# Transformation
cache_to_endpoint = collections.defaultdict(list)
for endpoint_nr, endpoint in enumerate(endpoints):
    (latency, connections) = endpoint
    for connection in connections:
        (cache_nr, latency_endpoint_to_cache) = connection
        cache_to_endpoint[cache_nr].append((endpoint_nr,
                                            latency - latency_endpoint_to_cache))

print(cache_to_endpoint)
# Output
def score(video, cache):
    pass

print('---')

