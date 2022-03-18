#!/bin/bash
# sends a POST request
curl -sL -F "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
