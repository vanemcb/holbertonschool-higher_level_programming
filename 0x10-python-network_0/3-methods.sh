#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -I $1 | grep -i Allow | cut -d " " -f1 --complement
