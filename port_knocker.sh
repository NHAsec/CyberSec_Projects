read -p "Enter target IP: " ip
read -p "Enter ports to knock on(space seperated): " ports

for p in $ports;do
	nc -z -w 1 $ip $p 2>/dev/null
	sleep 0.5
done
