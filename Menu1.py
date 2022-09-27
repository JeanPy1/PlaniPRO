from tkinter import Button, Label, Scrollbar, Button, Frame, Entry, messagebox
from tkinter.ttk import Treeview, Combobox
from scripts.sql import select, insert, update, delete
from scripts.BuscarDni import BuscarDni
from scripts.edad import Edad, Tiempo, FechaValida
from scripts.trabajador import datos

class Menu1(Frame):

    def __init__(self, contenedor):

        super().__init__(contenedor)

        self.DATOS = Treeview(self, columns=('#1', '#2', '#3'))
        self.DATOS.column('#0', width=0)
        self.DATOS.column('#1', width=30, minwidth=30, anchor='center')
        self.DATOS.column('#2', width=270, minwidth=270)
        self.DATOS.column('#3', width=70, minwidth=70, anchor='center')
        self.DATOS.heading('#1', text='N°')
        self.DATOS.heading('#2', text='Apellidos y Nombre')
        self.DATOS.heading('#3', text='Dni')

        scroll = Scrollbar(self, orient='vertical', command=self.DATOS.yview)
        self.DATOS.configure(yscrollcommand=scroll.set)

        self.DATOS.bind('<<TreeviewSelect>>', self.ShowDetails)

        scroll.place(x=396, y=20, height=550)
        self.DATOS.place(x=20, y=20, height=550)

        Label(self, text='  Nacimiento'  ).place(x=437, y= 20, width=200, height=54)
        Label(self, text='  Ingreso'     ).place(x=437, y= 75, width=200, height=54)
        Label(self, text='  Planilla'    ).place(x=437, y=130, width=200, height=54)
        Label(self, text='  Asignacion'  ).place(x=437, y=185, width=200, height=54)
        Label(self, text='  Movilidad'   ).place(x=437, y=240, width=200, height=54)
        Label(self, text='  Sueldo'      ).place(x=437, y=295, width=200, height=54)
        Label(self, text='  Cargo'       ).place(x=437, y=350, width=200, height=54)
        Label(self, text='  Aportacion'  ).place(x=437, y=405, width=200, height=54)
        Label(self, text='  Comision'    ).place(x=437, y=460, width=200, height=54)
        Label(self, text='  C.u.s.p.p.'  ).place(x=437, y=515, width=200, height=55)        
        Label(self, text='  Cuenta'      ).place(x=638, y= 20, width=200, height=54)       
        Label(self, text='  Licencia'    ).place(x=638, y= 75, width=200, height=54)
        Label(self, text='  Categoria'   ).place(x=638, y=130, width=200, height=54)
        Label(self, text='  Revalidacion').place(x=638, y=185, width=200, height=54)        
        Label(self, text='  Area'        ).place(x=638, y=240, width=200, height=54)
        Label(self, text='  Celular'     ).place(x=638, y=295, width=200, height=54)
        Label(self, text='  Distrito'    ).place(x=638, y=350, width=200, height=54)
        Label(self, text='  Edad'        ).place(x=638, y=405, width=200, height=54)
        Label(self, text='  Tiempo'      ).place(x=638, y=460, width=200, height=54)
        Label(self, text='  Retiro'      ).place(x=638, y=515, width=200, height=55)

        self.NACIMIENTO   = Label(self, fg='#000000', anchor='e')
        self.INGRESO      = Label(self, fg='#000000', anchor='e')
        self.PLANILLA     = Label(self, fg='#000000', anchor='e')
        self.ASIGNACION   = Label(self, fg='#000000', anchor='e')
        self.MOVILIDAD    = Label(self, fg='#000000', anchor='e')
        self.SUELDO       = Label(self, fg='#000000', anchor='e')
        self.CARGO        = Label(self, fg='#000000', anchor='e')
        self.APORTACION   = Label(self, fg='#000000', anchor='e')
        self.COMISION     = Label(self, fg='#000000', anchor='e')        
        self.CUSPP        = Label(self, fg='#000000', anchor='e')
        self.CUENTA       = Label(self, fg='#000000', anchor='e')
        self.LICENCIA     = Label(self, fg='#000000', anchor='e')
        self.CATEGORIA    = Label(self, fg='#000000', anchor='e')
        self.REVALIDACION = Label(self, fg='#000000', anchor='e')
        self.AREA         = Label(self, fg='#000000', anchor='e')
        self.CELULAR      = Label(self, fg='#000000', anchor='e')
        self.DISTRITO     = Label(self, fg='#000000', anchor='e')
        self.EDAD         = Label(self, fg='#000000', anchor='e')
        self.TIEMPO       = Label(self, fg='#000000', anchor='e')
        self.RETIRO       = Label(self, fg='#000000', anchor='e')
        
        self.NACIMIENTO.place   (x=448, y= 44, width=182)
        self.INGRESO.place      (x=448, y= 99, width=182)
        self.PLANILLA.place     (x=448, y=154, width=182)
        self.ASIGNACION.place   (x=448, y=209, width=182)
        self.MOVILIDAD.place    (x=448, y=264, width=182)
        self.SUELDO.place       (x=448, y=319, width=182)
        self.CARGO.place        (x=448, y=374, width=182)
        self.APORTACION.place   (x=448, y=429, width=182)
        self.COMISION.place     (x=448, y=484, width=182)
        self.CUSPP.place        (x=448, y=539, width=182)
        self.CUENTA.place       (x=649, y= 44, width=182)
        self.LICENCIA.place     (x=649, y= 99, width=182)
        self.CATEGORIA.place    (x=649, y=154, width=182)
        self.REVALIDACION.place (x=649, y=209, width=182)
        self.AREA.place         (x=649, y=264, width=182)
        self.CELULAR.place      (x=649, y=319, width=182)
        self.DISTRITO.place     (x=649, y=374, width=182)
        self.EDAD.place         (x=649, y=429, width=182)
        self.TIEMPO.place       (x=649, y=484, width=182)
        self.RETIRO.place       (x=649, y=539, width=182)

        # Botones de gestion
        Button(self, text='AGREGAR'  , command=self.Agregar   ).place(x=890, y=20, width=90, height=30)
        Button(self, text='MODIFICAR', command=self.Modify).place(x=890, y=55, width=90, height=30)
        Button(self, text='ELIMINAR' , command=self.Remove).place(x=890, y=90, width=90, height=30)
        Button(self, text='SALIR'    , command=lambda:self.destroy(), bg='#DF2F2F').place(x=890, y=125, width=90, height=30)

        # Cargamos datos al treeview
        self.LoadEmployee()

        # Posicionamos la ventana principal
        self.place(width=1000, height=600)

    def Agregar(self):
       
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
        if self.DATOS.selection():            
                
                # Id del trabajador           
                id = int(self.DATOS.item(self.DATOS.focus()).get('text'))
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
        if self.DATOS.selection():
            respuesta = messagebox.askyesno('ELIMINAR','SEGURO?', default='no')

            if respuesta:
                # Id del trabajador
                id = int(self.DATOS.item(self.DATOS.focus()).get('text'))

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
        self.DATOS.delete(*self.DATOS.get_children())
        
        # Obtenemos datos de todos los trabajadores
        datos = select('SELECT ID, NDNI, APAT, AMAT, NOMB FROM ACTIVO ORDER BY APAT, AMAT, NOMB ASC', True)

        # cargamos datos al treeview
        for index, dato in enumerate(datos, 1):
            nombre = f'{dato[2]} {dato[3]} {dato[4]}'    
            self.DATOS.insert('', 'end', text=dato[0], values=(index, nombre, dato[1]))   

    def RemoveDetails(self):

            # Limpiamos los cuadros de AllDetails
            self.NACIMIENTO['text'] = ''
            self.INGRESO['text'] = ''
            self.PLANILLA['text'] = ''
            self.ASIGNACION['text'] = ''
            self.MOVILIDAD['text'] = ''
            self.SUELDO['text'] = ''
            self.CARGO['text'] = ''
            self.APORTACION['text'] = ''
            self.COMISION['text'] = ''            
            self.CUSPP['text'] = ''
            self.CUENTA['text'] = ''
            self.LICENCIA['text'] = ''
            self.CATEGORIA['text'] = ''
            self.REVALIDACION['text'] = ''
            self.AREA['text'] = ''
            self.CELULAR['text'] = ''
            self.DISTRITO['text'] = ''
            self.EDAD['text'] = ''
            self.TIEMPO['text'] = ''
            self.RETIRO['text'] = ''

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
                self.buscarDni.delete(0, 'end')
                self.fechaNaci.focus_set()
            else:                
                messagebox.showinfo('BUSCAR', 'NO SE ENCONTRO EL NUMERO DE DNI')           
                self.buscarDni.focus()   

    def ShowDetails(self, e):
                
        # Mostramos AllDetails del trabajador selecionado
        if self.DATOS.selection():     

            self.RemoveDetails()
            
            # Id del trabajador             
            id = int(self.DATOS.item(self.DATOS.focus()).get('text'))
            
            # Obtener sus datos
            datos = select(f'SELECT * FROM ACTIVO WHERE ID = {id}', False)

            # Mostramos AllDetails del trabajador en los cuadros          
            self.NACIMIENTO['text']   = datos[5]
            self.INGRESO['text']      = datos[6]
            self.PLANILLA['text']     = f'{datos[7]:,.2f}'
            self.ASIGNACION['text']   = f'{datos[8]:,.2f}'
            self.MOVILIDAD['text']    = f'{datos[9]:,.2f}'
            self.SUELDO['text']       = f'{datos[7] + datos[8] + datos[9]:,.2f}'
            self.CARGO['text']        = datos[13]
            self.APORTACION['text']   = datos[10]
            self.COMISION['text']     = datos[11]
            self.CUSPP['text']        = datos[12]
            self.CUENTA['text']       = datos[14]
            self.LICENCIA['text']     = datos[16]
            self.CATEGORIA['text']    = datos[18]
            self.REVALIDACION['text'] = datos[17]
            self.AREA['text']         = datos[15]
            self.CELULAR['text']      = datos[19]
            self.DISTRITO['text']     = datos[20]
            self.EDAD['text']         = Edad(datos[5])
            self.TIEMPO['text']       = Tiempo(datos[6])
            self.RETIRO['text']       = datos[21]

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
                for index in self.DATOS.get_children():
                    if f"{self.DATOS.item(index).get('values')[2]:0>8}" == self.numeroDni['text']:
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
            seleccion = self.DATOS.focus()

            if seleccion:
                id = int(self.DATOS.item(seleccion).get('text'))

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
                for index in self.DATOS.get_children():
                    if int(self.DATOS.item(index).get('text')) == id:
                        self.DATOS.selection_set(index)
                        self.DATOS.focus(index)

            # Cerrar ventana                           
            self.agregar.destroy()


