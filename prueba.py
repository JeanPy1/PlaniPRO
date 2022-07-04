from sql import select, insert, update, delete
from dni import search

#insert('''INSERT INTO APOYO (IDAC, FECH) VALUES (2, '20/20/2020')''')
#update('''UPDATE APOYO SET FECH = '10/10/2010' WHERE ID = 64''')
#delete('''DELETE FROM APOYO WHERE ID = 15''', False)
#delete('''DELETE FROM ACTIVO WHERE ID = 6''', True)

datos = select('''SELECT * FROM ACTIVO''', True)
print(datos)

  
#print(search('48555618'))