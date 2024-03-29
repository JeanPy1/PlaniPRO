from tkinter import Button, Frame, Scrollbar
from tkinter.ttk import Treeview
from datetime import date
from scripts.sql import Select_Personal, Select_Detalle


class Menu3(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)

        columna = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', 
                   '#11', '#12', '#13', '#14', '#15', '#16', '#17', '#18', '#19', '#20',
                   '#21', '#22', '#23', '#24', '#25', '#26', '#27', '#28', '#29', '#30',
                   '#31', '#32', '#33', '#34', '#35')
        ancho = (26, 260, 70, 50, 50, 30, 30, 70, 50, 50, 30, 60, 30, 60, 30, 60,
                 30, 60, 70, 50, 50, 50, 50, 50, 50, 50, 50, 70, 50, 50, 50, 50, 50,
                 50, 50)
        titulo = ('N°', 'APELLIDOS Y NOMBRE', 'PLANILLA', 'A. F.', 'MOV.', 'DL', 'DNL',
                  'PLANILLA', 'A. F.', 'MOV.', 'V', 'MONTO', 'CV', 'MONTO', 'DM', 'MONTO',
                  'F', 'MONTO', 'R. BRUTA', 'ONP', 'COMI.', 'PRIM.', 'APOR.', 'REN. 5',
                  'DSCTO', 'INGSO', 'APOYO', 'R. NETA', 'MOV.', 'XFUERA', 'ESSA.', 'ONP',
                  'COM.', 'PRI.', 'APO.')
        
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
          
        datos = Select_Personal()
        
        for index, dato in enumerate(datos, 1):            
            
            idTrabajador = dato[0]
            nombre = f'{dato[2]} {dato[3]} {dato[4]}'
            ingreso = dato[6]
            planilla = float(dato[7])
            asignacion = float(dato[8])
            movilidad = float(dato[9])            
            aportacion = dato[10]
            comision = dato[11]
            retiro = dato[21]            
            
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

            diaApoyo = Select_Detalle("apoyo", idTrabajador)
            diaFalta = Select_Detalle("falta", idTrabajador)
            diaFeriado = Select_Detalle("feriado", idTrabajador)
            diaVacaciones = Select_Detalle("vacaciones", idTrabajador)
            diaCVacaciones = Select_Detalle("compravacaciones", idTrabajador)
            diaDMedico = Select_Detalle("descansomedico", idTrabajador)
            ingresos = Select_Detalle("ingreso", idTrabajador)
            descuentos = Select_Detalle("descuento", idTrabajador)
            adelanto = Select_Detalle("adelanto", idTrabajador)
            porfuera = Select_Detalle("porfuera", idTrabajador)
            
            print(diaApoyo)
            
            continue
            if not diaApoyo: diaApoyo = 0
            if not diaFalta: diaFalta = 0
            if not diaFeriado: diaFeriado = 0
            if diaVacaciones is None: diaVacaciones = 0
            if diaCVacaciones is None: diaCVacaciones = 0
            if diaDMedico is None: diaDMedico = 0            
            
            # Empieza Calculos de remuneracion            
            diasRemunerados = diasComputables - diaFalta
            diasNoRemunerados = totalDiasMes - diasRemunerados
            diasLaborados = diasRemunerados - diaVacaciones - diaDMedico
            diasNoLaborados = totalDiasMes - diasLaborados

            sueldoComputable = round(planilla / 30 * diasRemunerados, 2)
            movilidadComputable = round(movilidad / 30 * diasLaborados, 2)
            asignacionComputable = asignacion
            if diasRemunerados > totalDiasMes / 2:
                sueldoComputable = round(planilla - (planilla / 30 * diasNoRemunerados), 2)
            if diasLaborados > totalDiasMes / 2:
                movilidadComputable = round(movilidad - (movilidad / 30 * diasNoLaborados), 2)

            vacaciones = 0
            if diaVacaciones:
                if diaVacaciones == totalDiasMes:
                    vacaciones = planilla + asignacion
                    asignacionComputable = 0
                else:
                    vacaciones = round(planilla / 30 * diaVacaciones, 2)
                    if diaVacaciones > totalDiasMes / 2:
                        vacaciones = round(planilla - (planilla / 30 * (totalDiasMes - diaVacaciones)), 2)               

            dMedico = 0
            if diaDMedico:
                if diaDMedico == totalDiasMes:
                    dMedico = planilla
                else:
                    dMedico = round(planilla / 30 * diaDMedico, 2)
                    if diaDMedico > totalDiasMes / 2:
                        dMedico = round(planilla - (planilla / 30 * (totalDiasMes - diaDMedico)), 2)

            cVacaciones = 0
            if diaCVacaciones:
                cVacaciones = round((planilla + asignacion) / 30 * diaCVacaciones, 2)

            feriado = 0
            if diaFeriado:
                feriado = round((planilla) / 30 * (diaFeriado * 2), 2)

            sueldoComputable = round(sueldoComputable - vacaciones - dMedico, 2)  
            remuneracionBruta = round(sueldoComputable + asignacion + vacaciones + dMedico + feriado, 2)  
            if sueldoComputable < 0:
                sueldoComputable = 0

            #comisiones = select(f""" SELECT * FROM OPCIONES """, False)
           
            #habitatF = comisiones[0]
            #habitatM = comisiones[1]
            #integraF = comisiones[2]
            #integraM = comisiones[3]
            #primaF = comisiones[4]
            #primaM = comisiones[5]
            #profuturoF = comisiones[6]
            #profuturoM = comisiones[7]
            #primaS = comisiones[8]
            #aporteO = comisiones[9]
            #remMax = comisiones[10]
            #onpA = comisiones[11]

            #onp = 0
            #afpComision = 0
            #afpPrima = 0
            #afpAporte = 0
            #match aportacion:
            #    case "ONP":
            #        onp = remuneracionBruta * onpA
            #    case "HABITAT":                    
            #        afpComision = remuneracionBruta * habitatM
            #        if comision == "FLUJO":
            #            afpComision = remuneracionBruta * habitatF
            #        afpPrima = remuneracionBruta * primaS
            #        if planilla + movilidad > remMax:
            #            afpPrima = remMax * primaS
            #        afpAporte = remuneracionBruta * aporteO
            #    case "INTEGRA":
            #        afpComision = remuneracionBruta * integraM
            #        if comision == "FLUJO":
            #            afpComision = remuneracionBruta * integraF
            #        afpPrima = remuneracionBruta * primaS
            #        if planilla + movilidad > remMax:
            #            afpPrima = remMax * primaS
            #        afpAporte = remuneracionBruta * aporteO
            #    case "PRIMA":
            #        afpComision = remuneracionBruta * primaM
            #        if comision == "FLUJO":
            #            afpComision = remuneracionBruta * primaF
            #        afpPrima = remuneracionBruta * primaS
            #        if planilla + movilidad > remMax:
            #            afpPrima = remMax * primaS
            #        afpAporte = remuneracionBruta * aporteO
            #    case "PROFUTURO":
            #        afpComision = remuneracionBruta * profuturoM
            #        if comision == "FLUJO":
            #            afpComision = remuneracionBruta * profuturoF
            #        afpPrima = remuneracionBruta * primaS
            #        if planilla + movilidad > remMax:
            #            afpPrima = remMax * primaS
            #        afpAporte = remuneracionBruta * aporteO

            # Redondear a 2 decimales
            planilla = f"{planilla:.2f}"

            if not asignacion: asignacion = "" 
            else: asignacion = f"{asignacion:.2f}"
            
            if not asignacionComputable: asignacionComputable = "" 
            else: asignacionComputable = f"{asignacionComputable:.2f}"

            if not movilidad: movilidad = "" 
            else: movilidad = f"{movilidad:.2f}"

            if not diasLaborados: diasLaborados = ""
            if not diaFalta: diaFalta = ""
            if not diaVacaciones: diaVacaciones = ""
            if not diaCVacaciones: diaCVacaciones = ""
            if not diaDMedico: diaDMedico = ""
            if not diaFeriado: diaFeriado = ""

            if not sueldoComputable: sueldoComputable = ""
            else: sueldoComputable = f"{sueldoComputable:.2f}"

            if not movilidadComputable: movilidadComputable = ""
            else: movilidadComputable = f"{movilidadComputable:.2f}"

            if not vacaciones: vacaciones = ""
            else: vacaciones = f"{vacaciones:.2f}"

            if not cVacaciones: cVacaciones = ""
            else: cVacaciones = f"{cVacaciones:.2f}"

            if not dMedico: dMedico = ""
            else: dMedico = f"{dMedico:.2f}"

            if not feriado: feriado = ""
            else: feriado = f"{feriado:.2f}"

            remuneracionBruta = f"{remuneracionBruta:.2f}"

            if not onp: onp = "" 
            else: onp = f"{onp:.2f}"

            if not afpComision: afpComision = "" 
            else: afpComision = f"{afpComision:.2f}"

            if not afpPrima: afpPrima = "" 
            else: afpPrima = f"{afpPrima:.2f}"

            if not afpAporte: afpAporte = "" 
            else: afpAporte = f"{afpAporte:.2f}"

            detalles = (index, nombre, planilla, asignacion, movilidad, diasLaborados, diaFalta, 
            sueldoComputable, asignacionComputable, movilidadComputable, diaVacaciones, vacaciones, diaCVacaciones,
            cVacaciones, diaDMedico, dMedico, diaFeriado, feriado, remuneracionBruta, onp, afpComision, afpPrima, afpAporte)
            
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