#!/bin/bash
# set content with method POST
curl -sX POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
