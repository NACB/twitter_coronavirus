#!/bin/sh

for f in /data/Twitter\ dataset/geoTwitter20*.zip; do
    nohup ./src/map.py "--input_path=$f" &
done
