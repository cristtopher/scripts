#!/usr/bin/env python
import sys
import time
import math
import random

#
# Convert a tide table, which has only the extreme points of a tide
# to a smooth table, with elevation point every minute.
# Interpolate the points between two extremes using a cosine function.
#
# The format of the input file is as following:
# 2014-10-01	06:14	2.41
#               12:59   0.82
#               19:11   1.82
# 2014-10-02    00:43   1.02
#               07:25   2.39
#               14:23   0.77
#               20:33   1.86


def read_tide_table(file_name):
    '''Read a tide table from the specified file. The table has the following
    format: three columns, one having the date, the next the time and the last
    the tidal elevation.
    The format for the time is year-month-day HH:MM.
    If a row does not have the date, the date from the previous row is used.'''
    table = []
    f = open(file_name, 'rb')
    line_number = 0
    while True:
        line = f.readline()
        line_number += 1
        if line.startswith('#'): continue  # Skip comments
        if not line: break  # End of file reached
        s = line.split()
        if len(s) == 3:
            tide_date = s[0]
            tide_time = s[1]
            tide_elevation = s[2]
        elif len(s) == 2:
            tide_time = s[0]
            tide_elevation = s[1]
        else:
            print("Error, invalid number of elements in tide table.")
            sys.exit()
        try:
            date_time = tide_date + ' ' + tide_time
            unix_time = time.mktime(time.strptime(date_time, "%Y-%m-%d %H:%M"))
            elevation = float(tide_elevation)
        except:
            print "Error processing line", line_number, ":", line
            sys.exit() 
        table.append((unix_time, elevation))
    f.close()
    return table


def smooth_table(table):
    '''Smoth the tide table. Interpolate the elevation between two
    extreme points using a cosine function.'''
    length = len(table)
    for i in range(length-1):
        t0, elevation0 = table[i]
        t1, elevation1 = table[i+1]
        minutes_diff = (t1 - t0) / 60
        tidal_range = elevation1 - elevation0
        for t in range(int(minutes_diff)):
            e = -math.cos(t * math.pi / minutes_diff) * (tidal_range/2.0) + tidal_range / 2.0 + elevation0
            datetime = time.strftime("%Y-%m-%d %H:%M", time.localtime(t0 + t * 60))
            print "%s %.0f %.2f" % (datetime, (t0 + t * 60), e)

            


if __name__ == '__main__':
    
    table = read_tide_table(sys.argv[1])
    smooth_table(table)
    #for l in table:
    #    print l[0], l[1]



