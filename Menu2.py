
from tkinter import Button, Entry, Frame, Label, Scrollbar, messagebox
from tkinter.ttk import Treeview
from tkcalendar import Calendar
from scripts.sql import select, insert, update, delete

class Menu2(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)

        columna = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12')
        ancho = (30, 270, 40, 40, 40, 70, 70, 40, 40, 40, 70, 70)
        titulo = ('N°', 'APELLIDOS Y NOMBRE', 'APOYO', 'FALTA', 'FERIADO', 'INGRESO',
                   'DESCUENTO', 'D.M.', 'VACACIONES', 'C.V.', 'ADELANTI', 'POR FUERA')
        
        self.TRABAJADORES = Treeview(self, columns=columna)          

        for index, columna in enumerate(columna):
            self.TRABAJADORES.column(columna, width=ancho[index], minwidth=ancho[index], anchor='center')
            self.TRABAJADORES.heading(columna, text=titulo[index])    

        scroll = Scrollbar(self, orient='vertical', command=self.TRABAJADORES.yview)
        self.TRABAJADORES.configure(yscrollcommand=scroll.set)
       
        scroll.place(x=846, y=30, height=548)
        self.TRABAJADORES.place(x=20, y=30, height=548)

        Button(self, text='GENERAR').place(x=890, y=30, width=90, height=30)
        Button(self, text='MODIFICAR', command=self.Detalles).place(x=890, y=65, width=90, height=30)
        Button(self, text='REPORTE').place(x=890, y=100, width=90, height=30)
        Button(self, text='SALIR', command=lambda:self.destroy(), bg='#DF2F2F').place(x=890, y=135, width=90, height=30)
       
        self.CargarTrabajadores()      
        self.place(width=1000, height=600)

    def CargarTrabajadores(self):

        self.TRABAJADORES.delete(*self.TRABAJADORES.get_children())
        trabajadores = select('SELECT ID, APAT, AMAT, NOMB FROM ACTIVO ORDER BY APAT, AMAT, NOMB ASC', True)
      
        for index, trabajador in enumerate(trabajadores, 1):
            id = trabajador[0]           
            nombreCompleto = f'{trabajador[1]} {trabajador[2]} {trabajador[3]}'  

            apoyos = select(F'SELECT COUNT(FECH) FROM APOYO WHERE IDAC = {id}', False)[0]
            faltas = select(F'SELECT COUNT(FECH) FROM FALTA WHERE IDAC = {id}', False)[0]         
            feriados = select(F'SELECT COUNT(FECH) FROM FERIADO WHERE IDAC = {id}', False)[0]   
            ingresos = select(F'SELECT SUM(MONT) FROM INGRESO WHERE IDAC = {id}', False)[0]
            descuentos = select(F'SELECT SUM(MONT) FROM DESCUENTO WHERE IDAC = {id}', False)[0]
            descansoMedico = select(F'SELECT SUM(DTOT) FROM DMEDICO WHERE IDAC = {id}', False)[0]
            vacaciones = select(F'SELECT SUM(DTOT) FROM VACACIONES WHERE IDAC = {id}', False)[0]
            compraVacaciones = select(F'SELECT SUM(DTOT) FROM CVACACIONES WHERE IDAC = {id}', False)[0]
            adelantos = select(F'SELECT SUM(MONT) FROM ADELANTO WHERE IDAC = {id}', False)[0]
            porFuera = select(F'SELECT SUM(MONT) FROM XFUERA WHERE IDAC = {id}', False)[0]

            if not apoyos: apoyos = ''            
            if not faltas: faltas = ''
            if not feriados: feriados = ''
            if not descansoMedico: descansoMedico = ''
            if not vacaciones: vacaciones = ''
            if not compraVacaciones: compraVacaciones = ''
            
            if not ingresos: ingresos = ''
            else: ingresos = f'{ingresos:.2f}'
            if not descuentos: descuentos = ''
            else: descuentos = f'{descuentos:.2f}'  
            if not adelantos: adelantos = ''
            else: adelantos = f'{adelantos:.2f}'  
            if not porFuera: porFuera = ''
            else: porFuera = f'{porFuera:.2f}'         
            
            self.TRABAJADORES.insert('', 'end', text=id, values=(index, nombreCompleto, apoyos, faltas, feriados, ingresos,
                                            descuentos, descansoMedico, vacaciones, compraVacaciones, adelantos, porFuera))


    def Detalles(self):        
        
        if self.TRABAJADORES.selection():  
            contenedor = Frame(self)   
            self.calendario = Calendar(contenedor, menuselectmode='day', date_pattern='dd/MM/yyyy', cursor='hand2', borderwidth=0)
            self.calendario.place(x=20, y=30)
            #titulo = ('APOYO', 'FALTA', 'FERIADO', 'ADELANTO', 'INGRESO', 'DESCUENTO', 'VACACIONES', 'DESCANSO MEDICO', 'COMPRA VACACIONES')
            
            #for boton in range(9):
            #    Button(contenedor, text='APOYO', command=lambda:self.SaveTRABAJADORES('APO')).place(x=286, y= 20, width=100, height=22)       

            #Button(contenedor, text='APOYO'            , command=lambda:self.SaveTRABAJADORES('APO')).place(x=286, y= 20, width=100, height=22)
            #Button(contenedor, text='FALTA'            , command=lambda:self.SaveTRABAJADORES('FAL')).place(x=406, y= 20, width=100, height=22)
            #Button(contenedor, text='FERIADO'          , command=lambda:self.SaveTRABAJADORES('FER')).place(x=526, y= 20, width=100, height=22)
            #Button(contenedor, text='ADELANTO'         , command=lambda:self.SaveTRABAJADORES('ADE')).place(x=646, y= 20, width=160, height=22)
            #Button(contenedor, text='INGRESO'          , command=lambda:self.SaveTRABAJADORES('ING')).place(x= 20, y=237, width=265, height=22)
            #Button(contenedor, text='DESCUENTO'        , command=lambda:self.SaveTRABAJADORES('DES')).place(x=303, y=237, width=266, height=22)
            #Button(contenedor, text='VACACIONES'       , command=lambda:self.SaveTRABAJADORES('VAC')).place(x=586, y=237, width=220, height=22)
            #Button(contenedor, text='DESCANSO MEDICO'  , command=lambda:self.SaveTRABAJADORES('DME')).place(x= 20, y=418, width=548, height=22)
            #Button(contenedor, text='COMPRA VACACIONES', command=lambda:self.SaveTRABAJADORES('CVA')).place(x=586, y=418, width=220, height=22)

            self.fecha = []
            posicion = (20, 111, 221, 312, 422, 513, 623, 704, 820)
            for numero in range(9):
                label = Label(contenedor, cursor='hand2', anchor='center', bg='yellow')                
                label.place(x=posicion[numero], y=267, width=90, height=18)                             
                label.bind('<Button-1>', self.prueba)
                self.fecha.append(label)  
                
                

            self.apoyo = Treeview(contenedor, columns=('#1'))            
            self.apoyo.column('#1', width=84, minwidth=84, anchor='center')
            self.apoyo.heading('#1', text='APOYO', command=lambda:self.mama(self.apoyo))

            self.falta = Treeview(contenedor, columns=('#1'))          
            self.falta.column('#1', width=84, minwidth=84, anchor='center')
            self.falta.heading('#1', text='FALTA', command=lambda:self.mama(self.falta))

            self.feriado = Treeview(contenedor, columns=('#1'))           
            self.feriado.column('#1', width=84, minwidth=84, anchor='center')
            self.feriado.heading('#1', text='FERIADO', command=lambda:self.mama(self.feriado))

            self.adelanto = Treeview(contenedor, columns=('#1', '#2'))           
            self.adelanto.column('#1', width=84, anchor='center')  
            self.adelanto.column('#2', width=54, anchor='center') 
            self.adelanto.heading('#1', text='ADELANTO', command=lambda:self.mama(self.adelanto))
            self.adelanto.heading('#2', text='MONTO', command=lambda:self.mama(self.adelanto))
            
            self.ingreso = Treeview(contenedor, columns=('#1'))          
            self.ingreso.column('#1', width=199, minwidth=199, anchor='center')             
            self.ingreso.heading('#1', text='INGRESO', command=lambda:self.mama(self.ingreso))
            
            self.descuento = Treeview(contenedor, columns=('#1'))
            self.descuento.column('#1', width=199, minwidth=199, anchor='center')             
            self.descuento.heading('#1', text='DESCUENTO', command=lambda:self.mama(self.descuento))

            self.vacaciones = Treeview(contenedor, columns=('#1'))           
            self.vacaciones.column('#1', width=250, minwidth=250, anchor='center')            
            self.vacaciones.heading('#1', text='VACACIONES', command=lambda:self.mama(self.vacaciones))           

            self.dmedico = Treeview(contenedor, columns=('#1'))
            self.dmedico.column('#1', width= 250, minwidth= 250, anchor='center')           
            self.dmedico.heading('#1', text='DESCANSO MEDICO', command=lambda:self.mama(self.dmedico))      

            self.cvacaciones = Treeview(contenedor, columns=('#1'))
            self.cvacaciones.column('#1', width=250, minwidth=250, anchor='center')  
            self.cvacaciones.heading('#1', text='COMPRA VACACIONES', command=lambda:self.mama(self.cvacaciones))

            #self.adelantoImporte  = Entry(contenedor, justify='right')
            #self.ingresoDetalle   = Entry(contenedor)
            #self.ingresoImporte   = Entry(contenedor, justify='right')
            #self.descuentoDetalle = Entry(contenedor)
            #self.descuentoImporte = Entry(contenedor, justify='right')        
           

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
            

            self.apoyo.place      (x=286, y= 52, height=150)
            self.falta.place      (x=406, y= 52, height=150)
            self.feriado.place    (x=526, y= 52, height=150)
            self.adelanto.place   (x=646, y= 72, height=130)   
            self.ingreso.place    (x= 20, y=289, height= 90)
            self.descuento.place  (x=303, y=289, height= 90)
            self.vacaciones.place (x=586, y=289, height= 90)
            self.dmedico.place    (x= 20, y=470, height= 90)
            self.cvacaciones.place(x=586, y=470, height= 90)

            #self.date01.place(x=586, y=267, width=86, height=17)
            #self.date02.place(x=673, y=267, width=83, height=17)
            #self.date03.place(x= 20, y=447, width=86, height=17)
            #self.date04.place(x=107, y=447, width=83, height=17)
            #self.date05.place(x=586, y=447, width=86, height=17)
            #self.date06.place(x=673, y=447, width=83, height=17)

            #self.adelantoImporte.place (x=732, y= 50, width= 73, height=17)   
            #self.ingresoDetalle.place  (x= 20, y=267, width=201, height=17)        
            #self.ingresoImporte.place  (x=222, y=267, width= 63, height=17)
            #self.descuentoDetalle.place(x=303, y=267, width=201, height=17)        
            #self.descuentoImporte.place(x=505, y=267, width= 63, height=17)        
            #self.vacacionesTotal.place (x=757, y=267, width= 49, height=17)
            #self.dmedicoDetalle.place  (x=191, y=447, width=313, height=17)
            #self.dmedicoTotal.place    (x=505, y=447, width= 63, height=17)
            #self.cvacacionesTotal.place(x=757, y=447, width= 49, height=17) 

            Button(contenedor, text='ELIMINAR', command=self.DeleteTRABAJADORES).place(x=890, y=20, width=90, height=30)     
            Button(contenedor, text='SALIR', bg='#DF2F2F', command=lambda: contenedor.destroy()).place(x=890, y=55, width=90, height=30)

            self.CargarDetalles()    
            contenedor.place(width=1000, height=600)      

    def CargarDetalles(self):      
                  
        id = int(self.TRABAJADORES.item(self.TRABAJADORES.focus()).get('text'))
        apoy = select(F'SELECT ID, FECH FROM APOYO WHERE IDAC = {id}', True)
        falt = select(F'SELECT ID, FECH FROM FALTA WHERE IDAC = {id}', True) 
        feri = select(F'SELECT ID, FECH FROM FERIADO WHERE IDAC = {id}', True) 
        adel = select(F'SELECT ID, FECH, MONT FROM ADELANTO WHERE IDAC = {id}', True) 
        ingr = select(F'SELECT ID, DETA, MONT FROM INGRESO WHERE IDAC = {id}', True)
        desc = select(F'SELECT ID, DETA, MONT FROM DESCUENTO WHERE IDAC = {id}', True) 
        vaca = select(F'SELECT ID, FINI, FFIN, DTOT FROM VACACIONES WHERE IDAC = {id}', True) 
        dmed = select(F'SELECT ID, FINI, FFIN, DTOT FROM DMEDICO WHERE IDAC = {id}', True)
        cvac = select(F'SELECT ID, FINI, FFIN, DTOT FROM CVACACIONES WHERE IDAC = {id}', True) 

        for dato in apoy:
            self.apoyo.insert('', 'end', text=dato[0], values=(dato[1])) 

        for dato in falt:
            self.falta.insert('', 'end', text=dato[0], values=(dato[1]))

        for dato in feri:
            self.feriado.insert('', 'end', text=dato[0], values=(dato[1]))    

        for dato in adel:
            self.adelanto.insert('', 'end', text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))      

        for dato in ingr:
            self.ingreso.insert('', 'end', text=dato[0], values=(f'{dato[1]}    {dato[2]:.2f}',))    

        for dato in desc:  
            self.descuento.insert('', 'end', text=dato[0], values=(f'{dato[1]}    {dato[2]:.2f}',)) 

        for dato in vaca:
            self.vacaciones.insert('', 'end', text=dato[0], values=(f'{dato[1]}    {dato[2]}    {dato[3]}',)) 

        for dato in dmed:
            self.dmedico.insert('', 'end', text=dato[0], values=(f'{dato[1]}    {dato[2]}    {dato[3]}',)) 

        for dato in cvac:
            self.cvacaciones.insert('', 'end', text=dato[0], values=(f'{dato[1]}    {dato[2]}    {dato[3]}',))   
   

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


    def prueba(self, e):

        fecha = self.calendario.get_date()       
        e.widget['text'] = fecha
            



    def mama(self, widget):      

        
        valores = self.TRABAJADORES.item(self.TRABAJADORES.focus())['values']
        id = int(self.TRABAJADORES.item(self.TRABAJADORES.focus()).get('text'))
        fecha = self.calendario.get_date()       
        nombre = widget.winfo_name()[1:]
        detalle = {'treeview': 'APOYO', 'treeview2': 'FALTA', 'treeview3': 'FERIADO'}
        posicion = {'treeview': 2, 'treeview2': 3, 'treeview3': 4}
        print(nombre)
        if nombre == 'treeview' or nombre == 'treeview2' or nombre == 'treeview3':          
            for row in widget.get_children():
                if widget.item(row)['values'][0] == fecha:                   
                    return

            insert(f'INSERT INTO {detalle[nombre]} (IDAC, FECH) VALUES ({id}, "{fecha}")')
            idRegistro = select(f'SELECT ID FROM {detalle[nombre]} ORDER BY ID DESC', False)    

            widget.insert('', 'end', text=idRegistro[0], values=fecha)

            valores[posicion[nombre]] = len(widget.get_children())

            self.TRABAJADORES.item(self.TRABAJADORES.focus(), values=valores)
        
       
   
   
    def SaveTRABAJADORES(self, widget: str):

        valores = self.TRABAJADORES.item(self.TRABAJADORES.focus())['values']
        id = int(self.TRABAJADORES.item(self.TRABAJADORES.focus()).get('text'))
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
            self.apoyo.insert('', 'end', text=idRegistro[0], values=fecha)
                   
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
            self.falta.insert('', 'end', text=idRegistro[0], values=fecha)

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
            self.feriado.insert('', 'end', text=idRegistro[0], values=fecha)

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
                self.adelanto.insert('', 'end',text=idRegistro[0], values=(fecha, f'{monto:.2f}'))
                self.adelantoImporte.delete(0, 'end')

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
                self.ingreso.insert('', 'end', text=idRegistro[0], values=(self.ingresoDetalle.get(), f'{monto:.2f}'))
                self.ingresoDetalle.delete(0, 'end')
                self.ingresoImporte.delete(0, 'end')

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
                self.descuento.insert('', 'end', text=idRegistro[0], values=(self.descuentoDetalle.get(), f'{monto:.2f}'))
                self.descuentoDetalle.delete(0, 'end')
                self.descuentoImporte.delete(0, 'end')                    

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
                self.vacaciones.insert('', 'end', text=idRegistro[0], values=(fechaI, fechaF, total))
                self.date01['text'] = ''
                self.date02['text'] = ''
                self.vacacionesTotal.delete(0, 'end')

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
                self.dmedico.insert('', 'end', text=idRegistro[0], values=(dmedI, dmedF, detalle, total))
                self.date03['text'] = ''
                self.date04['text'] = ''
                self.dmedicoDetalle.delete(0, 'end')
                self.dmedicoTotal.delete(0, 'end')
               

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
                self.cvacaciones.insert('', 'end', text=idRegistro[0], values=(cvacI, cvacF, total))
                self.date05['text'] = ''
                self.date06['text'] = ''
                self.cvacacionesTotal.delete(0, 'end')               

        self.TRABAJADORES.item(self.TRABAJADORES.focus(), values=valores)

    def DeleteTRABAJADORES(self):

        valores = self.TRABAJADORES.item(self.TRABAJADORES.focus())['values']
                
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
            monto = float(self.adelanto.item(self.adelanto.focus())['values'][1])
            if float(valores[10]) == monto:
                valores[10] = ''
            else:
                saldo = float(valores[10]) - monto
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

        self.TRABAJADORES.item(self.TRABAJADORES.focus(), values=valores)        
