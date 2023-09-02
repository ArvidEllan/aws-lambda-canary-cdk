#!/bin/bash
URL= https://6dh80kej87.execute-api.eu-west-1.amazonaws.com/qa/
while true; do
	echo "$(date +%F_%H%M%S) - $(curl -s $URL)"
	sleep 5
done
