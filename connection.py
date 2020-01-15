import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-P9GNVS4;"
                      "username=niteesh1;"
                      "password=niteesh1;"
                      "Database=company;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM emp')

for row in cursor:
    print('row = %r' % (row,))
