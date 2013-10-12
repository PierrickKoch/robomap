#!/usr/bin/env python
from json import dumps
from lxml import etree
from time import sleep

result = {
    'easting': 0.0,
    'northing': 0.0,
}

def update(picoweb = "http://mana-superbase:8080", utmjson = "utm.json"):
    gps = etree.parse("%s/GPS?get=Infoutm"%picoweb)
    euler = gps.xpath("/GPS/Infoutm/data").pop()

    def getf(key):
        return float(euler.xpath(key).pop().text)

    previous = result.copy()
    for key in result.keys():
        result[key] = getf(key)

    if result == previous:
        return

    txt = dumps( result )
    with open(utmjson, 'w') as f:
        f.write( txt )

try:
    while 1:
        try:
            update()
            print(repr(result))
        except Exception as e:
            print("[error] %s"%str(e))
        sleep(.1)
except KeyboardInterrupt:
    print("[bye]")

'''
# test
from random import random
try:
    while 1:
        result['x'] += random()
        result['y'] += random()
        with open('pose.json', 'w') as f:
            f.write( dumps( result ) )
        sleep(.1)
except KeyboardInterrupt:
    print("[bye]")

    'roll':  0.0,
'''
