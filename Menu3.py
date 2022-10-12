from tkinter import Button, Entry, Frame, Label, Scrollbar, messagebox
from tkinter.ttk import Treeview
from scripts.sql import select, insert, delete
from scripts.edad import CompararFechas, TotalDias

class Menu3(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)
 
        self.tre3 = Treeview(self, show='headings', columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', 
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

        scroll = Scrollbar(self, orient='vertical', command=self.tre3.yview)
        scrol2 = Scrollbar(self, orient='horizontal', command=self.tre3.xview)
        self.tre3.configure(yscrollcommand=scroll.set, xscrollcommand=scrol2.set)
     
        # Posicionamiento de los elementos         
        scroll.place(x=851, y=20, height=556)
        scrol2.place(x=20, y=560, width=830)
        self.tre3.place(x=20, y=20, height=540, width=830)
        
        Button(self, text='GENERAR').place(x=890, y=20, width=90, height=30)
        Button(self, text='MODIFICAR').place(x=890, y=55, width=90, height=30)
        Button(self, text='REPORTE').place(x=890, y=90, width=90, height=30)
        Button(self, text='SALIR', command=lambda:self.destroy(), bg='#DF2F2F').place(x=890, y=125, width=90, height=30)

        # Cargamos datos al treeview
        self.CargarPlanilla()

        # Posicionamos la ventana principal
        self.place(width=1000, height=600)

    def CargarPlanilla(self):
        
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
