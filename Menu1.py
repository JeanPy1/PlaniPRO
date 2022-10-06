from tkinter import Button, Label, Scrollbar, Button, Frame, Entry, messagebox
from tkinter.ttk import Treeview, Combobox
from scripts.sql import select, insert, update, delete
from scripts.BuscarDni import BuscarDatosDni
from scripts.edad import FechaValida

class Menu1(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)

        self.TRABAJADORES = Treeview(self, columns=('#1', '#2', '#3'))       
        self.TRABAJADORES.column('#1', width=30, minwidth=30, anchor='center')
        self.TRABAJADORES.column('#2', width=270, minwidth=270)
        self.TRABAJADORES.column('#3', width=70, minwidth=70, anchor='center')
        self.TRABAJADORES.heading('#1', text='N°')
        self.TRABAJADORES.heading('#2', text='APELLIDOS Y NOMBRE')
        self.TRABAJADORES.heading('#3', text='DNI')

        scroll = Scrollbar(self, orient='vertical', command=self.TRABAJADORES.yview)
        self.TRABAJADORES.configure(yscrollcommand=scroll.set)
        self.TRABAJADORES.bind('<<TreeviewSelect>>', self.MostrarDetalles)
        scroll.place(x=396, y=30, height=548)
        self.TRABAJADORES.place(x=20, y=30, height=548)               

        titulos1 = (' Fecha de nacimiento', ' Fecha de ingreso', ' Planilla', ' Asignacion familiar', ' Movilidad',
                    ' Remuneracion total', ' Puesto laboral', ' Entidad de aportacion', ' Tipo de comision')
        titulos2 = (' Codigo cuspp', ' Cuenta bancaria', ' Numero de licencia', ' Tipo de categoria', ' Fecha de revalidacion',
                    ' Area de labor', ' Numero de celular', ' Distrito de residencia', ' Fecha de retiro')
                
        detalles1 = []
        detalles2 = []

        posicion = -31
        for numero in range(9):
            posicion+=61
            Label(self, text=titulos1[numero]).place(x=430, y=posicion, width=205, height=60)
            Label(self, text=titulos2[numero]).place(x=636, y=posicion, width=205, height=60)  

            detalles1.append(Label(self, fg='#000000', anchor='e'))   
            detalles1[numero].place(x=435, y=posicion+28, width=195)
            detalles2.append(Label(self, fg='#000000', anchor='e'))
            detalles2[numero].place(x=641, y=posicion+28, width=195)          
            
        self.DETALLES = detalles1 + detalles2    

        Button(self, text='AGREGAR', command=self.Agregar).place(x=890, y=30, width=90, height=30)
        Button(self, text='MODIFICAR', command=self.Modificar).place(x=890, y=65, width=90, height=30)
        Button(self, text='ELIMINAR', command=self.Eliminar).place(x=890, y=100, width=90, height=30)
        Button(self, text='SALIR', command=lambda:self.destroy(), bg='#DF2F2F').place(x=890, y=135, width=90, height=30)
 
        self.CargarTrabajadores()
        self.place(width=1000, height=600)

    def CargarTrabajadores(self):

        self.TRABAJADORES.delete(*self.TRABAJADORES.get_children())
        datos = select('SELECT ID, NDNI, APAT, AMAT, NOMB FROM ACTIVO ORDER BY APAT, AMAT, NOMB ASC', True)

        for index, dato in enumerate(datos, 1):
            nombre = f'{dato[2]} {dato[3]} {dato[4]}'    
            self.TRABAJADORES.insert('', 'end', text=dato[0], values=(index, nombre, dato[1]))

    def MostrarDetalles(self, e):
       
        if self.TRABAJADORES.selection():     

            self.BorrarDetalles()                      
            id = int(self.TRABAJADORES.item(self.TRABAJADORES.focus()).get('text'))               
            datos = select(f'''SELECT FNAC, FING, SPLA, AFAM, SMOV, PLAB, EAPO, TCOM, NCUS, NCUE, NLIC,
                                      CLIC, VLIC, ALAB, NCEL, DRES, FCES FROM ACTIVO WHERE ID = {id}''', False)
            
            detalles = list(datos)
            detalles.insert(5, datos[2] + datos[3] + datos[4])            
            
            for index, label in enumerate(self.DETALLES):
                label['text'] = detalles[index]    

    def BorrarDetalles(self):

        for label in self.DETALLES:
            label['text'] = ''   

    def BuscarDni(self):
      
        dni = self.buscarDni.get()
        if dni == '':
            messagebox.showinfo('BUSCAR', 'INGRESA EL NUMERO DE DNI')    
            self.buscarDni.focus()       
        elif len(dni) != 8 or not dni.isdigit():  
            messagebox.showinfo('BUSCAR', 'INGRESA CORRECTAMENTE EL NUMERO DE DNI') 
            self.buscarDni.focus()      
        else:
           
            persona = BuscarDatosDni(dni)

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

    def GrabarDatos(self):

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
            
            datosTrabajador = ( self.numeroDni['text'],         self.apPaterno['text'],
                                self.apMaterno['text'],         self.nombre['text'],
                                self.fechaNaci.get(),           self.fechaIngr.get(),
                                float(self.planilla.get()),     float(self.asignacion.get()),
                                float(self.movilidad.get()),    self.aportacion.get(),
                                self.comision.get(),            self.cuspp.get().upper(),
                                self.cargo.get(),               self.cuenta.get(),
                                self.area.get(),                self.codigo.get().upper(),                                
                                self.revalidacion.get(),        self.categoria.get(),
                                self.celular.get(),             self.distrito.get(),
                                self.retiro.get())

            if self.buscar['state'] == 'normal':

                for index in self.TRABAJADORES.get_children():
                    if f"{self.TRABAJADORES.item(index).get('values')[2]:0>8}" == self.numeroDni['text']:
                        messagebox.showinfo('GRABAR', 'DNI YA REGISTRADO')
                        return            

                query = f'''INSERT INTO ACTIVO (NDNI, APAT, AMAT, NOMB, FNAC, FING, SPLA, AFAM, SMOV, EAPO, TCOM, NCUS,
                            PLAB, NCUE, ALAB, NLIC, VLIC, CLIC, NCEL, DRES, FCES) VALUES {datosTrabajador}'''
                insert(query)
                
                self.CargarTrabajadores()

                seleccion = self.TRABAJADORES.focus()
                if seleccion:        
                    id = int(self.TRABAJADORES.item(seleccion).get('text'))
                    for index in self.TRABAJADORES.get_children():
                        if int(self.TRABAJADORES.item(index).get('text')) == id:
                            self.TRABAJADORES.selection_set(index)
                            self.TRABAJADORES.focus(index)
                            break

            else:                

                query = f'''UPDATE ACTIVO SET   FNAC = '{datosTrabajador[4]}',   FING = '{datosTrabajador[5]}', 
                                                SPLA =  {datosTrabajador[6]},    AFAM = '{datosTrabajador[7]}', 
                                                SMOV =  {datosTrabajador[8]},    EAPO = '{datosTrabajador[9]}',
                                                TCOM = '{datosTrabajador[10]}',  NCUS = '{datosTrabajador[11]}', 
                                                PLAB = '{datosTrabajador[12]}',  NCUE = '{datosTrabajador[13]}',
                                                ALAB = '{datosTrabajador[14]}',  NLIC = '{datosTrabajador[15]}', 
                                                VLIC = '{datosTrabajador[16]}',  CLIC = '{datosTrabajador[17]}',
                                                NCEL = '{datosTrabajador[18]}',  DRES = '{datosTrabajador[19]}', 
                                                FCES = '{datosTrabajador[20]}'   WHERE NDNI = {datosTrabajador[0]}'''           
                update(query)

                detalles = list(datosTrabajador)
                detalles.insert(9, datosTrabajador[6] + datosTrabajador[7] + datosTrabajador[8])
                detalles.insert(10, detalles.pop(13))    
                detalles.insert(18, detalles.pop(15))   
                
                for index, label in enumerate(self.DETALLES):
                    label['text'] = detalles[index+4]

            self.menuAgregar.destroy()

    def Agregar(self):

        contenedor = Frame(self)

        titulos1 = (' Buscar dni', ' Numero dni', ' Apellido paterno', ' Apellido materno', ' Nombres',
                    ' Fecha de nacimiento', ' Fecha de ingreso', ' Planilla', ' Puesto laboral')                    
        titulos2 = (' Cuenta bancaria', ' Entidad de aportacion', ' Tipo de comision', ' Codigo cuspp', ' No. de licencia',
                    ' Fecha de revalidacion', ' Area de labor', ' Distrito de residencia', ' Fecha de retiro')

        posicion = -61
        for numero in range(9):
            posicion+=61
            Label(contenedor, text=titulos1[numero]).place(x=  0, y=posicion, width=205, height=60)
            Label(contenedor, text=titulos2[numero]).place(x=206, y=posicion, width=205, height=60) 
       
        Label(contenedor, text=' Asigna.').place(x=68, y=427)
        Label(contenedor, text=' Movili.').place(x=134, y=427)        
        Label(contenedor, text=' Tipo categoria').place(x=306, y=244)      
        Label(contenedor, text=' Numero celular').place(x=306, y=366)            
       
        self.buscar       = Button(contenedor, text='BUSCAR', bg='#88C7FF', command=self.BuscarDni)
        self.buscarDni    = Entry(contenedor, relief='ridge', bd=2)     
        self.numeroDni    = Label(contenedor, fg='#000000', anchor='w')        
        self.apPaterno    = Label(contenedor, fg='#000000', anchor='w')
        self.apMaterno    = Label(contenedor, fg='#000000', anchor='w')
        self.nombre       = Label(contenedor, fg='#000000', anchor='w')
        self.fechaNaci    = Entry(contenedor, relief='ridge', bd=2)   
        self.fechaIngr    = Entry(contenedor, relief='ridge', bd=2)   
        self.planilla     = Entry(contenedor, relief='ridge', bd=2)           
        self.asignacion   = Entry(contenedor, relief='ridge', bd=2)   
        self.movilidad    = Entry(contenedor, relief='ridge', bd=2)   
        self.cargo        = Combobox(contenedor, state='readonly', values=['INSPECTOR VIAL', 'OPERADOR DE GRUA LIVIANA', 'OPERADOR DE GRUA PESADA', ''])       
        self.cuenta       = Entry(contenedor, relief='ridge', bd=2)   
        self.aportacion   = Combobox(contenedor, state='readonly', values=['ONP', 'HABITAT', 'INTEGRA', 'PRIMA', 'PROFUTURO',''])
        self.comision     = Combobox(contenedor, state='readonly', values=['FLUJO', 'MIXTA', ''])
        self.cuspp        = Entry(contenedor, relief='ridge', bd=2)   
        self.codigo       = Entry(contenedor, relief='ridge', bd=2) 
        self.categoria    = Combobox(contenedor, state='readonly', values=['AIIA', 'AIIB', 'AIIIA', 'AIIIB', 'AIIIC', ''])       
        self.revalidacion = Entry(contenedor, relief='ridge', bd=2)             
        self.area         = Combobox(contenedor, state='readonly', values=['SUR', 'NORTE', 'TALLER', 'OFICINA', ''])       
        self.celular      = Entry(contenedor, relief='ridge', bd=2)   
        self.distrito     = Combobox(contenedor, state='readonly', values=['ANCON', 'ATE VITARTE', 'CARABAYLLO', 'CHORRILLOS', 'COMAS', 'LOS OLIVOS',
                                        'LURIGANCHO', 'LURIN', 'PUCUSANA', 'PUENTE PIEDRA', 'RIMAC', 'SAN BARTOLO', 'SAN JUAN DE LURIGANCHO',
                                        'SAN JUAN DE MIRAFLORES', 'SAN MARTIN DE PORRES', 'SANTA ANITA', 'SANTIAGO DE SURCO', 'SURQUILLO',
                                        'VILLA EL SALVADOR', 'VILLA MARIA DEL TRIUNFO', ''])      
        self.retiro = Entry(contenedor, relief='ridge', bd=2)                       

        # Posicionamiento de los elementos      
        self.buscar.place      (x=139, y= 24, width= 61, height=28)    
        self.buscarDni.place   (x=  5, y= 24, width=129, height=28)    
        self.numeroDni.place   (x=  5, y= 85, width=195, height=28)
        self.apPaterno.place   (x=  5, y=146, width=195, height=28)
        self.apMaterno.place   (x=  5, y=207, width=195, height=28)
        self.nombre.place      (x=  5, y=268, width=195, height=28)        
        self.fechaNaci.place   (x=  5, y=329, width=195, height=28)        
        self.fechaIngr.place   (x=  5, y=390, width=195, height=28)
        self.planilla.place    (x=  5, y=451, width= 63, height=28)  
        self.asignacion.place  (x= 73, y=451, width= 61, height=28)      
        self.movilidad.place   (x=139, y=451, width= 61, height=28) 
        self.cargo.place       (x=  5, y=512, width=195, height=28)        
        self.cuenta.place      (x=211, y= 24, width=195, height=28)
        self.aportacion.place  (x=211, y= 85, width=195, height=28) 
        self.comision.place    (x=211, y=146, width=195, height=28)
        self.cuspp.place       (x=211, y=207, width=195, height=28)
        self.codigo.place      (x=211, y=268, width= 95, height=28)
        self.categoria.place   (x=311, y=268, width= 95, height=28)
        self.revalidacion.place(x=211, y=329, width=195, height=28)        
        self.area.place        (x=211, y=390, width= 95, height=28)
        self.celular.place     (x=311, y=390, width= 95, height=28)
        self.distrito.place    (x=211, y=451, width=195, height=28)
        self.retiro.place      (x=211, y=512, width=195, height=28)         
            
        # Creamos los botones principales
        Button(contenedor, text='GRABAR', command=self.GrabarDatos).place(x=460, width=90, height=30)     
        Button(contenedor, text='SALIR' , command=lambda:contenedor.destroy(), bg='#DF2F2F').place(x=460, y=35, width=90, height=30)

        # Foco en cuadro de busqueda y Superponemos la ventana principal
        self.buscarDni.focus_set()
        contenedor.grab_set()
        
        # Asignamos variablo global a contenedor para destruir
        self.menuAgregar = contenedor

        # Posicionamos la ventana principal
        contenedor.place(x=430, y=30, width=550, height=548)

    def Modificar(self):
        
        # Cargamos datos del trabajador a la ventana agregar
        if self.TRABAJADORES.selection():            
                
                # Id del trabajador           
                id = int(self.TRABAJADORES.item(self.TRABAJADORES.focus()).get('text'))
                datos = select(f'SELECT * FROM ACTIVO WHERE ID = {id}', False)
                
                self.Agregar()

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

    def Eliminar(self):

        if self.TRABAJADORES.selection():
            respuesta = messagebox.askyesno('ELIMINAR','SEGURO?', default='no')

            if respuesta:
                id = int(self.TRABAJADORES.item(self.TRABAJADORES.focus()).get('text'))

                if self.DETALLES[17] != '':
                    insert(f'INSERT INTO CESADO SELECT * FROM ACTIVO WHERE ID = {id}')

                delete(f'DELETE FROM ACTIVO WHERE ID = {id}', True)

                self.BorrarDetalles()
                self.CargarTrabajadores()
   

           
           
    

