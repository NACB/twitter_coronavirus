#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required = True)
parser.add_argument('--output_path', required = False)
args = parser.parse_args()

import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict

i = {hashtag: defaultdict(int) for hashtag in args.hashtags}
for files in os.listdir('outputs'):
    with open(os.path.join('outputs', files)) as f:
        x = json.load(f)
        date = files.split('.')[0]
        for hashtag in args.hashtags:
            if hashtag in x:
                total_count = sum(x[hashtag].values())
                i[hashtag][date] += total_count
            else:
                print("One or more missing")


#graphtime
plt.figure()
for hashtag, x in i.items():
    if x:
        dates, values = zip(*sorted(x.items()))
        plt.plot(dates, values, label=hashtag)
plt.legend()
plt.xlabel('Day')
plt.ylabel('Tweet Quantity')

plt.savefig('hashtag_use.png')
