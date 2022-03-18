#!/bin/bash
# sends a data in a json file to a server
curl -sL --data-binary @"$2" "$1"
