from sqlite3 import connect


def Create_Tables():

    con = connect("./data/db.sqlite3")
    cur = con.cursor()

    personal = """ CREATE TABLE IF NOT EXISTS personal (
	                id INTEGER PRIMARY KEY AUTOINCREMENT,
	                dni VARCHAR(8),
	                paterno VARCHAR(20),
	                materno VARCHAR(20),
	                nombre VARCHAR(30),
	                nacimiento VARCHAR(10),
	                ingreso VARCHAR(10),
	                planilla REAL,
	                asignacion REAL,
	                movilidad REAL,
	                aportacion VARCHAR(9),
	                comision VARCHAR(5),
	                cuspp VARCHAR(12),
	                cargo VARCHAR(30),
	                cuenta VARCHAR(20),	                
	                licencia VARCHAR(9),
	                categoria VARCHAR(5),
	                vencimiento VARCHAR(10),
                    area VARCHAR(10),
	                telefono VARCHAR(9),
	                distrito VARCHAR(30),
	                retiro VARCHAR(10)  )"""
    cesados = """ CREATE TABLE IF NOT EXISTS cesados (
	                dni VARCHAR(8),
	                paterno VARCHAR(20),
	                materno VARCHAR(20),
	                nombre VARCHAR(30),
	                nacimiento VARCHAR(10),
	                ingreso VARCHAR(10),
	                planilla REAL,
	                asignacion REAL,
	                movilidad REAL,
	                aportacion VARCHAR(9),
	                comision VARCHAR(5),
	                cuspp VARCHAR(12),
	                cargo VARCHAR(30),
	                cuenta VARCHAR(20),	                
	                licencia VARCHAR(9),
	                categoria VARCHAR(5),
	                vencimiento VARCHAR(10),
                    area VARCHAR(10),
	                telefono VARCHAR(9),
	                distrito VARCHAR(30),
	                retiro VARCHAR(10)  )"""
    apoyo = """ CREATE TABLE IF NOT EXISTS apoyo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    fecha VARCHAR(10),
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""
    falta = """ CREATE TABLE IF NOT EXISTS falta (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    fecha VARCHAR(10),
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""    
    feriado = """ CREATE TABLE IF NOT EXISTS feriado (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    fecha VARCHAR(10),
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""
    ingreso = """ CREATE TABLE IF NOT EXISTS ingreso (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    detalle VARCHAR(150),
                    importe REAL,
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""
    descuento = """ CREATE TABLE IF NOT EXISTS descuento (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    detalle VARCHAR(150),
                    importe REAL,
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""
    vacaciones = """ CREATE TABLE IF NOT EXISTS vacaciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    inicio VARCHAR(10),
                    final VARCHAR(10),
                    dias INTEGER,
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""
    compravacaciones = """ CREATE TABLE IF NOT EXISTS compravacaciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    inicio VARCHAR(10),
                    final VARCHAR(10),
                    dias INTEGER,
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""
    descansomedico = """ CREATE TABLE IF NOT EXISTS descansomedico (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    inicio VARCHAR(10),
                    final VARCHAR(10),
                    dias INTEGER,
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""
    adelanto = """ CREATE TABLE IF NOT EXISTS adelanto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    fecha VARCHAR(10),
                    importe REAL,
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""
    porfuera = """ CREATE TABLE IF NOT EXISTS porfuera (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    personal_id INTEGER,
                    fecha VARCHAR(10),
                    importe REAL,
                    FOREIGN KEY (personal_id) REFERENCES personal (id)
                    ON DELETE CASCADE   )"""

    copia = """ CREATE TRIGGER IF NOT EXISTS copia_personal AFTER DELETE ON personal 
                BEGIN
                INSERT INTO cesados (dni, paterno, materno, nombre, nacimiento, ingreso,
	                planilla, asignacion, movilidad, aportacion, comision, cuspp, cargo,
	                cuenta, licencia, categoria, vencimiento, area, telefono, distrito, retiro) 
                    VALUES (old.dni, old.paterno, old.materno, old.nombre, old.nacimiento, old.ingreso, 
                    old.planilla, old.asignacion, old.movilidad, old.aportacion, old.comision, old.cuspp, 
                    old.cargo, old.cuenta, old.licencia, old.categoria, old.vencimiento, old.area, 
                    old.telefono, old.distrito, old.retiro);
                END """

    cur.execute(personal)
    cur.execute(cesados)
    cur.execute(apoyo)
    cur.execute(falta)
    cur.execute(feriado)
    cur.execute(ingreso)
    cur.execute(descuento)
    cur.execute(vacaciones)
    cur.execute(compravacaciones)
    cur.execute(descansomedico)
    cur.execute(adelanto)
    cur.execute(porfuera)
    cur.execute(copia)

    con.commit()
    con.close()

def __Conexion(query:str, select: bool):
    
    con = connect("./data/db.sqlite3")
    cur = con.cursor()   
    cur.execute('PRAGMA foreign_keys = 1')       
   
    if select:
        result = cur.execute(query).fetchall()        
    else:
        cur.execute(query)    
        con.commit()

    con.close()

    if select:
        return result


def Select_Personal() -> list:

    query = f""" SELECT * FROM personal ORDER BY paterno ASC, materno ASC, nombre ASC """
    return __Conexion(query, True)

def Insert_Personal(dni: str, paterno: str, materno: str, nombre: str, nacimiento: str, ingreso: str, planilla: float,
					asignacion: float, movilidad: float, aportacion: str, comision: str, cuspp:str, cargo: str, cuenta: str,
                    licencia: str, categoria: str, vencimiento: str, area: str, telefono: str, distrito: str, retiro: str):					
	
	values = (dni, paterno, materno, nombre, nacimiento, ingreso, planilla, asignacion, movilidad, aportacion, comision, cuspp,
				cargo, cuenta, licencia, categoria, vencimiento, area, telefono, distrito, retiro)
	query = f""" INSERT INTO personal (dni, paterno, materno, nombre, nacimiento, ingreso, planilla, asignacion, movilidad,
										aportacion, comision, cuspp, cargo, cuenta, licencia, categoria, vencimiento, area,
										telefono, distrito, retiro) VALUES {values} """
	__Conexion(query, False)

def Update_Personal(id: int, nacimiento: str, ingreso: str, planilla: float, asignacion: float, movilidad: float, aportacion: str,
					comision: str, cuspp:str, cargo: str, cuenta: str, licencia: str, categoria: str, vencimiento: str,
					area: str, telefono: str, distrito: str, retiro: str):	
	
	query = f""" UPDATE personal SET nacimiento="{nacimiento}", ingreso="{ingreso}", planilla={planilla}, asignacion={asignacion},
					movilidad={movilidad}, aportacion="{aportacion}", comision="{comision}", cuspp="{cuspp}", cargo="{cargo}",
					cuenta="{cuenta}", licencia="{licencia}", categoria="{categoria}", vencimiento="{vencimiento}", area="{area}",
					telefono="{telefono}", distrito="{distrito}", retiro="{retiro}" WHERE id = {id} """
	__Conexion(query, False)

def Delete_Personal(id: int):
    
    query = f""" DELETE FROM personal WHERE ID = {id} """
    __Conexion(query, False)


def Select_Detalle(table_name: str, id: int) -> list:    

    query = f""" SELECT * FROM {table_name} WHERE personal_id = {id} """
    return __Conexion(query, True)

def Insert_Detalle(table_name: str, personal_id: int, datos: dict):
     
    if table_name == "apoyo" or table_name == "falta" or table_name == "feriado":
        query = f""" INSERT INTO {table_name} (personal_id, fecha) VALUES ({personal_id}, "{datos["fecha"]}") """
    elif table_name == "ingreso" or table_name == "descuento":
        query = f""" INSERT INTO {table_name} (personal_id, detalle, importe) VALUES ({personal_id}, "{datos["detalle"]}", {datos["importe"]}) """
    elif table_name == "vacaciones" or table_name == "compravacaciones" or table_name == "descansomedico":
        query = f""" INSERT INTO {table_name} (personal_id, inicio, final, dias) VALUES ({personal_id}, "{datos["inicio"]}", "{datos["final"]}", {datos["dias"]}) """
    elif table_name == "adelanto" or table_name == "porfuera":
        query = f""" INSERT INTO {table_name} (personal_id, fecha, importe) VALUES ({personal_id}, "{datos["fecha"]}", {datos["importe"]}) """

    __Conexion(query, False)

def Delete_Detalle(table_name: str, id: int):

    query = f""" DELETE FROM {table_name} WHERE ID = {id} """
    __Conexion(query, False)


def Select_Id(table_name: str) -> list:

    query = f""" SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1 """
    return __Conexion(query, True)

def Restablecer_Secuencia():

	query = f""" DELETE FROM sqlite_sequence """
	__Conexion(query, False)




