#!/bin/bash
# sends a request and prints only the status code
curl -sL -X HEAD -w %{http_code} "$1"
