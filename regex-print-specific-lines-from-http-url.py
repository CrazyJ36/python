#!/usr/bin/env python3
import urllib.request
import re

handler = urllib.request.urlopen(
    'https://www.google.com/robots.txt')

for line in handler:
    if re.search( 'Allow', line.decode().strip() ):
        print(line)




