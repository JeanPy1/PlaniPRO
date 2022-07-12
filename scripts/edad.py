
from datetime import datetime, timedelta
 
def Edad(nacimiento: str) -> int:
    
    today = datetime.now()  
    fecha = datetime.strptime(nacimiento, '%d/%m/%Y')    
    return today.year - fecha.year - ((today.month, today.day) < (fecha.month, fecha.day))


def __Bisiesto(anio: int) -> bool:

    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def obtener_dias_del_mes(mes: int, anio: int) -> int:
    
    if mes in [4, 6, 9, 11]: 
        return 30 # Abril, junio, septiembre y noviembre tienen 30
    
    if mes == 2:
        if __Bisiesto(anio): # Febrero depende de si es o no bisiesto
            return 29 
        else:
            return 28
    else:        
        return 31 # Todos los demas 




def Tiempo(ingreso: str):    

    hoy = datetime.today()
    fecha = f'{hoy.day}/{hoy.month}/{hoy.year}'
    
    fechaIngreso = datetime.strptime(ingreso, '%d/%m/%Y')       
    fechaActual = datetime.strptime(fecha, '%d/%m/%Y')     
        
    diasTranscurridos = fechaActual - fechaIngreso   

    if diasTranscurridos.days == 366:
        print('1 año')
    elif diasTranscurridos.days > 366:
        años = int(diasTranscurridos.days/365)
        print(años)
        if (diasTranscurridos.days - (años * 365)) > 30:
            meses = int((diasTranscurridos.days - (años * 365))/30)
            print(meses)
        else:
            meses = 0
            print(meses)
    else: 
        años = 0
        print(años)
        if diasTranscurridos.days > 30:
            meses = int(diasTranscurridos.days /30)
            print(meses)
        else:
            meses = 0
            print(meses)

  


fecha = Tiempo('10/03/2020')

