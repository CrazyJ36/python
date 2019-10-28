#!/usr/bin/env python3
import urllib.request
import os
import re

user = str(os.getlogin())

if os.name == 'nt':
    # '\' works as formatter to extend to multiple lines.
    file_url = 'file:///C:/Users/' + user + \
        '/development/python/http_scrape_pretty_local_html/index.html'

elif os.name == 'posix':
    file_url = 'file:///home/' + user + \
        '/development/python/http_scrape_pretty_local_html/index.html'
else:
    print('unknown os, set os.name in script')
    exit()

with urllib.request.urlopen(file_url) as response:
    html = str(response.read())

    # format multiple lines for functions:
    #     function('data'
    #              ).fuction()
    html_body = str(re.search(

        '<p>(.*?)</p>',  # <p> (. - get any, * - 0 or of any , ? - 1 time) </p>

        html).group(1)  # areas o f matches?

    ).replace("\\xe2\\x80\\x99", "'")
    #  Above .replace works for the string statement before.
    # Replaced the 'apostraphe' escape code with the actual char.

    if os.name == 'nt':
        html_body_text = html_body.split('\\n' + '\\r')  # is list
    elif os.name == 'posix':
        html_body_text = html_body.split('\\n')  # doesn't work the same.

    # putting list items in string.
    string = ''
    for x in html_body_text:
        string += x

# lstrip() strips whitespace on the left (as opposed to rstring() - right)
# This will make the terminal print text pretty regardless
#  of where spaces are on new lines.
print(string.lstrip().rstrip())
exit(0)
