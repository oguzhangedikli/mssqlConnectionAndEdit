import pyodbc
cxcn = pyodbc.connect('Driver={SQL Server};'
                      'Server=**.**.**.*;'
                      'Database=Person;'
                      'Uid=*****;'
                      'Pwd=********s;')

cursor = cxcn.cursor()
cursor.execute('SELECT * FROM Person.dbo.Kapi')

for row in cursor:
    print(row)

cxcn.commit()
#mssql veritabanı üzerinden veri çekmek için kurulan bağlantı.
