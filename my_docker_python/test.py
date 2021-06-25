import mariadb
import sys
def conectar():
    try:
        conn = mariadb.connect(user = "root", database ="testDB", host = "mariadb", password = "test123"
    except mariadb.error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn

con = conectar()
cur = con.cursor()
cons = 'select * from test'
cur.execute(cons)
que = cur.fetchall()
for id,name in que:
        print("id: " + str(id))
        print("nombre: " + str(name))
