from operator import contains
from queue import Empty
import mysql.connector
from tkinter import messagebox as mb

class RegistroDatos:
    def __init__ (self):
        self.conexion=mysql.connector.connect(host="localhost",user="root",
                                    passwd="",database="laboratoriohospital")
        

    def insertarPaciente(self,):
        con = self.conexion.cursor(apellido,nombre,CodTipoDoc,numeroDocumento,fechaNacimiento,nacionalidad,calle,numero,numeroDepartamento,CodBarrio,Telefono1,Telefono2,Email,CodGenero,CodSexo)
        #LOS NOMBRES DE COLUMNAS TAL CUAL COMO ESTAN EN LA BASE
        sql='''INSERT INTO Paciente (Apellido,Nombre,Numero,CodTipoDoc,NumeroDocumento,FechaNacimiento,Nacionalidad,Calle,Numero,NumeroDepartamento,CodBarrio,Telefono1,Telefono2,Email,CodGenero,CodSexo )
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(apellido,nombre,CodTipoDoc,numeroDocumento,fechaNacimiento,nacionalidad,calle,numero,numeroDepartamento,CodBarrio,Telefono1,Telefono2,Email,CodGenero,CodSexo)
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="Opcion válida",message="Datos almacenados con éxito")
        

    def mostrar(self):
        con = self.conexion.cursor()
        sql="SELECT * FROM Paciente"
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def buscarAlumno(self,Legajo_alumno):
        con = self.conexion.cursor()
        sql="SELECT * FROM Paciente where NumeroDocumento = {}".format(numeroDocumento)
        con.execute(sql)
        registroX = con.fetchall()
        con.close()
        return registroX

    def eliminarPaciente(self,dni):
        con = self.conexion.cursor()
        sql='''DELETE FROM Paciente where NumeroDocumento = {}'''.format(numeroDocumento)
        con.execute(sql)
        self.conexion.commit()
        con.close()

    def traerDni(self,numeroDocumento):
        con = self.conexion.cursor()
        sql="SELECT * FROM Paciente where NumeroDocumento = {}".format(numeroDocumento)
        con.execute(sql)
        registroX = con.fetchall()
        con.close()
        if len(registroX)>0:            
            mb.showerror(title="Opcion inválida",message="El DNI ingresado existe en la base de datos") 
            return False
        