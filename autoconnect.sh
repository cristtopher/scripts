#!/bin/bash
FECHA=$(date)
if ping -c1 www.innovex.cl &>/dev/null
then
        echo $FECHA "- Conectado..." >> /home/innovex/connection.log
        $@
else
	echo $FECHA "- Sin conexion" >> /home/innovex/connection.log
	wvdial up
fi
