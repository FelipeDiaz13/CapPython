import mysql.connector

conn = mysql.connector.connection(
    host='Localhost', 
    user='root',
    password='1234',
    database='prueba'

)

lista =[]
cursor = conn.cursor()
cursor.execute("select * from db")

resultados = cursor.fetchall()

for datos in resultados:
    
    for dato in datos:
        if dato == 'Y':
            lista.append(dato)
else:
    print("Notienes datos")

conn.close()

print(lista.count)

