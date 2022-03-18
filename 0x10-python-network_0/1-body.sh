#!/bin/bash
# prints the body of a response only if status is 200
if [ "$(curl -s -o /dev/null -sw '%{http_code}' "$1")" -eq 200 ]; then curl -s "$1"; fi
