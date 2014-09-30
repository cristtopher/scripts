import sys
import datetime
import sqlite3

connection = sqlite3.connect(sys.argv[1])
cursor = connection.cursor()
cursor2 = connection.cursor()

# cursor.execute('ALTER TABLE oxygen ADD date varchar(9)')
# cursor.execute('SELECT * FROM oxygen')
# for row in cursor:
#     values = (datetime.datetime.fromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M'), row[0])
#     cursor2.execute("UPDATE oxygen SET date = ? WHERE unixtime = ?", values)
#     connection.commit()

interval = 0.003472 # Mantisa de 6. coresponde a 5 min en julianday.
center = interval
count = 0
total = 0
cursor.execute('SELECT DISTINCT julianday(date) FROM oxygen')
for row in cursor:
    # Round para ambos, presicion del punto flotante.
    if round(row[0] - center, 6) == round(interval, 6):
        cursor2.execute("DELETE FROM oxygen WHERE julianday(date) = " + str(row[0]))
        connection.commit()
        count += 1
    center = row[0]
    total += 1
print count, "registros borrados de",total

count = 0
cursor.execute('SELECT * FROM oxygen')
for row in cursor:
    count

cursor.close()
connection.close()