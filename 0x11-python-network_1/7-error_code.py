#!/usr/bin/python3
""" Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response. """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if error occurred
    except requests.exceptions.HTTPError as err:
        err_code = err.response.status_code
        if err_code >= 400:
            print(f"Error code: {err_code}")
