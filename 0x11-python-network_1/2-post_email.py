#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import urllib.request
import sys

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    url = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(url) as response:
        body = response.decode("utf-8")
        print(body)
