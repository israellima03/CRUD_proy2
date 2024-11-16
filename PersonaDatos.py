import conexion as con

def save(persona):

    persona=dict(persona)
    try:
        db = con.conectar()
        cursor=db.cursor()
        columnas= tuple(persona.keys())
        valores= tuple(persona.values())
        sql="""
        INSERT INTO personas{campos} VALUES(?,?,?,?,?,?)
        """.format(campos=columnas)
        cursor.execute(sql,(valores))
        creada=cursor.rowcount>0
        db.commit()
        if creada:
            cursor.close()
            db.close()
            return {"respuesta":creada,"mensaje":"Persona registrada"}
        else:
            cursor.close()
            db.close()
            return {"respuesta":creada,"mensaje":"No se logro registrar a la persona"}
    except Exception as ex: 
        if "UNIQUE" in str(ex) and "correo" in str (ex):
            mensaje = "Ya existe una persona con ese correo"
        elif "UNIQUE" in str(ex) and "ci" in str (ex): 
            mensaje = "Ya existe una persona con ese ci"
        else:
            mensaje = str(ex)
        cursor.close()
        db.close()    
        return {"respuesta":False,"mensaje": mensaje}

def findAll():
    try:
        db = con.conectar()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM personas")
        personas = cursor.fetchall()
        if personas:
            cursor.close()
            db.close()
            return {"respuesta":True,"personas":personas,"mensaje":"Listado OK"}
        else:
            cursor.close()
            db.close()
            return {"respuesta":False,"personas":personas,"mensaje":"No hay personas registradas"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta":False,"mensaje":str(ex)}
    
def find(ciPersona):
    try:
        db = con.conectar()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM personas WHERE ci='{ci}'".format(ci = ciPersona))
        res = cursor.fetchall()
        if res:
            info=res[0]
            persona = {"id":info[0],"ci":info[1],"edad":info[2],"nombre":info[3],"apellido":info[4],"direccion":info[5],"correo":info[6]}
            cursor.close()
            db.close()
            return {"respuesta":True,"persona":persona,"mensaje":"Persona encontrada"}
        else:
            cursor.close()
            db.close()
            return {"respuesta":False,"mensaje":"No existe la persona"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta":False,"mensaje":str(ex)}
    
def update(persona):
    try:
        db=con.conectar()
        cursor=db.cursor()
        persona=dict(persona)
        ciPersona=persona.get('ci')
        persona.pop('ci')
        valores = tuple(persona.values())
        sql ="""
        UPDATE personas
        SET edad=?,nombre=?,apellido=?,direccion=?,correo=?
        WHERE ci={ci}
        """.format(ci=ciPersona)
        cursor.execute(sql,(valores))
        modificada = cursor.rowcount>0
        db.commit()
        cursor.close()
        db.close()
        if modificada:
            return {"respuesta":modificada,"mensaje":"Persona actualizada"}
        else:
            cursor.close()
            db.close()
            return {"respuesta":modificada,"mensaje":"No existe la persona con ese ci"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta":False,"mensaje":str(ex)}