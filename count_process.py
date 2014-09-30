#!/usr/bin/env python2.5
from threading import Thread
import subprocess
import sys
import os
from Queue import Queue

num_threads = 6
queue = Queue()
ips = []
txt = open(sys.argv[1], 'r')
key = txt.readline()
while key != "":
    ips.append(key)
    os.system("sshpass -p 'innovex' ssh innovex@%s ps aux | grep synchronize_db_http | wc -l" % key)
    key = txt.readline()
txt.close()


