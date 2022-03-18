#!/bin/bash
# prints all http methods supported by a server
curl -si -X OPTIONS "$1"
