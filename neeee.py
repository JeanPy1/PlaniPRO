from sql import select, insert, update, delete

#insert('''INSERT INTO APOYO (IDAC, FECH) VALUES (2, '20/20/2020')''')
#update('''UPDATE APOYO SET FECH = '10/10/2010' WHERE ID = 64''')
#delete('''DELETE FROM APOYO WHERE ID = 63''')

datos = select('''SELECT * FROM APOYO''', True)
print(datos)