#!/usr/bin/env python3
import urllib.request
import os

termux_url = 'file:///data/data/com.termux/files/home/development/python/http-local-html/index.html'
win_url = 'file:///C:/Users/CrazyJ36/development/python/http-local-html/index.html'


def get_data_termux():
    with urllib.request.urlopen(termux_url) as response:
        html = response.read()
        print(html)


def get_data_win():
    with urllib.request.urlopen(win_url) as response:
        html = response.read()
        print(html)


if os.environ.get("OS") == "Windows_NT":
    get_data_win()
else:
    # do elif  os.env... returns re.match("termu"...
    get_data_termux()

exit(0)
