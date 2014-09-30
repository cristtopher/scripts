#!/bin/bash
CONT=0
PATH="/home/cristtopher/"
if [ -e $PATH"udp.conf" ]; then
	FILE=$PATH"udp.conf";
elif [ -e $PATH"client.conf" ]; then
	FILE=$PATH"client.conf";
elif [ -e $PATH$(hostname)".conf" ]; then
	FILE=$PATH$(hostname)".conf";
else
	FILE="Null"
fi
echo $FILE
$(awk '/1194/ {print}' /home/cristtopher/udp.conf)
if [ $FILE == "Null" ]; then
	echo "File no encontrado en $PATH";
else
	echo "File es:" $FILE;
	while read line
	do
		if [ -n "$line" ]; then
			let CONT=$CONT+1;
		fi
	done < $FILE

	if [ $CONT -gt 100 ]; then # mayor que
		while read line
		do
			if [ "$line" == "proto udp" ]; then
		   		echo -e "$line";
		   		#$FILE <<< "hello world";
		   	elif [ "$line" == "remote vpn.innovex.cl 1194" ]; then
		   		echo -e "$line";
		   	elif [ "$line" == "remote vpn2.innovex.cl 1194" ]; then
		   		echo -e "$line";
		   	elif [ "$line" == "remote jaiba.homelinux.org 1194" ]; then
		   		echo -e "$line";
		   	fi
		done < $FILE
	else
		# Conf nueva con menos lineas
		sed 's/1194/443/g' $FILE;
		sed 's/proto udp/proto tcp/g' $FILE;
	fi
fi