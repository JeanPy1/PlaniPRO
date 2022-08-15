
from datetime import datetime
from dateutil.relativedelta import relativedelta
 
def Edad(nacimiento: str) -> int:
    
    today = datetime.now()  
    fecha = datetime.strptime(nacimiento, '%d/%m/%Y')    

    return today.year - fecha.year - ((today.month, today.day) < (fecha.month, fecha.day))

def Tiempo(ingreso: str) -> str:    

    hoy = datetime.today()
    fecha = f'{hoy.day}/{hoy.month}/{hoy.year}'
    
    fechaIngreso = datetime.strptime(ingreso, '%d/%m/%Y')       
    fechaActual = datetime.strptime(fecha, '%d/%m/%Y')   
   
    diferencia = relativedelta(fechaActual, fechaIngreso)   
    return f"{diferencia.years} - {diferencia.months} - {diferencia.days}"
    
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

def PlanillaMes(fecha: str) -> int:

    if FechaValida(fecha, True):
       
        fechaPlanilla = datetime.strptime(fecha, '%d/%m/%Y')   
        dias = __obtener_dias_del_mes(fechaPlanilla.month, fechaPlanilla.year)

        return dias
    
    else:
        
        return 0

def CompararFechas(fechaInicial: str, fechaFinal: str) -> bool:
    
    if FechaValida(fechaInicial, True) and FechaValida(fechaFinal, True):

        fechaIngreso = datetime.strptime(fechaInicial, '%d/%m/%Y')       
        fechaMes = datetime.strptime(fechaFinal, '%d/%m/%Y')   

        if fechaIngreso <= fechaMes: 
            return True
        else:
            return False