import csv
import sys
import datetime

with open(sys.argv[1], 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        f = input("Columna: ")
        print datetime.datetime.fromtimestamp(float(row[f])).strftime('%Y-%m-%d %H:%M:%S')
