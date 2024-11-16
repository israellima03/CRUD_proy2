import PersonaDatos as per

persona = {'edad':15, 'ci': '1237', 'nombre': "Daniel", 'apellido': 'Castillo', 'direccion': 'calle', 'correo': '222@'}
res = per.find("1237")
print(res)