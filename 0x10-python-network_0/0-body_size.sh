#!/bin/bash
# Sends a request to a URL passed as an argument and displays the size of the body of the response (in bytes)
curl -s "$1" | wc -c
