#!/bin/bash
# use curl to print the size of the response body
curl -sI $1 | grep -oP 'Content-Length: \K\d+'
