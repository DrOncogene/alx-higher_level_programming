#!/bin/bash
# sends a data in a json file to a server
curl -s -H "Content-Type: application/json" --data-binary @"$2" "$1"
