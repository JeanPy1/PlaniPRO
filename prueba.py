from sql import select, insert, update, delete
from dni import search

#insert('''INSERT INTO APOYO (IDAC, FECH) VALUES (1, '20/20/2022')''')
#update('''UPDATE ACTIVO SET NDNI = '08555618' WHERE ID = 3''')
#delete('''DELETE FROM APOYO WHERE ID = 2''', False)
#delete('''DELETE FROM ACTIVO WHERE ID = 6''', True)

#datos = select('''SELECT * FROM APOYO''', True)
#print(datos)

  
#print(search('48555618'))
#nombre = "abc1"
#row = ('ABC1', 'fdsfsd')
#if nombre.upper() == str(row[0]).upper():
#    print('ya existe')


from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    return today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))


print(calculateAge('28/12/1989'))