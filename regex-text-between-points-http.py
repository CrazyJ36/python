#!/usr/bin/env python3
import urllib.request, re

url = urllib.request.urlopen('https://hnrss.org/newest')


for line in url:
    if re.search('<title>(.*?)</title>', line.decode().strip(), re.I + re.S + re.M):
        print(line)
