
from datetime import date, datetime
 
def Edad(nacimiento:str):
    today = date.today()
    fecha = datetime.strptime(nacimiento, '%d/%m/%Y')    
    return today.year - fecha.year - ((today.month, today.day) < (fecha.month, fecha.day))

def Tiempo(ingreso:str):
    today = date.today()
    fecha = datetime.strptime(ingreso, '%d/%m/%Y')  
    
    return print((today.year - fecha.year) * 12 + today.month - fecha.month)

Tiempo('30/03/2022')
#print(aa)
