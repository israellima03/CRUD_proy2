import conexion as con

def save(persona):
    persona=dict(persona)
    try:
        db = con.conectar()
        cursor=db.cursor()
        columnas= persona.keys()
        valores= persona.values()
    except Exception as ex: