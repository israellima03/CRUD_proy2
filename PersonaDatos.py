import conexion as con

def save(persona):
    persona=dict(persona)
    return tuple(persona.keys())
    try:
        db = con.conectar()
        cursor=db.cursor()
        columnas= persona.keys()
        valores= persona.values()
        sql="""
        INSERT INTO personas{campos} VALUES(?,?,?,?,?,?)
        """.format(campos=columnas)
        cursor.execute(sql,(valores))
        creada=cursor.rowcount>0
        db.commit()
        if creada:
            return {"respuesta":creada,"mensaje":"Persona registrada"}
        else:
            return {"respuesta":creada,"mensaje":"No se logro registrar a la persona"}
    except Exception as ex: 
        
        return {"respuesta":False,"mensaje":str(ex)}
    finally:
        cursor.close()
        db.close()