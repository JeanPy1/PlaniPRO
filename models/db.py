from sqlalchemy import create_engine, Column, Integer, VARCHAR, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):

    __tablename__ = "persons"

    id = Column("id", Integer, primary_key=True)
    dni = Column("dni", VARCHAR(8))
    paterno = Column("paterno", VARCHAR(20))
    materno = Column("materno", VARCHAR(20))
    nombre = Column("nombre", VARCHAR(30))
    nacimiento = Column("nacimiento", VARCHAR(10))
    ingreso = Column("ingreso", VARCHAR(10))
    planilla = Column("planilla", Float)
    asignacion = Column("asignacion", Float)
    movilidad = Column("movilidad", Float)
    aportacion = Column("aportacion", VARCHAR(10))
    comision = Column("comision", VARCHAR(5))
    cuspp = Column("cuspp", VARCHAR(12))
    cargo = Column("cargo", VARCHAR(30))
    cuenta = Column("cuenta", VARCHAR(20))  
    licencia = Column("licencia", VARCHAR(9))
    categoria = Column("categoria", VARCHAR(5))
    vencimiento = Column("vencimiento", VARCHAR(10))
    area = Column("area", VARCHAR(10))
    celular = Column("celular", VARCHAR(9))
    distrito = Column("distrito", VARCHAR(30))
    retiro = Column("retiro", VARCHAR(10))

    def __init__(self,  dni: str, paterno: str, materno: str, nombre: str, nacimiento: str,
                        ingreso: str, planilla: float, asignacion: float, movilidad: float,
                        aportacion: str, comision: str, cuspp:str, cargo: str, cuenta: str,
                        licencia: str, categoria: str, vencimiento: str, area: str,
                        celular: str, distrito: str, retiro: str) -> None:
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
        self.celular = celular
        self.distrito = distrito
        self.retiro = retiro

    def __repr__(self) -> str:
        tupla =  f"""{self.id}, {self.dni}, {self.paterno}, {self.materno}, {self.nombre},
                     {self.nacimiento}, {self.ingreso}, {self.planilla}, {self.asignacion}, {self.movilidad},
                     {self.aportacion}, {self.comision}, {self.cuspp}, {self.cargo}, {self.cuenta}
                     {self.licencia}, {self.categoria}, {self.vencimiento}, {self.area}, {self.celular}
                     {self.distrito}, {self.retiro}"""
        
        return tupla

      
engine = create_engine("sqlite:///../data/db.sqlite3", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

