#!/bin/bash
# This script will display all HTTP methods the server will accept.
curl -X OPTIONS -sI "$1" | grep -i Allow | awk '{print $2, $3, $4}' | sed 's/,$//'
