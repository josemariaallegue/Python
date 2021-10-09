import pyodbc


print([x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')])
"""
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\Prueba access\Prueba.accdb;')
cursor = conn.cursor()
cursor.execute('select * from MOCK_DATA')

for row in cursor.fetchall():
    print(row)"""
