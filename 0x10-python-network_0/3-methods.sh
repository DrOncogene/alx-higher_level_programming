#!/bin/bash
# prints all http methods supported by a server
curl -si -X OPTIONS "$1" | grep 'Allow' | cut -d " " -f 2-
