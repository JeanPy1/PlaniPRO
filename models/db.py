from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):

    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    dni = Column(String(8))
    paterno = Column(String(20))
    materno = Column(String(20))
    nombre = Column(String(30))
    nacimiento = Column(String(10))
    ingreso = Column(String(10))
    planilla = Column(Float)
    asignacion = Column(Float)
    movilidad = Column(Float)
    aportacion = Column(String(10))
    comision = Column(String(5))
    cuspp = Column(String(12))
    cargo = Column(String(30))
    cuenta = Column(String(20))  
    licencia = Column(String(9))
    categoria = Column(String(5))
    vencimiento = Column(String(10))
    area = Column(String(10))
    telefono = Column(String(9))
    distrito = Column(String(30))
    retiro = Column(String(10))

    def __init__(self,  dni: str, paterno: str, materno: str, nombre: str, nacimiento: str,
                        ingreso: str, planilla: float, asignacion: float, movilidad: float,
                        aportacion: str, comision: str, cuspp:str, cargo: str, cuenta: str,
                        licencia: str, categoria: str, vencimiento: str, area: str,
                        telefono: str, distrito: str, retiro: str) -> None:
        self.dni = dni
        self.paterno = paterno
        self.materno = materno
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.ingreso = ingreso
        self.planilla = planilla
        self.asignacion = asignacion
        self.movilidad = movilidad
        self.aportacion = aportacion
        self.comision = comision
        self.cuspp = cuspp
        self.cargo = cargo
        self.cuenta = cuenta
        self.licencia = licencia
        self.categoria = categoria
        self.vencimiento = vencimiento
        self.area = area
        self.telefono = telefono
        self.distrito = distrito
        self.retiro = retiro

    def __repr__(self) -> str:       
        return f"{self.dni}, {self.paterno} {self.materno} {self.nombre}"
      
engine = create_engine("sqlite:///data/db.sqlite3", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()