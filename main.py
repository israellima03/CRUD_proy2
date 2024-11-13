import PersonaDatos as per

persona ={
         "dni":"1233",
         "nombre":"Camilo",
         "edad":14,
         "apellido":"Serna",
         "direccion":"Calle 45",
         "correo":"c@c.co"
         }
res=per.save(persona)
print(res)