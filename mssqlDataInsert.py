import pyodbc 
cxcn = pyodbc.connect('Driver={SQL Server};'
                      'Server=**.**.***.*;'
                      'Database=Person;'
                      'Uid=********;'
                      'Pwd=**********;')
while True:

    a= int (input ('Kapı No?\t: '))
    b= input ('Kapı Adı?\t: ')
    cursor = cxcn.cursor()
    cursor.execute('''SELECT * FROM Person.dbo.Kapi
INSERT INTO Kapi values (?,?)''',(a,b))
    x = input ('Çıkmak için x')
    if x=='x':
        break
cxcn.commit()
                   
#mssql üzerinde belirli bir alana veri girişi yapmak için kullanılan yapı.
