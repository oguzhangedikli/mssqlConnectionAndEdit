import pyodbc 
cxcn = pyodbc.connect('Driver={SQL Server};'
                      'Server=**.**.***.*;'
                      'Database=Person;'
                      'Uid=********;'
                      'Pwd=*******;')

cursor = cxcn.cursor()
cursor.execute('''create table tabloadı(
    Tablosütunu1 varchar(25) NOT NULL,
    Tablosütunu2 varchar(25) NOT NULL,
    Tablosütunu3 int NOT NULL,
    PRIMARY KEY (Tablosütunu1) )''')


cxcn.commit()
#Mssql üzerinden yeni bir tablo oluşturmak için gereken kod yapısı.
