#!/usr/bin/env bash
date
echo "me_at_the_zoo"
./solution.py input-sets/me_at_the_zoo.in > output/me_at_the_zoo.out
echo "done"
echo

date
echo "videos_worth_spreading"
./solution.py input-sets/videos_worth_spreading.in > output/videos_worth_spreading.out
echo "done"
echo

date
echo "trending_today"
./solution.py input-sets/trending_today.in > output/trending_today.out
echo "done"
echo

date
echo "kittens.in"
./solution.py input-sets/kittens.in > output/kittens.out
echo "done"

echo "all done"
date
