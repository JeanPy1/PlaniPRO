from tkinter import Button, Entry, Frame, Label, PhotoImage, Scrollbar, Tk, messagebox
from tkinter.constants import END
from tkinter.ttk import Treeview, Style, Combobox
from tkcalendar import Calendar
from scripts import select, insert, update, delete, Edad, Tiempo, FechaValida, PlanillaMes, CompararFechas, datos

from Menu1 import Menu1

class App(Tk):

    def __init__(self):
        super(App, self).__init__()

        # Creamos la ventana principal
        self.title('PlaniPRO')
        self.geometry('1000x600+-8+0')
        self.resizable(0,0)
        self.iconbitmap('./img/ico.ico')

        # Modificamos estilo de los diferentes widgets
        self.option_add('*Font', ('Segoe UI Semibold', '10'))
        self.option_add('*Button*Font', ('Segoe UI Semibold', '8'))
        self.option_add('*Button*BorderWidth', 0)
        self.option_add('*Button*Cursor', 'hand2')
        self.option_add('*Button*TakeFocus', False)
        self.option_add('*Button*Background', '#FFFFFF')
        self.option_add('*Entry*relief', 'flat')
        self.option_add('*Treeview*SelectMode', 'browse')
        self.option_add('*Treeview*Show', 'headings')
        self.option_add('*Treeview*padding', 2)
        self.option_add('*Treeview*Cursor', 'hand2')
        self.option_add('*Treeview*TakeFocus', False)
        self.option_add('*Label*Foreground', '#5B5857')
        self.option_add('*Label*Background', '#FFFFFF')
        self.option_add('*Label*Anchor', 'nw')

        # Modificados estilo de los treeview
        Style().configure('Treeview', font=('Segoe UI Semibold', 10))

        # Cargamos las imagenes de los botones
        img1 = PhotoImage(file='./img/menu1.png')
        img2 = PhotoImage(file='./img/menu2.png')
        img3 = PhotoImage(file='./img/menu3.png')
        img4 = PhotoImage(file='./img/menu4.png')
        img5 = PhotoImage(file='./img/menu5.png')
        img6 = PhotoImage(file='./img/menu6.png')

        # Creamos los botones del menu
        Button(self, bg='#F0F0F0', image=img1, command=self.Menu1).place(       width=100, height=100)
        Button(self, bg='#F0F0F0', image=img2, command=self.Menu2).place(y=100, width=100, height=100)
        Button(self, bg='#F0F0F0', image=img3, command=self.Menu3).place(y=200, width=100, height=100)
        Button(self, bg='#F0F0F0', image=img4, command=self.Menu4).place(y=300, width=100, height=100)
        Button(self, bg='#F0F0F0', image=img5, command=self.Menu5).place(y=400, width=100, height=100)
        Button(self, bg='#F0F0F0', image=img6, command=self.Menu6).place(y=500, width=100, height=100)

        

        # Corremos programa
        self.mainloop()

    
    def Menu1(self):
        
        # Creamos los elementos del menu 1
        window = Frame(self)

        self.employee = Treeview(window, columns=('#1', '#2', '#3'))
        self.employee.column('#0', width=  0)
        self.employee.column('#1', width= 30, minwidth= 30, anchor='center')
        self.employee.column('#2', width=270, minwidth=270)
        self.employee.column('#3', width= 70, minwidth= 70, anchor='center')
        self.employee.heading('#1', text='N°')
        self.employee.heading('#2', text='Apellidos y Nombre')
        self.employee.heading('#3', text='Dni')

        scroll = Scrollbar(window, orient='vertical', command=self.employee.yview)
        self.employee.configure(yscrollcommand=scroll.set)

        Label(window, text='  Nacimiento'  ).place(x=437, y= 20, width=200, height=54)
        Label(window, text='  Ingreso'     ).place(x=437, y= 75, width=200, height=54)
        Label(window, text='  Planilla'    ).place(x=437, y=130, width=200, height=54)
        Label(window, text='  Asignacion'  ).place(x=437, y=185, width=200, height=54)
        Label(window, text='  Movilidad'   ).place(x=437, y=240, width=200, height=54)
        Label(window, text='  Sueldo'      ).place(x=437, y=295, width=200, height=54)
        Label(window, text='  Cargo'       ).place(x=437, y=350, width=200, height=54)
        Label(window, text='  Aportacion'  ).place(x=437, y=405, width=200, height=54)
        Label(window, text='  Comision'    ).place(x=437, y=460, width=200, height=54)
        Label(window, text='  C.u.s.p.p.'  ).place(x=437, y=515, width=200, height=55)        
        Label(window, text='  Cuenta'      ).place(x=638, y= 20, width=200, height=54)       
        Label(window, text='  Licencia'    ).place(x=638, y= 75, width=200, height=54)
        Label(window, text='  Categoria'   ).place(x=638, y=130, width=200, height=54)
        Label(window, text='  Revalidacion').place(x=638, y=185, width=200, height=54)        
        Label(window, text='  Area'        ).place(x=638, y=240, width=200, height=54)
        Label(window, text='  Celular'     ).place(x=638, y=295, width=200, height=54)
        Label(window, text='  Distrito'    ).place(x=638, y=350, width=200, height=54)
        Label(window, text='  Edad'        ).place(x=638, y=405, width=200, height=54)
        Label(window, text='  Tiempo'      ).place(x=638, y=460, width=200, height=54)
        Label(window, text='  Retiro'      ).place(x=638, y=515, width=200, height=55)

        self.detail01 = Label(window, fg='#000000', anchor='e')
        self.detail02 = Label(window, fg='#000000', anchor='e')
        self.detail03 = Label(window, fg='#000000', anchor='e')
        self.detail04 = Label(window, fg='#000000', anchor='e')
        self.detail05 = Label(window, fg='#000000', anchor='e')
        self.detail06 = Label(window, fg='#000000', anchor='e')
        self.detail07 = Label(window, fg='#000000', anchor='e')
        self.detail08 = Label(window, fg='#000000', anchor='e')
        self.detail09 = Label(window, fg='#000000', anchor='e')        
        self.detail10 = Label(window, fg='#000000', anchor='e')
        self.detail11 = Label(window, fg='#000000', anchor='e')
        self.detail12 = Label(window, fg='#000000', anchor='e')
        self.detail13 = Label(window, fg='#000000', anchor='e')
        self.detail14 = Label(window, fg='#000000', anchor='e')
        self.detail15 = Label(window, fg='#000000', anchor='e')
        self.detail16 = Label(window, fg='#000000', anchor='e')
        self.detail17 = Label(window, fg='#000000', anchor='e')
        self.detail18 = Label(window, fg='#000000', anchor='e')
        self.detail19 = Label(window, fg='#000000', anchor='e')
        self.detail20 = Label(window, fg='#000000', anchor='e')

        # Evento de seleccion en treeview
        self.employee.bind('<<TreeviewSelect>>', self.ShowDetails)

        # Posicionamiento de los elementos
        scroll.place(x=396, y=20, height=550)
        self.employee.place(x=20, y=20, height=550)
        self.detail01.place(x=448, y= 44, width=182)
        self.detail02.place(x=448, y= 99, width=182)
        self.detail03.place(x=448, y=154, width=182)
        self.detail04.place(x=448, y=209, width=182)
        self.detail05.place(x=448, y=264, width=182)
        self.detail06.place(x=448, y=319, width=182)
        self.detail07.place(x=448, y=374, width=182)
        self.detail08.place(x=448, y=429, width=182)
        self.detail09.place(x=448, y=484, width=182)
        self.detail10.place(x=448, y=539, width=182)
        self.detail11.place(x=649, y= 44, width=182)
        self.detail12.place(x=649, y= 99, width=182)
        self.detail13.place(x=649, y=154, width=182)
        self.detail14.place(x=649, y=209, width=182)
        self.detail15.place(x=649, y=264, width=182)
        self.detail16.place(x=649, y=319, width=182)
        self.detail17.place(x=649, y=374, width=182)
        self.detail18.place(x=649, y=429, width=182)
        self.detail19.place(x=649, y=484, width=182)
        self.detail20.place(x=649, y=539, width=182)

        # Botones de gestion
        Button(window, text='AGREGAR'  , command=self.Add  ).place(x=890, y=20, width=90, height=30)
        Button(window, text='MODIFICAR', command=self.Modify).place(x=890, y=55, width=90, height=30)
        Button(window, text='ELIMINAR' , command=self.Remove ).place(x=890, y=90, width=90, height=30)
        Button(window, text='SALIR'    , command=lambda:window.destroy(), bg='#DF2F2F').place(x=890, y=125, width=90, height=30)

        # Cargamos datos al treeview
        self.LoadEmployee()

        # Posicionamos la ventana principal
        window.place(width=1000, height=600)

    def Add(self):
       
        # Creamos los elementos del menu 1 agregar
        menu = Frame(self)   

        Label(menu, bg='#F8FDFF', text='  Buscar Dni'         ).place(       width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Numero Dni'         ).place(y= 55, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Apellido Paterno'   ).place(y=110, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Apellido Materno'   ).place(y=165, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Nombre'             ).place(y=220, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Fecha de Nacimiento').place(y=275, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Fecha de Ingreso'   ).place(y=330, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Planilla'           ).place(y=385, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  A. Fami.'           ).place(x= 62, y=385)
        Label(menu, bg='#F8FDFF', text='  Movili.'            ).place(x=123, y=385)
        Label(menu, bg='#F8FDFF', text='  Cargo Laboral'      ).place(y=440, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Cuenta Bancaria'    ).place(y=495, width=200, height=55)
        Label(menu, bg='#F8FDFF', text='  Aportacion'         ).place(x=201, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Comision'           ).place(x=312)
        Label(menu, bg='#F8FDFF', text='  C.u.s.p.p.'         ).place(x=201, y= 55, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Catego.'            ).place(x=327, y= 55)
        Label(menu, bg='#F8FDFF', text='  Revalidacion'       ).place(x=201, y=110, width=200, height=54)        
        Label(menu, bg='#F8FDFF', text='  Licencia'           ).place(x=297, y=110)
        Label(menu, bg='#F8FDFF', text='  Area'               ).place(x=201, y=165, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Celular'            ).place(x=297, y=165)
        Label(menu, bg='#F8FDFF', text='  Distrito'           ).place(x=201, y=220, width=200, height=54)
        Label(menu, bg='#F8FDFF', text='  Fecha de Cese'      ).place(x=201, y=275, width=200, height=54)                
       
        self.buscar       = Button(menu, text='BUSCAR', bg='#88C7FF', command=self.SearchDni)
        self.buscarDni    = Entry(menu)     
        self.numeroDni    = Label(menu, bg='#FFFFFF', fg='#000000', anchor='w')        
        self.apPaterno    = Label(menu, bg='#FFFFFF', fg='#000000', anchor='w')
        self.apMaterno    = Label(menu, bg='#FFFFFF', fg='#000000', anchor='w')
        self.nombre       = Label(menu, bg='#FFFFFF', fg='#000000', anchor='w')
        self.fechaNaci    = Entry(menu)
        self.fechaIngr    = Entry(menu)
        self.planilla     = Entry(menu)        
        self.asignacion   = Entry(menu)
        self.movilidad    = Entry(menu)
        self.cargo        = Combobox(menu, state='readonly', values=['INSPECTOR VIAL', 'OPERADOR DE GRUA LIVIANA', 'OPERADOR DE GRUA PESADA', ''])       
        self.cuenta       = Entry(menu)
        self.aportacion   = Combobox(menu, state='readonly', values=['ONP', 'HABITAT', 'INTEGRA', 'PRIMA', 'PROFUTURO',''])
        self.comision     = Combobox(menu, state='readonly', values=['FLUJO', 'MIXTA', ''])
        self.cuspp        = Entry(menu)
        self.categoria    = Combobox(menu, state='readonly', values=['AIIA', 'AIIB', 'AIIIA', 'AIIIB', 'AIIIC', ''])       
        self.revalidacion = Entry(menu)
        self.codigo       = Entry(menu)
        self.area         = Combobox(menu, state='readonly', values=['SUR', 'NORTE', 'TALLER', 'OFICINA', ''])       
        self.celular      = Entry(menu)
        self.distrito     = Combobox(menu, state='readonly', values=['ANCON', 'ATE VITARTE', 'CARABAYLLO', 'CHORRILLOS', 'COMAS', 'LOS OLIVOS',
                                        'LURIGANCHO', 'LURIN', 'PUCUSANA', 'PUENTE PIEDRA', 'RIMAC', 'SAN BARTOLO', 'SAN JUAN DE LURIGANCHO',
                                        'SAN JUAN DE MIRAFLORES', 'SAN MARTIN DE PORRES', 'SANTA ANITA', 'SANTIAGO DE SURCO', 'SURQUILLO',
                                        'VILLA EL SALVADOR', 'VILLA MARIA DEL TRIUNFO', ''])      
        self.retiro = Entry(menu)                       

        # Posicionamiento de los elementos      
        self.buscar.place      (x=136, y= 23, width= 54, height=24)    
        self.buscarDni.place   (x= 10, y= 23, width=120, height=24)    
        self.numeroDni.place   (x= 10, y= 78, width=180, height=24)
        self.apPaterno.place   (x= 10, y=133, width=180, height=24)
        self.apMaterno.place   (x= 10, y=188, width=180, height=24)
        self.nombre.place      (x= 10, y=243, width=180, height=24)        
        self.fechaNaci.place   (x= 10, y=298, width=180, height=24)        
        self.fechaIngr.place   (x= 10, y=353, width=180, height=24)
        self.planilla.place    (x= 10, y=408, width= 56, height=24)  
        self.asignacion.place  (x= 72, y=408, width= 56, height=24)      
        self.movilidad.place   (x=134, y=408, width= 56, height=24) 
        self.cargo.place       (x= 10, y=463, width=180, height=24)        
        self.cuenta.place      (x= 10, y=518, width=180, height=24)
        self.aportacion.place  (x=211, y= 23, width=105, height=24) 
        self.comision.place    (x=322, y= 23, width= 69, height=24) 
        self.cuspp.place       (x=211, y= 78, width=120, height=24)
        self.categoria.place   (x=337, y= 78, width= 54, height=24)
        self.revalidacion.place(x=211, y=133, width= 90, height=24)
        self.codigo.place      (x=307, y=133, width= 84, height=24)
        self.area.place        (x=211, y=188, width= 90, height=24)
        self.celular.place     (x=307, y=188, width= 84, height=24)
        self.distrito.place    (x=211, y=243, width=180, height=24)
        self.retiro.place      (x=211, y=298, width=180, height=24)         
            
        # Creamos los botones principales
        Button(menu, text='GRABAR', command=self.SaveEmployee).place(x=453, width=90, height=30)     
        Button(menu, text='SALIR' , command=lambda:menu.destroy(), bg='#DF2F2F').place(x=453, y=35, width=90, height=30)

        # Foco en cuadro de busqueda y Superponemos la ventana principal
        self.buscarDni.focus_set()
        menu.grab_set()
        
        # Asignamos variablo global a menu para destruir
        self.agregar = menu

        # Posicionamos la ventana principal
        menu.place(x=437, y=20, width=563, height=550)

    def Modify(self):
        
        # Cargamos datos del trabajador a la ventana agregar
        if self.employee.selection():            
                
                # Id del trabajador           
                id = int(self.employee.item(self.employee.focus()).get('text'))
                datos = select(f'SELECT * FROM ACTIVO WHERE ID = {id}', False)

                # Mostramos datos del trabajador
                self.Add()     
                self.buscar.configure(state='disabled')
                self.buscarDni.configure(state='disabled')
                self.numeroDni['text'] = datos[1]
                self.apPaterno['text'] = datos[2]
                self.apMaterno['text'] = datos[3]
                self.nombre['text'] = datos[4]
                self.fechaNaci.insert(0, datos[5])
                self.fechaIngr.insert(0, datos[6])
                self.planilla.insert(0, datos[7])
                self.asignacion.insert(0, datos[8])
                self.movilidad.insert(0, datos[9])
                self.aportacion.set(datos[10])
                self.comision.set(datos[11])                                        
                self.cuspp.insert(0, datos[12])
                self.cargo.set(datos[13])
                self.cuenta.insert(0, datos[14])                
                self.area.set(datos[15])
                self.codigo.insert(0, datos[16])                    
                self.revalidacion.insert(0, datos[17])
                self.categoria.set(datos[18])
                self.celular.insert(0, datos[19])
                self.distrito.set(datos[20])
                self.retiro.insert(0, datos[21])

    def Remove(self):

        # Consulta para eliminar registro
        if self.employee.selection():
            respuesta = messagebox.askyesno('ELIMINAR','SEGURO?', default='no')

            if respuesta:
                # Id del trabajador
                id = int(self.employee.item(self.employee.focus()).get('text'))

                # Enviamos registro a cesado
                if self.retiro['text'] != '':
                    insert(f'INSERT INTO CESADO SELECT * FROM ACTIVO WHERE ID = {id}')

                # Eliminamos sus datos
                delete(f'DELETE FROM ACTIVO WHERE ID = {id}', True)

                # Limpiamos y cargamos AllDetails
                self.RemoveDetails()
                self.ShowDetails()

    def LoadEmployee(self):
        
        # Limpiamos el treeview
        self.employee.delete(*self.employee.get_children())
        
        # Obtenemos datos de todos los trabajadores
        datos = select('SELECT ID, NDNI, APAT, AMAT, NOMB FROM ACTIVO ORDER BY APAT, AMAT, NOMB ASC', True)

        # cargamos datos al treeview
        for index, dato in enumerate(datos, 1):
            nombre = f'{dato[2]} {dato[3]} {dato[4]}'    
            self.employee.insert('', 'end', text=dato[0], values=(index, nombre, dato[1]))   

    def RemoveDetails(self):

            # Limpiamos los cuadros de AllDetails
            self.detail01['text'] = ''
            self.detail02['text'] = ''
            self.detail03['text'] = ''
            self.detail04['text'] = ''
            self.detail05['text'] = ''
            self.detail06['text'] = ''
            self.detail07['text'] = ''
            self.detail08['text'] = ''
            self.detail09['text'] = ''            
            self.detail10['text'] = ''
            self.detail11['text'] = ''
            self.detail12['text'] = ''
            self.detail13['text'] = ''
            self.detail14['text'] = ''
            self.detail15['text'] = ''
            self.detail16['text'] = ''
            self.detail17['text'] = ''
            self.detail18['text'] = ''
            self.detail19['text'] = ''
            self.detail20['text'] = ''

    def SearchDni(self):
      
        # Validamos el numero de dni ingresado
        dni = self.buscarDni.get()
        if dni == '':
            messagebox.showinfo('BUSCAR', 'INGRESA EL NUMERO DE DNI')    
            self.buscarDni.focus()       
        elif len(dni) != 8 or not dni.isdigit():  
            messagebox.showinfo('BUSCAR', 'INGRESA CORRECTAMENTE EL NUMERO DE DNI') 
            self.buscarDni.focus()      
        else:

            # Buscar datos del dni
            persona = BuscarDni(dni)

            if persona:
                self.numeroDni['text'] = persona['numeroDocumento']
                self.apPaterno['text'] = persona['apellidoPaterno']
                self.apMaterno['text'] = persona['apellidoMaterno']
                self.nombre['text'] = persona['nombres']
                self.buscarDni.delete(0, END)
                self.fechaNaci.focus_set()
            else:                
                messagebox.showinfo('BUSCAR', 'NO SE ENCONTRO EL NUMERO DE DNI')           
                self.buscarDni.focus()   

    def ShowDetails(self, e):
                
        # Mostramos AllDetails del trabajador selecionado
        if self.employee.selection():     

            self.RemoveDetails()
            
            # Id del trabajador             
            id = int(self.employee.item(self.employee.focus()).get('text'))
            
            # Obtener sus datos
            datos = select(f'SELECT * FROM ACTIVO WHERE ID = {id}', False)

            # Mostramos AllDetails del trabajador en los cuadros          
            self.detail01['text'] = datos[5]
            self.detail02['text'] = datos[6]
            self.detail03['text'] = f'{datos[7]:,.2f}'
            self.detail04['text'] = f'{datos[8]:,.2f}'
            self.detail05['text'] = f'{datos[9]:,.2f}'
            self.detail06['text'] = f'{datos[7] + datos[8] + datos[9]:,.2f}'
            self.detail07['text'] = datos[13]
            self.detail08['text'] = datos[10]
            self.detail09['text'] = datos[11]
            self.detail10['text'] = datos[12]
            self.detail11['text'] = datos[14]
            self.detail12['text'] = datos[16]
            self.detail13['text'] = datos[18]
            self.detail14['text'] = datos[17]
            self.detail15['text'] = datos[15]
            self.detail16['text'] = datos[19]
            self.detail17['text'] = datos[20]
            self.detail18['text'] = Edad(datos[5])
            self.detail19['text'] = Tiempo(datos[6])
            self.detail20['text'] = datos[21]

    def SaveEmployee(self):

        # Validacion de dni
        if self.numeroDni['text'] == '':
            messagebox.showinfo('GRABAR', 'REGISTRA EL DNI')
            self.buscarDni.focus()

        # Validacion de fecha de nacimiento
        elif self.fechaNaci.get() == '':
            messagebox.showinfo('GRABAR', 'REGISTRA EL NACIMIENTO')
            self.fechaNaci.focus()
        elif len(self.fechaNaci.get()) != 10 or not FechaValida(self.fechaNaci.get(), False):
            messagebox.showinfo('GRABAR', 'REGISTRA CORRECTAMENTE EL NACIMIENTO')
            self.fechaNaci.focus()

        # Validacion de fecha de ingreso
        elif self.fechaIngr.get() == '':
            messagebox.showinfo('GRABAR', 'REGISTRA EL INGRESO')
            self.fechaIngr.focus()
        elif len(self.fechaIngr.get()) != 10 or not FechaValida(self.fechaIngr.get(), False):
            messagebox.showinfo('GRABAR', 'REGISTRA CORRECTAMENTE EL INGRESO')
            self.fechaIngr.focus()

        # Validacion de sueldo planilla
        elif self.planilla.get() == '':
            messagebox.showinfo('GRABAR', 'REGISTRA LA PLANILLA')
            self.planilla.focus()
        elif not self.planilla.get().replace('.','').isdigit() or self.planilla.get().count('.') > 1:
            messagebox.showinfo('GRABAR', 'REGISTRA CORRECTAMENTE LA PLANILLA')
            self.planilla.focus()

        # Validacion de asignacion familiar
        elif self.asignacion.get() == '':
            messagebox.showinfo('GRABAR', 'REGISTRA LA ASIGNACION')
            self.asignacion.focus()
        elif not self.asignacion.get().replace('.','').isdigit() or self.asignacion.get().count('.') > 1:
            messagebox.showinfo('GRABAR', 'REGISTRA CORRECTAMENTE LA ASIGNACION')
            self.asignacion.focus()

        # Validacion de movilidad
        elif self.movilidad.get() == '':
            messagebox.showinfo('GRABAR', 'REGISTRA LA MOVILIDAD')
            self.movilidad.focus()
        elif not self.movilidad.get().replace('.','').isdigit() or self.movilidad.get().count('.') > 1:
            messagebox.showinfo('GRABAR', 'REGISTRA CORRECTAMENTE LA MOVILIDAD')
            self.movilidad.focus()

        # Validacion de fecha del cese      
        elif self.retiro.get() != '' and not FechaValida(self.retiro.get(), True):
            messagebox.showinfo('GRABAR', 'REGISTRA CORRECTAMENTE EL RETIRO')
            self.retiro.focus()
        else:

            # Verificacion de dni ya registrado
            if self.buscar['state'] == 'normal':
                for index in self.employee.get_children():
                    if f"{self.employee.item(index).get('values')[2]:0>8}" == self.numeroDni['text']:
                        messagebox.showinfo('GRABAR', 'DNI YA REGISTRADO')
                        return            

            persona = datos(self.numeroDni.cget('text'),
                           self.apPaterno.cget('text'),
                           self.apMaterno.cget('text'),
                           self.nombre.cget('text'),
                           self.fechaNaci.get(),
                           self.fechaIngr.get(),
                           float(self.planilla.get()),
                           float(self.asignacion.get()),
                           float(self.movilidad.get()),
                           self.cargo.get(),
                           self.cuenta.get(),
                           self.aportacion.get(),
                           self.comision.get(),
                           self.cuspp.get().upper(),
                           self.categoria.get(),
                           self.revalidacion.get(),
                           self.codigo.get().upper(),
                           self.area.get(),
                           self.celular.get(),
                           self.distrito.get(),
                           self.retiro.get())

            values = persona.convert(persona)       

            # Id del trabajador seleccionado
            seleccion = self.employee.focus()

            if seleccion:
                id = int(self.employee.item(seleccion).get('text'))

            # Insertar nuevo trabajador
            if self.buscar['state'] == 'normal':
                query = f'''INSERT INTO ACTIVO (NDNI, APAT, AMAT, NOMB, FNAC, FING, SPLA, AFAM, SMOV, EAPO,
                            TCOM, NCUS, PLAB, NCUE, ALAB, NLIC, VLIC, CLIC, NCEL, DRES, FCES) VALUES {values}'''
                insert(query)

            # Actualizar datos de trabajador
            else:
                query = f'''UPDATE ACTIVO SET FNAC = '{persona.nacimiento}', FING = '{persona.ingreso}', SPLA = {persona.planilla},
                            AFAM = '{persona.asignacion}', SMOV = {persona.movilidad}, EAPO = '{persona.aportacion}',
                            TCOM = '{persona.comision}', NCUS = '{persona.cuspp}', PLAB = '{persona.cargo}', NCUE = '{persona.cuenta}',
                            ALAB = '{persona.area}', NLIC = '{persona.codigo}', VLIC = '{persona.revalidacion}', CLIC = '{persona.categoria}',
                            NCEL = '{persona.celular}', DRES = '{persona.distrito}', FCES = '{persona.retiro}'
                            WHERE ID = {id}'''           
                update(query)

            # Ordenamos los datos con el nuevo registro
            self.LoadEmployee()
            self.RemoveDetails()

            # Devolvemos la seleccion del trabajador
            if seleccion:
                for index in self.employee.get_children():
                    if int(self.employee.item(index).get('text')) == id:
                        self.employee.selection_set(index)
                        self.employee.focus(index)

            # Cerrar ventana                           
            self.agregar.destroy()


    def Menu2(self):

        # Creamos los elementos del menu 1
        window = Frame(self)

        self.details = Treeview(window, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12'))
        self.details.column('#0' , width=0)
        self.details.column('#1' , width= 30, minwidth= 30)
        self.details.column('#2' , width=270, minwidth=270)
        self.details.column('#3' , width= 40, minwidth= 40, anchor='center')
        self.details.column('#4' , width= 40, minwidth= 40, anchor='center')
        self.details.column('#5' , width= 40, minwidth= 40, anchor='center')
        self.details.column('#6' , width= 70, minwidth= 70, anchor='center')
        self.details.column('#7' , width= 70, minwidth= 70, anchor='center')
        self.details.column('#8' , width= 40, minwidth= 40, anchor='center')
        self.details.column('#9' , width= 40, minwidth= 40, anchor='center')
        self.details.column('#10', width= 40, minwidth= 40, anchor='center')
        self.details.column('#11', width= 70, minwidth= 70, anchor='center')
        self.details.column('#12', width= 70, minwidth= 70, anchor='center')
        self.details.heading('#1' , text='N°')
        self.details.heading('#2' , text='Apellidos y Nombre')
        self.details.heading('#3' , text='Apo.')
        self.details.heading('#4' , text='Fal.')
        self.details.heading('#5' , text='Fer.')
        self.details.heading('#6' , text='Ingreso')
        self.details.heading('#7' , text='Descuento')
        self.details.heading('#8' , text='D.M.')
        self.details.heading('#9' , text='Vac.')
        self.details.heading('#10', text='C.V.')
        self.details.heading('#11', text='Adelanto')
        self.details.heading('#12', text='Xfuera')

        scroll = Scrollbar(window, orient='vertical', command=self.details.yview)
        self.details.configure(yscrollcommand=scroll.set)

        # Posicionamiento de los elementos
        scroll.place(x=846, y=20, height=550)
        self.details.place(x=20, y=20, height=550)

        # Cargamos datos al treeview
        self.LoadDetails()

        Button(window, text='GENERAR'                              ).place(x=890, y=20, width=90, height=30)
        Button(window, text='MODIFICAR', command=self.OpenDetails).place(x=890, y=55, width=90, height=30)
        Button(window, text='REPORTE'                              ).place(x=890, y=90, width=90, height=30)
        Button(window, text='SALIR'    , command=lambda:window.destroy(), bg='#DF2F2F').place(x=890, y=125, width=90, height=30)
       
        # Creamos ventana de AllDetails y lo ocultamos
        self.AllDetails()
        self.HideDetails()

        # Posicionamos la ventana principal
        window.place(width=1000, height=600)

    def AllDetails(self):
        
        # Creamos los elementos del menu 2 AllDetails
        window = Frame(self)   

        self.calendario = Calendar(window, menuselectmode='day', date_pattern='dd/MM/yyyy', cursor='hand2', borderwidth=0)
      
        Button(window, text='APOYO'            , command=lambda:self.SaveDetails('APO')).place(x=286, y= 20, width=100, height=22)
        Button(window, text='FALTA'            , command=lambda:self.SaveDetails('FAL')).place(x=406, y= 20, width=100, height=22)
        Button(window, text='FERIADO'          , command=lambda:self.SaveDetails('FER')).place(x=526, y= 20, width=100, height=22)
        Button(window, text='ADELANTO'         , command=lambda:self.SaveDetails('ADE')).place(x=646, y= 20, width=160, height=22)
        Button(window, text='INGRESO'          , command=lambda:self.SaveDetails('ING')).place(x= 20, y=237, width=265, height=22)
        Button(window, text='DESCUENTO'        , command=lambda:self.SaveDetails('DES')).place(x=303, y=237, width=266, height=22)
        Button(window, text='VACACIONES'       , command=lambda:self.SaveDetails('VAC')).place(x=586, y=237, width=220, height=22)
        Button(window, text='DESCANSO MEDICO'  , command=lambda:self.SaveDetails('DME')).place(x= 20, y=418, width=548, height=22)
        Button(window, text='COMPRA VACACIONES', command=lambda:self.SaveDetails('CVA')).place(x=586, y=418, width=220, height=22)
        
        self.date01 = Label(window, cursor='hand2', anchor='e')
        self.date02 = Label(window, cursor='hand2', anchor='e')
        self.date03 = Label(window, cursor='hand2', anchor='e')
        self.date04 = Label(window, cursor='hand2', anchor='e')
        self.date05 = Label(window, cursor='hand2', anchor='e')
        self.date06 = Label(window, cursor='hand2', anchor='e')

        # Evento de click del label para seleccionar fecha
        self.date01.bind('<Button-1>', lambda e: self.SelectDate('vaca1'))
        self.date02.bind('<Button-1>', lambda e: self.SelectDate('vaca2')) 
        self.date03.bind('<Button-1>', lambda e: self.SelectDate('dmed1'))        
        self.date04.bind('<Button-1>', lambda e: self.SelectDate('dmed2'))        
        self.date05.bind('<Button-1>', lambda e: self.SelectDate('cvac1'))
        self.date06.bind('<Button-1>', lambda e: self.SelectDate('cvac2'))

        self.apoyo = Treeview(window, columns=('#1'))
        self.apoyo.column('#0', width=0)
        self.apoyo.column('#1', width=94, minwidth=94, anchor='center')
        self.apoyo.heading('#1', text='Fecha')
        self.falta = Treeview(window, columns=('#1'))
        self.falta.column('#0', width=0)
        self.falta.column('#1', width=94, minwidth=94, anchor='center')
        self.falta.heading('#1', text='Fecha')
        self.feriado = Treeview(window, columns=('#1'))
        self.feriado.column('#0', width=0)
        self.feriado.column('#1', width=94, minwidth=94, anchor='center')
        self.feriado.heading('#1', text='Fecha')
        self.adelanto = Treeview(window, columns=('#1', '#2'))
        self.adelanto.column('#0', width=0)
        self.adelanto.column('#1', width=82, anchor='center')         
        self.adelanto.column('#2', width=71, anchor='e')
        self.adelanto.heading('#1', text='Fecha')
        self.adelanto.heading('#2', text='Importe')        
        self.ingreso = Treeview(window, columns=('#1', '#2'))
        self.ingreso.column('#0', width=0)
        self.ingreso.column('#1', width=199, minwidth=199) 
        self.ingreso.column('#2', width= 60, minwidth= 60, anchor='e')
        self.ingreso.heading('#1', text='Fecha')
        self.ingreso.heading('#2', text='Importe')
        self.descuento = Treeview(window, columns=('#1', '#2'))
        self.descuento.column('#0', width=0)
        self.descuento.column('#1', width=199, minwidth=199) 
        self.descuento.column('#2', width= 60, minwidth= 60, anchor='e')
        self.descuento.heading('#1', text='Detalle')
        self.descuento.heading('#2', text='Importe')        
        self.vacaciones = Treeview(window, columns=('#1', '#2', '#3'))
        self.vacaciones.column('#0', width=0)
        self.vacaciones.column('#1', width=84, minwidth=84) 
        self.vacaciones.column('#2', width=84, minwidth=84) 
        self.vacaciones.column('#3', width=46, minwidth=46, anchor='e') 
        self.vacaciones.heading('#1', text='F. Inicial')
        self.vacaciones.heading('#2', text='F. Final')
        self.vacaciones.heading('#3', text='Dias')        
        self.dmedico = Treeview(window, columns=('#1', '#2', '#3', '#4'))
        self.dmedico.column('#0', width=0)
        self.dmedico.column('#1', width= 84, minwidth= 84) 
        self.dmedico.column('#2', width= 84, minwidth= 84) 
        self.dmedico.column('#3', width=314, minwidth=314) 
        self.dmedico.column('#4', width= 60, minwidth= 60, anchor='e') 
        self.dmedico.heading('#1', text='F. Inicial')
        self.dmedico.heading('#2', text='F. Final')
        self.dmedico.heading('#3', text='Detalle')
        self.dmedico.heading('#4', text='Dias')
        self.cvacaciones = Treeview(window, columns=('#1', '#2', '#3'))
        self.cvacaciones.column('#0', width=0)
        self.cvacaciones.column('#1', width=84, minwidth=84) 
        self.cvacaciones.column('#2', width=84, minwidth=84) 
        self.cvacaciones.column('#3', width=46, minwidth=46, anchor='e') 
        self.cvacaciones.heading('#1', text='F. Inicial')
        self.cvacaciones.heading('#2', text='F. Final')
        self.cvacaciones.heading('#3', text='Dias')

        self.adelantoImporte  = Entry(window, justify='right')
        self.ingresoDetalle   = Entry(window)
        self.ingresoImporte   = Entry(window, justify='right')
        self.descuentoDetalle = Entry(window)
        self.descuentoImporte = Entry(window, justify='right')        
        self.vacacionesTotal  = Entry(window, justify='right')
        self.dmedicoDetalle   = Entry(window)
        self.dmedicoTotal     = Entry(window, justify='right')
        self.cvacacionesTotal = Entry(window, justify='right')

        # Evento de click del treeview para quitar seleccion
        self.apoyo.bind('<Button-1>', self.RemoveSelection)
        self.falta.bind('<Button-1>', self.RemoveSelection) 
        self.feriado.bind('<Button-1>', self.RemoveSelection)
        self.adelanto.bind('<Button-1>', self.RemoveSelection)
        self.ingreso.bind('<Button-1>', self.RemoveSelection)
        self.descuento.bind('<Button-1>', self.RemoveSelection)
        self.vacaciones.bind('<Button-1>', self.RemoveSelection)
        self.dmedico.bind('<Button-1>', self.RemoveSelection)
        self.cvacaciones.bind('<Button-1>', self.RemoveSelection)
        
        # Posicionamos todos los elementos
        self.calendario.place(x=20, y=20)

        self.apoyo.place      (x=286, y= 52, height=150)
        self.falta.place      (x=406, y= 52, height=150)
        self.feriado.place    (x=526, y= 52, height=150)
        self.adelanto.place   (x=646, y= 72, height=130)   
        self.ingreso.place    (x= 20, y=289, height= 90)
        self.descuento.place  (x=303, y=289, height= 90)
        self.vacaciones.place (x=586, y=289, height= 90)
        self.dmedico.place    (x= 20, y=470, height= 90)
        self.cvacaciones.place(x=586, y=470, height= 90)

        self.date01.place(x=586, y=267, width=86, height=17)
        self.date02.place(x=673, y=267, width=83, height=17)
        self.date03.place(x= 20, y=447, width=86, height=17)
        self.date04.place(x=107, y=447, width=83, height=17)
        self.date05.place(x=586, y=447, width=86, height=17)
        self.date06.place(x=673, y=447, width=83, height=17)

        self.adelantoImporte.place (x=732, y= 50, width= 73, height=17)   
        self.ingresoDetalle.place  (x= 20, y=267, width=201, height=17)        
        self.ingresoImporte.place  (x=222, y=267, width= 63, height=17)
        self.descuentoDetalle.place(x=303, y=267, width=201, height=17)        
        self.descuentoImporte.place(x=505, y=267, width= 63, height=17)        
        self.vacacionesTotal.place (x=757, y=267, width= 49, height=17)
        self.dmedicoDetalle.place  (x=191, y=447, width=313, height=17)
        self.dmedicoTotal.place    (x=505, y=447, width= 63, height=17)
        self.cvacacionesTotal.place(x=757, y=447, width= 49, height=17)        
                    
        # Creamos los botones principales
        Button(window, text='ELIMINAR',            command=self.DeleteDetails).place(x=890, y=20, width=90, height=30)     
        Button(window, text='SALIR', bg='#DF2F2F', command=self.HideDetails ).place(x=890, y=55, width=90, height=30)

        # Asignamos variable para poder destruir la ventana
        self.men2_AllDetails = window

        # Posicionamos la ventana principal
        window.place(width=1000, height=600)         

    def LoadDetails(self):

        # Limpiamos el treeview
        self.details.delete(*self.details.get_children())
        
        # Obtenemos datos de todos los trabajadores
        datos = select('SELECT ID, APAT, AMAT, NOMB FROM ACTIVO ORDER BY APAT, AMAT, NOMB ASC', True)

        # Insertamos datos al treeview
        for index, dato in enumerate(datos, 1):
            id = dato[0]           
            nombre = f'{dato[1]} {dato[2]} {dato[3]}'  

            apoy = select(F'SELECT COUNT(FECH) FROM APOYO WHERE IDAC = {id}', False)
            falt = select(F'SELECT COUNT(FECH) FROM FALTA WHERE IDAC = {id}', False)         
            feri = select(F'SELECT COUNT(FECH) FROM FERIADO WHERE IDAC = {id}', False)   
            ingr = select(F'SELECT SUM(MONT) FROM INGRESO WHERE IDAC = {id}', False)
            desc = select(F'SELECT SUM(MONT) FROM DESCUENTO WHERE IDAC = {id}', False)
            dmed = select(F'SELECT SUM(DTOT) FROM DMEDICO WHERE IDAC = {id}', False)
            vaca = select(F'SELECT SUM(DTOT) FROM VACACIONES WHERE IDAC = {id}', False)
            cvac = select(F'SELECT SUM(DTOT) FROM CVACACIONES WHERE IDAC = {id}', False)
            adel = select(F'SELECT SUM(MONT) FROM ADELANTO WHERE IDAC = {id}', False)
            xfue = select(F'SELECT SUM(MONT) FROM XFUERA WHERE IDAC = {id}', False)

            if apoy[0] == 0:
                apoy = ''
            else:
                apoy = apoy[0]

            if falt[0] == 0:
                falt = ''
            else:
                falt = falt[0]   

            if feri[0] == 0:
                feri = ''
            else:
                feri = feri[0]  

            if ingr[0]:
                ingr = f'{ingr[0]:.2f}'
            else:
                ingr = ''

            if desc[0]:
                desc = f'{desc[0]:.2f}'
            else:
                desc = ''   

            if dmed[0]:
                dmed = dmed[0]
            else:
                dmed = ''                

            if vaca[0]:
                vaca = vaca[0]
            else:
                vaca = ''
                
            if cvac[0]:
                cvac = cvac[0]
            else:
                cvac = ''
                
            if adel[0]:
                adel = f'{adel[0]:.2f}'
            else:
                adel = ''                

            if xfue[0]:
                xfue = f'{xfue[0]:.2f}'
            else:
                xfue = ''                
            
            self.details.insert('', END, text=id, values=(index, nombre, apoy, falt, feri, ingr, desc, dmed, vaca, cvac, adel, xfue)) 

    def OpenDetails(self):
      
        # Mostramos la ventana AllDetails
        if self.details.selection():            
            id = int(self.details.item(self.details.focus()).get('text'))

            # Ejecutamos consultas de los AllDetails de cada trabajador en base de datos
            apoy = select(F'SELECT ID, FECH FROM APOYO WHERE IDAC = {id}', True)
            falt = select(F'SELECT ID, FECH FROM FALTA WHERE IDAC = {id}', True) 
            feri = select(F'SELECT ID, FECH FROM FERIADO WHERE IDAC = {id}', True) 
            adel = select(F'SELECT ID, FECH, MONT FROM ADELANTO WHERE IDAC = {id}', True) 
            ingr = select(F'SELECT ID, DETA, MONT FROM INGRESO WHERE IDAC = {id}', True)
            desc = select(F'SELECT ID, DETA, MONT FROM DESCUENTO WHERE IDAC = {id}', True) 
            vaca = select(F'SELECT ID, FINI, FFIN, DTOT FROM VACACIONES WHERE IDAC = {id}', True) 
            dmed = select(F'SELECT ID, FINI, FFIN, DETA, DTOT FROM DMEDICO WHERE IDAC = {id}', True)
            cvac = select(F'SELECT ID, FINI, FFIN, DTOT FROM CVACACIONES WHERE IDAC = {id}', True) 

            for dato in apoy:
                self.apoyo.insert('', END, text=dato[0], values=(dato[1])) 

            for dato in falt:
                self.falta.insert('', END, text=dato[0], values=(dato[1]))

            for dato in feri:
                self.feriado.insert('', END, text=dato[0], values=(dato[1]))    

            for dato in adel:
                self.adelanto.insert('', END, text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))      

            for dato in ingr:
                self.ingreso.insert('', END, text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))    

            for dato in desc:
                self.descuento.insert('', END, text=dato[0], values=(dato[1], f'{dato[2]:.2f}')) 

            for dato in vaca:
                self.vacaciones.insert('', END, text=dato[0], values=(dato[1], dato[2], dato[3])) 

            for dato in dmed:
                self.dmedico.insert('', END, text=dato[0], values=(dato[1], dato[2], dato[3], dato[4])) 

            for dato in cvac:
                self.cvacaciones.insert('', END, text=dato[0], values=(dato[1], dato[2], dato[3]))     
          
            self.men2_AllDetails.place(width=980, height=580) 
            self.men2_AllDetails.grab_set()

    def HideDetails(self):
        
        # Limpiamos los cuadros de la ventana AllDetails
        self.apoyo.delete(*self.apoyo.get_children())
        self.falta.delete(*self.falta.get_children())
        self.feriado.delete(*self.feriado.get_children())
        self.adelanto.delete(*self.adelanto.get_children())
        self.ingreso.delete(*self.ingreso.get_children())
        self.descuento.delete(*self.descuento.get_children())
        self.vacaciones.delete(*self.vacaciones.get_children())
        self.dmedico.delete(*self.dmedico.get_children())
        self.cvacaciones.delete(*self.cvacaciones.get_children())

        self.date01['text'] = ''
        self.date02['text'] = ''
        self.date03['text'] = ''
        self.date04['text'] = ''
        self.date05['text'] = ''
        self.date06['text'] = ''

        self.adelantoImporte.delete(0, END)
        self.ingresoDetalle.delete(0, END)
        self.ingresoImporte.delete(0, END)
        self.descuentoDetalle.delete(0, END)
        self.descuentoImporte.delete(0, END)        
        self.vacacionesTotal.delete(0, END)       
        self.dmedicoDetalle.delete(0, END)
        self.dmedicoTotal.delete(0, END)
        self.cvacacionesTotal.delete(0, END)
        
        # Ocultamos la ventana AllDetails
        self.men2_AllDetails.place_forget() 
        self.men2_AllDetails.grab_release()   

    def RemoveSelection(self, e):
        
        # Quitar seleccion de otros treeview
        self.apoyo.selection_set('') 
        self.falta.selection_set('')      
        self.feriado.selection_set('')       
        self.adelanto.selection_set('')        
        self.ingreso.selection_set('')
        self.descuento.selection_set('')
        self.vacaciones.selection_set('')
        self.dmedico.selection_set('')
        self.cvacaciones.selection_set('')

    def SelectDate(self, boton: str):

        fecha = self.calendario.get_date()

        if boton == 'vaca1':
            self.date01['text'] = fecha            
        elif boton == 'vaca2':
            self.date02['text'] = fecha
        elif boton == 'dmed1':  
            self.date03['text'] = fecha
        elif boton == 'dmed2':  
            self.date04['text'] = fecha
        elif boton == 'cvac1':  
            self.date05['text'] = fecha
        elif boton == 'cvac2':  
            self.date06['text'] = fecha

    def SaveDetails(self, widget: str):

        valores = self.details.item(self.details.focus())['values']
        id = int(self.details.item(self.details.focus()).get('text'))
        fecha = self.calendario.get_date()

        if widget == 'APO':
            for row in self.apoyo.get_children():
                if self.apoyo.item(row)['values'][0] == fecha:
                    return

            if valores[2] == '':
                valores[2] = 1
            else:
                valores[2] = int(valores[2]) + 1

            insert(f'INSERT INTO APOYO (IDAC, FECH) VALUES ({id}, "{fecha}")')
            idRegistro = select(f'SELECT ID FROM APOYO ORDER BY ID DESC', False)
            self.apoyo.insert('', END, text=idRegistro[0], values=fecha)
                   
        elif widget == 'FAL':
            for row in self.falta.get_children():
                if self.falta.item(row)['values'][0] == fecha:
                    return
        
            if valores[3] == '':
                valores[3] = 1
            else:
                valores[3] = int(valores[3]) + 1           

            insert(f'INSERT INTO FALTA (IDAC, FECH) VALUES ({id}, "{fecha}")')
            idRegistro = select(f'SELECT ID FROM FALTA ORDER BY ID DESC', False)
            self.falta.insert('', END, text=idRegistro[0], values=fecha)

        elif widget == 'FER':
            for row in self.feriado.get_children():
                if self.feriado.item(row)['values'][0] == fecha:
                    return
        
            if valores[4] == '':
                valores[4] = 1
            else:
                valores[4] = int(valores[4]) + 1           

            insert(f'INSERT INTO FERIADO (IDAC, FECH) VALUES ({id}, "{fecha}")')
            idRegistro = select(f'SELECT ID FROM FERIADO ORDER BY ID DESC', False)
            self.feriado.insert('', END, text=idRegistro[0], values=fecha)

        elif widget == 'ADE':
            if self.adelantoImporte.get() == '':
                self.adelantoImporte.focus_set()
                messagebox.showinfo('ADELANTO', 'Registra el importe del adelanto !')
            elif self.adelantoImporte.get().count('.') > 1:
                self.adelantoImporte.focus_set()
                messagebox.showinfo('ADELANTO', 'Registra correctamente el importe del adelanto !')
            elif not self.adelantoImporte.get().replace('.','').isnumeric():
                self.adelantoImporte.focus_set()
                messagebox.showinfo('ADELANTO', 'Registra correctamente el importe del adelanto !')
            else:
                for row in self.adelanto.get_children():
                    if self.adelanto.item(row)['values'][0] == fecha:
                        return

                monto = float(self.adelantoImporte.get())

                if valores[10] == '':
                    valores[10] = f'{monto:.2f}'
                else:                    
                    valores[10] = f'{float(valores[10]) + monto:.2f}'

                insert(f'INSERT INTO ADELANTO (IDAC, FECH, MONT) VALUES ({id}, "{fecha}", {monto})')
                idRegistro = select(f'SELECT ID FROM ADELANTO ORDER BY ID DESC', False)
                self.adelanto.insert('', END,text=idRegistro[0], values=(fecha, f'{monto:.2f}'))
                self.adelantoImporte.delete(0, END)

        elif widget == 'ING':

            # Validamos los cuadros de ingreso si estan vacios enviar el foco
            if self.ingresoDetalle.get() == '':
                self.ingresoDetalle.focus_set()
                messagebox.showinfo('INGRESO', 'Registra el detalle del ingreso !')
            elif self.ingresoImporte.get() == '':
                self.ingresoImporte.focus_set()
                messagebox.showinfo('INGRESO', 'Registra el importe del ingreso !')
            elif self.ingresoImporte.get().count('.') > 1:
                self.ingresoImporte.focus_set()
                messagebox.showinfo('INGRESO', 'Registra correctamente el importe del ingreso !')
            elif not self.ingresoImporte.get().replace('.','').isnumeric():
                self.ingresoImporte.focus_set()
                messagebox.showinfo('INGRESO', 'Registra correctamente el importe del ingreso !')
            else:
                detalle = self.ingresoDetalle.get()
                monto = float(self.ingresoImporte.get())

                if valores[5] == '':
                    valores[5] = f'{monto:.2f}'
                else:                    
                    valores[5] = f'{float(valores[5]) + monto:.2f}'                   

                insert(f'INSERT INTO INGRESO (IDAC, DETA, MONT) VALUES ({id}, "{detalle}", {monto})')
                idRegistro = select(f'SELECT ID FROM INGRESO ORDER BY ID DESC', False)
                self.ingreso.insert('', END, text=idRegistro[0], values=(self.ingresoDetalle.get(), f'{monto:.2f}'))
                self.ingresoDetalle.delete(0, END)
                self.ingresoImporte.delete(0, END)

        elif widget == 'DES':

            # Validamos los cuadros de descuento si estan vacios enviar el foco
            if self.descuentoDetalle.get() == '':
                self.descuentoDetalle.focus_set()
                messagebox.showinfo('DESCUENTO', 'Registra el detalle del descuento !')
            elif self.descuentoImporte.get() == '':
                self.descuentoImporte.focus_set()
                messagebox.showinfo('DESCUENTO', 'Registra el importe del descuento !')
            elif self.descuentoImporte.get().count('.') > 1:
                self.descuentoImporte.focus_set()
                messagebox.showinfo('DESCUENTO', 'Registra correctamente el importe del descuento !')
            elif not self.descuentoImporte.get().replace('.','').isnumeric():
                self.descuentoImporte.focus_set()
                messagebox.showinfo('DESCUENTO', 'Registra correctamente el importe del descuento !')
            else:
                detalle = self.descuentoDetalle.get()
                monto = float(self.descuentoImporte.get())

                if valores[6] == '':
                    valores[6] = f'{monto:.2f}'
                else:                    
                    valores[6] = f'{float(valores[6]) + monto:.2f}'                  

                insert(f'INSERT INTO DESCUENTO (IDAC, DETA, MONT) VALUES ({id}, "{detalle}", {monto})')
                idRegistro = select(f'SELECT ID FROM DESCUENTO ORDER BY ID DESC', False)
                self.descuento.insert('', END, text=idRegistro[0], values=(self.descuentoDetalle.get(), f'{monto:.2f}'))
                self.descuentoDetalle.delete(0, END)
                self.descuentoImporte.delete(0, END)                    

        elif widget == 'VAC':

            # Validamos los cuadros de vacaciones si estan vacios enviar el foco           
            if self.date01['text'] == '':
                self.vacacionesTotal.focus_set() 
                messagebox.showinfo('VACACIONES', 'Selecciona la fecha inicial de las vacaciones !')
            elif self.date02['text'] == '':
                self.vacacionesTotal.focus_set() 
                messagebox.showinfo('VACACIONES', 'Selecciona la fecha final de las vacaciones !')
            elif self.vacacionesTotal.get() == '':
                self.vacacionesTotal.focus_set()   
                messagebox.showinfo('VACACIONES', 'Registra el total de dias de las vacaciones !')
            elif not self.vacacionesTotal.get().isnumeric():
                self.vacacionesTotal.focus_set()   
                messagebox.showinfo('VACACIONES', 'Registra correctamente el total de dias de las vacaciones !')
            else:
                fechaI = self.date01['text']
                fechaF = self.date02['text']

                total =int(self.vacacionesTotal.get())

                if valores[8] == '':
                    valores[8] = total
                else:                    
                    valores[8] = int(valores[8]) + total                

                insert(F'INSERT INTO VACACIONES (IDAC, FINI, FFIN, DTOT) VALUES ({id}, "{fechaI}", "{fechaF}", {total})')
                idRegistro = select(F'SELECT ID FROM VACACIONES ORDER BY ID DESC', False)
                self.vacaciones.insert('', END, text=idRegistro[0], values=(fechaI, fechaF, total))
                self.date01['text'] = ''
                self.date02['text'] = ''
                self.vacacionesTotal.delete(0, END)

        elif widget == 'DME':
            
            # Validamos los cuadros de descanso medico si estan vacios enviar el foco
            if self.date03['text'] == '':
                self.dmedicoDetalle.focus_set() 
                messagebox.showinfo('DESCANSO MEDICO', 'Selecciona la fecha inicial del descanso medico !')
            elif self.date04['text'] == '':
                self.dmedicoDetalle.focus_set() 
                messagebox.showinfo('DESCANSO MEDICO', 'Selecciona la fecha final del descanso medico !')
            elif self.dmedicoDetalle.get() == '':
                self.dmedicoDetalle.focus_set()   
                messagebox.showinfo('DESCANSO MEDICO', 'Registra el detalle del descanso medico !')
            elif self.dmedicoTotal.get() == '':
                self.dmedicoTotal.focus_set()   
                messagebox.showinfo('DESCANSO MEDICO', 'Registra el total de dias del descanso medico !')
            elif not self.dmedicoTotal.get().isnumeric():
                self.dmedicoTotal.focus_set()   
                messagebox.showinfo('DESCANSO MEDICO', 'Registra correctamente el total de dias del descanso medico !')
            else:
                dmedI = self.date03['text']
                dmedF = self.date04['text']
                
                detalle = self.dmedicoDetalle.get()
                total =int(self.dmedicoTotal.get())

                if valores[7] == '':
                    valores[7] = total
                else:                    
                    valores[7] = int(valores[7]) + total     

                insert(f'INSERT INTO DMEDICO (IDAC, FINI, FFIN, DETA, DTOT) VALUES ({id}, "{dmedI}", "{dmedF}", "{detalle}", {total})')
                idRegistro = select(f'SELECT ID FROM DMEDICO ORDER BY ID DESC', False)
                self.dmedico.insert('', END, text=idRegistro[0], values=(dmedI, dmedF, detalle, total))
                self.date03['text'] = ''
                self.date04['text'] = ''
                self.dmedicoDetalle.delete(0, END)
                self.dmedicoTotal.delete(0, END)
               

        elif widget == 'CVA':

             # Validamos los cuadros de compra de vacaciones si estan vacios enviar el foco
            if self.date05['text'] == '':
                self.cvacacionesTotal.focus_set() 
                messagebox.showinfo('COMPRA DE VACACIONES', 'Selecciona la fecha inicial de la compra de vacaciones !')
            elif self.date06['text'] == '':
                self.cvacacionesTotal.focus_set() 
                messagebox.showinfo('COMPRA DE VACACIONES', 'Selecciona la fecha final de la compra de vacaciones !')
            elif self.cvacacionesTotal.get() == '':
                self.cvacacionesTotal.focus_set()   
                messagebox.showinfo('COMPRA DE VACACIONES', 'Registra el total de dias de la compra de vacaciones !')
            elif not self.cvacacionesTotal.get().isnumeric():
                self.cvacacionesTotal.focus_set()   
                messagebox.showinfo('COMPRA DE VACACIONES', 'Registra correctamente el total de dias de la compra de vacaciones !')
            else:
                cvacI = self.date05['text']
                cvacF = self.date06['text']

                total =int(self.cvacacionesTotal.get())

                if valores[9] == '':
                    valores[9] = total
                else:                    
                    valores[9] = int(valores[9]) + total

                insert(f'INSERT INTO CVACACIONES (IDAC, FINI, FFIN, DTOT) VALUES ({id}, "{cvacI}", "{cvacF}", {total})')
                idRegistro = select(f'SELECT ID FROM CVACACIONES ORDER BY ID DESC', False)
                self.cvacaciones.insert('', END, text=idRegistro[0], values=(cvacI, cvacF, total))
                self.date05['text'] = ''
                self.date06['text'] = ''
                self.cvacacionesTotal.delete(0, END)               

        self.details.item(self.details.focus(), values=valores)

    def DeleteDetails(self):

        valores = self.details.item(self.details.focus())['values']
                
        if self.apoyo.selection():
            if valores[2] == 1:
                valores[2] = ''
            else:
                valores[2] = int(valores[2]) - 1

            id = int(self.apoyo.item(self.apoyo.focus())['text'])
            delete(F'DELETE FROM APOYO WHERE ID = {id}', False)
            self.apoyo.delete(self.apoyo.focus())
  
        if self.falta.selection():
            if valores[3] == 1:
                valores[3] = ''
            else:
                valores[3] = int(valores[3]) - 1
            
            id = int(self.falta.item(self.falta.focus())['text'])
            delete(F'DELETE FROM FALTA WHERE ID = {id}', False)
            self.falta.delete(self.falta.focus())      

        if self.feriado.selection():
            if valores[4] == 1:
                valores[4] = ''
            else:
                valores[4] = int(valores[4]) - 1

            id = int(self.feriado.item(self.feriado.focus())['text'])
            delete(F'DELETE FROM FERIADO WHERE ID = {id}', False)
            self.feriado.delete(self.feriado.focus())

        if self.adelanto.selection():
            if float(valores[10]) == float(self.adelanto.item(self.adelanto.focus())['values'][1]):
                valores[10] = ''
            else:
                saldo = float(valores[10]) - float(self.adelanto.item(self.adelanto.focus())['values'][1])
                valores[10] = f'{saldo:.2f}'

            id = int(self.adelanto.item(self.adelanto.focus())['text'])
            delete(F'DELETE FROM ADELANTO WHERE ID = {id}', False)
            self.adelanto.delete(self.adelanto.focus())
            
        if self.ingreso.selection():
            if float(valores[5]) == float(self.ingreso.item(self.ingreso.focus())['values'][1]):
                valores[5] = ''
            else:
                saldo = float(valores[5]) - float(self.ingreso.item(self.ingreso.focus())['values'][1])
                valores[5] = f'{saldo:.2f}'                

            id = int(self.ingreso.item(self.ingreso.focus())['text'])
            delete(F'DELETE FROM INGRESO WHERE ID = {id}', False)
            self.ingreso.delete(self.ingreso.focus())

        if self.descuento.selection():
            if float(valores[6]) == float(self.descuento.item(self.descuento.focus())['values'][1]):
                valores[6] = ''
            else:
                saldo = float(valores[6]) - float(self.descuento.item(self.descuento.focus())['values'][1])
                valores[6] = f'{saldo:.2f}'

            id = int(self.descuento.item(self.descuento.focus())['text'])
            delete(F'DELETE FROM DESCUENTO WHERE ID = {id}', False)
            self.descuento.delete(self.descuento.focus())

        if self.vacaciones.selection():
            if int(valores[8]) == int(self.vacaciones.item(self.vacaciones.focus())['values'][2]):
                valores[8] = ''
            else:
                dias = int(valores[8]) - int(self.vacaciones.item(self.vacaciones.focus())['values'][2])
                valores[8] = dias            

            id = int(self.vacaciones.item(self.vacaciones.focus())['text'])
            delete(F'DELETE FROM VACACIONES WHERE ID = {id}', False)
            self.vacaciones.delete(self.vacaciones.focus())

        if self.dmedico.selection():
            if int(valores[7]) == int(self.dmedico.item(self.dmedico.focus())['values'][3]):
                valores[7] = ''
            else:
                dias = int(valores[7]) - int(self.dmedico.item(self.dmedico.focus())['values'][3])
                valores[7] = dias            

            id = int(self.dmedico.item(self.dmedico.focus())['text'])
            delete(F'DELETE FROM DMEDICO WHERE ID = {id}', False)
            self.dmedico.delete(self.dmedico.focus())

        if self.cvacaciones.selection():
            if int(valores[9]) == int(self.cvacaciones.item(self.cvacaciones.focus())['values'][2]):
                valores[9] = ''
            else:
                dias = int(valores[9]) - int(self.cvacaciones.item(self.cvacaciones.focus())['values'][2])
                valores[9] = dias            

            id = int(self.cvacaciones.item(self.cvacaciones.focus())['text'])
            delete(F'DELETE FROM CVACACIONES WHERE ID = {id}', False)
            self.cvacaciones.delete(self.cvacaciones.focus())

        self.details.item(self.details.focus(), values=valores)        


    def Menu3(self):
        
        # Creamos los elementos del menu 1      
        menu = Frame(self)                     
      
        self.tre3 = Treeview(menu, show='headings', columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', 
                                                            '#11', '#12', '#13', '#14', '#15', '#16', '#17', '#18', '#19', '#20',
                                                            '#21', '#22', '#23', '#24', '#25', '#26', '#27', '#28', '#29', '#30'))
        self.tre3.column('#0', width=0)
        self.tre3.column('#1', width=30, minwidth=30)
        self.tre3.column('#2', width=240, minwidth=240)
        self.tre3.column('#3', width=70, minwidth=70, anchor='e')  
        self.tre3.column('#4', width=60, minwidth=60, anchor='e')
        self.tre3.column('#5', width=60, minwidth=60, anchor='e')
        self.tre3.column('#6', width=30, minwidth=30, anchor='e') 
        self.tre3.column('#7', width=30, minwidth=30, anchor='e')
        self.tre3.column('#8', width=70, minwidth=70, anchor='e')        
        self.tre3.column('#9', width=60, minwidth=60, anchor='e') 
        self.tre3.column('#10', width=30, minwidth=30, anchor='e')     
        self.tre3.column('#11', width=70, minwidth=70, anchor='e') 
        self.tre3.column('#12', width=30, minwidth=30, anchor='e')
        self.tre3.column('#13', width=70, minwidth=70, anchor='e') 
        self.tre3.column('#14', width=30, minwidth=30, anchor='e')
        self.tre3.column('#15', width=70, minwidth=70, anchor='e') 
        self.tre3.column('#16', width=30, minwidth=30, anchor='e')
        self.tre3.column('#17', width=60, minwidth=60, anchor='e') 
        self.tre3.column('#18', width=70, minwidth=70, anchor='e')
        self.tre3.column('#19', width=60, minwidth=60, anchor='e') 
        self.tre3.column('#20', width=60, minwidth=60, anchor='e')
        self.tre3.column('#21', width=60, minwidth=60, anchor='e') 
        self.tre3.column('#22', width=60, minwidth=60, anchor='e')
        self.tre3.column('#23', width=60, minwidth=60, anchor='e') 
        self.tre3.column('#24', width=60, minwidth=60, anchor='e')
        self.tre3.column('#25', width=60, minwidth=60, anchor='e') 
        self.tre3.column('#26', width=60, minwidth=60, anchor='e')
        self.tre3.column('#27', width=70, minwidth=70, anchor='e') 
        self.tre3.column('#28', width=60, minwidth=60, anchor='e')
        self.tre3.column('#29', width=60, minwidth=60, anchor='e')
        self.tre3.column('#30', width=60, minwidth=60, anchor='e')

        self.tre3.heading('#1', text='N°')
        self.tre3.heading('#2', text='Apellidos y Nombre')
        self.tre3.heading('#3', text='Planilla')
        self.tre3.heading('#4', text='AsignacionF')
        self.tre3.heading('#5', text='Movilidad')
        self.tre3.heading('#6', text='DiaT')
        self.tre3.heading('#7', text='DiaF')
        self.tre3.heading('#8', text='Planilla') 
        self.tre3.heading('#9', text='Movilidad')        
        self.tre3.heading('#10', text='DiaV')
        self.tre3.heading('#11', text='Vacaciones')
        self.tre3.heading('#12', text='DiaCV')
        self.tre3.heading('#13', text='CompraV')
        self.tre3.heading('#14', text='DiaDM')
        self.tre3.heading('#15', text='DescansoM')
        self.tre3.heading('#16', text='DiaF')
        self.tre3.heading('#17', text='Feriados')
        self.tre3.heading('#18', text='Planilla')
        self.tre3.heading('#19', text='Onp')
        self.tre3.heading('#20', text='Comision')
        self.tre3.heading('#21', text='PrimaS')
        self.tre3.heading('#22', text='Aporte')
        self.tre3.heading('#23', text='RentaQ')
        self.tre3.heading('#24', text='Descuento')
        self.tre3.heading('#25', text='Apoyo')
        self.tre3.heading('#26', text='Ingreso')
        self.tre3.heading('#27', text='PlanillaT')
        self.tre3.heading('#28', text='MovilidadT')
        self.tre3.heading('#29', text='PorFuera')
        self.tre3.heading('#30', text='Essalud')        

        scroll = Scrollbar(menu, orient='vertical', command=self.tre3.yview)
        scrol2 = Scrollbar(menu, orient='horizontal', command=self.tre3.xview)
        self.tre3.configure(yscrollcommand=scroll.set, xscrollcommand=scrol2.set)
     
        # Posicionamiento de los elementos         
        scroll.place(x=851, y=20, height=556)
        scrol2.place(x=20, y=560, width=830)
        self.tre3.place(x=20, y=20, height=540, width=830)
        
        Button(menu, text='GENERAR').place(x=890, y=20, width=90, height=30)
        Button(menu, text='MODIFICAR').place(x=890, y=55, width=90, height=30)
        Button(menu, text='REPORTE').place(x=890, y=90, width=90, height=30)
        Button(menu, text='SALIR', command=lambda:menu.destroy(), bg='#DF2F2F').place(x=890, y=125, width=90, height=30)

        # Cargamos datos al treeview
        self.CargarPlanilla()

        # Posicionamos la ventana principal
        menu.place(width=1000, height=600)
        
    def CargarPlanilla(self):
        
        mes = '01/07/2022'
        diasDelMes = PlanillaMes(mes)        

        if diasDelMes == 0:
            return

        # Obtener datos para elaborar planilla
        datos = select(f'SELECT ID, APAT, AMAT, NOMB, FING, SPLA, AFAM, SMOV, EAPO, TCOM, FCES FROM ACTIVO', True)        
        
        for index, dato in enumerate(datos, 1):
            
            id = dato[0]
            nombreCompleto = f'{dato[1]} {dato[2]} {dato[3]}'
            fechaIngreso = dato[4]
            sueldoPlanilla = float(dato[5])
            asignacionFamiliar = float(dato[6])
            sueldoMovilidad = float(dato[7])
            totalSueldo = sueldoPlanilla + asignacionFamiliar + sueldoMovilidad
            entidadAportacion = dato[8]
            comisionAportacion = dato[9]
            fechaCese = dato[10]
            
            diasApoyos = int(select(F'SELECT COUNT(FECH) FROM APOYO WHERE IDAC = {id}', False)[0])
            diasFaltas = int(select(F'SELECT COUNT(FECH) FROM FALTA WHERE IDAC = {id}', False)[0])      
            diasFeriados = int(select(F'SELECT COUNT(FECH) FROM FERIADO WHERE IDAC = {id}', False)[0])
            totalIngresos = select(F'SELECT SUM(MONT) FROM INGRESO WHERE IDAC = {id}', False)[0]
            totalDescuentos = select(F'SELECT SUM(MONT) FROM DESCUENTO WHERE IDAC = {id}', False)[0]            
            diasVacaciones = select(F'SELECT SUM(DTOT) FROM VACACIONES WHERE IDAC = {id}', False)[0]
            diasCompraVacaciones = select(F'SELECT SUM(DTOT) FROM CVACACIONES WHERE IDAC = {id}', False)[0]
            diasDescansoMedico = select(F'SELECT SUM(DTOT) FROM DMEDICO WHERE IDAC = {id}', False)[0]
            totalAdelantos = select(F'SELECT SUM(MONT) FROM ADELANTO WHERE IDAC = {id}', False)[0]
            totalXfuera = select(F'SELECT SUM(MONT) FROM XFUERA WHERE IDAC = {id}', False)[0]

            if totalIngresos:
                totalIngresos = float(totalIngresos)
            else:
                totalIngresos = 0

            if totalDescuentos:
                totalDescuentos = float(totalDescuentos)
            else:
                totalDescuentos = 0

            if diasVacaciones:
                diasVacaciones = int(diasVacaciones)
            else:
                diasVacaciones = 0

            if diasCompraVacaciones:
                diasCompraVacaciones = int(diasCompraVacaciones)
            else:
                diasCompraVacaciones = 0
            
            if diasDescansoMedico:
                diasDescansoMedico = int(diasDescansoMedico)
            else:
                diasDescansoMedico = 0


            if CompararFechas(fechaIngreso, mes):
                diasLaborados = diasDelMes - diasFaltas - diasVacaciones - diasDescansoMedico
            else:
                diasLaborados = diasDelMes - (int(fechaIngreso[:2]) + 1) - diasFaltas - diasVacaciones - diasDescansoMedico

            DiasComputables = diasLaborados + diasVacaciones + diasDescansoMedico
            diasNoComputables = diasDelMes - DiasComputables

            if DiasComputables > (diasDelMes / 2):
                planillaBruta = sueldoPlanilla - (sueldoPlanilla / 30 * diasNoComputables) #+ asignacionFamiliar                
            else:                
                planillaBruta = sueldoPlanilla / 30 * DiasComputables #+ asignacionFamiliar

            if diasLaborados > (diasDelMes / 2):
                movilidadBruta = sueldoMovilidad - (sueldoMovilidad / 30 * diasNoComputables)
            else:
                movilidadBruta = sueldoMovilidad / 30 * diasLaborados

            if diasVacaciones > 0:
                if diasVacaciones >= diasDelMes:
                    totalVacaciones = planillaBruta              
                else:                    
                    if diasVacaciones > 15:                        
                        totalVacaciones = (sueldoPlanilla + asignacionFamiliar) - ((sueldoPlanilla + asignacionFamiliar) / 30 * (diasDelMes - diasVacaciones))
                    else:
                        totalVacaciones = (sueldoPlanilla + asignacionFamiliar) / 30 * diasVacaciones  
            else:
                  totalVacaciones = 0

            if diasDescansoMedico > 0:
                if diasDescansoMedico >= diasDelMes:
                    totalDescansoMedico = planillaBruta            
                else:
                    if diasDescansoMedico > 15:                        
                        totalDescansoMedico = (sueldoPlanilla + asignacionFamiliar) - ((sueldoPlanilla + asignacionFamiliar) / 30 * (diasDelMes - diasDescansoMedico))
                    else:
                        totalDescansoMedico = (sueldoPlanilla + asignacionFamiliar) / 30 * diasDescansoMedico
            else:
                  totalDescansoMedico = 0
                      
            if diasLaborados > 0:
                planillaBruta = planillaBruta - totalVacaciones - totalDescansoMedico
            else:
                planillaBruta = 0

            totalApoyos = (totalSueldo / 30) * diasApoyos
            totalFeriados = sueldoPlanilla / 30 * diasFeriados * 2
            totalCompraVacaciones = (sueldoPlanilla + asignacionFamiliar) / 30 * diasCompraVacaciones
            totalPlanillaBruta = planillaBruta + totalVacaciones + totalCompraVacaciones + totalDescansoMedico + totalFeriados

            totalOnp = 0
            totalComision = 0
            totalPrima = 0
            totalAporte = 0

            if entidadAportacion == 'ONP':
                totalOnp = totalPlanillaBruta * 0.13
            elif entidadAportacion == 'HABITAT':
                if comisionAportacion == 'FLUJO':
                    totalComision = totalPlanillaBruta * 0.027
                elif comisionAportacion == 'MIXTA':
                    totalComision = totalPlanillaBruta * 0.027             
                totalPrima = totalPlanillaBruta * 0.027
                totalAporte = totalPlanillaBruta * 0.027
            elif entidadAportacion == 'INTEGRA':
                if comisionAportacion == 'FLUJO':
                    totalComision = totalPlanillaBruta * 0.027
                elif comisionAportacion == 'MIXTA':
                    totalComision = totalPlanillaBruta * 0.027                 
                totalPrima = totalPlanillaBruta * 0.027
                totalAporte = totalPlanillaBruta * 0.027
            elif entidadAportacion == 'PRIMA':
                if comisionAportacion == 'FLUJO':
                    totalComision = totalPlanillaBruta * 0.027
                elif comisionAportacion == 'MIXTA':
                    totalComision = totalPlanillaBruta * 0.027             
                totalPrima = totalPlanillaBruta * 0.027
                totalAporte = totalPlanillaBruta * 0.027
            elif entidadAportacion == 'PROFUTURO':
                if comisionAportacion == 'FLUJO':
                    totalComision = totalPlanillaBruta * 0.027
                elif comisionAportacion == 'MIXTA':
                    totalComision = totalPlanillaBruta * 0.027             
                totalPrima = totalPlanillaBruta * 0.027
                totalAporte = totalPlanillaBruta * 0.027

            if totalPlanillaBruta > 1025:
                totalEssalud = totalPlanillaBruta * 0.09
            else:
                totalEssalud = 1025 * 0.09


            self.tre3.insert('', END, text=id, values=(index, nombreCompleto, sueldoPlanilla, asignacionFamiliar, sueldoMovilidad,
                                                    diasLaborados, diasFaltas, round(planillaBruta, 2), round(movilidadBruta, 2),
                                                    diasVacaciones, round(totalVacaciones, 2), diasCompraVacaciones, round(totalCompraVacaciones, 2), 
                                                    diasDescansoMedico, round(totalDescansoMedico, 2), diasFeriados, round(totalFeriados, 2),
                                                    round(totalPlanillaBruta, 2), round(totalOnp, 2), round(totalComision, 2), round(totalPrima, 2),
                                                    round(totalAporte, 2), '', round(totalDescuentos, 2), round(totalApoyos, 2), round(totalIngresos, 2),
                                                    '', '', '', round(totalEssalud, 2)))
        
        self.tre3.insert('', END, values=('100', 'OROPEZA INCA JEANCARLOS ALBERTO', '1,900.00', '102.50', '350.00',
                                                    '30', '10', '1,900.00', '350.00', '30', '1,900.00', '30', '1,900.00', 
                                                    '30', '1,900.00','2', '250.00',
                                                    '1,900.00', '320.00', '100.00', '100.00',
                                                    '100.00', '100.00', '500.00', '600.00', '200.00',
                                                    '', '', '', '125.00'))


    def Menu4(self):
            
            # Creamos los elementos del menu 1      
            menu = Frame(self)

            Button(menu, text='SALIR'    , bg='#DF2F2F', command=lambda:menu.destroy()).place(x=890, y=125, width=90, height=30)

            # Posicionamos la ventana principal
            menu.place(width=1000, height=600)


    def Menu5(self):
            
        aaa = Menu1(self)

        return
        # Creamos los elementos del menu 1      
        menu = Frame(self)

        Button(menu, text='SALIR'    , bg='#DF2F2F', command=lambda:menu.destroy()).place(x=890, y=125, width=90, height=30)

        # Posicionamos la ventana principal
        menu.place(width=1000, height=600)


    def Menu6(self):
        
        # Creamos los elementos del menu 1      
        menu = Frame(self)
        
        Label(menu, anchor='center', bg='#DDDDDD', text='Entidad\nAFP'                ).place(x= 20, y=20, width=100, height=48)
        Label(menu, anchor='center', bg='#DDDDDD', text='Comision\nFlujo        Mixta').place(x=121, y=20, width=121, height=48)       
        Label(menu, anchor='center', bg='#DDDDDD', text='Prima\nSeguro'               ).place(x=243, y=20, width= 60, height=48)        
        Label(menu, anchor='center', bg='#DDDDDD', text='Aporte\nMensual'             ).place(x=304, y=20, width= 60, height=48)        
        Label(menu, anchor='center', bg='#DDDDDD', text='Sueldo\nMaximo'              ).place(x=365, y=20, width= 60, height=48)      
        
        Label(menu, text=' Habitat'             ).place(x= 20, y= 69, width=100, height=24)
        Label(menu, anchor='e', text='1.47%'    ).place(x=121, y= 69, width= 60, height=24)
        Label(menu, anchor='e', text='0.23%'    ).place(x=182, y= 69, width= 60, height=24)
        
        Label(menu, text=' Integra'             ).place(x= 20, y= 94, width=100, height=24)
        Label(menu, anchor='e', text='1.55%'    ).place(x=121, y= 94, width= 60, height=24)
        Label(menu, anchor='e', text='0.00%'    ).place(x=182, y= 94, width= 60, height=24)
        
        Label(menu, text=' Prima'               ).place(x= 20, y=119, width=100, height=24)
        Label(menu, anchor='e', text='1.60%'    ).place(x=121, y=119, width= 60, height=24)
        Label(menu, anchor='e', text='0.18%'    ).place(x=182, y=119, width= 60, height=24)
        
        Label(menu, text=' Profuturo'           ).place(x= 20, y=144, width=100, height=24)
        Label(menu, anchor='e', text='1.69%'    ).place(x=121, y=144, width= 60, height=24)
        Label(menu, anchor='e', text='0.28%'    ).place(x=182, y=144, width= 60, height=24)

        Label(menu, anchor='e', text='1.74%'    ).place(x=243, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='10.00%'   ).place(x=304, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='11,002.84').place(x=365, y= 69, width= 60, height=99)

        Label(menu, anchor='center', bg='#DDDDDD', text='Fondo\nOnp'       ).place(x=445, y=20, width= 60, height=48)    
        Label(menu, anchor='center', bg='#DDDDDD', text='Essalud'          ).place(x=506, y=20, width= 60, height=48)    
        Label(menu, anchor='center', bg='#DDDDDD', text='Sueldo\nMinimo'   ).place(x=567, y=20, width= 60, height=48) 
        Label(menu, anchor='center', bg='#DDDDDD', text='Asigna.\nFamiliar').place(x=628, y=20, width= 60, height=48)         
        
        Label(menu, anchor='e', text='13.00%'   ).place(x=445, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='9.00%'    ).place(x=506, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='1,025.00' ).place(x=567, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='10.00%'   ).place(x=628, y= 69, width= 60, height=99)
        

        Button(menu, text='MODIFICAR').place(x=890, y=20, width=90, height=30)
        Button(menu, text='SALIR'    , bg='#DF2F2F', command=lambda:menu.destroy()).place(x=890, y=125, width=90, height=30)

        # Posicionamos la ventana principal
        menu.place(width=1000, height=600)



   







if __name__ == '__main__':
    aplicacion = App()      