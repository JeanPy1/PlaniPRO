from tkinter import Button, Label, Scrollbar, Button, Frame, Entry, messagebox
from tkinter.ttk import Treeview, Combobox
from datetime import datetime
from requests import get
from scripts.sql import Select_Personal, Delete_Personal, Insert_Personal, Update_Personal

class Menu1(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)
        
        self.trabajadores = Treeview(self, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10',
                                                    '#11', '#12', '#13', '#14', '#15', '#16', '#17', '#18', '#19',
                                                    '#20', '#21', '#22', '#23', '#24', '#25'))       
        self.trabajadores.column('#1', width=30, minwidth=30, anchor='center')
        self.trabajadores.column('#2', width=270, minwidth=270)
        self.trabajadores.column('#3', width=70, minwidth=70, anchor='center')
        self.trabajadores.heading('#1', text='N°')
        self.trabajadores.heading('#2', text='APELLIDOS Y NOMBRE')
        self.trabajadores.heading('#3', text='DNI')
        self.trabajadores["displaycolumns"] = ('#1', '#2', '#3')

        scroll = Scrollbar(self, orient='vertical', command=self.trabajadores.yview)
        self.trabajadores.configure(yscrollcommand=scroll.set)

        self.trabajadores.bind('<<TreeviewSelect>>', self.MostrarDetalles)

        scroll.place(x=396, y=30, height=548)
        self.trabajadores.place(x=20, y=30, height=548)         

        Label(self, text=' Fecha de nacimiento').place(x=430, y=30, width=205, height=60)
        Label(self, text=' Fecha de ingreso').place(x=430, y=91, width=205, height=60)  
        Label(self, text=' Planilla').place(x=430, y=152, width=205, height=60)
        Label(self, text=' Asignacion familiar').place(x=430, y=213, width=205, height=60) 
        Label(self, text=' Movilidad').place(x=430, y=274, width=205, height=60)
        Label(self, text=' Remuneracion total').place(x=430, y=335, width=205, height=60)  
        Label(self, text=' Entidad de aportacion').place(x=430, y=396, width=205, height=60)
        Label(self, text=' Tipo de comision').place(x=430, y=457, width=205, height=60)  
        Label(self, text=' Codigo cuspp').place(x=430, y=518, width=205, height=60)
        Label(self, text=' Puesto laboral').place(x=636, y= 30, width=205, height=60)
        Label(self, text=' Cuenta bancaria').place(x=636, y= 91, width=205, height=60)
        Label(self, text=' Numero de licencia').place(x=636, y=152, width=205, height=60) 
        Label(self, text=' Tipo de categoria').place(x=636, y=213, width=205, height=60)
        Label(self, text=' Fecha de revalidacion').place(x=636, y=274, width=205, height=60)  
        Label(self, text=' Area de labor').place(x=636, y=335, width=205, height=60)
        Label(self, text=' Numero de celular').place(x=636, y=396, width=205, height=60)  
        Label(self, text=' Distrito de residencia').place(x=636, y=457, width=205, height=60)
        Label(self, text=' Fecha de retiro').place(x=636, y=518, width=205, height=60)  

        self.lnacimiento = Label(self, fg='#000000', anchor='e')
        self.lingreso = Label(self, fg='#000000', anchor='e')
        self.lplanila = Label(self, fg='#000000', anchor='e')
        self.lasignacion = Label(self, fg='#000000', anchor='e')
        self.lmovilidad = Label(self, fg='#000000', anchor='e')
        self.ltotal = Label(self, fg='#000000', anchor='e')
        self.laportacion = Label(self, fg='#000000', anchor='e')
        self.lcomision = Label(self, fg='#000000', anchor='e')
        self.lcuspp = Label(self, fg='#000000', anchor='e')
        self.lcargo = Label(self, fg='#000000', anchor='e')
        self.lcuenta = Label(self, fg='#000000', anchor='e')
        self.llicencia = Label(self, fg='#000000', anchor='e')
        self.lcategoria = Label(self, fg='#000000', anchor='e')
        self.lvencimiento = Label(self, fg='#000000', anchor='e')
        self.larea = Label(self, fg='#000000', anchor='e')
        self.ltelefono = Label(self, fg='#000000', anchor='e')
        self.ldistrito = Label(self, fg='#000000', anchor='e')
        self.lretiro = Label(self, fg='#000000', anchor='e')

        self.lnacimiento.place(x=435, y=58, width=195)
        self.lingreso.place(x=435, y=119, width=195)
        self.lplanila.place(x=435, y=180, width=195) 
        self.lasignacion.place(x=435, y=241, width=195)
        self.lmovilidad.place(x=435, y=302, width=195)
        self.ltotal.place(x=435, y=363, width=195) 
        self.laportacion.place(x=435, y=424, width=195) 
        self.lcomision.place(x=435, y=485, width=195)
        self.lcuspp.place(x=435, y=546, width=195)
        self.lcargo.place(x=641, y=58, width=195)
        self.lcuenta.place(x=641, y=119, width=195)
        self.llicencia.place(x=641, y=180, width=195)
        self.lcategoria.place(x=641, y=241, width=195)
        self.lvencimiento.place(x=641, y=302, width=195)
        self.larea.place(x=641, y=363, width=195)
        self.ltelefono.place(x=641, y=424, width=195)
        self.ldistrito.place(x=641, y=485, width=195)
        self.lretiro.place(x=641, y=546, width=195)       
       
        Button(self, text='AGREGAR', command=self.Agregar).place(x=890, y=30, width=90, height=30)
        Button(self, text='MODIFICAR', command=self.Modificar).place(x=890, y=65, width=90, height=30)
        Button(self, text='ELIMINAR', command=self.Eliminar).place(x=890, y=100, width=90, height=30)
        Button(self, text='SALIR', command=lambda:self.destroy(), bg='#DF2F2F').place(x=890, y=135, width=90, height=30)
 
        self.CargarTrabajadores()
        self.place(width=1000, height=600)        

    def CargarTrabajadores(self):

        self.trabajadores.delete(*self.trabajadores.get_children())
        persons = Select_Personal()        
        for index, person in enumerate(persons, 1):          
            nombre = f"{person[2]} {person[3]} {person[4]}"
            datos = (index, nombre, person[1]) + person      
            self.trabajadores.insert('', 'end', text=person[0], values=datos)      

    def MostrarDetalles(self, e):
       
        if self.trabajadores.selection():
            self.BorrarDetalles() 

            datos = self.trabajadores.item(self.trabajadores.selection()).get("values")
            planilla = float(datos[10])
            asignacion = float(datos[11])
            movilidad = float(datos[12])
            totalSueldo = planilla + asignacion + movilidad
            self.lnacimiento["text"] = datos[8]
            self.lingreso["text"] = datos[9]
            self.lplanila["text"] = f"{planilla:.2f}"
            self.lasignacion["text"] = f"{asignacion:.2f}"
            self.lmovilidad["text"] = f"{movilidad:.2f}"
            self.ltotal["text"] = f"{totalSueldo:.2f}"
            self.laportacion["text"] = datos[13]
            self.lcomision["text"] = datos[14]
            self.lcuspp["text"] = datos[15]
            self.lcargo["text"] = datos[16]
            self.lcuenta["text"] = datos[17]
            self.llicencia["text"] = datos[18]
            self.lcategoria["text"] = datos[19]
            self.lvencimiento["text"] = datos[20]
            self.larea["text"] = datos[21]
            self.ltelefono["text"] = datos[22]
            self.ldistrito["text"] = datos[23]
            self.lretiro["text"] = datos[24] 
   
    def BorrarDetalles(self):

        self.lnacimiento["text"] = ""
        self.lingreso["text"] = ""
        self.lplanila["text"] = ""
        self.lasignacion["text"] = ""
        self.lmovilidad["text"] = ""
        self.ltotal["text"] = ""
        self.laportacion["text"] = ""
        self.lcomision["text"] = ""
        self.lcuspp["text"] = ""
        self.lcargo["text"] = ""
        self.lcuenta["text"] = ""
        self.llicencia["text"] = ""
        self.lcategoria["text"] = ""
        self.lvencimiento["text"] = ""
        self.larea["text"] = ""
        self.ltelefono["text"] = ""
        self.ldistrito["text"] = ""
        self.lretiro["text"] = ""

    def BuscarDni(self):
      
        dni = self.buscarDni.get()
        if dni == '':
            messagebox.showinfo('BUSCAR', 'INGRESA EL NUMERO DE DNI')    
            self.buscarDni.focus()       
        elif len(dni) != 8 or not dni.isdigit():  
            messagebox.showinfo('BUSCAR', 'INGRESA CORRECTAMENTE EL NUMERO DE DNI') 
            self.buscarDni.focus()      
        else:        

            parametros = {'numero': dni}
            url = 'https://api.apis.net.pe/v1/dni'
            headers = { 'Authorization': 'apis-token-1.aTSI1U7KEuT-6bbbCguH-4Y8TI6KS73N', 
                        'Referer': 'https://apis.net.pe/api-tipo-cambio.html'}

            response = get(url, headers=headers, params=parametros)
                
            if response.status_code == 200:
                persona = response.json()   
                self.dni['text'] = persona['numeroDocumento']
                self.paterno['text'] = persona['apellidoPaterno']
                self.materno['text'] = persona['apellidoMaterno']
                self.nombre['text'] = persona['nombres']
                self.buscarDni.delete(0, 'end')
                self.nacimiento.focus_set()            
            else:                
                messagebox.showinfo('BUSCAR', 'NO SE ENCONTRO EL NUMERO DE DNI')           
                self.buscarDni.focus()   

    def GrabarDatos(self):   

        # Validacion de dni
        if self.dni['text'] == '':
            messagebox.showinfo('GRABAR', 'REGISTRA EL DNI')
            self.buscarDni.focus()

        # Validacion de fecha de nacimiento
        elif self.nacimiento.get() == '':
            messagebox.showinfo('GRABAR', 'REGISTRA EL NACIMIENTO')
            self.nacimiento.focus()
        elif len(self.nacimiento.get()) != 10 or not self.ValidarFecha(self.nacimiento.get()):
            messagebox.showinfo('GRABAR', 'REGISTRA CORRECTAMENTE EL NACIMIENTO')
            self.nacimiento.focus()

        # Validacion de fecha de ingreso
        elif self.ingreso.get() == '':
            messagebox.showinfo('GRABAR', 'REGISTRA EL INGRESO')
            self.ingreso.focus()
        elif len(self.ingreso.get()) != 10 or not self.ValidarFecha(self.ingreso.get()):
            messagebox.showinfo('GRABAR', 'REGISTRA CORRECTAMENTE EL INGRESO')
            self.ingreso.focus()

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
        elif self.retiro.get() != '' and not self.ValidarFecha(self.retiro.get()):
            messagebox.showinfo('GRABAR', 'REGISTRA CORRECTAMENTE EL RETIRO')
            self.retiro.focus()
        else:           

            dni = self.dni['text']
            paterno = self.paterno['text']
            materno = self.materno['text']
            nombre = self.nombre['text']
            nacimiento = self.nacimiento.get()
            ingreso = self.ingreso.get()
            planilla = float(self.planilla.get())
            asignacion = float(self.asignacion.get())
            movilidad = float(self.movilidad.get())
            aportacion = self.aportacion.get()
            comision = self.comision.get()
            cuspp = self.cuspp.get().upper()
            cargo = self.cargo.get()
            cuenta = self.cuenta.get()
            licencia = self.licencia.get()
            categoria = self.categoria.get().upper()
            vencimiento = self.vencimiento.get()
            area = self.area.get()
            telefono = self.telefono.get()
            distrito = self.distrito.get()
            retiro = self.retiro.get()
           
            seleccion = self.trabajadores.focus()
            if seleccion:
                id = int(self.trabajadores.item(seleccion).get('text'))

            if self.buscar['state'] == 'normal':
                for index in self.trabajadores.get_children():
                    if f"{self.trabajadores.item(index).get('values')[2]:0>8}" == self.dni['text']:
                        messagebox.showinfo('GRABAR', 'DNI YA REGISTRADO')
                        return            

                Insert_Personal(dni, paterno, materno, nombre, nacimiento, ingreso, planilla, asignacion, movilidad, aportacion,
                                comision, cuspp, cargo, cuenta, licencia, categoria, vencimiento, area, telefono, distrito, retiro)

            else:
                Update_Personal(id, nacimiento, ingreso, planilla, asignacion, movilidad, aportacion, comision, cuspp, cargo,
                                cuenta, licencia, categoria, vencimiento, area, telefono, distrito, retiro)

            self.CargarTrabajadores()
                        
            if seleccion:    
                for index in self.trabajadores.get_children():
                    if int(self.trabajadores.item(index).get('text')) == id:
                        self.trabajadores.selection_set(index)
                        self.trabajadores.focus(index)
                        break

            self.menuAgregar.destroy()

    def ValidarFecha(self, fecha: str):

        try:
            datetime.strptime(fecha, '%d/%m/%Y')
            return True
        except ValueError:
            return False
 
    def Agregar(self):

        contenedor = Frame(self)

        Label(contenedor, text=' Buscar DNI').place(width=205, height=60)
        Label(contenedor, text=' Numero DNI').place(y=61, width=205, height=60)
        Label(contenedor, text=' Apellido Paterno').place(y=122, width=205, height=60)
        Label(contenedor, text=' Apellido Materno').place(y=183, width=205, height=60)
        Label(contenedor, text=' Nombre').place(y=244, width=205, height=60)
        Label(contenedor, text=' Fecha de Nacimiento').place(y=305, width=205, height=60)
        Label(contenedor, text=' Fecha de Ingreso').place(y=366, width=205, height=60)
        Label(contenedor, text=' Planilla').place(y=427, width=205, height=60)
        Label(contenedor, text=' Cargo Laboral').place(y=488, width=205, height=60)
        Label(contenedor, text=' Cuenta Bancaria').place(x=206, width=205, height=60)
        Label(contenedor, text=' Entidad de Aportacion').place(x=206, y=61, width=205, height=60)
        Label(contenedor, text=' Tipo de Comision').place(x=206, y=122, width=205, height=60)
        Label(contenedor, text=' Codigo Cuspp').place(x=206, y=183, width=205, height=60)
        Label(contenedor, text=' No. de Licencia').place(x=206, y=244, width=205, height=60)
        Label(contenedor, text=' Fecha de Revalidacion').place(x=206, y=305, width=205, height=60)
        Label(contenedor, text=' Area de Labor').place(x=206, y=366, width=205, height=60)
        Label(contenedor, text=' Distrito de Residencia').place(x=206, y=427, width=205, height=60)
        Label(contenedor, text=' Fecha de Retiro').place(x=206, y=488, width=205, height=60)
        Label(contenedor, text=' Asigna.').place(x=68, y=427)
        Label(contenedor, text=' Movili.').place(x=134, y=427)        
        Label(contenedor, text=' Categoria').place(x=306, y=244)      
        Label(contenedor, text=' Telefono').place(x=306, y=366)                    
       
        self.buscar = Button(contenedor, text='BUSCAR', bg='#88C7FF', command=self.BuscarDni)
        self.buscarDni = Entry(contenedor, relief='ridge', bd=2)     
        self.dni = Label(contenedor, fg='#000000', anchor='w')        
        self.paterno = Label(contenedor, fg='#000000', anchor='w')
        self.materno = Label(contenedor, fg='#000000', anchor='w')
        self.nombre = Label(contenedor, fg='#000000', anchor='w')
        self.nacimiento = Entry(contenedor, relief='ridge', bd=2)   
        self.ingreso = Entry(contenedor, relief='ridge', bd=2)   
        self.planilla = Entry(contenedor, relief='ridge', bd=2)           
        self.asignacion = Entry(contenedor, relief='ridge', bd=2)   
        self.movilidad = Entry(contenedor, relief='ridge', bd=2)   
        self.cargo = Combobox(contenedor, state='readonly', values=['INSPECTOR VIAL', 'OPERADOR DE GRUA LIVIANA',
                                                                    'OPERADOR DE GRUA PESADA', ''])       
        self.cuenta = Entry(contenedor, relief='ridge', bd=2)   
        self.aportacion = Combobox(contenedor, state='readonly', values=['ONP', 'HABITAT', 'INTEGRA', 'PRIMA', 'PROFUTURO',''])
        self.comision = Combobox(contenedor, state='readonly', values=['FLUJO', 'MIXTA', ''])
        self.cuspp = Entry(contenedor, relief='ridge', bd=2)   
        self.licencia = Entry(contenedor, relief='ridge', bd=2) 
        self.categoria = Combobox(contenedor, state='readonly', values=['AIIA', 'AIIB', 'AIIIA', 'AIIIB', 'AIIIC', ''])       
        self.vencimiento = Entry(contenedor, relief='ridge', bd=2)             
        self.area = Combobox(contenedor, state='readonly', values=['SUR', 'NORTE', 'TALLER', 'OFICINA', ''])       
        self.telefono = Entry(contenedor, relief='ridge', bd=2)   
        self.distrito = Combobox(contenedor, state='readonly', values=['ANCON', 'ATE VITARTE', 'CARABAYLLO', 'CHORRILLOS', 'COMAS',
                                        'LOS OLIVOS', 'LURIGANCHO', 'LURIN', 'PUCUSANA', 'PUENTE PIEDRA', 'RIMAC', 'SAN BARTOLO',
                                        'SAN JUAN DE LURIGANCHO', 'SAN JUAN DE MIRAFLORES', 'SAN MARTIN DE PORRES', 'SANTA ANITA',
                                        'SANTIAGO DE SURCO', 'SURQUILLO', 'VILLA EL SALVADOR', 'VILLA MARIA DEL TRIUNFO', ''])      
        self.retiro = Entry(contenedor, relief='ridge', bd=2)
      
        self.buscar.place(x=139, y=24, width=61, height=28)    
        self.buscarDni.place(x=5, y=24, width=129, height=28)    
        self.dni.place(x=5, y=85, width=195, height=28)
        self.paterno.place(x=5, y=146, width=195, height=28)
        self.materno.place(x=5, y=207, width=195, height=28)
        self.nombre.place(x=5, y=268, width=195, height=28)        
        self.nacimiento.place(x=5, y=329, width=195, height=28)        
        self.ingreso.place(x=5, y=390, width=195, height=28)
        self.planilla.place(x=5, y=451, width=63, height=28)  
        self.asignacion.place(x=73, y=451, width=61, height=28)      
        self.movilidad.place(x=139, y=451, width=61, height=28) 
        self.cargo.place(x=5, y=512, width=195, height=28)        
        self.cuenta.place(x=211, y=24, width=195, height=28)
        self.aportacion.place(x=211, y=85, width=195, height=28) 
        self.comision.place(x=211, y=146, width=195, height=28)
        self.cuspp.place(x=211, y=207, width=195, height=28)
        self.licencia.place(x=211, y=268, width=95, height=28)
        self.categoria.place(x=311, y=268, width=95, height=28)
        self.vencimiento.place(x=211, y=329, width=195, height=28)        
        self.area.place(x=211, y=390, width=95, height=28)
        self.telefono.place(x=311, y=390, width=95, height=28)
        self.distrito.place(x=211, y=451, width=195, height=28)
        self.retiro.place(x=211, y=512, width=195, height=28)
       
        Button(contenedor, text='GRABAR', command=self.GrabarDatos).place(x=460, width=90, height=30)     
        Button(contenedor, text='SALIR' , command=lambda:contenedor.destroy(), bg='#DF2F2F').place(x=460, y=35, width=90, height=30)

        self.buscarDni.focus_set()
        contenedor.grab_set()
        
        self.menuAgregar = contenedor

        contenedor.place(x=430, y=30, width=550, height=548)

    def Modificar(self):

        if self.trabajadores.selection():          

            datos = self.trabajadores.item(self.trabajadores.focus()).get('values')
          
            self.Agregar()
            self.buscar.configure(state='disabled')
            self.buscarDni.configure(state='disabled')

            self.dni['text'] = datos[4]
            self.paterno['text'] = datos[5]
            self.materno['text'] = datos[6]
            self.nombre['text'] = datos[7]
            self.nacimiento.insert(0, datos[8])
            self.ingreso.insert(0, datos[9])
            self.planilla.insert(0, datos[10])
            self.asignacion.insert(0, datos[11])
            self.movilidad.insert(0, datos[12])
            self.aportacion.set(datos[13])
            self.comision.set(datos[14])
            self.cuspp.insert(0, datos[15])
            self.cargo.set(datos[16])
            self.cuenta.insert(0, datos[17])            
            self.licencia.insert(0, datos[18])
            self.categoria.set(datos[19])
            self.vencimiento.insert(0, datos[20])            
            self.area.set(datos[21])
            self.telefono.insert(0, datos[22])
            self.distrito.set(datos[23])
            self.retiro.insert(0, datos[24])

    def Eliminar(self):

        if self.trabajadores.selection():
            respuesta = messagebox.askyesno('ELIMINAR','SEGURO?', default='no')

            if respuesta:
                id = int(self.trabajadores.item(self.trabajadores.focus()).get('text'))                
                
                Delete_Personal(id)

                self.BorrarDetalles()
                self.CargarTrabajadores()
   

           
           
    

