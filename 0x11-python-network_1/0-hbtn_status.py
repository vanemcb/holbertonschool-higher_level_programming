#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status """

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()

print(
    "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: OK".
    format(type(html), html))
