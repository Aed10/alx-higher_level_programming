#!/bin/bash
# This script will display all HTTP methods the server will accept.
curl -X OPTIONS -sI "$1"
