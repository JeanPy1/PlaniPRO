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