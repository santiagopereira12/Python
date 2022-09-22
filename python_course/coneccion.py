from ast import Try
from logging import exception
import pymysql

class dataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='prueba_python'
        )

        self.cursor = self.connection.cursor()
        print("conexion exitosa")
    
    def seleccionar_usuario(self, id):
        sql = 'SELECT nombre, apellidos, numero_documento FROM usuarios WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            #print ("ID:", user[0])
            print ("Username: ", user[0])
            print ("Lastname: ", user[1])
            print ("Document: ", user[2])
        except exception as e:
            raise

    def seleccionar_tabla(self):
        sql = 'SELECT * FROM usuarios'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            for user in users:
                print ("Username: ", user[1])
                print ("Lastname: ", user[2])
                print ("Document: ", user[3])
                print("_____________\n")
        except exception as e:
            raise
    
    def update_User(self, id , tip_doc):
        sql = "UPDATE usuarios SET numero_documento='{}' WHERE id='{}'".format(tip_doc, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except exception as e:
            raise

    def close(self):
        self.connection.close()

data = dataBase()
data.seleccionar_usuario(2)

data.update_User(2, '1007532984')

data.seleccionar_usuario(2)

data.close()