#!/bin/bash

NET="192.168.12"

for i in $(seq 1 254)
do
	(
		if ping -c 1 -W 1 $NET.$i &> /dev/null
		then
			echo "Host $NET.$i is up"
		fi
	) &
done

wait
