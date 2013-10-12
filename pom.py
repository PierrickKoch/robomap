#!/usr/bin/env python
import json

with open('pom.log') as f:
    lines = f.readlines()

path = []
lines.pop(0) # remove header
lines.pop(-1) # remove header
# date yaw pitch roll x y z
for line in lines:
  ll = line.split()
  x = float(ll[4])
  y = float(ll[5])
  path.append([x,y])

with open('pom.json', 'w') as f:
    json.dump(path, f)
