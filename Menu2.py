from tkinter import Button, Entry, Frame, Label, Scrollbar, messagebox
from tkinter.ttk import Treeview
from tkcalendar import Calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scripts.sql import Select_Personal, Select_Apoyo_Id, Insert_Apoyo, Select_Falta_Id

class Menu2(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)        
        
        self.TRABAJADORES = Treeview(self, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12'))          
        self.TRABAJADORES.column('#1', width=30, minwidth=30, anchor='center')
        self.TRABAJADORES.column('#2', width=270, minwidth=270)
        self.TRABAJADORES.column('#3', width=40, minwidth=40, anchor='center')
        self.TRABAJADORES.column('#4', width=40, minwidth=40, anchor='center')
        self.TRABAJADORES.column('#5', width=40, minwidth=40, anchor='center')
        self.TRABAJADORES.column('#6', width=70, minwidth=70, anchor='center')
        self.TRABAJADORES.column('#7', width=70, minwidth=70, anchor='center')
        self.TRABAJADORES.column('#8', width=40, minwidth=40, anchor='center')
        self.TRABAJADORES.column('#9', width=40, minwidth=40, anchor='center')
        self.TRABAJADORES.column('#10', width=40, minwidth=40, anchor='center')
        self.TRABAJADORES.column('#11', width=70, minwidth=70, anchor='center')
        self.TRABAJADORES.column('#12', width=70, minwidth=70, anchor='center')
        self.TRABAJADORES.heading('#1', text='N°')
        self.TRABAJADORES.heading('#2', text='APELLIDOS Y NOMBRE')    
        self.TRABAJADORES.heading('#3', text='APO')    
        self.TRABAJADORES.heading('#4', text='FAL')    
        self.TRABAJADORES.heading('#5', text='FER')    
        self.TRABAJADORES.heading('#6', text='INGRE')    
        self.TRABAJADORES.heading('#7', text='DESCU')    
        self.TRABAJADORES.heading('#8', text='DME')    
        self.TRABAJADORES.heading('#9', text='VAC')    
        self.TRABAJADORES.heading('#10', text='CVA')    
        self.TRABAJADORES.heading('#11', text='ADELA')
        self.TRABAJADORES.heading('#12', text='FUERA')

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

        Insert_Apoyo(5, "02/01/2022")
        self.TRABAJADORES.delete(*self.TRABAJADORES.get_children())
        trabajadores = Select_Personal()
      
        for index, trabajador in enumerate(trabajadores, 1):         
            id = int(trabajador[0])           
            nombreCompleto = f'{trabajador[2]} {trabajador[3]} {trabajador[4]}'  

           
            feriados = ""
            adelantos = ""
            porFuera = ""
            ingresos = ""
            descuentos = ""
            vacaciones = ""
            compraVacaciones = ""
            descansoMedico = ""

            apoyo = len(Select_Apoyo_Id(id))
            falta = len(Select_Falta_Id(id))
            #faltas = select(F'SELECT COUNT(FECH) FROM FALTA WHERE IDAC = {id}', False)[0]         
            #feriados = select(F'SELECT COUNT(FECH) FROM FERIADO WHERE IDAC = {id}', False)[0]   
            #adelantos = select(F'SELECT SUM(MONT) FROM ADELANTO WHERE IDAC = {id}', False)[0]
            #porFuera = select(F'SELECT SUM(MONT) FROM XFUERA WHERE IDAC = {id}', False)[0]
            #ingresos = select(F'SELECT SUM(MONT) FROM INGRESO WHERE IDAC = {id}', False)[0]
            #descuentos = select(F'SELECT SUM(MONT) FROM DESCUENTO WHERE IDAC = {id}', False)[0]
            #vacaciones = select(F'SELECT SUM(DTOT) FROM VACACIONES WHERE IDAC = {id}', False)[0]
            #compraVacaciones = select(F'SELECT SUM(DTOT) FROM CVACACIONES WHERE IDAC = {id}', False)[0]
            #descansoMedico = select(F'SELECT SUM(DTOT) FROM DMEDICO WHERE IDAC = {id}', False)[0]

            #if not apoyos: apoyos = ''            
            #if not faltas: faltas = ''
            #if not feriados: feriados = ''            
            #if not vacaciones: vacaciones = ''
            #if not compraVacaciones: compraVacaciones = ''
            #if not descansoMedico: descansoMedico = ''
            
            #if not adelantos: adelantos = ''
            #else: adelantos = f'{adelantos:.2f}'  
            #if not porFuera: porFuera = ''
            #else: porFuera = f'{porFuera:.2f}'        
            #if not ingresos: ingresos = ''
            #else: ingresos = f'{ingresos:.2f}'
            #if not descuentos: descuentos = ''
            #else: descuentos = f'{descuentos:.2f}'             
            
            self.TRABAJADORES.insert('', 'end', text=id, values=(index, nombreCompleto, apoyo, falta, feriados, ingresos,
                                            descuentos, descansoMedico, vacaciones, compraVacaciones, adelantos, porFuera))

    def Detalles(self):

        if not self.TRABAJADORES.selection(): return

        contenedor = Frame(self)   
        self.calendario = Calendar(contenedor, menuselectmode='day', date_pattern='dd/MM/yyyy', cursor='hand2')
        self.calendario.place(x=20, y=30, width=240, height=230)

        self.apoyo = Treeview(contenedor, columns=('#1'))            
        self.apoyo.column('#1', width=84, minwidth=84, anchor='center')
        self.apoyo.heading('#1', text='APOYO', command=lambda:self.RegistrarDetalle(1))
        self.apoyo.place(x=270, y=30, height=230)            

        self.falta = Treeview(contenedor, columns=('#1'))
        self.falta.column('#1', width=84, minwidth=84, anchor='center')
        self.falta.heading('#1', text='FALTA', command=lambda:self.RegistrarDetalle(2))
        self.falta.place(x=370, y=30, height=230)

        self.feriado = Treeview(contenedor, columns=('#1'))           
        self.feriado.column('#1', width=84, minwidth=84, anchor='center')
        self.feriado.heading('#1', text='FERIADO', command=lambda:self.RegistrarDetalle(3))
        self.feriado.place(x=470, y= 30, height=230)

        self.adelanto = Treeview(contenedor, columns=('#1', '#2'))           
        self.adelanto.column('#1', width=74, minwidth=74, anchor='center')  
        self.adelanto.column('#2', width=53, minwidth=53, anchor='center')             
        self.adelanto.heading('#1', text='ADELANTO', command=lambda:self.RegistrarDetalle(4))
        self.adelanto.heading('#2', text='MONTO', command=lambda:self.RegistrarDetalle(4))
        self.adelanto.place(x=570, y=30, height=210) 

        self.porFuera = Treeview(contenedor, columns=('#1', '#2'))           
        self.porFuera.column('#1', width=74, minwidth=74, anchor='center')  
        self.porFuera.column('#2', width=53, minwidth=53, anchor='center')             
        self.porFuera.heading('#1', text='POR FUERA', command=lambda:self.RegistrarDetalle(5))
        self.porFuera.heading('#2', text='MONTO', command=lambda:self.RegistrarDetalle(5))
        self.porFuera.place(x=713, y=30, height=210)  

        self.ingreso = Treeview(contenedor, columns=('#1', '#2'))          
        self.ingreso.column('#1', width=349, minwidth=349)  
        self.ingreso.column('#2', width=53, minwidth=53, anchor='center')              
        self.ingreso.heading('#1', text='INGRESO', command=lambda:self.RegistrarDetalle(6))
        self.ingreso.heading('#2', text='MONTO', command=lambda:self.RegistrarDetalle(6))
        self.ingreso.place(x=20, y=288, height=110)

        self.descuento = Treeview(contenedor, columns=('#1', '#2'))
        self.descuento.column('#1', width=349, minwidth=349)      
        self.descuento.column('#2', width=53, minwidth=53, anchor='center')             
        self.descuento.heading('#1', text='DESCUENTO', command=lambda:self.RegistrarDetalle(7))
        self.descuento.heading('#2', text='MONTO', command=lambda:self.RegistrarDetalle(7))
        self.descuento.place(x=438, y=288, height=110)

        self.vacaciones = Treeview(contenedor, columns=('#1', '#2'))           
        self.vacaciones.column('#1', width=213, minwidth=213, anchor='center')  
        self.vacaciones.column('#2', width=50, minwidth=50, anchor='center')
        self.vacaciones.heading('#1', text='VACACIONES', command=lambda:self.RegistrarDetalle(8))       
        self.vacaciones.heading('#2', text='DIAS', command=lambda:self.RegistrarDetalle(8))    
        self.vacaciones.place (x=20, y=447, height=110)               

        self.cvacaciones = Treeview(contenedor, columns=('#1', '#2'))
        self.cvacaciones.column('#1', width=213, minwidth=213, anchor='center')  
        self.cvacaciones.column('#2', width=50, minwidth=50, anchor='center') 
        self.cvacaciones.heading('#1', text='COMPRA DE VACACIONES', command=lambda:self.RegistrarDetalle(9))
        self.cvacaciones.heading('#2', text='DIAS', command=lambda:self.RegistrarDetalle(9))
        self.cvacaciones.place(x=299, y=447, height=110)

        self.dmedico = Treeview(contenedor, columns=('#1', '#2'))
        self.dmedico.column('#1', width=212, minwidth=212, anchor='center')
        self.dmedico.column('#2', width=50, minwidth=50, anchor='center')
        self.dmedico.heading('#1', text='DESCANSO MEDICO', command=lambda:self.RegistrarDetalle(10))
        self.dmedico.heading('#2', text='DIAS', command=lambda:self.RegistrarDetalle(10))
        self.dmedico.place(x=578, y=447, height=110)

        self.apoyo.bind('<Button-1>', self.QuitarSeleccion)
        self.falta.bind('<Button-1>', self.QuitarSeleccion) 
        self.feriado.bind('<Button-1>', self.QuitarSeleccion)
        self.adelanto.bind('<Button-1>', self.QuitarSeleccion)
        self.porFuera.bind('<Button-1>', self.QuitarSeleccion)
        self.ingreso.bind('<Button-1>', self.QuitarSeleccion)
        self.descuento.bind('<Button-1>', self.QuitarSeleccion)
        self.vacaciones.bind('<Button-1>', self.QuitarSeleccion)            
        self.cvacaciones.bind('<Button-1>', self.QuitarSeleccion)
        self.dmedico.bind('<Button-1>', self.QuitarSeleccion)

        self.fechaAdelanto = Label(contenedor, cursor='hand2', anchor='center', bg='yellow')
        self.fechaPorFuera = Label(contenedor, cursor='hand2', anchor='center', bg='yellow')
        self.fechaVacaciones1 = Label(contenedor, cursor='hand2', anchor='center', bg='yellow')
        self.fechaVacaciones2 = Label(contenedor, cursor='hand2', anchor='center', bg='yellow')
        self.fechaCVacaciones1 = Label(contenedor, cursor='hand2', anchor='center', bg='yellow')
        self.fechaCVacaciones2 = Label(contenedor, cursor='hand2', anchor='center', bg='yellow')
        self.fechaDMedico1 = Label(contenedor, cursor='hand2', anchor='center', bg='yellow')
        self.fechaDMedico2 = Label(contenedor, cursor='hand2', anchor='center', bg='yellow')

        self.fechaAdelanto.bind('<Button-1>', self.SeleccionarFecha)
        self.fechaPorFuera.bind('<Button-1>', self.SeleccionarFecha)
        self.fechaVacaciones1.bind('<Button-1>', self.SeleccionarFecha)
        self.fechaVacaciones2.bind('<Button-1>', self.SeleccionarFecha)
        self.fechaCVacaciones1.bind('<Button-1>', self.SeleccionarFecha)
        self.fechaCVacaciones2.bind('<Button-1>', self.SeleccionarFecha)
        self.fechaDMedico1.bind('<Button-1>', self.SeleccionarFecha)
        self.fechaDMedico2.bind('<Button-1>', self.SeleccionarFecha)

        self.fechaAdelanto.place(x=571, y=243, width=74, height=17)
        self.fechaPorFuera.place(x=714, y=243, width=74, height=17)
        self.fechaVacaciones1.place(x=21, y=560, width=132, height=17)
        self.fechaVacaciones2.place(x=156, y=560, width=132, height=17)
        self.fechaCVacaciones1.place(x=300, y=560, width=132, height=17)
        self.fechaCVacaciones2.place(x=435, y=560, width=132, height=17)
        self.fechaDMedico1.place(x=579, y=560, width=132, height=17)
        self.fechaDMedico2.place(x=714, y=560, width=131, height=17)

        self.montoAdelanto = Entry(contenedor, cursor='hand2', bg='yellow')
        self.montoPorFuera = Entry(contenedor, cursor='hand2', bg='yellow')
        self.detalleIngreso = Entry(contenedor, cursor='hand2', bg='yellow')
        self.montoIngreso = Entry(contenedor, cursor='hand2', bg='yellow')
        self.detalleDescuento = Entry(contenedor, cursor='hand2', bg='yellow')
        self.montoDescuento = Entry(contenedor, cursor='hand2', bg='yellow')

        self.montoAdelanto.place(x=648, y=243, width=54, height=17)
        self.montoPorFuera.place(x=791, y=243, width=54, height=17)
        self.detalleIngreso.place(x=21, y=401, width=349, height=17)
        self.montoIngreso.place(x=373, y=401, width=54, height=17)
        self.detalleDescuento.place(x=439, y=401, width=349, height=17)
        self.montoDescuento.place(x=791, y=401, width=54, height=17)     
       
        Button(contenedor, text='ELIMINAR', command=self.EliminarDetalle).place(x=890, y=30, width=90, height=30)     
        Button(contenedor, text='SALIR', bg='#DF2F2F', command=lambda: contenedor.destroy()).place(x=890, y=65, width=90, height=30)

        self.CargarDetalles()
        contenedor.place(width=1000, height=600)

    def CargarDetalles(self):      
                  
        id = int(self.TRABAJADORES.item(self.TRABAJADORES.focus()).get('text'))
        apoyo = Select_Apoyo_Id(id)
        falta = Select_Falta_Id(id)
        #feri = select(F'SELECT ID, FECH FROM FERIADO WHERE IDAC = {id}', True) 
        #adel = select(F'SELECT ID, FECH, MONT FROM ADELANTO WHERE IDAC = {id}', True) 
        #xfue = select(F'SELECT ID, FECH, MONT FROM XFUERA WHERE IDAC = {id}', True) 
        #ingr = select(F'SELECT ID, DETA, MONT FROM INGRESO WHERE IDAC = {id}', True)
        #desc = select(F'SELECT ID, DETA, MONT FROM DESCUENTO WHERE IDAC = {id}', True) 
        #vaca = select(F'SELECT ID, FINI, FFIN, DTOT FROM VACACIONES WHERE IDAC = {id}', True)         
        #cvac = select(F'SELECT ID, FINI, FFIN, DTOT FROM CVACACIONES WHERE IDAC = {id}', True) 
        #dmed = select(F'SELECT ID, FINI, FFIN, DTOT FROM DMEDICO WHERE IDAC = {id}', True)

        for dato in apoyo: self.apoyo.insert('', 'end', text=dato[0], values=(dato[2]))
        for dato in falta: self.falta.insert('', 'end', text=dato[0], values=(dato[2]))
        #for dato in feri: self.feriado.insert('', 'end', text=dato[0], values=(dato[1]))
        #for dato in adel: self.adelanto.insert('', 'end', text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))
        #for dato in xfue: self.porFuera.insert('', 'end', text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))
        #for dato in ingr: self.ingreso.insert('', 'end', text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))
        #for dato in desc: self.descuento.insert('', 'end', text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))
        #for dato in vaca: self.vacaciones.insert('', 'end', text=dato[0], values=(f'{dato[1]} - {dato[2]}', dato[3]))
        #for dato in cvac: self.cvacaciones.insert('', 'end', text=dato[0], values=(f'{dato[1]} - {dato[2]}', dato[3]))
        #for dato in dmed: self.dmedico.insert('', 'end', text=dato[0], values=(f'{dato[1]} - {dato[2]}', dato[3]))
   
    def QuitarSeleccion(self, e):
        
        self.apoyo.selection_set('') 
        self.falta.selection_set('')      
        self.feriado.selection_set('')       
        self.adelanto.selection_set('')  
        self.porFuera.selection_set('')  
        self.ingreso.selection_set('')
        self.descuento.selection_set('')
        self.vacaciones.selection_set('')        
        self.cvacaciones.selection_set('')
        self.dmedico.selection_set('')

    def SeleccionarFecha(self, e):

        fecha = self.calendario.get_date()       
        e.widget['text'] = fecha
    
    def RegistrarDetalle(self, treeview: int):        
        
        filaTrabajador = self.TRABAJADORES.focus()
        detallesTrabajador = self.TRABAJADORES.item(filaTrabajador)['values']

        idTrabajador = int(self.TRABAJADORES.item(filaTrabajador).get('text'))

        fechaCalendario = self.calendario.get_date()        

        match treeview:
            case 1:
                for fila in self.apoyo.get_children():
                    apoyo = self.apoyo.item(fila)['values'][0]
                    if apoyo == fechaCalendario: return
                
                insert(f'INSERT INTO APOYO (IDAC, FECH) VALUES ({idTrabajador}, "{fechaCalendario}")')
                idApoyo = select(f'SELECT ID FROM APOYO ORDER BY ID DESC', False)[0]

                self.apoyo.insert('', 'end', text=idApoyo, values=fechaCalendario)
                detallesTrabajador[2] = len(self.apoyo.get_children())
                
            case 2:
                for fila in self.falta.get_children():
                    falta = self.falta.item(fila)['values'][0]
                    if falta == fechaCalendario: return
                
                insert(f'INSERT INTO FALTA (IDAC, FECH) VALUES ({idTrabajador}, "{fechaCalendario}")')
                idFalta = select(f'SELECT ID FROM FALTA ORDER BY ID DESC', False)[0]

                self.falta.insert('', 'end', text=idFalta, values=fechaCalendario)
                detallesTrabajador[3] = len(self.falta.get_children())
            
            case 3:
                for fila in self.feriado.get_children():
                    feriado = self.feriado.item(fila)['values'][0]
                    if feriado == fechaCalendario: return
                
                insert(f'INSERT INTO FERIADO (IDAC, FECH) VALUES ({idTrabajador}, "{fechaCalendario}")')
                idFeriado = select(f'SELECT ID FROM FERIADO ORDER BY ID DESC', False)[0]

                self.feriado.insert('', 'end', text=idFeriado, values=fechaCalendario)
                detallesTrabajador[4] = len(self.feriado.get_children())
            
            case 4:
                monto = self.montoAdelanto.get()

                if not self.fechaAdelanto['text']:
                    messagebox.showinfo('ADELANTO', 'Registra la fecha del adelanto !')
                elif monto == '':
                    self.montoAdelanto.focus_set()
                    messagebox.showinfo('ADELANTO', 'Registra el importe del adelanto !')
                elif monto.count('.') > 1:
                    self.montoAdelanto.focus_set()
                    messagebox.showinfo('ADELANTO', 'Registra correctamente el importe del adelanto !')
                elif not monto.replace('.','').isnumeric():
                    self.montoAdelanto.focus_set()
                    messagebox.showinfo('ADELANTO', 'Registra correctamente el importe del adelanto !')
                else:
                    
                    insert(f'INSERT INTO ADELANTO (IDAC, FECH, MONT) VALUES ({idTrabajador}, "{fechaCalendario}", {float(monto)})')
                    idAdelanto = select(f'SELECT ID FROM ADELANTO ORDER BY ID DESC', False)[0]

                    self.adelanto.insert('', 'end',text=idAdelanto, values=(fechaCalendario, f'{float(monto):.2f}'))                    

                    if detallesTrabajador[10]:
                        totalIngresos = float(detallesTrabajador[10]) + float(monto)
                        detallesTrabajador[10] =  f'{totalIngresos:.2f}'
                    else:                    
                        detallesTrabajador[10] = f'{float(monto):.2f}'

                    self.fechaAdelanto['text'] = ''
                    self.montoAdelanto.delete(0, 'end')

            case 5:
                monto = self.montoPorFuera.get()

                if not self.fechaPorFuera['text']:
                    messagebox.showinfo('POR FUERA', 'Registra la fecha del por fuera !')
                elif monto == '':
                    self.montoPorFuera.focus_set()
                    messagebox.showinfo('POR FUERA', 'Registra el importe del por fuera !')
                elif monto.count('.') > 1:
                    self.montoPorFuera.focus_set()
                    messagebox.showinfo('POR FUERA', 'Registra correctamente el importe del por fuera !')
                elif not monto.replace('.','').isnumeric():
                    self.montoPorFuera.focus_set()
                    messagebox.showinfo('POR FUERA', 'Registra correctamente el importe del por fuera !')
                else:
                    
                    insert(f'INSERT INTO XFUERA (IDAC, FECH, MONT) VALUES ({idTrabajador}, "{fechaCalendario}", {float(monto)})')
                    idPorFuera = select(f'SELECT ID FROM XFUERA ORDER BY ID DESC', False)[0]

                    self.porFuera.insert('', 'end',text=idPorFuera, values=(fechaCalendario, f'{float(monto):.2f}'))                    

                    if detallesTrabajador[11]:
                        totalPorFuera = float(detallesTrabajador[11]) + float(monto)
                        detallesTrabajador[11] =  f'{totalPorFuera:.2f}'
                    else:                    
                        detallesTrabajador[11] = f'{float(monto):.2f}'

                    self.fechaPorFuera['text'] = ''
                    self.montoPorFuera.delete(0, 'end')                     

            case 6:
                monto = self.montoIngreso.get()
                detalle = self.detalleIngreso.get().upper()

                if detalle == '':
                    messagebox.showinfo('INGRESO', 'Registra el detalle del ingreso !')
                    self.detalleIngreso.focus_set()
                elif monto == '':
                    self.montoIngreso.focus_set()
                    messagebox.showinfo('INGRESO', 'Registra el importe del ingreso !')
                elif monto.count('.') > 1:
                    self.montoIngreso.focus_set()
                    messagebox.showinfo('INGRESO', 'Registra correctamente el importe del ingreso !')
                elif not monto.replace('.','').isnumeric():
                    self.montoIngreso.focus_set()
                    messagebox.showinfo('INGRESO', 'Registra correctamente el importe del ingreso !')
                else:
                    
                    insert(f'INSERT INTO INGRESO (IDAC, DETA, MONT) VALUES ({idTrabajador}, "{detalle}", {float(monto)})')
                    idIngreso = select(f'SELECT ID FROM INGRESO ORDER BY ID DESC', False)[0]

                    self.ingreso.insert('', 'end',text=idIngreso, values=(detalle, f'{float(monto):.2f}'))                    

                    if detallesTrabajador[5]:
                        totalIngreso = float(detallesTrabajador[5]) + float(monto)
                        detallesTrabajador[5] =  f'{totalIngreso:.2f}'
                    else:                    
                        detallesTrabajador[5] = f'{float(monto):.2f}'

                    self.detalleIngreso.delete(0, 'end') 
                    self.montoIngreso.delete(0, 'end')        

            case 7:
                monto = self.montoDescuento.get()
                detalle = self.detalleDescuento.get().upper()

                if detalle == '':
                    messagebox.showinfo('DESCUENTO', 'Registra el detalle del descuento !')
                    self.detalleDescuento.focus_set()
                elif monto == '':
                    self.montoDescuento.focus_set()
                    messagebox.showinfo('DESCUENTO', 'Registra el importe del descuento !')
                elif monto.count('.') > 1:
                    self.montoDescuento.focus_set()
                    messagebox.showinfo('DESCUENTO', 'Registra correctamente el importe del descuento !')
                elif not monto.replace('.','').isnumeric():
                    self.montoDescuento.focus_set()
                    messagebox.showinfo('DESCUENTO', 'Registra correctamente el importe del descuento !')
                else:
                    
                    insert(f'INSERT INTO DESCUENTO (IDAC, DETA, MONT) VALUES ({idTrabajador}, "{detalle}", {float(monto)})')
                    idDescuento = select(f'SELECT ID FROM DESCUENTO ORDER BY ID DESC', False)[0]

                    self.descuento.insert('', 'end',text=idDescuento, values=(detalle, f'{float(monto):.2f}'))                    

                    if detallesTrabajador[6]:
                        totalDescuento = float(detallesTrabajador[6]) + float(monto)
                        detallesTrabajador[6] =  f'{totalDescuento:.2f}'
                    else:                    
                        detallesTrabajador[6] = f'{float(monto):.2f}'

                    self.detalleDescuento.delete(0, 'end') 
                    self.montoDescuento.delete(0, 'end')  

            case 8:
                fechaInicial = self.fechaVacaciones1['text']
                fechaFinal = self.fechaVacaciones2['text']                

                if not fechaInicial:
                    messagebox.showinfo('VACACIONES', 'Registra la fecha inicial de las vacaciones !')
                elif not fechaFinal:
                    messagebox.showinfo('VACACIONES', 'Registra la fecha final de las vacaciones !')
                elif not self.CompararFechas(fechaInicial, fechaFinal):
                    messagebox.showinfo('VACACIONES', 'Registra correctamente las fechas !')
                else:

                    diferencia = relativedelta( datetime.strptime(fechaFinal, '%d/%m/%Y'), 
                                                datetime.strptime(fechaInicial, '%d/%m/%Y'))  
                    totalDias = diferencia.days + 1

                    insert(f'''INSERT INTO VACACIONES (IDAC, FINI, FFIN, DTOT)
                                VALUES ({idTrabajador}, "{fechaInicial}", "{fechaFinal}", {totalDias})''')
                    idVacaciones = select(f'SELECT ID FROM VACACIONES ORDER BY ID DESC', False)[0]

                    self.vacaciones.insert('', 'end',text=idVacaciones, values=(f'{fechaInicial} - {fechaFinal}', totalDias))

                    if detallesTrabajador[8]:
                        totalVacaciones = int(detallesTrabajador[8]) + totalDias
                        detallesTrabajador[8] = totalVacaciones
                    else:
                        detallesTrabajador[8] = totalDias

                    self.fechaVacaciones1['text'] = ''
                    self.fechaVacaciones2['text'] = ''

            case 9:
                fechaInicial = self.fechaCVacaciones1['text']
                fechaFinal = self.fechaCVacaciones2['text']                

                if not fechaInicial:
                    messagebox.showinfo('COMPRA DE VACACIONES', 'Registra la fecha inicial de la compra de vacaciones !')
                elif not fechaFinal:
                    messagebox.showinfo('COMPRA DE VACACIONES', 'Registra la fecha final de la compra de vacaciones !')
                elif not self.CompararFechas(fechaInicial, fechaFinal):
                    messagebox.showinfo('COMPRA DE VACACIONES', 'Registra correctamente la compra de vacaciones !')
                else:

                    diferencia = relativedelta( datetime.strptime(fechaFinal, '%d/%m/%Y'), 
                                                datetime.strptime(fechaInicial, '%d/%m/%Y'))  
                    totalDias = diferencia.days + 1

                    insert(f'''INSERT INTO CVACACIONES (IDAC, FINI, FFIN, DTOT)
                                VALUES ({idTrabajador}, "{fechaInicial}", "{fechaFinal}", {totalDias})''')
                    idCVacaciones = select(f'SELECT ID FROM CVACACIONES ORDER BY ID DESC', False)[0]

                    self.cvacaciones.insert('', 'end',text=idCVacaciones, values=(f'{fechaInicial} - {fechaFinal}', totalDias))

                    if detallesTrabajador[9]:
                        totalCVacaciones = int(detallesTrabajador[9]) + totalDias
                        detallesTrabajador[9] = totalCVacaciones
                    else:
                        detallesTrabajador[9] = totalDias

                    self.fechaCVacaciones1['text'] = ''
                    self.fechaCVacaciones2['text'] = ''

            case 10:
                fechaInicial = self.fechaDMedico1['text']
                fechaFinal = self.fechaDMedico2['text']                

                if not fechaInicial:
                    messagebox.showinfo('DESCANSO MEDICO', 'Registra la fecha inicial del descanso medico !')
                elif not fechaFinal:
                    messagebox.showinfo('DESCANSO MEDICO', 'Registra la fecha final del descanso medico !')
                elif not self.CompararFechas(fechaInicial, fechaFinal):
                    messagebox.showinfo('DESCANSO MEDICO', 'Registra correctamente el descanso medico !')
                else:

                    diferencia = relativedelta( datetime.strptime(fechaFinal, '%d/%m/%Y'), 
                                                datetime.strptime(fechaInicial, '%d/%m/%Y'))  
                    totalDias = diferencia.days + 1

                    insert(f'''INSERT INTO DMEDICO (IDAC, FINI, FFIN, DTOT)
                                VALUES ({idTrabajador}, "{fechaInicial}", "{fechaFinal}", {totalDias})''')
                    idDMedico = select(f'SELECT ID FROM DMEDICO ORDER BY ID DESC', False)[0]

                    self.dmedico.insert('', 'end',text=idDMedico, values=(f'{fechaInicial} - {fechaFinal}', totalDias))

                    if detallesTrabajador[7]:
                        totalDMedico = int(detallesTrabajador[7]) + totalDias
                        detallesTrabajador[7] = totalDMedico
                    else:
                        detallesTrabajador[7] = totalDias

                    self.fechaDMedico1['text'] = ''
                    self.fechaDMedico2['text'] = ''

        self.TRABAJADORES.item(filaTrabajador, values=detallesTrabajador)
           
    def EliminarDetalle(self):

        filaTrabajador = self.TRABAJADORES.focus()
        detallesTrabajador = self.TRABAJADORES.item(filaTrabajador)['values']
                
        if self.apoyo.selection():
            fila = self.apoyo.focus()
            id = int(self.apoyo.item(fila)['text'])
            delete(F'DELETE FROM APOYO WHERE ID = {id}', False)
            self.apoyo.delete(fila)

            if len(self.apoyo.get_children()) >= 1:
                detallesTrabajador[2] = int(detallesTrabajador[2]) - 1
            else:
               detallesTrabajador[2] = ''            
  
        elif self.falta.selection():
            fila = self.falta.focus()
            id = int(self.falta.item(fila)['text'])
            delete(F'DELETE FROM FALTA WHERE ID = {id}', False)
            self.falta.delete(fila)

            if len(self.falta.get_children()) >= 1:
                detallesTrabajador[3] = int(detallesTrabajador[3]) - 1
            else:
               detallesTrabajador[3] = ''       

        elif self.feriado.selection():
            fila = self.feriado.focus()
            id = int(self.feriado.item(fila)['text'])
            delete(F'DELETE FROM FERIADO WHERE ID = {id}', False)
            self.feriado.delete(fila)

            if len(self.feriado.get_children()) >= 1:
                detallesTrabajador[4] = int(detallesTrabajador[4]) - 1
            else:
               detallesTrabajador[4] = ''   

        elif self.adelanto.selection():
            
            fila = self.adelanto.focus()
            id = int(self.adelanto.item(fila)['text'])
            delete(F'DELETE FROM ADELANTO WHERE ID = {id}', False)

            monto = float(self.adelanto.item(fila)['values'][1])          
            
            self.adelanto.delete(fila)

            if len(self.adelanto.get_children()) >= 1:
                saldo = float(detallesTrabajador[10]) - monto
                detallesTrabajador[10] = f'{saldo:.2f}'
            else:
               detallesTrabajador[10] = ''
          
        elif self.porFuera.selection():
            fila = self.porFuera.focus()
            id = int(self.porFuera.item(fila)['text'])
            delete(F'DELETE FROM XFUERA WHERE ID = {id}', False)

            monto = float(self.porFuera.item(fila)['values'][1])          
            
            self.porFuera.delete(fila)

            if len(self.porFuera.get_children()) >= 1:
                saldo = float(detallesTrabajador[11]) - monto
                detallesTrabajador[11] = f'{saldo:.2f}'
            else:
               detallesTrabajador[11] = ''    
            
        elif self.ingreso.selection():
            fila = self.ingreso.focus()
            id = int(self.ingreso.item(fila)['text'])
            delete(F'DELETE FROM INGRESO WHERE ID = {id}', False)

            monto = float(self.ingreso.item(fila)['values'][1])          
            
            self.ingreso.delete(fila)

            if len(self.ingreso.get_children()) >= 1:
                saldo = float(detallesTrabajador[5]) - monto
                detallesTrabajador[5] = f'{saldo:.2f}'
            else:
               detallesTrabajador[5] = ''   

        elif self.descuento.selection():
            fila = self.descuento.focus()
            id = int(self.descuento.item(fila)['text'])
            delete(F'DELETE FROM DESCUENTO WHERE ID = {id}', False)

            monto = float(self.descuento.item(fila)['values'][1])          
            
            self.descuento.delete(fila)

            if len(self.descuento.get_children()) >= 1:
                saldo = float(detallesTrabajador[6]) - monto
                detallesTrabajador[6] = f'{saldo:.2f}'
            else:
               detallesTrabajador[6] = ''   

        elif self.vacaciones.selection():
            fila = self.vacaciones.focus()
            id = int(self.vacaciones.item(fila)['text'])
            delete(F'DELETE FROM VACACIONES WHERE ID = {id}', False)

            dias = int(self.vacaciones.item(fila)['values'][1])          
            
            self.vacaciones.delete(fila)

            if len(self.vacaciones.get_children()) >= 1:
                saldo = int(detallesTrabajador[8]) - dias
                detallesTrabajador[8] = saldo
            else:
               detallesTrabajador[8] = ''   

        elif self.cvacaciones.selection():
            fila = self.cvacaciones.focus()
            id = int(self.cvacaciones.item(fila)['text'])
            delete(F'DELETE FROM CVACACIONES WHERE ID = {id}', False)

            dias = int(self.cvacaciones.item(fila)['values'][1])          
            
            self.cvacaciones.delete(fila)

            if len(self.cvacaciones.get_children()) >= 1:
                saldo = int(detallesTrabajador[9]) - dias
                detallesTrabajador[9] = saldo
            else:
               detallesTrabajador[9] = ''   
       
        elif self.dmedico.selection():
            fila = self.dmedico.focus()
            id = int(self.dmedico.item(fila)['text'])
            delete(F'DELETE FROM DMEDICO WHERE ID = {id}', False)

            dias = int(self.dmedico.item(fila)['values'][1])          
            
            self.dmedico.delete(fila)

            if len(self.dmedico.get_children()) >= 1:
                saldo = int(detallesTrabajador[7]) - dias
                detallesTrabajador[7] = saldo
            else:
               detallesTrabajador[7] = ''   
        
        self.TRABAJADORES.item(filaTrabajador, values=detallesTrabajador)        

    def CompararFechas(self, fechaInicial: str, fechaFinal: str):
        
        inicio = datetime.strptime(fechaInicial, '%d/%m/%Y')       
        fin = datetime.strptime(fechaFinal, '%d/%m/%Y')   

        if inicio <= fin: 
            return True
        else:
            return False