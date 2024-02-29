#!/bin/bash
# This script will send a POST request to a URL passed as an argument, and display the body of the response.
curl -sX POST -d "email: test@gmail.com" -d "subject: I will always be here for PLD" "$1"
