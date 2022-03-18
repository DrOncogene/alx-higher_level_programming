#!/bin/bash
# prints all http methods supported by a server
curl -sI -X OPTIONS "$1" | grep -oP 'Allow: \K\S+'
