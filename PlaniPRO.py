
from tkinter import Button, Entry, Frame, Label, PhotoImage, Scrollbar, Tk, messagebox
from tkinter.constants import END
from tkinter.ttk import Treeview, Style, Combobox
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tkcalendar import Calendar
from dni import search
from sql import select, insert, update, delete

class App(Tk):

    def __init__(self):
        super(App, self).__init__()  
      
        # Creamos la ventana principal
        self.title     ('PlaniPRO')
        self.geometry  ('1100x600+-8+0')
        self.resizable (0,0)     
        self.iconbitmap('./img/0.ico')  

        # Modificamos estilo de los diferentes widgets
        self.option_add('*Font', ('Segoe UI Semibold', '10'))   
        self.option_add('*Button*Font', ('Segoe UI Semibold', '8'))  
        self.option_add('*Button*BorderWidth', 0)  
        self.option_add('*Button*Cursor', 'hand2')         
        self.option_add('*Button*TakeFocus', False) 
        self.option_add('*Entry*relief', 'flat')        
        self.option_add('*Treeview*SelectMode', 'browse') 
        self.option_add('*Treeview*Show', 'tree') 
        self.option_add('*Treeview*padding', -1) 
        self.option_add('*Treeview*TakeFocus', False)  
        self.option_add('*Label*Foreground', '#5B5857')  

        # Modificados estilo de los treeview
        Style().configure('Treeview', background='#F0F0F0', font=('Segoe UI Semibold', 10)) 

        # Cargamos las imagenes de los botones
        img1 = PhotoImage(file='./img/1.png')
        img2 = PhotoImage(file='./img/2.png')
        img3 = PhotoImage(file='./img/3.png')
        img4 = PhotoImage(file='./img/4.png')
        img5 = PhotoImage(file='./img/5.png')        
        img6 = PhotoImage(file='./img/6.png')

        # Creamos los botones del menu  
        self.btn1 = Button(self, image=img1, command=self.Menu1)
        self.btn2 = Button(self, image=img2, command=self.Menu2)
        self.btn3 = Button(self, image=img3, )
        self.btn4 = Button(self, image=img4, )
        self.btn5 = Button(self, image=img5, )
        self.btn6 = Button(self, image=img6, )

        # Posicionamos los botones
        self.btn1.place(       width=100, height=100)        
        self.btn2.place(y=100, width=100, height=100)       
        self.btn3.place(y=200, width=100, height=100)          
        self.btn4.place(y=300, width=100, height=100)             
        self.btn5.place(y=400, width=100, height=100)         
        self.btn6.place(y=500, width=100, height=100)

        # Remuneracion minima vital RMV
        self.rmv = 1025

        # Variable global para el control de los menus
        self.menu = 0
            
        # Corremos programa
        self.mainloop()  
         

    def BloquearBotones(self):
        
        # Activar y desactivar botones del menu
        if self.menu == 0:
            self.btn1.configure(state='disabled')
            self.btn2.configure(state='disabled')
            self.btn3.configure(state='disabled')
            self.btn4.configure(state='disabled')
            self.btn5.configure(state='disabled')
            self.btn6.configure(state='disabled') 

        else:
            self.btn1.configure(state='normal')
            self.btn2.configure(state='normal')
            self.btn3.configure(state='normal')
            self.btn4.configure(state='normal')
            self.btn5.configure(state='normal')
            self.btn6.configure(state='normal')                     

                 
    def Menu1(self):  
        
        # desactivamos los botones
        self.BloquearBotones()
        
        # activamos el boton
        self.btn1.configure(state='normal')
        
        # Validacion para destruir el menu si esta activo
        if self.menu == 1: 

            self.men1.destroy()      
            self.menu = 0

            return
        
        # Asignamos el numero de menu activo
        self.menu = 1
               
        # Creamos la ventana principal
        menu = Frame(self, bg='#FFFFFF')  
        
        # Creamos encabezados de treeview
        Label(menu, text='N°'                ).place(x= 15, y=15, width= 30, height=30)
        Label(menu, text='APELLIDOS Y NOMBRE').place(x= 45, y=15, width=280, height=30)
        Label(menu, text='DNI'               ).place(x=325, y=15, width= 82, height=30)
    
        # Creamos el treeview
        self.tre1 = Treeview(menu, columns=('#1','#2','#3'))
        self.tre1.column('#0', width=  0)
        self.tre1.column('#1', width= 30)
        self.tre1.column('#2', width=270)
        self.tre1.column('#3', width= 90)  
            
        # Creamos el scrollbar              
        scroll = Scrollbar(menu, orient='vertical', command=self.tre1.yview)
        self.tre1.configure(yscrollcommand=scroll.set)  
        
        # Posicionamos el treeview y scrollbar
        self.tre1.place(x= 15, y=45, height=520)
        scroll.place   (x=409, y=15, height=550)  
        
        # Evento de seleccion en treeview
        self.tre1.bind('<<TreeviewSelect>>', self.MostrarDetalles)
    
        # Creamos cuadros para mostar detalles de los trabajadores
        Label(menu, text=' Fecha de Nacimiento'    , anchor='nw').place(x=437, y= 15, width=200, height=54)
        Label(menu, text=' Fecha de Ingreso'       , anchor='nw').place(x=437, y= 70, width=200, height=54)
        Label(menu, text=' Planilla'               , anchor='nw').place(x=437, y=125, width=200, height=54)
        Label(menu, text=' Asignacion Familiar'    , anchor='nw').place(x=437, y=180, width=200, height=54)
        Label(menu, text=' Movilidad'              , anchor='nw').place(x=437, y=235, width=200, height=54)
        Label(menu, text=' Sueldo Total'           , anchor='nw').place(x=437, y=290, width=200, height=54)
        Label(menu, text=' Cargo Laboral'          , anchor='nw').place(x=437, y=345, width=200, height=54)
        Label(menu, text=' Cuenta Bancaria'        , anchor='nw').place(x=437, y=400, width=200, height=54)
        Label(menu, text=' Entidad Pensionaria'    , anchor='nw').place(x=437, y=455, width=200, height=54)
        Label(menu, text=' Tipo de Comision S.P.P' , anchor='nw').place(x=437, y=510, width=200, height=55)
        Label(menu, text=' Categoria de Licencia'  , anchor='nw').place(x=638, y= 15, width=200, height=54)
        Label(menu, text=' Vencimiento de Licencia', anchor='nw').place(x=638, y= 70, width=200, height=54)
        Label(menu, text=' Area de Labor'          , anchor='nw').place(x=638, y=125, width=200, height=54)
        Label(menu, text=' Numero de Celular'      , anchor='nw').place(x=638, y=180, width=200, height=54)
        Label(menu, text=' Distrito'               , anchor='nw').place(x=638, y=235, width=200, height=54)
        Label(menu, text=' Edad'                   , anchor='nw').place(x=638, y=290, width=200, height=54)
        Label(menu, text=' Tiempo'                 , anchor='nw').place(x=638, y=345, width=200, height=54)
        Label(menu, text=' Entidad Bancaria'       , anchor='nw').place(x=638, y=400, width=200, height=54)
        Label(menu, text=' C.U.S.P.P.'             , anchor='nw').place(x=638, y=455, width=200, height=54)
        Label(menu, text=' Fecha de Baja'          , anchor='nw').place(x=638, y=510, width=200, height=55)
            
        # Creamos los textos que mostraran los detalles
        self.naci = Label(menu, fg='#000000', anchor='e')
        self.ingr = Label(menu, fg='#000000', anchor='e')
        self.plan = Label(menu, fg='#000000', anchor='e')
        self.asig = Label(menu, fg='#000000', anchor='e')
        self.movi = Label(menu, fg='#000000', anchor='e')
        self.suel = Label(menu, fg='#000000', anchor='e')
        self.carg = Label(menu, fg='#000000', anchor='e')
        self.cuen = Label(menu, fg='#000000', anchor='e')
        self.apor = Label(menu, fg='#000000', anchor='e')        
        self.comi = Label(menu, fg='#000000', anchor='e')
        self.lice = Label(menu, fg='#000000', anchor='e')
        self.venc = Label(menu, fg='#000000', anchor='e')
        self.area = Label(menu, fg='#000000', anchor='e')
        self.celu = Label(menu, fg='#000000', anchor='e')
        self.dist = Label(menu, fg='#000000', anchor='e')
        self.edad = Label(menu, fg='#000000', anchor='e')
        self.tiem = Label(menu, fg='#000000', anchor='e')
        self.banc = Label(menu, fg='#000000', anchor='e')
        self.cusp = Label(menu, fg='#000000', anchor='e')
        self.cese = Label(menu, fg='#000000', anchor='e')       
        
        # Posicionamos los textos de los detalles
        self.naci.place(x=448, y= 40, width=184) 
        self.ingr.place(x=448, y= 95, width=184)
        self.plan.place(x=448, y=150, width=184)
        self.asig.place(x=448, y=205, width=184)    
        self.movi.place(x=448, y=260, width=184)
        self.suel.place(x=448, y=315, width=184)
        self.carg.place(x=448, y=370, width=184)
        self.cuen.place(x=448, y=425, width=184) 
        self.apor.place(x=448, y=480, width=184)        
        self.comi.place(x=448, y=535, width=184)
        self.lice.place(x=649, y= 40, width=184)
        self.venc.place(x=649, y= 95, width=184)    
        self.area.place(x=649, y=150, width=184)
        self.celu.place(x=649, y=205, width=184)
        self.dist.place(x=649, y=260, width=184)
        self.edad.place(x=649, y=315, width=184) 
        self.tiem.place(x=649, y=370, width=184)
        self.banc.place(x=649, y=425, width=184)
        self.cusp.place(x=649, y=480, width=184) 
        self.cese.place(x=649, y=535, width=184)   
                  
        # Creamos los botones principales
        Button(menu, text='AGREGAR'  , command= lambda: self.Agregar('agregar')).place(x=875, y= 15, width=90, height=30)     
        Button(menu, text='MODIFICAR', command=self.Modificar                  ).place(x=875, y= 50, width=90, height=30)
        Button(menu, text='ELIMINAR' , command=self.Eliminar                   ).place(x=875, y= 85, width=90, height=30)        
        
        # Cargamos datos al treeview
        self.MostrarDatos()
        
        # Posicionamos la ventana principal
        menu.place(x=110, y=10, width=980, height=578) 
        
        # Asignamos variable para poder destruir la ventana
        self.men1 = menu
       
    def Agregar(self, accion):   

        # Preguntamos si desea agregar un nuevo trabajador
        if accion == 'agregar':

            respuesta = messagebox.askyesno('AGREGAR','Estas seguro de agregar un trabajador ?', icon = 'warning', default='no')       
            
            if not respuesta:
                
                return 

        # Creamos la ventana principal
        menu = Frame(self.men1, background='#FFFFFF')  
        
        # Creamos los campos de cada detalle
        Label(menu, text='  Buscar Dni'         , anchor='nw').place(x=  0, y=  0, width=200, height=54)
        Label(menu, text='  Numero Dni'         , anchor='nw').place(x=  0, y= 55, width=200, height=54)
        Label(menu, text='  Apellido Paterno'   , anchor='nw').place(x=  0, y=110, width=200, height=54)
        Label(menu, text='  Apellido Materno'   , anchor='nw').place(x=  0, y=165, width=200, height=54)
        Label(menu, text='  Nombres'            , anchor='nw').place(x=  0, y=220, width=200, height=54)
        Label(menu, text='  Fecha de Nacimiento', anchor='nw').place(x=  0, y=275, width=200, height=54)
        Label(menu, text='  Fecha de Ingreso'   , anchor='nw').place(x=  0, y=330, width=200, height=54)
        Label(menu, text='  Planilla'           , anchor='nw').place(x=  0, y=385, width=200, height=54)
        Label(menu, text='  A. Fam.'            , anchor='nw').place(x= 62, y=385)
        Label(menu, text='  Movili.'            , anchor='nw').place(x=123, y=385)
        Label(menu, text='  Cargo Laboral'      , anchor='nw').place(x=  0, y=440, width=200, height=54)
        Label(menu, text='  Cuenta Bancaria'    , anchor='nw').place(x=  0, y=495, width=200, height=55)
        Label(menu, text='  Entidad Pensio.'    , anchor='nw').place(x=201, y=  0, width=200, height=54)
        Label(menu, text='  Comision'           , anchor='nw').place(x=312, y=  0)
        Label(menu, text='  Codigo Unico S.P.P.', anchor='nw').place(x=201, y= 55, width=200, height=54)
        Label(menu, text='  Licencia'           , anchor='nw').place(x=201, y=110, width=200, height=54)
        Label(menu, text='  Vencimi.'           , anchor='nw').place(x=265, y=110)
        Label(menu, text='  Cod.'               , anchor='nw').place(x=351, y=110)
        Label(menu, text='  Area'               , anchor='nw').place(x=201, y=165, width=200, height=54)
        Label(menu, text='  Celular'            , anchor='nw').place(x=297, y=165)
        Label(menu, text='  Distrito'           , anchor='nw').place(x=201, y=220, width=200, height=54)
        Label(menu, text='  Fecha de Baja'      , anchor='nw').place(x=201, y=275, width=200, height=54)
                
        # Creamos los cuadros para escribir los detalles
        self.busc = Button(menu, text='BUSCAR', bg='#88C7FF', command=self.BuscarDni)
        self.bdni = Entry(menu)     
        self.ndni = Label(menu, bg='#FFFFFF', fg='#000000', anchor='w')        
        self.apat = Label(menu, bg='#FFFFFF', fg='#000000', anchor='w')
        self.amat = Label(menu, bg='#FFFFFF', fg='#000000', anchor='w')
        self.nomb = Label(menu, bg='#FFFFFF', fg='#000000', anchor='w')
        self.fnac = Entry(menu)
        self.fing = Entry(menu)
        self.spla = Entry(menu)        
        self.afam = Combobox(menu, state='readonly', values=['SI', 'NO'])       
        self.smov = Entry(menu)
        self.plab = Combobox(menu, state='readonly', values=['INSPECTOR VIAL', 'OP. DE GRUA LIVIANA', 'OP. DE GRUA PESADA'])       
        self.ncue = Entry(menu)
        self.eapo = Combobox(menu, state='readonly', values=['ONP', 'HABITAT', 'INTEGRA', 'PRIMA', 'PROFUTURO',''])
        self.ecom = Combobox(menu, state='disable' , values=['FLUJO', 'MIXTA'])
        self.ecus = Entry(menu, state='disable')
        self.cate = Combobox(menu, state='readonly', values=['AI', 'AIIA', 'AIIB', 'AIIIA', 'AIIIB', 'AIIIC', ''])       
        self.fven = Entry(menu, state='disable')
        self.codi = Entry(menu, state='disable')
        self.alab = Combobox(menu, state='readonly', values=['SUR', 'NORTE', 'TALLER', 'OFICINA'])       
        self.ncel = Entry(menu)
        self.dres = Combobox(menu, state='readonly', values=['ANCON', 'ATE VITARTE', 'CARABAYLLO', 'CHORRILLOS', 'COMAS', 'LOS OLIVOS', 
                                                            'LURIGANCHO', 'LURIN', 'PUCUSANA', 'PUENTE PIEDRA', 'RIMAC', 'SAN BARTOLO',
                                                            'SAN JUAN DE LURIGANCHO', 'SAN JUAN DE MIRAFLORES', 'SAN MARTIN DE PORRES', 
                                                            'SANTA ANITA', 'SANTIAGO DE SURCO', 'SURQUILLO', 'VILLA EL SALVADOR', 'VILLA MARIA DEL TRIUNFO'])      
        self.fces = Entry(menu)
                
        # Evento al seleccionar item del combobox
        self.eapo.bind('<<ComboboxSelected>>', self.CambioAporte) 
        self.cate.bind('<<ComboboxSelected>>', self.CambioLicencia)    

        # Posicionamos los cuadros de los detalles
        self.busc.place(x=136, y= 23, width= 54, height=24)    
        self.bdni.place(x= 10, y= 23, width=120, height=24)    
        self.ndni.place(x= 10, y= 78, width=180, height=24)
        self.apat.place(x= 10, y=133, width=180, height=24)
        self.amat.place(x= 10, y=188, width=180, height=24)
        self.nomb.place(x= 10, y=243, width=180, height=24)        
        self.fnac.place(x= 10, y=298, width=180, height=24)        
        self.fing.place(x= 10, y=353, width=180, height=24)
        self.spla.place(x= 10, y=408, width= 56, height=24)  
        self.afam.place(x= 72, y=408, width= 56, height=24)      
        self.smov.place(x=134, y=408, width= 56, height=24) 
        self.plab.place(x= 10, y=463, width=180, height=24)        
        self.ncue.place(x= 10, y=518, width=180, height=24)
        self.eapo.place(x=211, y= 23, width=105, height=24) 
        self.ecom.place(x=322, y= 23, width= 69, height=24) 
        self.ecus.place(x=211, y= 78, width=180, height=24)
        self.cate.place(x=211, y=133, width= 58, height=24)
        self.fven.place(x=275, y=133, width= 80, height=24)
        self.codi.place(x=361, y=133, width= 30, height=24)
        self.alab.place(x=211, y=188, width= 90, height=24)
        self.ncel.place(x=307, y=188, width= 84, height=24)
        self.dres.place(x=211, y=243, width=180, height=24)
        self.fces.place(x=211, y=298, width=180, height=24)         
            
        # Creamos los botones principales
        Button(menu, text='GRABAR', command=self.Grabar                      ).place(x=438, y= 0, width=90, height=30)     
        Button(menu, text='SALIR' , command= lambda: self.men1_agre.destroy()).place(x=438, y=35, width=90, height=30)

        # Posicionamos la ventana principal
        menu.place(x=437, y=15, width=528, height=550)
        
        # Foco en cuadro de busqueda y Superponemos la ventana principal
        self.bdni.focus_set()
        menu.grab_set()

        # Asignamos variable para poder destruir la ventana
        self.men1_agre = menu
           
    def Modificar(self):        
        
        # Preguntamos si desea modificar los datos del trabajador
        if self.tre1.selection():

            respuesta = messagebox.askyesno('MODIFICAR','Estas seguro de modificar los datos de este trabajador ?', icon = 'warning', default='no')       
            
            if respuesta: 
                
                # Obtener id del trabajador           
                id = int(self.tre1.item(self.tre1.focus()).get('text'))

                # Obtenemos sus datos
                datos = select(f'SELECT * FROM ACTIVO WHERE ID = {id}', False)

                # Abrimos el menu de registro
                self.Agregar('modificar')     

                # Desactivamos la opcion de buscar dni
                self.bdni.configure(state='disabled')
                self.busc.configure(state='disabled')

                # Ingresamos los datos del trabajador en los cuadros
                self.ndni['text'] = datos[1]
                self.apat['text'] = datos[2]
                self.amat['text'] = datos[3]
                self.nomb['text'] = datos[4]
                self.fnac.insert(0, datos[5])
                self.fing.insert(0, datos[6])
                self.spla.insert(0, datos[7])
                self.eapo.set(datos[10])
                self.plab.set(datos[13])
                self.ncue.insert(0, datos[14])                
                self.alab.set(datos[15])
                self.ncel.insert(0, datos[19])
                self.dres.set(datos[20])
                self.fces.insert(0, datos[21])

                if datos[8] == 0:
                    self.afam.set('NO')
                else:
                    self.afam.set('SI')

                if datos[9] > 0:
                    self.smov.insert(0, datos[9])      
                
                if len(datos[10]) > 3:                
                    self.ecom.configure(state='readonly')
                    self.ecom.set(datos[11])
                    self.ecus.configure(state='normal')                     
                    self.ecus.insert(0, datos[12])
                
                if datos[16] != '':
                    self.codi.configure(state='normal')
                    self.codi.insert(0, datos[16][:1])
                    self.fven.configure(state='normal')
                    self.fven.insert(0, datos[17])
                    self.cate.set(datos[18])

        else:
            messagebox.showinfo('Modificar', 'Debes Seleccionar un Trabajador !', icon = 'warning')  
        
    def Eliminar(self):  

        # Ejecutar codigo si hay seleccion y se acepta el cuadro de dialogo
        if self.tre1.selection():

            respuesta = messagebox.askyesno('ELIMINAR','Estas seguro de eliminar a este trabajador ?', icon = 'warning', default='no')       
            
            if respuesta: 
                
                # Tomamos la seleccion del treeview para capturar el ID del trabajador                
                id = int(self.tre1.item(self.tre1.focus()).get('text'))    

                # Si hay fecha de cese copiar datos a tabla de cesados
                if self.cese['text'] != '':
                    insert(f'INSERT INTO CESADO SELECT * FROM ACTIVO WHERE ID = {id}')                   

                # Ejecutamos la consulta sql de eliminacion
                delete(f'DELETE FROM ACTIVO WHERE ID = {id}', True)   
                
                # Llamamos a la funcion de limpiar datos de informacion
                self.BorrarDetalles()             
                
                # Cargamos nuevamente los datos al treeview
                self.MostrarDatos()   

        else:
            messagebox.showinfo('Eliminar', 'Debes Seleccionar un Trabajador !', icon = 'warning')                      
        
    def MostrarDatos(self):
        
        # Limpiamos el treeview
        self.tre1.delete(*self.tre1.get_children())
        
        # Buscamos datos en la base de datos
        datos = select('SELECT * FROM ACTIVO', True)

        # Registramos datos en el treeview
        for index, dato in enumerate(datos, 1):

            nombre = f'{dato[2]} {dato[3]} {dato[4]}'    
            self.tre1.insert('', END, text=dato[0], values=(index, nombre, dato[1]))   
    
    def BorrarDetalles(self):

            # Limpiamos los cuadros de informacion del menu1
            self.naci['text'] = ''
            self.ingr['text'] = ''
            self.plan['text'] = ''
            self.asig['text'] = ''
            self.movi['text'] = ''
            self.suel['text'] = ''
            self.carg['text'] = ''
            self.cuen['text'] = ''
            self.apor['text'] = ''            
            self.comi['text'] = ''
            self.lice['text'] = ''
            self.venc['text'] = ''
            self.area['text'] = ''
            self.celu['text'] = ''
            self.dist['text'] = ''
            self.edad['text'] = ''
            self.tiem['text'] = ''
            self.banc['text'] = ''
            self.cusp['text'] = ''
            self.cese['text'] = ''
     
    def BuscarDni(self):
      
        # Validamos el dni ingresado
        if self.bdni.get() == '':
            messagebox.showinfo('BUSCAR', 'Registra el dni del trabajador !', icon = 'warning')    
            self.bdni.focus()       
        elif len(self.bdni.get()) != 8: 
            messagebox.showinfo('BUSCAR', 'Registra correctamente el dni del trabajador !', icon = 'warning') 
            self.bdni.focus()
        elif not self.bdni.get().isdigit(): 
            messagebox.showinfo('BUSCAR', 'Registra correctamente el dni del trabajador !', icon = 'warning') 
            self.bdni.focus()
        else:

            dni = self.bdni.get()
            persona = search(dni)

            # Si encuentra datos extraer a los textbox
            if persona != None:
                self.ndni['text'] = persona['numeroDocumento']
                self.apat['text'] = persona['apellidoPaterno']
                self.amat['text'] = persona['apellidoMaterno']
                self.nomb['text'] = persona['nombres']
                
                self.bdni.delete(0, END)   
                self.fnac.focus_set()                
                
            # Si no encuentra enviar mensaje de aviso
            else:                
                messagebox.showinfo('BUSCAR', 'El numero de Dni ingresado no existe !', icon = 'warning')           
                self.bdni.focus()   
        
    def Grabar(self):                
        
        # Validacion de dni
        if self.ndni['text'] == '':    
            messagebox.showinfo('GRABAR', 'Busca los datos del trabajador !', icon = 'warning')            
            self.bdni.focus()                      

        # Validacion de fecha de nacimiento
        elif self.fnac.get() == '':
            messagebox.showinfo('GRABAR', 'Registra la fecha de nacimiento !', icon = 'warning')  
            self.fnac.focus()
        elif len(self.fnac.get()) != 10:
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')  
            self.fnac.focus()
        elif not self.fnac.get().replace('/','').isdigit() or len(self.fnac.get().replace('/','')) != 8:
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                     
            self.fnac.focus()
        elif self.fnac.get()[2] != '/' or self.fnac.get()[5] != '/':
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                      
            self.fnac.focus()
        elif int(self.fnac.get()[6:10]) < (datetime.today().year - 100):                               
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                         
            self.fnac.focus()    
        elif int(self.fnac.get()[6:10]) > (datetime.today().year - 18):                               
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                            
            self.fnac.focus()  
        else:            
            try:                  
                datetime.strptime(self.fnac.get() , '%d/%m/%Y')                                                                                             
            except ValueError:
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                                 
                self.fnac.focus()        
                return

            # Validacion de fecha de ingreso                          
            if self.fing.get() == '':
                messagebox.showinfo('GRABAR', 'Registra la fecha de ingreso !', icon = 'warning') 
                self.fing.focus()
            elif len(self.fing.get()) != 10:
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')  
                self.fing.focus()
            elif not self.fing.get().replace('/','').isdigit() or len(self.fing.get().replace('/','')) != 8:
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')                             
                self.fing.focus()
            elif self.fing.get()[2] != '/' or self.fing.get()[5] != '/':
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')                          
                self.fing.focus()
            elif int(self.fing.get()[6:10]) < (datetime.today().year - 50):                                
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')                              
                self.fing.focus()                                                          
            else:                
                try:                  
                    datetime.strptime(self.fing.get() , '%d/%m/%Y')                                                                                             
                except ValueError:
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')                             
                    self.fnac.focus()        
                    return

                # Validacion de sueldo planilla   
                if self.spla.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la remuneracion de la planilla !', icon = 'warning')  
                    self.spla.focus()
                elif not self.spla.get().isdigit(): 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la remuneracion de la planilla !', icon = 'warning')   
                    self.spla.focus()
                elif int(self.spla.get()) <=0: 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la remuneracion de la planilla !', icon = 'warning')  
                    self.spla.focus()
                    
                # Validacion de asignacion familiar
                elif self.afam.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la asignacion familiar !', icon = 'warning')  
                    self.afam.focus()
                    
                # Validacion de movilidad
                elif self.smov.get() != '' and not self.smov.get().isdigit():
                    messagebox.showinfo('GRABAR', 'Registra correctamente la remuneracion de la movilidad !', icon = 'warning')  
                    self.smov.focus()
                elif self.smov.get() != '' and int(self.smov.get()) <=0: 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la remuneracion de la movilidad !', icon = 'warning')  
                    self.smov.focus()
                    
                # Validacion de cargo laboral
                elif self.plab.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra el cargo laboral !', icon = 'warning')  
                    self.plab.focus()  

                # Validacion de cuenta bancaria                              
                elif self.ncue.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la cuenta bancaria !', icon = 'warning')  
                    self.ncue.focus()
                elif len(self.ncue.get()) != 14 and len(self.ncue.get()) != 20: 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la cuenta bancaria !', icon = 'warning')  
                    self.ncue.focus()
                elif not self.ncue.get().isdigit(): 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la cuenta bancaria !', icon = 'warning')  
                    self.ncue.focus()
                    
                # Validacion de entidad de aportacion
                elif self.eapo.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la entidad pensionaria !', icon = 'warning')  
                    self.eapo.focus()

                # Validacion de comision de la entidad de aportacion     
                elif self.ecom.state()[0] == 'readonly' and self.ecom.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la comision de la entidad pensionaria !', icon = 'warning')                                          
                    self.ecom.focus()
                elif self.ecom.state()[0] == 'focus' and self.ecom.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la comision de la entidad pensionaria !', icon = 'warning')                                            
                    self.ecom.focus()                                            
               
                # Validacion del cusp de la entidad de aportacion     
                elif self.ecus.get() != '' and len(self.ecus.get()) != 12:
                    messagebox.showinfo('GRABAR', 'Registra correctamente el cusp de la entidad pensionaria !', icon = 'warning')                                           
                    self.ecus.focus()
                elif self.ecus.get() != '' and not self.ecus.get().isalnum():
                    messagebox.showinfo('GRABAR', 'Registra correctamente el cusp de la entidad pensionaria !', icon = 'warning')                                      
                    self.ecus.focus()               
                                     
                # Validacion de vencimiento de la licencia de conducir
                elif self.cate.get() != '' and self.fven.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la fecha de revalidacion de la licencia !', icon = 'warning')                                          
                    self.fven.focus()    
                elif self.fven.get() != '' and len(self.fven.get()) != 10:
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                                    
                    self.fven.focus()  
                elif self.fven.get() != '' and not self.fven.get().replace('/','').isdigit():
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                        
                    self.fven.focus()
                elif self.fven.get() != '' and len(self.fven.get().replace('/','')) != 8:
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                       
                    self.fven.focus()    
                elif self.fven.get() != '' and self.fven.get()[2] != '/':
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                         
                    self.fven.focus()
                elif self.fven.get() != '' and self.fven.get()[5] != '/':
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                        
                    self.fven.focus()
                elif self.fven.get() != '' and int(self.fven.get()[6:10]) < (datetime.today().year - 100):                               
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                           
                    self.fven.focus()    
                else:
                    if self.cate.get() != '':
                        try:                  
                            datetime.strptime(self.fven.get() , '%d/%m/%Y')                                                                                             
                        except ValueError:
                            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                               
                            self.fven.focus()        
                            return
                        
                    # Validacion del codigo de la licencia de conducir
                    if self.cate.get() != '' and self.codi.get() == '':   
                        messagebox.showinfo('GRABAR', 'Registra el codigo de la licencia !', icon = 'warning')                           
                        self.codi.focus()  
                    elif self.cate.get() != '' and len(self.codi.get()) != 1:   
                        messagebox.showinfo('GRABAR', 'Registra correctamente el codigo de la licencia !', icon = 'warning')                            
                        self.codi.focus()   
                    elif self.cate.get() != '' and not self.codi.get().isalpha():   
                        messagebox.showinfo('GRABAR', 'Registra correctamente el codigo de la licencia !', icon = 'warning')                             
                        self.codi.focus()           

                    # Validacion del area de labor 
                    elif self.alab.get() == '':
                        messagebox.showinfo('GRABAR', 'Registra el area de labor !', icon = 'warning')                                          
                        self.alab.focus()

                    # Validacion del numero celular             
                    elif self.ncel.get() == '':
                        messagebox.showinfo('GRABAR', 'Registra el numero de celular !', icon = 'warning')                                              
                        self.ncel.focus()
                    elif len(self.ncel.get()) != 9:
                        messagebox.showinfo('GRABAR', 'Registra correctamente el numero de celular !', icon = 'warning')                                        
                        self.ncel.focus()
                    elif not self.ncel.get().isdigit():
                        messagebox.showinfo('GRABAR', 'Registra correctamente el numero de celular !', icon = 'warning')                                       
                        self.ncel.focus()
                    
                    # Validacion del distrito de residencia
                    elif self.dres.get() == '':                                                    
                        messagebox.showinfo('GRABAR', 'Registra el distrito de residencia !', icon = 'warning')
                        self.dres.focus()
                      
                    # Validacion de fecha del cese
                    elif self.fces.get() != '' and len(self.fces.get()) != 10:
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                                        
                        self.fces.focus()
                    elif self.fces.get() != '' and not self.fces.get().replace('/','').isdigit():
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                            
                        self.fces.focus()
                    elif self.fces.get() != '' and len(self.fces.get().replace('/','')) != 8:
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                             
                        self.fces.focus()    
                    elif self.fces.get() != '' and self.fces.get()[2] != '/':
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                          
                        self.fces.focus()
                    elif self.fces.get() != '' and self.fces.get()[5] != '/':
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                              
                        self.fces.focus()  
                    elif self.fces.get() != '' and int(self.fces.get()[6:10]) != datetime.today().year: 
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                              
                        self.fces.focus() 
                    else:              
                        if self.fces.get() != '':
                            try:                  
                                datetime.strptime(self.fces.get() , '%d/%m/%Y')                                                                                             
                            except ValueError:
                                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                               
                                self.fces.focus()        
                                return     

                        # Verificacion de dni ya registrado      
                        if self.busc['state'] == 'normal':
                            for index in self.tre1.get_children():
                                if f'''{self.tre1.item(index).get('values')[2]:0>8}''' == self.ndni['text']:                                    
                                    messagebox.showinfo('GRABAR', 'El trabajador ya esta registrado !', icon = 'warning')    
                                    return

                        # Guardar datos registrados en variables                                                                                                                                                                   
                        dni  = self.ndni.cget('text')
                        apat = self.apat.cget('text')
                        amat = self.amat.cget('text')
                        nomb = self.nomb.cget('text')
                        naci = self.fnac.get()
                        ingr = self.fing.get()
                        plan = int(self.spla.get())      

                        if self.afam.get() == 'NO':
                            asig = 0
                        else:
                            asig = self.rmv * 0.1

                        if self.smov.get() == '':
                            movi = 0  
                        else:                            
                            movi = int(self.smov.get())   

                        carg = self.plab.get()
                        cuen = self.ncue.get()
                        apor = self.eapo.get()
                        comi = self.ecom.get()
                        cusp = self.ecus.get().upper()
                        lice = self.cate.get()
                        venc = self.fven.get()
                        codi = self.codi.get().upper()
                        
                        if self.cate.get() != '':
                            codi = self.codi.get().upper() + dni                       

                        area = self.alab.get()
                        celu = self.ncel.get()
                        dist = self.dres.get()              
                        cese = self.fces.get()                         
                        
                        # Obtener el id del trabajador seleccionado
                        seleccion = self.tre1.focus()                        
                        if seleccion !='':
                            id = int(self.tre1.item(seleccion).get('text'))   

                        # Si esta activo boton de dni, nuevo registro (consulta sql)
                        if self.busc['state'] == 'normal':                                            
                            query = f'''INSERT INTO ACTIVO (NDNI, APAT, AMAT, NOMB, FNAC, FING, SPLA, AFAM, SMOV, EAPO, TCOM, NCUS, PLAB, NCUE, ALAB, NLIC, VLIC, CLIC, NCEL, DRES, FCES) VALUES (
                                '{dni}','{apat}','{amat}','{nomb}','{naci}','{ingr}',{plan},'{asig}',{movi},'{apor}','{comi}','{cusp}','{carg}','{cuen}','{area}','{codi}','{venc}','{lice}','{celu}','{dist}','{cese}')'''
                            insert(query)
                        # Si no esta activo boton de dni, actualizar registro (consulta sql)               
                        else:                            
                            query = f'''UPDATE ACTIVO SET FNAC = '{naci}', FING = '{ingr}', SPLA = {plan}, AFAM = '{asig}', SMOV = {movi}, EAPO = '{apor}' , TCOM = '{comi}', NCUS = '{cusp}', 
                                    PLAB = '{carg}', NCUE = '{cuen}', ALAB = '{area}', NLIC = '{codi}', VLIC = '{venc}', CLIC = '{lice}', NCEL = '{celu}', DRES = '{dist}', FCES = '{cese}' WHERE ID = {id}'''           
                            update(query)
                        # Crear conexion con la base de datos y ejecutar sql                                                                                         
                        

                        # Llamar a funciones para actualizar lista    
                        self.MostrarDatos()
                        self.BorrarDetalles()                        
                        
                        # Volver a poner el selector del treview en el mismo lugar
                        if seleccion !='':
                            for index in self.tre1.get_children():
                                if int(self.tre1.item(index).get('text')) == id:
                                    self.tre1.selection_set(index)
                                    self.tre1.focus(index)    

                        # Cerrar ventana                           
                        self.men1_agre.destroy()
    
    def CambioAporte(self, e):
        
        # Desactivamos y activamos los elementos del combobox
        if self.eapo.get() == 'ONP' or self.eapo.get() == '':
            self.ecom.set('')
            self.ecom['state'] = 'disable'
            self.ecus.delete(0, END)
            self.ecus['state'] = 'disable'            
        else:                 
            self.ecom['state'] = 'readonly'
            self.ecus['state'] = 'normal'

    def CambioLicencia(self, e):
        
        # Activamos demas detalles si tiene licencia
        if self.cate.get() == '':  
            self.fven.delete(0, END)   
            self.codi.delete(0, END)           
            self.fven['state'] = 'disable' 
            self.codi['state'] = 'disable'                            
        else: 
            self.fven['state'] = 'normal'
            self.codi['state'] = 'normal' 

    def MostrarDetalles(self, e):
                
        # Si seleccionamos un item se ejecutara el codigo
        if self.tre1.selection():
            
            # Limpiamos los cuadros
            self.BorrarDetalles()
            
            # Obtenemos el id del trabajador          
            id = int(self.tre1.item(self.tre1.focus()).get('text'))
            
            # Tomamos los datos del trabajador
            datos = select(f'SELECT * FROM ACTIVO WHERE ID = {id}', False)

            # Extraemos datos del trabajador           
            edad        = relativedelta(datetime.now(), datetime.strptime(datos[5], '%d/%m/%Y'))
            tiempo      = relativedelta(datetime.now(), datetime.strptime(datos[6], '%d/%m/%Y'))   
            #total       = planilla + asignacion + movilidad        
            
            banco       = ''
            if len(datos[14]) == 14:                
                banco = 'BANCO DE CREDITO'
            elif len(datos[14]) == 20:                 
                if datos[14][:3] == '018':
                    banco = 'BANCO DE LA NACION' 
                elif datos[14][:3] == '003':
                    banco = 'INTERBANK' 
                elif datos[14][:3] == '009':
                    banco = 'SCOTIABANK' 
                elif datos[14][:3] == '011':
                    banco = 'BBVA CONTINENTAL' 

            # Mostramos datos del trabajador en los cuadros
            self.naci['text'] = datos[5]
            self.ingr['text'] = datos[6]
            self.plan['text'] = f'{datos[7]:,.2f}'
            self.asig['text'] = f'{datos[8]:,.2f}'
            self.movi['text'] = f'{datos[9]:,.2f}'
            self.suel['text'] = f'{datos[7] + datos[8] + datos[9]:,.2f}'
            self.carg['text'] = datos[13]
            self.cuen['text'] = datos[14]
            self.apor['text'] = datos[10]
            self.comi['text'] = datos[11]
            self.lice['text'] = datos[18]
            self.venc['text'] = datos[17]
            self.area['text'] = datos[15]
            self.celu['text'] = datos[19]
            self.dist['text'] = datos[20]
            self.edad['text'] = edad.years
            self.tiem['text'] = f'{tiempo.years} - {tiempo.months} - {tiempo.days}'
            self.banc['text'] = banco
            self.cusp['text'] = datos[12]
            self.cese['text'] = datos[21]
                                                

    def Menu2(self):  

        # Activamos o desactivamos los botones
        self.BloquearBotones()
        
        # Dejamos BloquearBotones el boton 1
        self.btn2.configure(state='normal')
        
        # Validacion para destruir el menu 1 si esta BloquearBotones y detener la ejecucion
        if self.menu == 2: 
            self.men2.destroy()      
            self.menu = 0
            return
        
        # Asignamos el numero de menu BloquearBotones
        self.menu = 2
               
        # Creamos el frame       
        menu = Frame(self, background='#FFFFFF')  
        
        # Creamos y posicionamos encabezados de treeview        
        Label(menu, text='N°'                , font=('Segoe UI Semibold', 8)).place(x= 15, y=15, width= 46, height=30)
        Label(menu, text='APELLIDOS Y NOMBRE', font=('Segoe UI Semibold', 8)).place(x= 61, y=15, width=271, height=30)
        Label(menu, text='APOYO'             , font=('Segoe UI Semibold', 8)).place(x=332, y=15, width= 51, height=30)             
        Label(menu, text='FALTA'             , font=('Segoe UI Semibold', 8)).place(x=383, y=15, width= 51, height=30)
        Label(menu, text='FERIADO'           , font=('Segoe UI Semibold', 8)).place(x=434, y=15, width= 51, height=30)
        Label(menu, text='INGRESO'           , font=('Segoe UI Semibold', 8)).place(x=485, y=15, width= 81, height=30)     
        Label(menu, text='RECORTE'           , font=('Segoe UI Semibold', 8)).place(x=566, y=15, width= 81, height=30)
        Label(menu, text='D. ME.'            , font=('Segoe UI Semibold', 8)).place(x=647, y=15, width= 51, height=30)        
        Label(menu, text='VACA.'             , font=('Segoe UI Semibold', 8)).place(x=698, y=15, width= 51, height=30)     
        Label(menu, text='C. VA.'            , font=('Segoe UI Semibold', 8)).place(x=749, y=15, width= 51, height=30)
        Label(menu, text='ADELANTO'          , font=('Segoe UI Semibold', 8)).place(x=800, y=15, width= 81, height=30)    
        Label(menu, text='XFUERA'            , font=('Segoe UI Semibold', 8)).place(x=881, y=15, width= 73, height=30)            
      
        # Crear treeview
        self.tre2 = Treeview(menu, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12'))
        self.tre2.column('#0',  width=  0)
        self.tre2.column('#1',  width= 30)
        self.tre2.column('#2',  width=268)
        self.tre2.column('#3',  width= 50, anchor='center')  
        self.tre2.column('#4',  width= 50, anchor='center')
        self.tre2.column('#5',  width= 50, anchor='center')
        self.tre2.column('#6',  width= 81, anchor='center') 
        self.tre2.column('#7',  width= 80, anchor='center')
        self.tre2.column('#8',  width= 52, anchor='center')
        self.tre2.column('#9',  width= 50, anchor='center') 
        self.tre2.column('#10', width= 50, anchor='center') 
        self.tre2.column('#11', width= 87, anchor='center')     
        self.tre2.column('#12', width= 87, anchor='center') 
        
        # Crear scrollbar              
        scroll = Scrollbar(menu, orient='vertical', command=self.tre2.yview)
        self.tre2.configure(yscrollcommand=scroll.set)  
        
        # Evento de seleccion en treeview       
        self.tre2.bind('<Double-1>', self.Menu2DetallesMostrar)

        # Posicionamos treeview y scrollbar
        self.tre2.place(x= 15, y=45, height=520)
        scroll.place   (x=950, y=15, height=550)
            
        # Cargamos datos al treeview
        self.Menu2CargarDatos()

        # Posicionamos la ventana
        menu.place(x=110, y=10, width=980, height=580)   

        # Asignamos variable a la ventana para poder destruirlo
        self.men2 = menu
                
        # Creamos ventana de detalles y lo ocultamos
        self.Menu2Detalles()
        self.Menu2DetallesOcultar()

    def Menu2CargarDatos(self):

         # Crear conexion a base de datos
        conexion = sqlite3.connect('PlaniPRO.db')    
        cursor = conexion.cursor()

        orden = 0  

        # Recorrer datos almacenados en pandas para agregar informacion a treeview            
        for fila in self.datos.index: 

            orden+=1                  
            id      = self.datos['ID'][fila]  
            apat    = self.datos['APAT'][fila]
            amat    = self.datos['AMAT'][fila]
            nomb    = self.datos['NOMB'][fila]
            nombre  = f'{apat} {amat} {nomb}'  

            # Ejecutamos consultas de los detalles de cada trabajador en base de datos
            apoyo       = cursor.execute(F'SELECT COUNT(FECH) FROM APOYO       WHERE IDAC = {id}').fetchone()  
            falta       = cursor.execute(F'SELECT COUNT(FECH) FROM FALTA       WHERE IDAC = {id}').fetchone()           
            feriado     = cursor.execute(F'SELECT COUNT(FECH) FROM FERIADO     WHERE IDAC = {id}').fetchone()              
            ingreso     = cursor.execute(F'SELECT SUM(MONT)   FROM INGRESO     WHERE IDAC = {id}').fetchone()  
            descuento   = cursor.execute(F'SELECT SUM(MONT)   FROM DESCUENTO   WHERE IDAC = {id}').fetchone()  
            dmedico     = cursor.execute(F'SELECT SUM(DTOT)   FROM DMEDICO     WHERE IDAC = {id}').fetchone()  
            vacaciones  = cursor.execute(F'SELECT SUM(DTOT)   FROM VACACIONES  WHERE IDAC = {id}').fetchone()  
            cvacaciones = cursor.execute(F'SELECT SUM(DTOT)   FROM CVACACIONES WHERE IDAC = {id}').fetchone()  
            adelanto    = cursor.execute(F'SELECT SUM(MONT)   FROM ADELANTO    WHERE IDAC = {id}').fetchone()  
            xfuera      = cursor.execute(F'SELECT SUM(MONT)   FROM XFUERA      WHERE IDAC = {id}').fetchone()  
                       
            if ingreso[0] == None:
                ingreso = '0.00'
            else:
                ingreso = f'{ingreso[0]:.2f}'

            if descuento[0] == None:
                descuento = '0.00'
            else:
                descuento = f'{descuento[0]:.2f}'

            if dmedico[0] == None:
                dmedico = '0'
            else:
                dmedico = dmedico[0]

            if vacaciones[0] == None:
                vacaciones = '0'
            else:
                vacaciones = vacaciones[0]

            if cvacaciones[0] == None:
                cvacaciones = '0'
            else:
                cvacaciones = cvacaciones[0]

            if adelanto[0] == None:
                adelanto = '0.00'
            else:
                adelanto = f'{adelanto[0]:.2f}'

            if xfuera[0] == None:
                xfuera = '0.00'
            else:
                xfuera = f'{xfuera[0]:.2f}'
                   
            # Insertamos datos al treeview
            self.tre2.insert('', END, text=id, values=(orden, nombre, apoyo[0], falta[0], feriado[0], ingreso, descuento, dmedico, vacaciones, cvacaciones, adelanto, xfuera)) 

        # Cerramos conexion a base de datos
        conexion.close()        

    def Menu2Detalles(self):                   
        
        # Creamos el frame 
        menu = Frame(self.men2, background='#FFFFFF')          

        # Creamos el widget del calendario
        self.calendario = Calendar(menu, menuselectmode='day', date_pattern='dd/MM/yyyy', cursor='hand2')
        self.calendario.place(x=15, y=15)

        # Creamos los botones de cada detalle para grabar
        Button(menu, text='APOYO'               , command=lambda: self.Menu2DetallesGrabar('APOYO'      )).place(x=275, y= 15, width= 94, height=22)
        Button(menu, text='FALTA'               , command=lambda: self.Menu2DetallesGrabar('FALTA'      )).place(x=377, y= 15, width= 94, height=22)
        Button(menu, text='FERIADO'             , command=lambda: self.Menu2DetallesGrabar('FERIADO'    )).place(x=479, y= 15, width= 94, height=22)
        Button(menu, text='ADELANTO'            , command=lambda: self.Menu2DetallesGrabar('ADELANTO'   )).place(x=581, y= 15, width=153, height=22)
        Button(menu, text='INGRESO'             , command=lambda: self.Menu2DetallesGrabar('INGRESO'    )).place(x= 15, y=240, width=255, height=22)
        Button(menu, text='DESCUENTO'           , command=lambda: self.Menu2DetallesGrabar('DESCUENTO'  )).place(x=277, y=240, width=255, height=22)
        Button(menu, text='VACACIONES'          , command=lambda: self.Menu2DetallesGrabar('VACACIONES' )).place(x=539, y=240, width=194, height=22)
        Button(menu, text='DESCANSO MEDICO'     , command=lambda: self.Menu2DetallesGrabar('DMEDICO'    )).place(x= 15, y=402, width=516, height=22)
        Button(menu, text='COMPRA DE VACACIONES', command=lambda: self.Menu2DetallesGrabar('CVACACIONES')).place(x=539, y=402, width=194, height=22)

        # Botones de cada detalle para extraer fecha
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('fivacaciones' )).place(x=621, y=268, width=10, height=14)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('ffvacaciones' )).place(x=696, y=268, width=10, height=14)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('fidmedico'    )).place(x= 97, y=430, width=10, height=14)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('ffdmedico'    )).place(x=172, y=430, width=10, height=14)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('ficvacaciones')).place(x=621, y=430, width=10, height=14)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('ffcvacaciones')).place(x=696, y=430, width=10, height=14)

        # Creamos las etiquetas de cada detalle
        Label(menu, text='Importe', bg='#FFFFFF').place(x=609, y= 41, height=16)     
        Label(menu, text='Detalle', bg='#FFFFFF').place(x= 15, y=266, height=16)
        Label(menu, text='Monto',   bg='#FFFFFF').place(x=217, y=266, height=16)
        Label(menu, text='Detalle', bg='#FFFFFF').place(x=277, y=266, height=16)
        Label(menu, text='Monto',   bg='#FFFFFF').place(x=479, y=266, height=16)
        Label(menu, text='Inicio',  bg='#FFFFFF').place(x=539, y=266, height=16)
        Label(menu, text='Final',   bg='#FFFFFF').place(x=633, y=266, height=16)
        Label(menu, text='Dias',    bg='#FFFFFF').place(x=708, y=266, height=16)
        Label(menu, text='Inicio',  bg='#FFFFFF').place(x=539, y=428, height=16)
        Label(menu, text='Final',   bg='#FFFFFF').place(x=633, y=428, height=16)
        Label(menu, text='Dias',    bg='#FFFFFF').place(x=708, y=428, height=16)
        Label(menu, text='Inicio',  bg='#FFFFFF').place(x= 15, y=428, height=16)
        Label(menu, text='Final',   bg='#FFFFFF').place(x=109, y=428, height=16)
        Label(menu, text='Detalle', bg='#FFFFFF').place(x=186, y=428, height=16)
        Label(menu, text='Dias',    bg='#FFFFFF').place(x=505, y=428, height=16)

        # Creamos los treeview de cada detalle
        self.apoyo = Treeview(menu, columns=('#1'))
        self.apoyo.column('#0', width= 0)
        self.apoyo.column('#1', width=92)   
        self.falta = Treeview(menu, columns=('#1'))
        self.falta.column('#0', width= 0)
        self.falta.column('#1', width=92) 
        self.feriado = Treeview(menu, columns=('#1'))
        self.feriado.column('#0', width= 0)
        self.feriado.column('#1', width=92) 
        self.adelanto = Treeview(menu, columns=('#1', '#2'))
        self.adelanto.column('#0', width= 0)
        self.adelanto.column('#1', width=80) 
        self.adelanto.column('#2', width=70, anchor='e')
        self.ingreso = Treeview(menu, columns=('#1', '#2'))
        self.ingreso.column('#0', width=  0)
        self.ingreso.column('#1', width=182) 
        self.ingreso.column('#2', width= 70, anchor='e') 
        self.descuento = Treeview(menu, columns=('#1', '#2'))
        self.descuento.column('#0', width=  0)
        self.descuento.column('#1', width=182) 
        self.descuento.column('#2', width= 70, anchor='e') 
        self.vacaciones = Treeview(menu, columns=('#1', '#2', '#3'))
        self.vacaciones.column('#0', width= 0)
        self.vacaciones.column('#1', width=74) 
        self.vacaciones.column('#2', width=74, anchor='e') 
        self.vacaciones.column('#3', width=45, anchor='e') 
        self.dmedico = Treeview(menu, columns=('#1', '#2', '#3', '#4'))
        self.dmedico.column('#0', width=  0)
        self.dmedico.column('#1', width= 74) 
        self.dmedico.column('#2', width= 75, anchor='e') 
        self.dmedico.column('#3', width=321) 
        self.dmedico.column('#4', width= 45, anchor='e') 
        self.cvacaciones = Treeview(menu, columns=('#1', '#2', '#3'))
        self.cvacaciones.column('#0', width= 0)
        self.cvacaciones.column('#1', width=74) 
        self.cvacaciones.column('#2', width=74, anchor='e') 
        self.cvacaciones.column('#3', width=45, anchor='e') 

        # Evento de click del treeview para quitar seleccion
        self.apoyo.bind      ('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.falta.bind      ('<Button-1>', self.Menu2DetallesQuitarSeleccion) 
        self.feriado.bind    ('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.adelanto.bind   ('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.ingreso.bind    ('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.descuento.bind  ('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.vacaciones.bind ('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.dmedico.bind    ('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.cvacaciones.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion)

        # Creamos las cajas de texto de cada detalle
        self.adelantoImporte    = Entry(menu, bg='#F0F0F0', justify='right')
        self.ingresoDetalle     = Entry(menu, bg='#F0F0F0')
        self.ingresoImporte     = Entry(menu, bg='#F0F0F0', justify='right')
        self.descuentoDetalle   = Entry(menu, bg='#F0F0F0')
        self.descuentoImporte   = Entry(menu, bg='#F0F0F0', justify='right')
        self.vacacionesInicial  = Entry(menu, bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.vacacionesFinal    = Entry(menu, bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.vacacionesTotal    = Entry(menu, bg='#F0F0F0', justify='right')
        self.dmedicoInicial     = Entry(menu, bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.dmedicoFinal       = Entry(menu, bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.dmedicoDetalle     = Entry(menu, bg='#F0F0F0')
        self.dmedicoTotal       = Entry(menu, bg='#F0F0F0', justify='right')
        self.cvacacionesInicial = Entry(menu, bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.cvacacionesFinal   = Entry(menu, bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.cvacacionesTotal   = Entry(menu, bg='#F0F0F0', justify='right')

        # Posicionamos los treeview de cada detalle
        self.apoyo.place      (x=275, y= 42, height=160)
        self.falta.place      (x=377, y= 42, height=160)
        self.feriado.place    (x=479, y= 42, height=160)
        self.adelanto.place   (x=581, y= 62, height=140)   
        self.ingreso.place    (x= 15, y=304, height= 60)
        self.descuento.place  (x=277, y=304, height= 60)
        self.vacaciones.place (x=539, y=304, height= 60)
        self.dmedico.place    (x= 15, y=466, height= 60)
        self.cvacaciones.place(x=539, y=466, height= 60)

        # Posicionamos las cajas de texto de cada detalle
        self.adelantoImporte.place   (x=671, y= 42, width= 60, height=17)   
        self.ingresoDetalle.place    (x= 15, y=284, width=198, height=17)        
        self.ingresoImporte.place    (x=217, y=284, width= 50, height=17)
        self.descuentoDetalle.place  (x=277, y=284, width=198, height=17)        
        self.descuentoImporte.place  (x=479, y=284, width= 50, height=17)
        self.vacacionesInicial.place (x=539, y=284, width= 92, height=17)        
        self.vacacionesFinal.place   (x=633, y=284, width= 73, height=17)        
        self.vacacionesTotal.place   (x=708, y=284, width= 24, height=17)   
        self.dmedicoInicial.place    (x= 15, y=446, width= 92, height=17)
        self.dmedicoFinal.place      (x=109, y=446, width= 73, height=17)
        self.dmedicoDetalle.place    (x=186, y=446, width=317, height=17)
        self.dmedicoTotal.place      (x=505, y=446, width= 25, height=17)
        self.cvacacionesInicial.place(x=539, y=446, width= 92, height=17)
        self.cvacacionesFinal.place  (x=633, y=446, width= 73, height=17)
        self.cvacacionesTotal.place  (x=708, y=446, width= 24, height=17)        
                    
        # Asignamos variable a la ventana para poder destruirlo
        self.men2_detalles = menu

        # Creamos los botones finales
        Button(menu, text='ELIMINAR', command=self.Menu2DetallesEliminar).place(x=875, y=15, width=90, height=30)     
        Button(menu, text='SALIR'   , command=self.Menu2DetallesOcultar ).place(x=875, y=50, width=90, height=30)

        # Posicionamos la ventana principal
        menu.place(x=0, y=0, width=980, height=580) 

    def Menu2DetallesMostrar(self, e):
      
        # Mostramos la ventana detalles
        if self.tre2.selection():
            
            id = int(self.tre2.item(self.tre2.focus()).get('text'))

            # Crear conexion a base de datos
            conexion = sqlite3.connect('PlaniPRO.db')    
            cursor = conexion.cursor()

            # Ejecutamos consultas de los detalles de cada trabajador en base de datos
            apoyo       = cursor.execute(F'SELECT ID, FECH                      FROM APOYO       WHERE IDAC = {id}').fetchall() 
            falta       = cursor.execute(F'SELECT ID, FECH                      FROM FALTA       WHERE IDAC = {id}').fetchall()  
            feriado     = cursor.execute(F'SELECT ID, FECH                      FROM FERIADO     WHERE IDAC = {id}').fetchall()  
            adelanto    = cursor.execute(F'SELECT ID, FECH, MONT                FROM ADELANTO    WHERE IDAC = {id}').fetchall()  
            ingreso     = cursor.execute(F'SELECT ID, DETA, MONT                FROM INGRESO     WHERE IDAC = {id}').fetchall() 
            descuento   = cursor.execute(F'SELECT ID, DETA, MONT                FROM DESCUENTO   WHERE IDAC = {id}').fetchall()  
            vacaciones  = cursor.execute(F'SELECT ID, FINI, FFIN, DTOT          FROM VACACIONES  WHERE IDAC = {id}').fetchall()  
            dmedico     = cursor.execute(F'SELECT ID, FINI, FFIN, DETA, DTOT    FROM DMEDICO     WHERE IDAC = {id}').fetchall() 
            cvacaciones = cursor.execute(F'SELECT ID, FINI, FFIN, DTOT          FROM CVACACIONES WHERE IDAC = {id}').fetchall()  

            for dato in apoyo:
                self.apoyo.insert('', END, text=dato[0], values=(dato[1])) 

            for dato in falta:
                self.falta.insert('', END, text=dato[0], values=(dato[1]))

            for dato in feriado:
                self.feriado.insert('', END, text=dato[0], values=(dato[1]))    

            for dato in adelanto:
                self.adelanto.insert('', END, text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))      

            for dato in ingreso:
                self.ingreso.insert('', END, text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))    

            for dato in descuento:
                self.descuento.insert('', END, text=dato[0], values=(dato[1], f'{dato[2]:.2f}')) 

            for dato in vacaciones:
                self.vacaciones.insert('', END, text=dato[0], values=(dato[1], dato[2], dato[3])) 

            for dato in dmedico:
                self.dmedico.insert('', END, text=dato[0], values=(dato[1], dato[2], dato[3], dato[4])) 

            for dato in cvacaciones:
                self.cvacaciones.insert('', END, text=dato[0], values=(dato[1], dato[2], dato[3]))     
          
            conexion.close()

            self.men2_detalles.place(x=0, y=0, width=980, height=580) 
            self.men2_detalles.grab_set()

    def Menu2DetallesOcultar(self):
        
        # Limpiamos los cuadros de la ventana detalles
        self.apoyo.delete(*self.apoyo.get_children())
        self.falta.delete(*self.falta.get_children())
        self.feriado.delete(*self.feriado.get_children())
        self.adelanto.delete(*self.adelanto.get_children())
        self.ingreso.delete(*self.ingreso.get_children())
        self.descuento.delete(*self.descuento.get_children())
        self.vacaciones.delete(*self.vacaciones.get_children())
        self.dmedico.delete(*self.dmedico.get_children())
        self.cvacaciones.delete(*self.cvacaciones.get_children())
        
        # Ocultamos la ventana detalles
        self.men2_detalles.place_forget() 
        self.men2_detalles.grab_release()   
        
    def Menu2DetallesGrabar(self, widget):  

        # Actualizamos la fila seleccionada y aunmentamos +1 apoyo
        valores = self.tre2.item(self.tre2.focus())['values'] 

        # Crear conexion a base de datos
        conexion = sqlite3.connect('PlaniPRO.db')    
        cursor = conexion.cursor()    

        # Obtener id de trabajador
        id = int(self.tre2.item(self.tre2.focus()).get('text'))

        if widget == 'APOYO':
            
         # Verificamos si se repite la fecha para anular registro       
            for row in self.apoyo.get_children():
                fecha = self.apoyo.item(row)['values'][0]            
                if fecha == self.calendario.get_date():
                    return                   
        
            valores[2] = int(valores[2]) + 1           
        
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'INSERT INTO APOYO (IDAC, FECH) VALUES ({id}, "{self.calendario.get_date()}")')

            idRegistro = cursor.execute(F'SELECT ID FROM APOYO ORDER BY ID DESC').fetchone()  
            
            # Si no esta registrado la fecha agregamos al treeview
            self.apoyo.insert('',END, text=idRegistro[0] ,values=self.calendario.get_date())
                   
        elif widget == 'FALTA':

            # Verificamos si se repite la fecha para anular registro       
            for row in self.falta.get_children():
                fecha = self.falta.item(row)['values'][0]            
                if fecha == self.calendario.get_date():
                    return                   
        
            valores[3] = int(valores[3]) + 1           
        
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'INSERT INTO FALTA (IDAC, FECH) VALUES ({id}, "{self.calendario.get_date()}")')

            idRegistro = cursor.execute(F'SELECT ID FROM FALTA ORDER BY ID DESC').fetchone()  
            # Si no esta registrado la fecha agregamos al treeview
            self.falta.insert('',END, text=idRegistro[0], values=self.calendario.get_date())

        elif widget == 'FERIADO':

            # Verificamos si se repite la fecha para anular registro       
            for row in self.feriado.get_children():
                fecha = self.feriado.item(row)['values'][0]            
                if fecha == self.calendario.get_date():
                    return                   
        
            valores[4] = int(valores[4]) + 1           
        
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'INSERT INTO FERIADO (IDAC, FECH) VALUES ({id}, "{self.calendario.get_date()}")')
            idRegistro = cursor.execute(F'SELECT ID FROM FERIADO ORDER BY ID DESC').fetchone()
            # Si no esta registrado la fecha agregamos al treeview
            self.feriado.insert('',END,text=idRegistro[0], values=self.calendario.get_date())

        elif widget == 'ADELANTO':

            # Verificamos si esta vacio el cuadro de registro de importe
            if self.adelantoImporte.get() == '':
                self.adelantoImporte.focus_set()   
                messagebox.showinfo('ADELANTO', 'Registra el importe del adelanto !', icon = 'warning')    
            else:

                # Verificamos si se repite la fecha para anular registro
                for row in self.adelanto.get_children():         
                    fecha = self.adelanto.item(row)['values'][0]               
                    if fecha == self.calendario.get_date():                
                        return

                # Si no se repite la fecha verificamos que el importe este correctamente escrito 
                if self.adelantoImporte.get().count('.') == 1 or self.adelantoImporte.get().count('.') == 0:          
                    if self.adelantoImporte.get().replace('.','').isnumeric():

                        # Si todo esta ok, registramos en el treeview
                        monto = float(self.adelantoImporte.get())  

                        valores[10] = f'{float(valores[10]) + monto:.2f}'             
        
                        # Ejecutamos la query de grabar dia de apoyo
                        cursor.execute(F'INSERT INTO ADELANTO (IDAC, FECH, MONT) VALUES ({id}, "{self.calendario.get_date()}", {monto})')

                        idRegistro = cursor.execute(F'SELECT ID FROM ADELANTO ORDER BY ID DESC').fetchone()
                        self.adelanto.insert('',END ,text=idRegistro[0], values=(self.calendario.get_date(), f'{monto:.2f}'))
                        self.adelantoImporte.delete(0, END)                    
                
                # Si esta mal la validacion del importe o esta vacio enviamos el foco al cuadro
                    else:
                        self.adelantoImporte.focus_set()   
                        messagebox.showinfo('ADELANTO', 'Registra correctamente el importe del adelanto !', icon = 'warning')                          
                else:
                    self.adelantoImporte.focus_set()
                    messagebox.showinfo('ADELANTO', 'Registra correctamente el importe del adelanto !', icon = 'warning')    

        elif widget == 'INGRESO':

            # Validamos los cuadros de ingreso si estan vacios enviar el foco
            if self.ingresoDetalle.get() == '':
                self.ingresoDetalle.focus_set()
                messagebox.showinfo('INGRESO', 'Registra el detalle del ingreso !', icon = 'warning')
            elif self.ingresoImporte.get() == '':
                self.ingresoImporte.focus_set()    
                messagebox.showinfo('INGRESO', 'Registra el importe del ingreso !', icon = 'warning')  
            else:
                
                # Validamos el importe que este bien escrito 
                if self.ingresoImporte.get().count('.') == 1 or self.ingresoImporte.get().count('.') == 0:          
                    if self.ingresoImporte.get().replace('.','').isnumeric():

                        # Si todo esta ok, registramos en el treeview
                        monto = float(self.ingresoImporte.get())

                        valores[5] = f'{float(valores[5]) + monto:.2f}' 

                        # Ejecutamos la query de grabar dia de apoyo
                        cursor.execute(F'INSERT INTO INGRESO (IDAC, DETA, MONT) VALUES ({id}, "{self.ingresoDetalle.get()}", {monto})')

                        idRegistro = cursor.execute(F'SELECT ID FROM INGRESO ORDER BY ID DESC').fetchone()
                        self.ingreso.insert('', END,text=idRegistro[0], values=(self.ingresoDetalle.get(), f'{monto:.2f}'))

                        self.ingresoDetalle.delete(0, END)
                        self.ingresoImporte.delete(0, END)
                    
                # Si esta mal la validacion del importe o esta vacio enviamos el foco al cuadro
                    else:
                        self.ingresoImporte.focus_set()  
                        messagebox.showinfo('INGRESO', 'Registra correctamente el importe del ingreso !', icon = 'warning')   
                else:
                    self.ingresoImporte.focus_set()
                    messagebox.showinfo('INGRESO', 'Registra correctamente el importe del ingreso !', icon = 'warning')   

        elif widget == 'DESCUENTO':

            # Validamos los cuadros de descuento si estan vacios enviar el foco
            if self.descuentoDetalle.get() == '':
                self.descuentoDetalle.focus_set()
                messagebox.showinfo('DESCUENTO', 'Registra el detalle del descuento !', icon = 'warning')
            elif self.descuentoImporte.get() == '':
                self.descuentoImporte.focus_set()    
                messagebox.showinfo('DESCUENTO', 'Registra el importe del descuento !', icon = 'warning')
            else:
                
                # Validamos el importe que este bien escrito 
                if self.descuentoImporte.get().count('.') == 1 or self.descuentoImporte.get().count('.') == 0:          
                    if self.descuentoImporte.get().replace('.','').isnumeric():
                                                                   
                        # Si todo esta ok, registramos en el treeview
                        monto = float(self.descuentoImporte.get())

                        valores[6] = f'{float(valores[6]) + monto:.2f}' 

                        # Ejecutamos la query de grabar dia de apoyo
                        cursor.execute(F'INSERT INTO DESCUENTO (IDAC, DETA, MONT) VALUES ({id}, "{self.descuentoDetalle.get()}", {monto})')

                        idRegistro = cursor.execute(F'SELECT ID FROM DESCUENTO ORDER BY ID DESC').fetchone()
                        self.descuento.insert('', END,text=idRegistro[0], values=(self.descuentoDetalle.get(), f'{monto:.2f}'))

                        self.descuentoDetalle.delete(0, END)
                        self.descuentoImporte.delete(0, END)
                    
                # Si esta mal la validacion del importe o esta vacio enviamos el foco al cuadro
                    else:
                        self.descuentoImporte.focus_set()    
                        messagebox.showinfo('DESCUENTO', 'Registra correctamente el importe del descuento !', icon = 'warning') 
                else:
                    self.descuentoImporte.focus_set()
                    messagebox.showinfo('DESCUENTO', 'Registra correctamente el importe del descuento !', icon = 'warning')

        elif widget == 'VACACIONES':

            # Validamos los cuadros de vacaciones si estan vacios enviar el foco
            if self.vacacionesInicial.get() == '':
                self.vacacionesTotal.focus_set() 
                messagebox.showinfo('VACACIONES', 'Selecciona la fecha inicial de las vacaciones !', icon = 'warning')
            elif self.vacacionesFinal.get() == '':
                self.vacacionesTotal.focus_set() 
                messagebox.showinfo('VACACIONES', 'Selecciona la fecha final de las vacaciones !', icon = 'warning')
            elif self.vacacionesTotal.get() == '':
                self.vacacionesTotal.focus_set()   
                messagebox.showinfo('VACACIONES', 'Registra el total de dias de las vacaciones !', icon = 'warning')
            else:
                
                # Validamos el total que este bien escrito             
                if self.vacacionesTotal.get().isnumeric():
                    
                    # Si todo esta ok, registramos en el treeview
                    total =int(self.vacacionesTotal.get())                    

                    valores[8] = int(valores[8]) + total

                    # Ejecutamos la query de grabar dia de apoyo
                    cursor.execute(F'INSERT INTO VACACIONES (IDAC, FINI, FFIN, DTOT) VALUES ({id}, "{self.vacacionesInicial.get()}", "{self.vacacionesFinal.get()}",  {total})')

                    idRegistro = cursor.execute(F'SELECT ID FROM VACACIONES ORDER BY ID DESC').fetchone()
                    self.vacaciones.insert('', END,text=idRegistro[0], values=(self.vacacionesInicial.get(), self.vacacionesFinal.get(), total))

                    self.vacacionesInicial.configure(state='normal')
                    self.vacacionesFinal.configure(state='normal')
                    self.vacacionesInicial.delete(0, END)
                    self.vacacionesFinal.delete(0, END)
                    self.vacacionesTotal.delete(0, END)
                    self.vacacionesInicial.configure(state='readonly')
                    self.vacacionesFinal.configure(state='readonly')
                    
                # Si esta mal la validacion del total enviamos el foco al cuadro               
                else:
                    self.vacacionesTotal.focus_set()
                    messagebox.showinfo('VACACIONES', 'Registra correctamente el total de dias de las vacaciones !', icon = 'warning')

        elif widget == 'DMEDICO':
            
            # Validamos los cuadros de descanso medico si estan vacios enviar el foco
            if self.dmedicoInicial.get() == '':
                self.dmedicoDetalle.focus_set() 
                messagebox.showinfo('DESCANSO MEDICO', 'Selecciona la fecha inicial del descanso medico !', icon = 'warning')
            elif self.dmedicoFinal.get() == '':
                self.dmedicoDetalle.focus_set() 
                messagebox.showinfo('DESCANSO MEDICO', 'Selecciona la fecha final del descanso medico !', icon = 'warning')
            elif self.dmedicoDetalle.get() == '':
                self.dmedicoDetalle.focus_set()   
                messagebox.showinfo('DESCANSO MEDICO', 'Registra el detalle del descanso medico !', icon = 'warning')
            elif self.dmedicoTotal.get() == '':
                self.dmedicoTotal.focus_set()   
                messagebox.showinfo('DESCANSO MEDICO', 'Registra el total de dias del descanso medico !', icon = 'warning')
            else:
                
                # Validamos el total que este bien escrito             
                if self.dmedicoTotal.get().isnumeric():
                    
                    # Si todo esta ok, registramos en el treeview
                    total =int(self.dmedicoTotal.get())                    

                    valores[7] = int(valores[7]) + total

                    # Ejecutamos la query de grabar dia de apoyo
                    cursor.execute(F'INSERT INTO DMEDICO (IDAC, FINI, FFIN, DETA, DTOT) VALUES ({id}, "{self.dmedicoInicial.get()}", "{self.dmedicoFinal.get()}", "{self.dmedicoDetalle.get()}",  {total})')

                    idRegistro = cursor.execute(F'SELECT ID FROM DMEDICO ORDER BY ID DESC').fetchone()
                    self.dmedico.insert('', END,text=idRegistro[0], values=(self.dmedicoInicial.get(), self.dmedicoFinal.get(), self.dmedicoDetalle.get(), total))

                    self.dmedicoInicial.configure(state='normal')
                    self.dmedicoFinal.configure(state='normal')
                    self.dmedicoInicial.delete(0, END)
                    self.dmedicoFinal.delete(0, END)
                    self.dmedicoDetalle.delete(0, END)
                    self.dmedicoTotal.delete(0, END)
                    self.dmedicoInicial.configure(state='readonly')
                    self.dmedicoFinal.configure(state='readonly')

                # Si esta mal la validacion del total enviamos el foco al cuadro               
                else:
                    self.dmedicoTotal.focus_set()
                    messagebox.showinfo('DESCANSO MEDICO', 'Registra correctamente el total de dias del descanso medico !', icon = 'warning')

        elif widget == 'CVACACIONES':

             # Validamos los cuadros de compra de vacaciones si estan vacios enviar el foco
            if self.cvacacionesInicial.get() == '':
                self.cvacacionesTotal.focus_set() 
                messagebox.showinfo('COMPRA DE VACACIONES', 'Selecciona la fecha inicial de la compra de vacaciones !', icon = 'warning')
            elif self.cvacacionesFinal.get() == '':
                self.cvacacionesTotal.focus_set() 
                messagebox.showinfo('COMPRA DE VACACIONES', 'Selecciona la fecha final de la compra de vacaciones !', icon = 'warning')
            elif self.cvacacionesTotal.get() == '':
                self.cvacacionesTotal.focus_set()   
                messagebox.showinfo('COMPRA DE VACACIONES', 'Registra el total de dias de la compra de vacaciones !', icon = 'warning')
            else:
                
                # Validamos el total que este bien escrito             
                if self.cvacacionesTotal.get().isnumeric():

                    # Si todo esta ok, registramos en el treeview
                    total =int(self.cvacacionesTotal.get())                    

                    valores[9] = int(valores[9]) + total

                    # Ejecutamos la query de grabar dia de apoyo
                    cursor.execute(F'INSERT INTO CVACACIONES (IDAC, FINI, FFIN, DTOT) VALUES ({id}, "{self.cvacacionesInicial.get()}", "{self.cvacacionesFinal.get()}",  {total})')

                    idRegistro = cursor.execute(F'SELECT ID FROM CVACACIONES ORDER BY ID DESC').fetchone()
                    self.cvacaciones.insert('', END,text=idRegistro[0], values=(self.cvacacionesInicial.get(), self.cvacacionesFinal.get(), total))

                    self.cvacacionesInicial.configure(state='normal')
                    self.cvacacionesFinal.configure(state='normal')
                    self.cvacacionesInicial.delete(0, END)
                    self.cvacacionesFinal.delete(0, END)
                    self.cvacacionesTotal.delete(0, END)
                    self.cvacacionesInicial.configure(state='readonly')
                    self.cvacacionesFinal.configure(state='readonly')

                # Si esta mal la validacion del total enviamos el foco al cuadro               
                else:
                    self.cvacacionesTotal.focus_set()
                    messagebox.showinfo('COMPRA DE VACACIONES', 'Registra correctamente el total de dias de la compra de vacaciones !', icon = 'warning')

        # Grabamos cambios en base de datos y cerramos conexion
        conexion.commit()
        conexion.close()

        self.tre2.item(self.tre2.focus(), values=valores)
 
    def Menu2DetallesEliminar(self):

        valores = self.tre2.item(self.tre2.focus())['values'] 

        # Crear conexion a base de datos
        conexion = sqlite3.connect('PlaniPRO.db')    
        cursor = conexion.cursor()    
                
        if self.apoyo.selection():
            
            valores[2] = int(valores[2]) - 1            

            # Obtener id de trabajador
            id = int(self.apoyo.item(self.apoyo.focus())['text'] )                
            
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM APOYO WHERE ID = {id}')
            
            # Grabamos cambios en base de datos y cerramos conexion     
            self.apoyo.delete(self.apoyo.focus())          
  
        if self.falta.selection():
            
            valores[3] = int(valores[3]) - 1            

            # Obtener id de trabajador
            id = int(self.falta.item(self.falta.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM FALTA WHERE ID = {id}')
            
            self.falta.delete(self.falta.focus())      

        if self.feriado.selection():

            valores[4] = int(valores[4]) - 1            

            # Obtener id de trabajador
            id = int(self.feriado.item(self.feriado.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM FERIADO WHERE ID = {id}')
            
            self.feriado.delete(self.feriado.focus())     

        if self.adelanto.selection():
            
            monto = float(self.adelanto.item(self.adelanto.focus())['values'][1])    
            saldo = float(valores[10]) - monto    
            valores[10] = f'{saldo:.2f}'      

            # Obtener id de trabajador
            id = int(self.adelanto.item(self.adelanto.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM ADELANTO WHERE ID = {id}')
            
            self.adelanto.delete(self.adelanto.focus())     
            
        if self.ingreso.selection():

            monto = float(self.ingreso.item(self.ingreso.focus())['values'][1])    
            saldo = float(valores[5]) - monto    
            valores[5] = f'{saldo:.2f}'      

            # Obtener id de trabajador
            id = int(self.ingreso.item(self.ingreso.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM INGRESO WHERE ID = {id}')
            
            self.ingreso.delete(self.ingreso.focus())     

        if self.descuento.selection():

            monto = float(self.descuento.item(self.descuento.focus())['values'][1])    
            saldo = float(valores[6]) - monto    
            valores[6] = f'{saldo:.2f}'      

            # Obtener id de trabajador
            id = int(self.descuento.item(self.descuento.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM DESCUENTO WHERE ID = {id}')
            
            self.descuento.delete(self.descuento.focus())     

        if self.vacaciones.selection():
            
            total = int(self.vacaciones.item(self.vacaciones.focus())['values'][2])    
            dias = int(valores[8]) - total    
            valores[8] = dias     

            # Obtener id de trabajador
            id = int(self.vacaciones.item(self.vacaciones.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM VACACIONES WHERE ID = {id}')
            
            self.vacaciones.delete(self.vacaciones.focus())     

        if self.dmedico.selection():

            total = int(self.dmedico.item(self.dmedico.focus())['values'][3])    
            dias = int(valores[7]) - total    
            valores[7] = dias     

            # Obtener id de trabajador
            id = int(self.dmedico.item(self.dmedico.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM DMEDICO WHERE ID = {id}')
            
            self.dmedico.delete(self.dmedico.focus())       

        if self.cvacaciones.selection():

            total = int(self.cvacaciones.item(self.cvacaciones.focus())['values'][2])    
            dias = int(valores[9]) - total    
            valores[9] = dias     

            # Obtener id de trabajador
            id = int(self.cvacaciones.item(self.cvacaciones.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM CVACACIONES WHERE ID = {id}')
            
            self.cvacaciones.delete(self.cvacaciones.focus())       


        self.tre2.item(self.tre2.focus(), values=valores)

        conexion.commit()
        conexion.close()

    def Menu2DetallesQuitarSeleccion(self, e):

        # Obtener el widget que activo el evento, esta en orden de creacion
        widget = str(e.widget).split(".")[-1][1:]   

        # Desactivar foco de los demas treeview
        if widget == 'treeview':                
            print(self.apoyo.item(self.apoyo.focus())['text'])
            self.falta.selection_set('')      
            self.feriado.selection_set('')       
            self.adelanto.selection_set('')        
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview2':
            print(self.falta.item(self.falta.focus())['text'])
            self.apoyo.selection_set('')      
            self.feriado.selection_set('')       
            self.adelanto.selection_set('')        
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview3':
            print(self.feriado.item(self.feriado.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.adelanto.selection_set('')        
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview4':
            print(self.adelanto.item(self.adelanto.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview5':
            print(self.ingreso.item(self.ingreso.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview6':
            print(self.descuento.item(self.descuento.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.ingreso.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview7':
            print(self.vacaciones.item(self.vacaciones.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview8':
            print(self.dmedico.item(self.dmedico.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview9':
            print(self.cvacaciones.item(self.cvacaciones.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')        
          
    def Menu2DetallesSeleccionarFecha(self, boton):

        if boton == 'fivacaciones':
            # Agregar fecha inicial al cuadro de vacaciones
            self.vacacionesInicial.configure(state='normal')
            self.vacacionesInicial.delete(0, END)
            self.vacacionesInicial.insert(0, self.calendario.get_date())
            self.vacacionesInicial.configure(state='readonly')
        elif boton == 'ffvacaciones':
            # Agregar fecha final al cuadro de vacaciones
            self.vacacionesFinal.configure(state='normal')
            self.vacacionesFinal.delete(0, END)
            self.vacacionesFinal.insert(0, self.calendario.get_date())
            self.vacacionesFinal.configure(state='readonly')
        elif boton == 'fidmedico':  
            # Agregar fecha inicial al cuadro de descanso medico
            self.dmedicoInicial.configure(state='normal')
            self.dmedicoInicial.delete(0, END)
            self.dmedicoInicial.insert(0, self.calendario.get_date())
            self.dmedicoInicial.configure(state='readonly')
        elif boton == 'ffdmedico':  
            # Agregar fecha final al cuadro de descanso medico
            self.dmedicoFinal.configure(state='normal')
            self.dmedicoFinal.delete(0, END)
            self.dmedicoFinal.insert(0, self.calendario.get_date())
            self.dmedicoFinal.configure(state='readonly')
        elif boton == 'ficvacaciones':  
            # Agregar fecha inicial al cuadro de compra de vacaciones
            self.cvacacionesInicial.configure(state='normal')
            self.cvacacionesInicial.delete(0, END)
            self.cvacacionesInicial.insert(0, self.calendario.get_date())
            self.cvacacionesInicial.configure(state='readonly')
        elif boton == 'ffcvacaciones':  
            # Agregar fecha final al cuadro de compra de vacaciones
            self.cvacacionesFinal.configure(state='normal')
            self.cvacacionesFinal.delete(0, END)
            self.cvacacionesFinal.insert(0, self.calendario.get_date())
            self.cvacacionesFinal.configure(state='readonly')






if __name__ == '__main__':       
    aplicacion = App()
