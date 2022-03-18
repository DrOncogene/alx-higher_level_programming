#!/bin/bash
# sends a GET request with a custom header
curl -sL -H "X-School-User-Id: 98" "$1"
