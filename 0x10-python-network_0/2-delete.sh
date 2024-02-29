#!/bin/bash
# This script will send a DELETE request to a URL passed as an argument, and display the body of the response.
curl -X DELETE -sL "$1"
