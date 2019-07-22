#!/usr/bin/env python3
import urllib.request

# open local file with urllib
with urllib.request.urlopen('file:///data/data/com.termux/files/home/development/python/http-local-html/index.html') as response:
    # gets requested html file
    html = response.read()

# prints the html file
print(html)
