import sqlite3

def conectar():
    miConexion = sqlite3.connect("cruddb")
    cursor = miConexion.cursor()
    try:
        sql="""
        CREATE TABLE IF NOT EXISTS personas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ci TEXT NOT NULL UNIQUE,
            edad INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            direccion TEXT DEFAULT 'NO TIENE',
            correo TEXT NOT NULL UNIQUE
        )
        """
        cursor.execute(sql)
        cursor.close()
        return miConexion
    except Exception as ex:
        print("Error de conexion:",ex)
    finally:    
        cursor.close()