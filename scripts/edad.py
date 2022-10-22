
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
