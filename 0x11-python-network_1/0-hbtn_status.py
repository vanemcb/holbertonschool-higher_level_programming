#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        utf8_content = r.headers['content-type']
        if 'utf-8' in utf8_content:
            utf8_content = 'OK'

    print(
        "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".
        format(type(html), html, utf8_content))
