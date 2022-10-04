
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
        Button(self, text='MODIFICAR', command=self.OpenTRABAJADORES).place(x=890, y=65, width=90, height=30)
        Button(self, text='REPORTE').place(x=890, y=100, width=90, height=30)
        Button(self, text='SALIR', command=lambda:self.destroy(), bg='#DF2F2F').place(x=890, y=135, width=90, height=30)
       
        self.CargarTrabajadores()
        
        # Creamos ventana de AllTRABAJADORES y lo ocultamos
        #self.AllTRABAJADORES()
        #self.HideTRABAJADORES()
        
        self.place(width=1000, height=600)


    def CargarTrabajadores(self):

        self.TRABAJADORES.delete(*self.TRABAJADORES.get_children())
        trabajadores = select('SELECT ID, APAT, AMAT, NOMB FROM ACTIVO ORDER BY APAT, AMAT, NOMB ASC', True)

        # Insertamos datos al treeview
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


    def AllTRABAJADORES(self):
        
        # Creamos los elementos del menu 2 AllTRABAJADORES
        self = Frame(self)   

        self.calendario = Calendar(self, menuselectmode='day', date_pattern='dd/MM/yyyy', cursor='hand2', borderwidth=0)
      
        Button(self, text='APOYO'            , command=lambda:self.SaveTRABAJADORES('APO')).place(x=286, y= 20, width=100, height=22)
        Button(self, text='FALTA'            , command=lambda:self.SaveTRABAJADORES('FAL')).place(x=406, y= 20, width=100, height=22)
        Button(self, text='FERIADO'          , command=lambda:self.SaveTRABAJADORES('FER')).place(x=526, y= 20, width=100, height=22)
        Button(self, text='ADELANTO'         , command=lambda:self.SaveTRABAJADORES('ADE')).place(x=646, y= 20, width=160, height=22)
        Button(self, text='INGRESO'          , command=lambda:self.SaveTRABAJADORES('ING')).place(x= 20, y=237, width=265, height=22)
        Button(self, text='DESCUENTO'        , command=lambda:self.SaveTRABAJADORES('DES')).place(x=303, y=237, width=266, height=22)
        Button(self, text='VACACIONES'       , command=lambda:self.SaveTRABAJADORES('VAC')).place(x=586, y=237, width=220, height=22)
        Button(self, text='DESCANSO MEDICO'  , command=lambda:self.SaveTRABAJADORES('DME')).place(x= 20, y=418, width=548, height=22)
        Button(self, text='COMPRA VACACIONES', command=lambda:self.SaveTRABAJADORES('CVA')).place(x=586, y=418, width=220, height=22)
        
        self.date01 = Label(self, cursor='hand2', anchor='e')
        self.date02 = Label(self, cursor='hand2', anchor='e')
        self.date03 = Label(self, cursor='hand2', anchor='e')
        self.date04 = Label(self, cursor='hand2', anchor='e')
        self.date05 = Label(self, cursor='hand2', anchor='e')
        self.date06 = Label(self, cursor='hand2', anchor='e')

        # Evento de click del label para seleccionar fecha
        self.date01.bind('<Button-1>', lambda e: self.SelectDate('vaca1'))
        self.date02.bind('<Button-1>', lambda e: self.SelectDate('vaca2')) 
        self.date03.bind('<Button-1>', lambda e: self.SelectDate('dmed1'))        
        self.date04.bind('<Button-1>', lambda e: self.SelectDate('dmed2'))        
        self.date05.bind('<Button-1>', lambda e: self.SelectDate('cvac1'))
        self.date06.bind('<Button-1>', lambda e: self.SelectDate('cvac2'))

        self.apoyo = Treeview(self, columns=('#1'))
        self.apoyo.column('#0', width=0)
        self.apoyo.column('#1', width=94, minwidth=94, anchor='center')
        self.apoyo.heading('#1', text='Fecha')
        self.falta = Treeview(self, columns=('#1'))
        self.falta.column('#0', width=0)
        self.falta.column('#1', width=94, minwidth=94, anchor='center')
        self.falta.heading('#1', text='Fecha')
        self.feriado = Treeview(self, columns=('#1'))
        self.feriado.column('#0', width=0)
        self.feriado.column('#1', width=94, minwidth=94, anchor='center')
        self.feriado.heading('#1', text='Fecha')
        self.adelanto = Treeview(self, columns=('#1', '#2'))
        self.adelanto.column('#0', width=0)
        self.adelanto.column('#1', width=82, anchor='center')         
        self.adelanto.column('#2', width=71, anchor='e')
        self.adelanto.heading('#1', text='Fecha')
        self.adelanto.heading('#2', text='Importe')        
        self.ingreso = Treeview(self, columns=('#1', '#2'))
        self.ingreso.column('#0', width=0)
        self.ingreso.column('#1', width=199, minwidth=199) 
        self.ingreso.column('#2', width= 60, minwidth= 60, anchor='e')
        self.ingreso.heading('#1', text='Fecha')
        self.ingreso.heading('#2', text='Importe')
        self.descuento = Treeview(self, columns=('#1', '#2'))
        self.descuento.column('#0', width=0)
        self.descuento.column('#1', width=199, minwidth=199) 
        self.descuento.column('#2', width= 60, minwidth= 60, anchor='e')
        self.descuento.heading('#1', text='Detalle')
        self.descuento.heading('#2', text='Importe')        
        self.vacaciones = Treeview(self, columns=('#1', '#2', '#3'))
        self.vacaciones.column('#0', width=0)
        self.vacaciones.column('#1', width=84, minwidth=84) 
        self.vacaciones.column('#2', width=84, minwidth=84) 
        self.vacaciones.column('#3', width=46, minwidth=46, anchor='e') 
        self.vacaciones.heading('#1', text='F. Inicial')
        self.vacaciones.heading('#2', text='F. Final')
        self.vacaciones.heading('#3', text='Dias')        
        self.dmedico = Treeview(self, columns=('#1', '#2', '#3', '#4'))
        self.dmedico.column('#0', width=0)
        self.dmedico.column('#1', width= 84, minwidth= 84) 
        self.dmedico.column('#2', width= 84, minwidth= 84) 
        self.dmedico.column('#3', width=314, minwidth=314) 
        self.dmedico.column('#4', width= 60, minwidth= 60, anchor='e') 
        self.dmedico.heading('#1', text='F. Inicial')
        self.dmedico.heading('#2', text='F. Final')
        self.dmedico.heading('#3', text='Detalle')
        self.dmedico.heading('#4', text='Dias')
        self.cvacaciones = Treeview(self, columns=('#1', '#2', '#3'))
        self.cvacaciones.column('#0', width=0)
        self.cvacaciones.column('#1', width=84, minwidth=84) 
        self.cvacaciones.column('#2', width=84, minwidth=84) 
        self.cvacaciones.column('#3', width=46, minwidth=46, anchor='e') 
        self.cvacaciones.heading('#1', text='F. Inicial')
        self.cvacaciones.heading('#2', text='F. Final')
        self.cvacaciones.heading('#3', text='Dias')

        self.adelantoImporte  = Entry(self, justify='right')
        self.ingresoDetalle   = Entry(self)
        self.ingresoImporte   = Entry(self, justify='right')
        self.descuentoDetalle = Entry(self)
        self.descuentoImporte = Entry(self, justify='right')        
        self.vacacionesTotal  = Entry(self, justify='right')
        self.dmedicoDetalle   = Entry(self)
        self.dmedicoTotal     = Entry(self, justify='right')
        self.cvacacionesTotal = Entry(self, justify='right')

        # Evento de click del treeview para quitar seleccion
        #self.apoyo.bind('<Button-1>', self.RemoveSelection)
        #self.falta.bind('<Button-1>', self.RemoveSelection) 
        #self.feriado.bind('<Button-1>', self.RemoveSelection)
        #self.adelanto.bind('<Button-1>', self.RemoveSelection)
        #self.ingreso.bind('<Button-1>', self.RemoveSelection)
        #self.descuento.bind('<Button-1>', self.RemoveSelection)
        #self.vacaciones.bind('<Button-1>', self.RemoveSelection)
        #self.dmedico.bind('<Button-1>', self.RemoveSelection)
        #self.cvacaciones.bind('<Button-1>', self.RemoveSelection)
        
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
        Button(self, text='ELIMINAR',            command=self.DeleteTRABAJADORES).place(x=890, y=20, width=90, height=30)     
        Button(self, text='SALIR', bg='#DF2F2F', command=self.HideTRABAJADORES ).place(x=890, y=55, width=90, height=30)

        # Asignamos variable para poder destruir la ventana
        self.men2_AllTRABAJADORES = self

        # Posicionamos la ventana principal
        self.place(width=1000, height=600)         

    
    def OpenTRABAJADORES(self):
      
        # Mostramos la ventana AllTRABAJADORES
        if self.TRABAJADORES.selection():            
            id = int(self.TRABAJADORES.item(self.TRABAJADORES.focus()).get('text'))

            # Ejecutamos consultas de los AllTRABAJADORES de cada trabajador en base de datos
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
                self.apoyo.insert('', 'end', text=dato[0], values=(dato[1])) 

            for dato in falt:
                self.falta.insert('', 'end', text=dato[0], values=(dato[1]))

            for dato in feri:
                self.feriado.insert('', 'end', text=dato[0], values=(dato[1]))    

            for dato in adel:
                self.adelanto.insert('', 'end', text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))      

            for dato in ingr:
                self.ingreso.insert('', 'end', text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))    

            for dato in desc:
                self.descuento.insert('', 'end', text=dato[0], values=(dato[1], f'{dato[2]:.2f}')) 

            for dato in vaca:
                self.vacaciones.insert('', 'end', text=dato[0], values=(dato[1], dato[2], dato[3])) 

            for dato in dmed:
                self.dmedico.insert('', 'end', text=dato[0], values=(dato[1], dato[2], dato[3], dato[4])) 

            for dato in cvac:
                self.cvacaciones.insert('', 'end', text=dato[0], values=(dato[1], dato[2], dato[3]))     
          
            self.men2_AllTRABAJADORES.place(width=980, height=580) 
            self.men2_AllTRABAJADORES.grab_set()

    def HideTRABAJADORES(self):
        
        # Limpiamos los cuadros de la ventana AllTRABAJADORES
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

        self.adelantoImporte.delete(0, 'end')
        self.ingresoDetalle.delete(0, 'end')
        self.ingresoImporte.delete(0, 'end')
        self.descuentoDetalle.delete(0, 'end')
        self.descuentoImporte.delete(0, 'end')        
        self.vacacionesTotal.delete(0, 'end')       
        self.dmedicoDetalle.delete(0, 'end')
        self.dmedicoTotal.delete(0, 'end')
        self.cvacacionesTotal.delete(0, 'end')
        
        # Ocultamos la ventana AllTRABAJADORES
        self.men2_AllTRABAJADORES.place_forget() 
        self.men2_AllTRABAJADORES.grab_release()   

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

        self.TRABAJADORES.item(self.TRABAJADORES.focus(), values=valores)        
