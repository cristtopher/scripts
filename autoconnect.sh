#!/bin/bash
# connects Point-to-Point Protocol dialer 
# if there is no connection to the url
FECHA=$(date)
if ping -c1 www.innovex.cl &>/dev/null
then
        echo $FECHA "- Conectado..." >> /home/innovex/connection.log
        $@
else
	echo $FECHA "- Sin conexion" >> /home/innovex/connection.log
	wvdial up
fi
