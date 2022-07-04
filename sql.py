from sqlite3 import connect

def __conexion(query:str, multiline:bool, foreignkey:bool):

    database = 'PlaniPRO.db'
    conexion = connect(database)  
    
    if foreignkey:
        conexion.execute('PRAGMA foreign_keys = 1')

    cursor = conexion.cursor()
    cursor.execute(query)

    if multiline:
        respuesta = cursor.fetchall()
    else:
        respuesta = cursor.fetchone()
          
    conexion.commit()
    conexion.close()
        
    return respuesta
      
def select(query:str, multiline:bool):
    return __conexion(query, multiline, False)

def insert(query:str):
    __conexion(query, False, False)

def update(query:str):
    __conexion(query, False, False)    

def delete(query:str, foreignkey:bool):
    __conexion(query, False, foreignkey)  