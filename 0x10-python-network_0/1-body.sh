#!/bin/bash
# This script will send a request to a URL passed as an argument, and display the body of the response.
curl -X GET -sfL "$1"