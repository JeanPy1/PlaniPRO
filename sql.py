import sqlite3

def __conexion(query:str, multiline:bool):

    database = 'PlaniPRO.db'
    conexion = sqlite3.connect(database)  
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
    return __conexion(query, multiline)

def insert(query:str):
    __conexion(query, False)

def update(query:str):
    __conexion(query, False)    

def delete(query:str):
    __conexion(query, False)  

