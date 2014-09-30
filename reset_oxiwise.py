#!/usr/bin/env python

import serial
import sys
import os
from innovex.configuration import Configuration

#
# Main
#
if __name__ == '__main__':
    if not os.geteuid() is 0:
        print 'Ejecutar como root!'
        sys.exit(1)
    else:
        if len(sys.argv) < 2:
            try:
                fp = open('/etc/innovex.cfg')
            except(IOError):
                print 'El archivo /etc/innovex.cfg no existe'
                sys.exit()
        else:
            # For now do nothing
            pass

        config = Configuration(fp)

        # Kill multireceiver
        os.system("ps ax | grep multireceiver | grep -v grep | awk '{print $2}' | xargs kill")

        # Open serial port
        try:
            serial_port = serial.Serial(config.serialport,
            baudrate=config.baudrate, timeout=0.3)
            while 1:
                try:
                    l = serial_port.read(2)
                    if(not l):
                        continue
                    print l
                    if(l.startswith('#>')):
                        serial_port.write('RST')
                        serial_port.flush()
                        os.system('minicom -b %s -D %s' % (config.baudrate,
                        config.serialport))
                        break
                except(IOError):
                    print "Error, no se puede leer"
        except:
            print 'Unable to open serial port.'
            sys.exit()
        serial_port.close()
