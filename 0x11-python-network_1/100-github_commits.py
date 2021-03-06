#!/usr/bin/python3
""" Script taht lists 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”"""

import requests
from sys import argv

if __name__ == "__main__":

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])

    r = requests.get(url)

    try:
        for i in range(10):
            print("{}: {}".format(r.json()[i].get('sha'), r.json()[
                i].get('commit').get('author').get('name')))
    except:
        pass
