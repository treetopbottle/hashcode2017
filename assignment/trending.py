#!/usr/bin/env python3

import fileinput
import sys
import collections

(header, *lines) = fileinput.input()
lines = [l.strip() for l in lines]

nr_videos, nr_endpoints, nr_request_descriptions, nr_cache_servers, capacity =\
    [int(i) for i in header.strip().split(' ')]

videos_mb = [int(i) for i in lines.pop(0).split(' ')]

endpoints = []
for i in range(nr_endpoints):
    latency, nr_connected_cache_servers = [int(i) for i in lines.pop(0).split(' ')]
    connected_cache_servers = []
    for j in range(nr_connected_cache_servers):
        id_, latency = [int(i) for i in lines.pop(0).split(' ')]
        connected_cache_servers.append((id_, latency))
    endpoints.append((latency, connected_cache_servers))

endpoint_to_request_description = collections.defaultdict(list)
request_descriptions = []
for i in range(nr_request_descriptions):
    video_id, endpoint_id, nr_requests = [int(i) for i in lines.pop(0).split(' ')]
    request_descriptions.append((video_id, endpoint_id, nr_requests))
    endpoint_to_request_description[endpoint_id].append((video_id, nr_requests))

# Transformation
cache_to_endpoint = collections.defaultdict(list)
for endpoint_nr, endpoint in enumerate(endpoints):
    (latency, connections) = endpoint
    for connection in connections:
        (cache_nr, latency_endpoint_to_cache) = connection
        cache_to_endpoint[cache_nr].append((endpoint_nr,
                                            latency - latency_endpoint_to_cache))

# Generate Solution
def score(cache):
    video_to_score = collections.defaultdict(int)
    for endpoint_nr, latency_improvements in cache_to_endpoint[cache]:
        for video_id, nr_requests in endpoint_to_request_description[endpoint_nr]:
            video_to_score[video_id] += nr_requests * latency_improvements
    return video_to_score

def cache_to_candidates(cache_id):
    cache0 = score(cache_id)
    top_videos = sorted(cache0.keys(), key=lambda v: -cache0[v] / videos_mb[v])
    return top_videos

def videos_for_cache(cache_id):
    candidates = cache_to_candidates(cache_id)
    remaining_size = capacity
    for candidate in candidates:
        if videos_mb[candidate] <= remaining_size:
            remaining_size -= videos_mb[candidate]
            yield candidate

s = sorted((v, i) for i,v in enumerate(videos_mb))
cache_size_remaining = [capacity for i in range(nr_cache_servers)]

cache_server_descriptions = collections.defaultdict(list)
while len(s):
    placed_video = False
    for cache_id in range(nr_cache_servers):
        if (len(s) == 0):
            break
        if (s[-1][0] <= cache_size_remaining[cache_id]):
            (size, video_id) = s.pop()
            cache_size_remaining[cache_id] -= size
            cache_server_descriptions[cache_id].append(video_id)
            placed_video = True
    if not placed_video:
        s.pop()

print(len(cache_server_descriptions))
for i in cache_server_descriptions:
    output = [i] + cache_server_descriptions[i]
    print(' '.join([str(o) for o in output]))
