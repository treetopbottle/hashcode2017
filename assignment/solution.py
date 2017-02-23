#!/usr/bin/env python3

import fileinput
import sys
import collections
import random
# random.seed(0)
from bisect import bisect_left

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


endpoint_request_cutoff = [0]

endpoint_to_request_description = collections.defaultdict(list)
request_descriptions = []
for i in range(nr_request_descriptions):
    video_id, endpoint_id, nr_requests = [int(i) for i in lines.pop(0).split(' ')]
    request_descriptions.append((video_id, endpoint_id, nr_requests))
    endpoint_request_cutoff.append (endpoint_request_cutoff [-1] + nr_requests)
    latency = endpoints[endpoint_id][0]
    endpoint_to_request_description[endpoint_id].append((video_id, nr_requests, latency))



cache_server_descriptions = collections.defaultdict (list)
cache_server_used = collections.defaultdict (int)
    
def update_cache_for_video (cache_id, video):
    if video in cache_server_descriptions [cache_id]:
        cache_server_descriptions[cache_id].remove (video)
        cache_server_descriptions[cache_id] = [video] + cache_server_descriptions [cache_id]
    else:
        cache_server_descriptions[cache_id] = [video] + cache_server_descriptions [cache_id]
        cache_server_used [cache_id] += videos_mb [video]
        while (cache_server_used [cache_id] > capacity):
            old_video = cache_server_descriptions [cache_id].pop ()
            cache_server_used [cache_id] -= videos_mb [old_video]
           
                                  
def best_cache_for (endpoint_id):
    random.shuffle (endpoints [endpoint_id][1])
    if (len (endpoints [endpoint_id][1]) == 0):
        return -1
    else:
        return min (endpoints [endpoint_id][1], key = lambda v: v[1]) [0]
    
def simulate (request):
    cache_id = best_cache_for (request [1])
    if (cache_id >= 0):
        update_cache_for_video (cache_id, request [0])


for i in range (500000):
    random_req = random.random () * (endpoint_request_cutoff [-1])
    random_index = bisect_left (endpoint_request_cutoff, random_req)
    simulate (request_descriptions [random_index - 1])

    

print(len(cache_server_descriptions))
for i in cache_server_descriptions:
    output = [i] + cache_server_descriptions[i]
    print(' '.join([str(o) for o in output]))
