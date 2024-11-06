import sqlite3
con = sqlite3.connect("crud.db")

cur = con.cursos()
cur.execute("""
CREATE TABLE peliculas(id INT PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            anio INTEGER, puntacion INTEGER)""")