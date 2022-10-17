from tkinter import HORIZONTAL, VERTICAL, Button, Entry, Frame, IntVar, Label, Scrollbar, StringVar, Tk, ttk
from conexion import *
from sqlite3 import Date
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkcalendar import Calendar
from unicodedata import numeric
from unittest.util import _MAX_LENGTH

class RegistroPaciente(Frame):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,*args,**kwargs)

        self.frame1 = Frame(master,text = "Datos personales",font= ("arial",12),bg="#B9FFE8" )
        self.frame1.grid(row=0,column=0,padx=40,pady=10,ipadx= 15, ipady= 15,sticky="NW")
        self.frame1.config(width=450,height=300,relief="sunken",bd=3)

        self.frame2 = Frame(master,text = "Datos de Contacto",font= ("arial",12),bg="#B9FFE8" )
        self.frame2.grid(row=0,column=1,padx=40,pady=10,ipadx= 15, ipady= 15,sticky="NW")
        self.frame2.config(width=450,height=300,relief="sunken",bd=3)

        self.frame3 = Frame(master,bg="#B9FFE8" )
        self.frame3.grid(row=1,spamcolumn=2,padx=40,pady=10,ipadx= 15, ipady= 15,sticky="NW")
        self.frame3.config(width=450,height=300,relief="sunken",bd=3)
        
        self.frame4 = Frame(master,bg="#B9FFE8" )
        self.frame4.grid(row=2,spamcolumn=2,padx=40,pady=10,ipadx= 15, ipady= 15,sticky="NW")
        self.frame4.config(width=450,height=300,relief="sunken",bd=3)
        
        self.dni =StringVar()
        self.apellido=StringVar()
        self.nombre=StringVar()
        self.fecha_nacimiento=Date()
        self.nacionalidad=StringVar()
        self.cargar_seleccion_genero=StringVar()
        self.cargar_seleccion_sexo=StringVar()
        self.calle =StringVar()
        self.altura =StringVar()
        self.departamento =StringVar()
        self.barrio =StringVar()
        self.telefono_1 =StringVar()
        self.telefono_2 =StringVar()
        self.email =StringVar()
        self.buscar=IntVar()

        self.base_datos=DataBase()
        self.create_widgets()
        
    def create_widgets(self):
    
        Label(self.frame1,text = "DNI *",width = 20,anchor="w",font= ("arial",12), bg ="#89FFD8").grid(row=0,column=0,padx=10,pady=10,ipadx= 5, ipady= 5,sticky=W )
        Label(self.frame1,text = "APELLIDO *",width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=1,column=0, padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame1,text = "NOMBRE *",width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=2,column=0,padx=10,pady=10,ipadx= 5, ipady= 5,sticky=W)
        Label(self.frame1,text = "FECHA DE NACIMIENTO *",width = 20,anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=3,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame1,text = "NACIONALIDAD *",width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=4,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame1,text = "GÉNERO *",width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=5,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame1,text = "SEXO *",width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=6,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        
        Entry(self.frame1,textvariable=self.dni,width = 30, font= ("arial",12), bg ="white"  ).grid(columnspan=2,row=0,column=1, padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame1,textvariable=self.apellido,width = 30, font= ("arial",12), bg ="white"  ).grid(columnspan=2,row=1,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame1,textvariable=self.nombre,width = 30, font= ("arial",12), bg ="white"  ).grid(columnspan=2,row=2,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame1,textvariable=self.fecha_nacimiento,width = 30, font= ("arial",12), bg ="white"  ).grid(row=3,column=2,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame1,textvariable=self.nacionalidad,width = 30, font= ("arial",12), bg ="white"  ).grid(columnspan=2,row=4,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        
        Label(self.frame2,text = "DOMICILIO *",width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=0,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame2,text = "CALLE *",width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=1,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame2,text = "ALTURA *",width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=2,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame2,text = "PISO/DPTO",width = 20, anchor="w", font= ("arial",12), bg ="#89FFD8"  ).grid(row=3,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame2,text = "BARRIO *",width = 20, anchor="w", font= ("arial",12), bg ="#89FFD8"  ).grid(row=4,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame2,text = "TELEFONO 1 *",width = 20, anchor="w", font= ("arial",12), bg ="#89FFD8"  ).grid(row=5,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame2,text = "TELEFONO 2", width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=6,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame2,text = "E-MAIL",width = 20, anchor="w",font= ("arial",12), bg ="#89FFD8"  ).grid(row=7,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Label(self.frame4,text = "( * ) Campo obligatorio",width = 20, anchor="w",font= ("arial",12), bg ="#B9FFE8"  ).place(x = 50 , y = 620)
        
        
        
        Entry(self.frame2,textvariable=self.calle,width = 30, font= ("arial",12), bg ="white").grid(row=1,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame2,textvariable=self.altura,width = 30, font= ("arial",12), bg ="white"  ).grid(row=2,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame2,textvariable=self.departamento,width = 30, font= ("arial",12), bg ="white"  ).grid(row=3,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame2,textvariable=self.barrio,width = 30, font= ("arial",12), bg ="white"  ).grid(row=4,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame2,textvariable=self.telefono_1,width = 30, font= ("arial",12), bg ="white"  ).grid(row=5,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame2,textvariable=self.telefono_2,width = 30, font= ("arial",12), bg ="white"  ).grid(row=6,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame2,textvariable=self.email,width = 30, font= ("arial",12), bg ="white"  ).grid(row=7,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)

        Button(self.frame1,width = 30, font= ("arial",12), text = "Seleccionar fecha",command = self.elegir_fecha, bg ="white").grid(row=4,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)

        Combobox(self.frame1, font= ("arial",12), values=["Femenino", "Masculino", "No Binario", "Otro"]).grid(row=5,column=1,padx=10 ,pady=10,ipadx= 5, ipady= 5)
        Combobox.bind("<<ComboboxSelected>>", self.cargar_genero)

        Combobox(self.frame1, font= ("arial",12), values=["Masculino", "Femenino", "Intersex"]).grid(row=6,column=1,padx=10 ,pady=10,ipadx= 5, ipady= 5)
        Combobox.bind("<<ComboboxSelected>>", self.cargar_sexo)

        Button(self.frame4,text = " REGISTRAR ",width = 15,height= 2,font = ("arial bold",10), command= self.agregar_datos, bg = "#00E800").grid(row=3,columnspam=2,padx=10,pady=10,ipadx= 5, ipady= 5)
        Button(self.frame4,command=self.limpiar_campos_tabla,text= 'LIMPIAR',font=('Arial bold',10),bg = "#0066FF").grid(row=1,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Button(self.frame4,command=self.eliminar_fila,text= 'ELIMINAR',font=('Arial bold',10),bg='magenta2').grid(row=1,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Button(self.frame4,command=self.buscar_dni,text= 'BUSCAR PACIENTE',font=('Arial bold',10),bg='magenta2').grid(row=0,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
        Entry(self.frame4,width = 30, font= ("arial",12), bg ="white"  ).grid(row=0,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
        Button(self.frame4,command=self.mostrar_todo,text= 'Mostrar datos de SQL',font=('Arial',10,'bold'),bg='green2').grid(columnspan=2,column=0,row=2,padx=10,pady=10,ipadx= 5, ipady= 5)
        
        ladox= Scrollbar(self.frame3, orient= HORIZONTAL,command=self.tabla.xview)
        ladox.grid(column=0,row=1,sticky='ew')
        ladoy=Scrollbar(self.frame3, orient= VERTICAL,command=self.tabla.yview)
        ladoy.grid(column=1,row=0,sticky='ns')
        
        self.tabla.configure(xscrollcommand=ladox.set,yscrollcommand=ladoy.set)
        self.tabla['columns'] = ('Apellido','Nombre','DNI','Fecha Nac.','Nacionalidad','Género','Sexo','Calle','Altura','Piso/Depto','Barrio','Teléfono 1','Teléfono 2','Email')
        
        self.tabla.column('#0',minwidth=100,width=120,anchor='center')
        self.tabla.column('Apellido',minwidth=100,width=130,anchor='center')
        self.tabla.column('Nombre',minwidth=100,width=130,anchor='center')
        self.tabla.column('DNI',minwidth=100,width=50,anchor='center')
        self.tabla.column('Fecha Nac.',minwidth=100,width=150,anchor='center')
        self.tabla.column('Nacionalidad',minwidth=100,width=150,anchor='center')
        self.tabla.column('Género',minwidth=100,width=50,anchor='center')
        self.tabla.column('Sexo',minwidth=100,width=50,anchor='center')
        self.tabla.column('Calle',minwidth=100,width=150,anchor='center')
        self.tabla.column('Altura',minwidth=100,width=150,anchor='center')
        self.tabla.column('Piso/Depto',minwidth=100,width=150,anchor='center')
        self.tabla.column('Barrio',minwidth=100,width=150,anchor='center')
        self.tabla.column('Teléfono 1',minwidth=100,width=50,anchor='center')
        self.tabla.column('Teléfono 2',minwidth=100,width=50,anchor='center')
        self.tabla.column('Email',minwidth=100,width=150,anchor='center')


        self.tabla.heading('#0',text='Legajo',anchor='center')
        self.tabla.heading('Apellido',text='Apellido',anchor='center')
        self.tabla.heading('Nombre',text='Nombre',anchor='center')
        self.tabla.heading('DNI',text='DNI',anchor='center')
        self.tabla.heading('Fecha Nac.',text='Fecha Nac.',anchor='center')
        self.tabla.heading('Nacionalidad',text='Nacionalidad',anchor='center')
        self.tabla.heading('Género',text='Género',anchor='center')
        self.tabla.heading('Sexo',text='Sexo',anchor='center')
        self.tabla.heading('Calle',text='Calle',anchor='center')
        self.tabla.heading('Altura',text='Altura',anchor='center')
        self.tabla.heading('Piso/Depto',text='Piso/Depto',anchor='center')
        self.tabla.heading('Barrio',text='Barrio',anchor='center')
        self.tabla.heading('Teléfono 1',text='Teléfono 1',anchor='center')
        self.tabla.heading('Teléfono 2',text='Teléfono 2',anchor='center')
        self.tabla.heading('Email',text='Email',anchor='center')

        
        estilo= ttk.Style(self.frame3)
        estilo.theme_use('alt')
        estilo.configure(".",font=('Arial',12,'bold'),foreground='red2')
        estilo.configure("Treeview",font=('Arial',12,'bold'),foreground='black',background='white')
        estilo.map('Treeview',background=[('selected','green2')],foreground=[('selected','black')])

        self.tabla.bind("<<TreeviewSelect>>",self.obtener_fila)    
            
    
    def agregar_datos(self):
        self.tabla.get_children()
        apellido=self.apellido.get()
        nombre=self.nombre.get()
        dni=self.dni.get()
        fecha_Nacimiento=self.cal.get_date()
        nacionalidad = self.nacionalidad.get()
        cargar_genero=self.cargar_genero.get()
        cargar_sexo=self.cargar_sexo.get()
        calle=self.calle.get()
        altura=self.altura.get()
        departamento=self.departamento.get()
        barrio=self.barrio.get()
        telefono_1=self.telefono_1.get()
        telefono_2=self.telefono_2.get()
        email=self.email.get()       
        datos = (apellido, nombre, dni,fecha_Nacimiento,nacionalidad,cargar_genero, cargar_sexo,calle,altura,departamento,barrio,telefono_1,telefono_2,email)
        if apellido and nombre and dni and fecha_Nacimiento and nacionalidad and calle and altura and barrio and telefono_1 and email and cargar_genero and cargar_sexo !='':
            dni_numerico(self,dni)
            if self.base_datos.traerDni(dni) is False:
               limpio_Dni(self)
               return
            validar_apellido(self,apellido)
            validar_nombre(self,nombre)
            self.tabla.insert('',0,text=dni, values=datos)
            self.base_datos.insertar(apellido,nombre,dni,fecha_Nacimiento,nacionalidad,cargar_genero, cargar_sexo,calle,altura,departamento,barrio,telefono_1,telefono_2,email)
            limpiar_campos(self)
        else:
            messagebox.showerror(title="Opcion inválida",message="Debe completar todos los campos que son obligatorios.")

    def limpiar_campos_tabla(self):
        self.tabla.delete(*self.tabla.get_children())
        self.dni.set('')
        self.apellido.set('')
        self.nombre.set('')
        self.fecha_nacimiento.set('')
        self.nacionalidad.set('')
        self.cargar_genero.set('')
        self.cargar_sexo.set('')
        self.calle.set('')
        self.altura.set('')
        self.departamento.set('')
        self.barrio.set('')
        self.telefono_1.set('')
        self.telefono_2.set('')
        self.email.set('')

    def buscar_dni(self):
        legajo=self.buscar.get()
        dniBuscado=self.base_datos.buscarPaciente(self.dni)
        self.tabla.delete(*self.tabla.get_children())
        i=-1
        for dato in dniBuscado:
            i=i+1 
            self.tabla.insert('',i,text=dniBuscado[i][1:2],values=dniBuscado[i][2:6])

    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro=self.base_datos.mostrar()
        i= -1
        for dato in registro:
            i=i+1
            self.tabla.insert('',i,text=registro[i][1:2], values=registro[i][2:6])
        
    def eliminar_fila(self):
        fila=self.tabla.selection()
        if len(fila)!=0:
            self.tabla.delete(fila)
            paciente = self.dniBorrar
            self.base_datos.eliminarPaciente(paciente)

    def obtener_fila(self,event):
        current_item= self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.dniBorrar = data['values'][2]
        #self.apellidoBorrar = data['values'][0]

def limpiar_campos(self):
    self.dni.set('')
    self.apellido.set('')
    self.nombre.set('')
    self.fecha_nacimiento.set('')
    self.nacionalidad.set('')
    self.cargar_genero.set('')
    self.cargar_sexo.set('')
    self.calle.set('')
    self.altura.set('')
    self.departamento.set('')
    self.barrio.set('')
    self.telefono_1.set('')
    self.telefono_2.set('')
    self.email.set('')
        
def limpio_Dni(self):
    self.dni.set('')        
        
def dni_numerico(self,dni):
        while len (dni) not in range (6, 9) or any(num.isalpha() for num in dni):
            messagebox.showerror(title="Opcion inválida",message="El campo DNI acepta sólo números.Mínimo de caracteres: 6 y máximo de caracteres: 9")
            self.dni.set('')
            dni_numerico(dni)
        else:
            dniInt = int(dni)
            return True
        
def validar_apellido(self,apellido):
    while (apellido.isspace() or len(apellido) <= 2):
        messagebox.showerror(title="Opcion inválida",message="Mínimo de carácteres en Apellido: 2 y no debe comenzar con un espacio")
        self.apellido.set('')
        validar_apellido(apellido)
    else:
        return True

def validar_nombre(self,nombre):
    while (nombre.isspace() or len(nombre) <= 1):
        messagebox.showerror(title="Opcion inválida",message="Mínimo de carácteres en Nombre: 3 y no debe comenzar con un espacio")
        self.nombre.set('')
        validar_nombre(nombre)
    else:
        return True

def validar_calle(self,calle):
    while (calle.isspace() or len(calle) <= 2):
        messagebox.showerror(title="Opcion inválida",message="Mínimo de carácteres en Calle: 2 y no debe comenzar con un espacio")
        self.calle.set('')
        validar_calle(calle)
    else:
        return True

def altura_numero(self,altura):
    while len (altura) not in range (1, 6) or any(num.isalpha() for num in altura):
        messagebox.showerror(title="Opcion inválida",message="El campo Altura acepta sólo números.Mínimo de caracteres: 1 y máximo de caracteres: 6")
        self.altura.set('')
        altura_numero(altura)
    else:
        altura1Int = int(altura)
        return True

def validar_nombre_barrio(self,barrio):
    while (barrio.isspace() or len(barrio) <= 1):
        messagebox.showerror(title="Opcion inválida",message="Mínimo de carácteres en Barrio: 3 y no debe comenzar con un espacio")
        self.barrio.set('')
        validar_nombre_barrio(barrio)
    else:
        return True

def telefono1(self,telefono_1):  #? ver nombre que acompania al self
    while len (telefono_1) not in range (1, 12) or any(num.isalpha() for num in telefono_1):
        messagebox.showerror(title="Opcion inválida",message="El campo Telefono 1 acepta sólo números.Mínimo de caracteres: 1 y máximo de caracteres: 12")
        self.telefono_1.set('')
        altura_numero(telefono_1)
    else:
        telefono1Int = int(telefono1)
        return True

def telefono2(self,telefono_2):
    while len (telefono_2) not in range (1, 12) or any(num.isalpha() for num in telefono_2):
        messagebox.showerror(title="Opcion inválida",message="El campo Telefono 2 acepta sólo números.Mínimo de caracteres: 1 y máximo de caracteres: 12")
        self.telefono_2.set('')
        altura_numero(telefono_2)
    else:
        telefono2Int = int(telefono2)
        return True    
    
# def cargar_sexo(event):
#     selection = elegir_sexo.get()
#     messagebox.showinfo(title="Nuevo elemento seleccionado",message=selection)
    
# def cargar_genero(event):
#     selection = elegir_genero.get()
#     messagebox.showinfo(title="Nuevo elemento seleccionado",message=selection)
    
def elegir_fecha():  
    ventana_fecha = Tk()
    ventana_fecha.title("Fecha de nacimiento") 
    ventana_fecha.geometry("400x400") 
    cal = Calendar(ventana_fecha, selectmode = 'day', year = 2020, month = 5, day = 22)  
    cal.pack(pady = 20) 
    def grad_date(): 
        fecha_nacimiento.config(text = "La fecha seleccionada es: " + cal.get_date()) 
    Button(ventana_fecha, text = "Obtener fecha", 
        command = grad_date).pack(pady = 20) 
    fecha_nacimiento = Entry(self.frame1,textvariable=fecha_nacimiento,width = 30, font= ("arial",12), bg ="white"  ).grid(row=3,column=2,padx=10,pady=10,ipadx= 5, ipady= 5)  
    ventana_fecha.mainloop()
    

def main():
    ventana = Tk()
    ventana.title("REGISTRO DE PACIENTE")
    width= ventana.winfo_screenwidth() 
    height= ventana.winfo_screenheight() 
    ventana.geometry("%dx%d" % (width, height))
    ventana.resizable(width=False, height=False) 
    ventana.config(bg="#B9FFE8")
    app= RegistroPaciente(ventana)
    app.mainloop()

if __name__ =="__main__":
    main()        