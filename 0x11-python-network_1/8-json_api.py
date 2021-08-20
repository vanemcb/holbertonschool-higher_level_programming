#!/usr/bin/python3
""" Script that takes in a letter and sends a POST request to
http: // 0.0.0.0: 5000/search_user with the letter as a parameter. """

import requests
from sys import argv

if __name__ == "__main__":

    url = 'http://bcd8ad1df972.c3bcb5f8.hbtn-cod.io:5000/search_user'

    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    r = requests.post(url, data={'q': q})

    try:
        dict = r.json()
        if dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(dict.get('id'), dict.get('name')))
    except:
        print("Not a valid JSON")
