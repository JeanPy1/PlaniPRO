from tkinter import Button, Frame, Scrollbar
from tkinter.ttk import Treeview
from datetime import date
from scripts.sql import select

class Menu3(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)

        columna = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', 
                   '#11', '#12', '#13', '#14', '#15', '#16', '#17', '#18', '#19', '#20',
                   '#21', '#22', '#23', '#24', '#25', '#26', '#27', '#28', '#29', '#30')
        ancho = (26, 260, 70, 50, 50, 30, 30, 70, 50, 30, 60, 30, 60, 30, 60,
                 30, 60, 70, 50, 50, 50, 50, 50, 50, 50, 50, 70, 50, 50, 50)
        titulo = ('N°', 'APELLIDOS Y NOMBRE', 'PLANILLA', 'A. F.', 'MOV.', 'DL', 'DNL',
                  'PLANILLA', 'MOV.', 'V', 'MONTO', 'CV', 'MONTO', 'DM', 'MONTO',
                  'F', 'MONTO', 'R. BRUTA', 'ONP', 'COMI.', 'PRIM.', 'APOR.', 'REN. 5',
                  'DSCTO', 'INGSO', 'APOYO', 'R. NETA', 'MOV.', 'XFUERA', 'ESSA.')
        
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
        Button(self, text='REPORTE').place(x=890, y=100, width=90, height=30)
        Button(self, text='SALIR', command=lambda:self.destroy(), bg='#DF2F2F').place(x=890, y=135, width=90, height=30)

        self.CargarPlanilla()
        self.place(width=1000, height=600)

    def CargarPlanilla(self):
        
        mes = 10
        año = 2022
        totalDiasMes = self.TotalDiasMes(mes, año)
        fechaInicial = date(año, mes, 1) 
        fechaFinal = date(año, mes, totalDiasMes)  
          
        datos = select(f'''SELECT ID, APAT, AMAT, NOMB, FING, SPLA, AFAM, SMOV, EAPO, TCOM, FCES
                                    FROM ACTIVO ORDER BY APAT, AMAT, NOMB ASC''', True)
        
        for index, dato in enumerate(datos, 1):
            
            idTrabajador = dato[0]
            nombre = f'{dato[1]} {dato[2]} {dato[3]}'
            ingreso = dato[4]
            planilla = float(dato[5])
            asignacion = float(dato[6])
            movilidad = float(dato[7])            
            aportacion = dato[8]
            comision = dato[9]
            retiro = dato[10]
            
            fechaIngreso = date(int(ingreso[6:10]), int(ingreso[3:5]), int(ingreso[0:2]))   
            if fechaIngreso > fechaFinal:
                continue   

            diasComputables = 0
            if retiro:
                fechaRetiro = date(int(retiro[6:10]), int(retiro[3:5]), int(retiro[0:2]))
                diasComputables = fechaRetiro.day - fechaInicial.day + 1
                if fechaIngreso > fechaInicial:
                    diasComputables = fechaRetiro.day - fechaIngreso.day + 1               
            else:                
                if fechaIngreso <= fechaInicial:
                    diasComputables = totalDiasMes
                else:
                    diasComputables = totalDiasMes - fechaIngreso.day +1

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
            
            diasRemunerados = diasComputables - diaFalta
            diasNoRemunerados = totalDiasMes - diasRemunerados
            diasLaborados = diasRemunerados - diaVacaciones - diaDMedico
            diasNoLaborados = totalDiasMes - diasLaborados

            sueldoComputable = round(planilla / 30 * diasRemunerados, 2)
            movilidadComputable = round(movilidad / 30 * diasLaborados, 2)
            if diasComputables > totalDiasMes / 2:
                sueldoComputable = round(planilla - (planilla / 30 * diasNoRemunerados), 2)
            if diasLaborados > totalDiasMes / 2:
                movilidadComputable = round(movilidad - (movilidad / 30 * diasNoLaborados), 2)

            vacaciones = 0
            if diaVacaciones:
                if diaVacaciones == totalDiasMes:
                    vacaciones = planilla + asignacion
                else:
                    vacaciones = round(planilla / 30 * diaVacaciones, 2)
                    if diaVacaciones > totalDiasMes / 2:
                        vacaciones = round(planilla - (planilla / 30 * (totalDiasMes - diaVacaciones)), 2)               

            dMedico = 0
            if diaDMedico:
                if diaDMedico == totalDiasMes:
                    dMedico = planilla + asignacion
                else:
                    dMedico = round(planilla / 30 * diaDMedico, 2)
                    if diaDMedico > totalDiasMes / 2:
                        dMedico = round(planilla - (planilla / 30 * (totalDiasMes - diaDMedico)), 2)

            cVacaciones = 0
            if diaCVacaciones:
                cVacaciones = round((planilla + asignacion) / 30 * diaCVacaciones, 2)

            feriado = 0
            if diaFeriado:
                feriado = round(planilla / 30 * (diaFeriado * 2), 2)

            sueldoComputable = round(sueldoComputable - vacaciones - dMedico, 2)  

            remuneracionBruta = round(sueldoComputable + vacaciones + dMedico, 2)  


            detalles = (index, nombre, planilla, asignacion, movilidad, diasLaborados, diaFalta, 
            sueldoComputable, movilidadComputable, diaVacaciones, vacaciones, diaCVacaciones,
            cVacaciones, diaDMedico, dMedico, diaFeriado, feriado, remuneracionBruta)
            
            self.TRABAJADORES.insert('', 'end', text=idTrabajador, values=detalles)

  
    def TotalDiasMes(self, mes: int, año: int) -> int:
        
        if mes in [4, 6, 9, 11]: 
            return 30 # Abril, junio, septiembre y noviembre tienen 30
        
        if mes == 2:
            if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0): # Febrero depende de si es o no bisiesto
                return 29 
            else:
                return 28
        else:        
            return 31 # Todos los demas 