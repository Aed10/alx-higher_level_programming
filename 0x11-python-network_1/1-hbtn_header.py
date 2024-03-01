#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and displays
the value of X-Request-Id variable found in the header of the response."""

import urllib.request
import sys

if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        html_data = response.read()
        headers = response.getheaders()
        for name, value in headers:
            if name == "X-Request-Id":
                print(value)
