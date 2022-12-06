from dataclasses import dataclass, astuple

@dataclass
class datos:
    dni         : str
    apPaterno   : str
    apMaterno   : str
    nombre      : str
    nacimiento  : str
    ingreso     : str
    planilla    : float
    asignacion  : float
    movilidad   : float
    cargo       : str 
    cuenta      : str 
    aportacion  : str 
    comision    : str 
    cuspp       : str 
    categoria   : str 
    revalidacion: str 
    codigo      : str 
    area        : str 
    celular     : str 
    distrito    : str 
    retiro      : str 

    def convert(self, object: object) -> tuple:
        return astuple(object)





from ..models.db import Person, session

persona = Person("48555618", "LAURA", "INCA", "JEANCARLOS ALBERTO", "01/01/2000", "10/10/2010", 1200, 102.50, 100,
                "ONP", "MIXTA", "FDSDFSDFSDFD", "RRHH", "194578457845", "A48555618", "AI", "01/01/2030", "OFICINA",
                 "984578457", "CHORRILLOS", "01/01/2020")
session.add(persona)
session.commit()