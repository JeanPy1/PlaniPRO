
from datetime import datetime
 
def Edad(nacimiento: str) -> int:
    
    today = datetime.now()  
    fecha = datetime.strptime(nacimiento, '%d/%m/%Y')    

    return today.year - fecha.year - ((today.month, today.day) < (fecha.month, fecha.day))

def Tiempo(ingreso: str) -> list:    

    hoy = datetime.today()
    fecha = f'{hoy.day}/{hoy.month}/{hoy.year}'
    
    fechaIngreso = datetime.strptime(ingreso, '%d/%m/%Y')       
    fechaActual = datetime.strptime(fecha, '%d/%m/%Y')     
        
    diasTranscurridos = fechaActual - fechaIngreso   

    años = 0
    meses = 0
    dias = 0

    if diasTranscurridos.days == 366:
        años = 1
    elif diasTranscurridos.days > 366:
        años = int(diasTranscurridos.days / 365)
        if (diasTranscurridos.days - (años * 365)) > 30:
            meses = int((diasTranscurridos.days - (años * 365)) / 30)
    else:
        if diasTranscurridos.days > 30:
            meses = int(diasTranscurridos.days / 30)           
        else:           
            dias = diasTranscurridos.days         

    return [años, meses, dias]

def __Bisiesto(anio: int) -> bool:

    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def __obtener_dias_del_mes(mes: int, anio: int) -> int:
        
    if mes in [4, 6, 9, 11]: 
        return 30 # Abril, junio, septiembre y noviembre tienen 30
    
    if mes == 2:
        if __Bisiesto(anio): # Febrero depende de si es o no bisiesto
            return 29 
        else:
            return 28
    else:        
        return 31 # Todos los demas 

def FechaValida(fecha: str, posterior: bool) -> bool:

    try:
        validar = datetime.strptime(fecha, '%d/%m/%Y') 
        if validar > datetime.today():
            if posterior:
                return True
            else:
                return False
        else:
            if validar.year < (datetime.today().year - 100):
                return False
            else:
                return True
    except:
        return False