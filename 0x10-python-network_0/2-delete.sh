#!/bin/bash
# Sends a delete request to the URL passed as the first argument and display body of the response"
curl -sX DELETE "$1"
