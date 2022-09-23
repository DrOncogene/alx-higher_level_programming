#!/bin/bash
# sends a request to a server for it to return 'You got me!'
curl -X PUT -H "Origin: School" -d user_id=98 -sL 0.0.0.0:5000/catch_me_2
