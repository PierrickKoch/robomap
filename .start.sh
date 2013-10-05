#!/bin/sh

test -d js || (
    mkdir js; cd js
    wget -q http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.6.4/leaflet.min.css \
            http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.6.4/leaflet.js \
            https://raw.github.com/proj4js/proj4js/1.4.1/dist/proj4.js
    mkdir images; cd images
    wget -q http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.6.4/images/marker-shadow.png \
            http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.6.4/images/marker-icon.png \
            http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.6.4/images/marker-icon-2x.png
)
python -m SimpleHTTPServer 8000 & webpid=$!
which xdg-open && xdg-open http://localhost:8000
python pose.py
# kill $webpid
