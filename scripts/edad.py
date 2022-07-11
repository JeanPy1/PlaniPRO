
from datetime import datetime, timedelta
 
def Edad(nacimiento:str):
    today = datetime.now()  
    fecha = datetime.strptime(nacimiento, '%d/%m/%Y')    
    return today.year - fecha.year - ((today.month, today.day) < (fecha.month, fecha.day))


def es_bisiesto(anio:int) -> bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def obtener_dias_del_mes(mes: int, anio: int) -> int:
    # Abril, junio, septiembre y noviembre tienen 30
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31




def Tiempo(ingreso:str):    

    hoy = datetime.today()
    fecha = f'{hoy.day}/{hoy.month}/{hoy.year}'
    
    fechaIngreso = datetime.strptime(ingreso, '%d/%m/%Y')       
    fechaActual = datetime.strptime(fecha, '%d/%m/%Y')     
        
    diferencia = fechaActual - fechaIngreso   

    print(fechaIngreso + timedelta(days=365 * 4))

    if diferencia.days > 364:
        años = int(diferencia.days / 365)        
        if (diferencia.days - (365 * años)) > 30:
            meses = int(diferencia.days - (365 * años) /30)           
            print(f'{años} y {meses}')    
        else:
            print(f'{años}')  
    elif diferencia.days < 364:
        if dias > 30:
            meses = int(dias / 30)           
            print(f'{meses}')
        else:         
            print('menos de 1 mes')
    else:
        print('1 año')


       





fecha = Tiempo('20/07/2018')

