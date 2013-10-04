from json import dumps
from lxml import etree
from time import sleep

result = {
    'x': 0.0,
    'y': 0.0,
    'z': 0.0,
    'yaw':   0.0,
    'pitch': 0.0,
    'roll':  0.0,
}

def update(picoweb = "http://localhost:8080", posejson = "pose.json"):
    pom = etree.parse("%s/pom?get=Pos"%picoweb)
    euler = pom.xpath("/pom/Pos/data/pomPos/mainToOrigin/euler").pop()

    def getf(key):
        return float(euler.xpath(key).pop().text)

    for key in result.keys():
        result[key] = getf(key)

    with open(posejson, 'w') as f:
        f.write( dumps( result ) )

try:
    update()
except Exception as e:
    print("[error] %s"%str(e))

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
