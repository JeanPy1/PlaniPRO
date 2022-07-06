from sql import select, insert, update, delete
from dni import search

#insert('''INSERT INTO APOYO (IDAC, FECH) VALUES (1, '20/20/2022')''')
#update('''UPDATE ACTIVO SET NDNI = '08555618' WHERE ID = 3''')
#delete('''DELETE FROM APOYO WHERE ID = 2''', False)
#delete('''DELETE FROM ACTIVO WHERE ID = 6''', True)

datos = select('''SELECT * FROM APOYO''', True)
print(datos)

  
#print(search('48555618'))

