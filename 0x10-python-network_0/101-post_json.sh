#!/bin/bash
# sends a data in a json file to a server
curl -sL --data @"$2" "$1"
