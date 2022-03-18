#!/bin/bash
# sends a data in a json file to a server
curl -sL -H "Content-Type: application/octet-stream" --data-binary @"$2" "$1"
