#!/usr/bin/bash

# Login first time on boot
python /home/pi/nac_login.py > /home/pi/debug_nac_login.log 2>&1

# After initial login check for continuous connectivity
while true
do
	#echo "Checking internet connectivity..."
	ping -c 1 www.fast.com>>/dev/null

	if [ $? -eq  0 ]
		then
		echo "Able to reach internet"
	else
		echo " Not able to check internet connectivity!"
		python /home/pi/nac_login.py > /home/pi/debug_nac_login.log 2>&1
	fi

done