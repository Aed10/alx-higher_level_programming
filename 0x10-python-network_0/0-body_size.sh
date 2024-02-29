#!/bin/bash
# This script will print the size of the body of the response.
URL=$1
curl -sI "$URL" | grep -i Content-length | awk '{print $2}'