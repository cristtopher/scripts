#!/bin/bash
if [ $2 == 'UDP' ]; then
    ssh paula@vpn.innovex.cl 'cat /etc/openvpn/openvpn-status.log | grep ' $1
elif [ $2 == 'TCP' ]; then
    ssh paula@vpn.innovex.cl 'cat /etc/openvpn/openvpn-status_443.log | grep ' $1
else
    echo 'Unknown Protocol!'
fi