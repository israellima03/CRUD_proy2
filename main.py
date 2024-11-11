import sqlite3
con = sqlite3.connect("crud.db")

cur = con.cursor()

valores = ("Rambo",1999,8)
res=cur.execute("SELECT * FROM peliculas where id=547")
print(res.fetchone())
