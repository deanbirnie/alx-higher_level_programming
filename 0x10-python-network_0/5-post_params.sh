#!/bin/bash
# Send a post request to the passed URL and displays the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
