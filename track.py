#!/usr/bin/env python
import json

with open('tracking.output') as f:
    lines = f.readlines()

track = []
#  x y
for line in lines:
  pose = line.split()
  x = float(pose[0])
  y = float(pose[1])
  track.append([x,y])

with open('track.json', 'w') as f:
    json.dump(track, f)
