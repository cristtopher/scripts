import time
#import xlwt
#import xlrd

#wb = xlrd.open_workbook('file.xls')
#wb.sheet_names()
#sh = wb.sheet_by_index(0)
#first_column = sh.col_values(0)
#for r in range(8, len(first_column)):
    #print first_column[r]
for mes in range(1, 3):
    for dia in range(1, 32):
        for hora in range(00, 24):
            for seg in range(00, 60, 5):
                #print dia, mes, hora, seg
                date_time = str(dia) + "-" + str(mes) + "-2013 " +\
                str(hora) + ":" + str(seg)
                unix_time = time.mktime(time.strptime(date_time, "%d-%m-%Y %H:%M"))
                print unix_time
