#!/bin/bash
# display if success
http_response=$(curl -X GET -s -o body.txt -w "%{http_code}" "$1"); if [ "$http_response" -eq 200 ]; then cat body.txt; fi ; rm body.txt
