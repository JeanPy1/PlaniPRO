from tkinter import Button, Frame, Scrollbar
from tkinter.ttk import Treeview
from scripts.sql import select
from scripts.edad import PlanillaMes, CompararFechas, TotalDias

class Menu3(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)

        columna = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', 
                   '#11', '#12', '#13', '#14', '#15', '#16', '#17', '#18', '#19', '#20',
                   '#21', '#22', '#23', '#24', '#25', '#26', '#27', '#28', '#29', '#30')
        ancho = (30, 270, 80, 70, 70, 40, 40, 80, 70, 40, 70, 40, 70, 40, 70,
                 40, 70, 80, 70, 70, 70, 70, 70, 70, 70, 70, 80, 70, 70, 70)
        titulo = ('N°', 'APELLIDOS Y NOMBRE', 'PLANILLA', 'ASIG. FAM.', 'MOVILIDA', 'D TR', 'D FA',
                  'PLANILLA', 'MOVILIDA', 'D VA', 'VACACIO.', 'D CV', 'C. VACA.', 'D DM', 'DES. MEDI.',
                  'D FE', 'FERIADO', 'REM. BRUTA', 'ONP', 'COMISION', 'PRI. SEG.', 'APORTE', 'RENTA 5',
                  'DESCUEN.', 'INGRESO', 'APOYO', 'REM. NETA', 'MOV. NETA', 'POR FUERA', 'ESSALUD')
        
        self.TRABAJADORES = Treeview(self, columns=columna)          

        for index, columna in enumerate(columna):
            self.TRABAJADORES.column(columna, width=ancho[index], minwidth=ancho[index], anchor='e')
            self.TRABAJADORES.heading(columna, text=titulo[index])        

        scroll = Scrollbar(self, orient='vertical', command=self.TRABAJADORES.yview)
        scrol2 = Scrollbar(self, orient='horizontal', command=self.TRABAJADORES.xview)
        self.TRABAJADORES.configure(yscrollcommand=scroll.set, xscrollcommand=scrol2.set)

        self.TRABAJADORES.place(x=20, y=30, height=548, width=830)
        scroll.place(x=851, y=30, height=548)
        scrol2.place(x=20, y=579, width=830)        
        
        Button(self, text='GENERAR').place(x=890, y=30, width=90, height=30)
        Button(self, text='MODIFICAR').place(x=890, y=65, width=90, height=30)
        Button(self, text='REPORTE').place(x=890, y=105, width=90, height=30)
        Button(self, text='SALIR', command=lambda:self.destroy(), bg='#DF2F2F').place(x=890, y=140, width=90, height=30)

        self.CargarPlanilla()

        self.place(width=1000, height=600)

    def CargarPlanilla(self):
        
        mes = 10
        año = 2022
        dias = PlanillaMes(mes, año)
        fechaInicial = f'01/{mes:02d}/{año}'
        fechaFinal = f'{dias}/{mes:02d}/{año}'

        datos = select(f'SELECT ID, APAT, AMAT, NOMB, FING, SPLA, AFAM, SMOV, EAPO, TCOM, FCES FROM ACTIVO', True)
        
        for index, dato in enumerate(datos, 1):
            
            idTrabajador = dato[0]
            nombre = f'{dato[1]} {dato[2]} {dato[3]}'
            ingreso = dato[4]
            planilla = float(dato[5])
            asignacion = float(dato[6])
            movilidad = float(dato[7])
            total = planilla + asignacion + movilidad
            aportacion = dato[8]
            comision = dato[9]
            retiro = dato[10]
            
            diaApoyo = select(F'SELECT COUNT(FECH) FROM APOYO WHERE IDAC = {idTrabajador}', False)[0]
            diaFalta = select(F'SELECT COUNT(FECH) FROM FALTA WHERE IDAC = {idTrabajador}', False)[0]
            diaFeriado = select(F'SELECT COUNT(FECH) FROM FERIADO WHERE IDAC = {idTrabajador}', False)[0]
            diaVacaciones = select(F'SELECT SUM(DTOT) FROM VACACIONES WHERE IDAC = {idTrabajador}', False)[0]
            diaCVacaciones = select(F'SELECT SUM(DTOT) FROM CVACACIONES WHERE IDAC = {idTrabajador}', False)[0]
            diaDMedico = select(F'SELECT SUM(DTOT) FROM DMEDICO WHERE IDAC = {idTrabajador}', False)[0]
            ingresos = select(F'SELECT SUM(MONT) FROM INGRESO WHERE IDAC = {idTrabajador}', False)[0]
            descuentos = select(F'SELECT SUM(MONT) FROM DESCUENTO WHERE IDAC = {idTrabajador}', False)[0]
            adelanto = select(F'SELECT SUM(MONT) FROM ADELANTO WHERE IDAC = {idTrabajador}', False)[0]
            porfuera = select(F'SELECT SUM(MONT) FROM XFUERA WHERE IDAC = {idTrabajador}', False)[0]

            if not diaApoyo: diaApoyo = 0
            if not diaFalta: diaFalta = 0
            if not diaFeriado: diaFeriado = 0
            if diaVacaciones is None: diaVacaciones = 0
            if diaCVacaciones is None: diaCVacaciones = 0
            if diaDMedico is None: diaDMedico = 0
                       
            diasComputables = 0

            if CompararFechas(ingreso, fechaInicial):
                if retiro:
                    diasComputables = TotalDias(fechaInicial, retiro)
                else:
                    diasComputables = dias
            else:
                if retiro:
                    diasComputables = TotalDias(ingreso, retiro)
                else:
                    diasComputables = TotalDias(ingreso, fechaFinal) 
            
            diaslaborados = diasComputables - diaFalta - diaVacaciones - diaDMedico

            diasRemunerados = diasComputables - diaFalta
            diasNoremunerados = dias - diasRemunerados

            planillaBruta = 0
            movilidadBruta = 0
            if diasRemunerados > dias / 2:
                planillaBruta = planilla - (planilla / 30 * diasNoremunerados)   
                movilidadBruta = movilidad - (movilidad / 30 * diasNoremunerados)                
            else:
                planillaBruta = planilla / 30 * diasRemunerados    
                movilidadBruta = (movilidad / 30 * diasRemunerados)   

            vacaciones = 0
            dmedico = 0
            if diasRemunerados == diaVacaciones:
                vacaciones = planillaBruta
                planillaBruta = 0
            elif diasRemunerados == diaDMedico:
                dmedico = planillaBruta
                planillaBruta = 0
            else:
                if diaVacaciones:
                    calculoVacaciones = planilla / 30 * diaVacaciones
                    if calculoVacaciones == planillaBruta:
                        calculoVacaciones = calculoVacaciones - (planilla / 30 * 1)
                    vacaciones = calculoVacaciones
                    planillaBruta = planillaBruta - vacaciones
                if diaDMedico:
                    calculoDMedico = planilla / 30 * diaDMedico
                    if calculoDMedico == planillaBruta:
                        calculoDMedico = calculoDMedico - (planilla / 30 * 1)
                    dmedico = calculoDMedico
                    planillaBruta = planillaBruta - dmedico

                print(planillaBruta)
                if planillaBruta < 0:
                    saldoPlanillabruta = planillaBruta - vacaciones
                    planillaBruta = saldoPlanillabruta / (diaslaborados + diaDMedico) * diaslaborados
                    dmedico = saldoPlanillabruta / (diaslaborados + diaDMedico) * diaDMedico

                

                

                



            detalles = (index, nombre, planilla, asignacion, movilidad, diaslaborados, diaFalta, planillaBruta, movilidadBruta,
                        diaVacaciones, vacaciones, diaCVacaciones, 'cvaca', diaDMedico, dmedico, diaFeriado, 'feria')
            self.TRABAJADORES.insert('', 'end', text=idTrabajador, values=detalles)
           