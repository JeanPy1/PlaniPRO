from tkinter import Button, Frame, Label, PhotoImage, Scrollbar, Tk
from tkinter.ttk import Treeview, Style
from scripts import select, PlanillaMes, CompararFechas

from Menu1 import Menu1
from Menu2 import Menu2

class App(Tk):

    def __init__(self):
        super(App, self).__init__()

        # Creamos la ventana principal
        self.title('PlaniPRO')
        self.geometry('1000x600+-8+0')
        self.resizable(0,0)
        self.iconbitmap('./img/ico.ico')

        # Modificamos estilo de los diferentes widgets
        self.option_add('*Font', ('Segoe UI Semibold', '10'))
        self.option_add('*Button*Font', ('Segoe UI Semibold', '8'))
        self.option_add('*Button*BorderWidth', 0)
        self.option_add('*Button*Cursor', 'hand2')
        self.option_add('*Button*TakeFocus', False)
        self.option_add('*Button*Background', '#FFFFFF')
        self.option_add('*Entry*relief', 'flat')
        self.option_add('*Treeview*SelectMode', 'browse')
        self.option_add('*Treeview*Show', 'headings')
        self.option_add('*Treeview*padding', 2)
        self.option_add('*Treeview*Cursor', 'hand2')
        self.option_add('*Treeview*TakeFocus', False)
        self.option_add('*Label*Foreground', '#5B5857')
        self.option_add('*Label*Background', '#FFFFFF')
        self.option_add('*Label*Anchor', 'nw')

        # Modificados estilo de los treeview
        Style().configure('Treeview', font=('Segoe UI Semibold', 10))

        # Cargamos las imagenes de los botones
        img1 = PhotoImage(file='./img/menu1.png')
        img2 = PhotoImage(file='./img/menu2.png')
        img3 = PhotoImage(file='./img/menu3.png')
        img4 = PhotoImage(file='./img/menu4.png')
        img5 = PhotoImage(file='./img/menu5.png')
        img6 = PhotoImage(file='./img/menu6.png')

        # Creamos los botones del menu
        Button(self, bg='#F0F0F0', image=img1, command=self.Menu1).place(       width=100, height=100)
        Button(self, bg='#F0F0F0', image=img2, command=self.Menu2).place(y=100, width=100, height=100)
        Button(self, bg='#F0F0F0', image=img3, command=self.Menu3).place(y=200, width=100, height=100)
        Button(self, bg='#F0F0F0', image=img4, command=self.Menu4).place(y=300, width=100, height=100)
        Button(self, bg='#F0F0F0', image=img5, command=self.Menu5).place(y=400, width=100, height=100)
        Button(self, bg='#F0F0F0', image=img6, command=self.Menu6).place(y=500, width=100, height=100)
     

        # Corremos programa
        self.mainloop()
    
    def Menu1(self):        
        Menu1(self)

    def Menu2(self):      
        Menu2(self)
        
    def Menu3(self):
        
        # Creamos los elementos del menu 1      
        menu = Frame(self)                     
      
        self.tre3 = Treeview(menu, show='headings', columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', 
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

        scroll = Scrollbar(menu, orient='vertical', command=self.tre3.yview)
        scrol2 = Scrollbar(menu, orient='horizontal', command=self.tre3.xview)
        self.tre3.configure(yscrollcommand=scroll.set, xscrollcommand=scrol2.set)
     
        # Posicionamiento de los elementos         
        scroll.place(x=851, y=20, height=556)
        scrol2.place(x=20, y=560, width=830)
        self.tre3.place(x=20, y=20, height=540, width=830)
        
        Button(menu, text='GENERAR').place(x=890, y=20, width=90, height=30)
        Button(menu, text='MODIFICAR').place(x=890, y=55, width=90, height=30)
        Button(menu, text='REPORTE').place(x=890, y=90, width=90, height=30)
        Button(menu, text='SALIR', command=lambda:menu.destroy(), bg='#DF2F2F').place(x=890, y=125, width=90, height=30)

        # Cargamos datos al treeview
        self.CargarPlanilla()

        # Posicionamos la ventana principal
        menu.place(width=1000, height=600)
        
    def CargarPlanilla(self):
        
        mes = '01/07/2022'
        diasDelMes = PlanillaMes(mes)        

        if diasDelMes == 0:
            return

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

            if totalIngresos:
                totalIngresos = float(totalIngresos)
            else:
                totalIngresos = 0

            if totalDescuentos:
                totalDescuentos = float(totalDescuentos)
            else:
                totalDescuentos = 0

            if diasVacaciones:
                diasVacaciones = int(diasVacaciones)
            else:
                diasVacaciones = 0

            if diasCompraVacaciones:
                diasCompraVacaciones = int(diasCompraVacaciones)
            else:
                diasCompraVacaciones = 0
            
            if diasDescansoMedico:
                diasDescansoMedico = int(diasDescansoMedico)
            else:
                diasDescansoMedico = 0


            if CompararFechas(fechaIngreso, mes):
                diasLaborados = diasDelMes - diasFaltas - diasVacaciones - diasDescansoMedico
            else:
                diasLaborados = diasDelMes - (int(fechaIngreso[:2]) + 1) - diasFaltas - diasVacaciones - diasDescansoMedico

            DiasComputables = diasLaborados + diasVacaciones + diasDescansoMedico
            diasNoComputables = diasDelMes - DiasComputables

            if DiasComputables > (diasDelMes / 2):
                planillaBruta = sueldoPlanilla - (sueldoPlanilla / 30 * diasNoComputables) #+ asignacionFamiliar                
            else:                
                planillaBruta = sueldoPlanilla / 30 * DiasComputables #+ asignacionFamiliar

            if diasLaborados > (diasDelMes / 2):
                movilidadBruta = sueldoMovilidad - (sueldoMovilidad / 30 * diasNoComputables)
            else:
                movilidadBruta = sueldoMovilidad / 30 * diasLaborados

            if diasVacaciones > 0:
                if diasVacaciones >= diasDelMes:
                    totalVacaciones = planillaBruta              
                else:                    
                    if diasVacaciones > 15:                        
                        totalVacaciones = (sueldoPlanilla + asignacionFamiliar) - ((sueldoPlanilla + asignacionFamiliar) / 30 * (diasDelMes - diasVacaciones))
                    else:
                        totalVacaciones = (sueldoPlanilla + asignacionFamiliar) / 30 * diasVacaciones  
            else:
                  totalVacaciones = 0

            if diasDescansoMedico > 0:
                if diasDescansoMedico >= diasDelMes:
                    totalDescansoMedico = planillaBruta            
                else:
                    if diasDescansoMedico > 15:                        
                        totalDescansoMedico = (sueldoPlanilla + asignacionFamiliar) - ((sueldoPlanilla + asignacionFamiliar) / 30 * (diasDelMes - diasDescansoMedico))
                    else:
                        totalDescansoMedico = (sueldoPlanilla + asignacionFamiliar) / 30 * diasDescansoMedico
            else:
                  totalDescansoMedico = 0
                      
            if diasLaborados > 0:
                planillaBruta = planillaBruta - totalVacaciones - totalDescansoMedico
            else:
                planillaBruta = 0

            totalApoyos = (totalSueldo / 30) * diasApoyos
            totalFeriados = sueldoPlanilla / 30 * diasFeriados * 2
            totalCompraVacaciones = (sueldoPlanilla + asignacionFamiliar) / 30 * diasCompraVacaciones
            totalPlanillaBruta = planillaBruta + totalVacaciones + totalCompraVacaciones + totalDescansoMedico + totalFeriados

            totalOnp = 0
            totalComision = 0
            totalPrima = 0
            totalAporte = 0

            if entidadAportacion == 'ONP':
                totalOnp = totalPlanillaBruta * 0.13
            elif entidadAportacion == 'HABITAT':
                if comisionAportacion == 'FLUJO':
                    totalComision = totalPlanillaBruta * 0.027
                elif comisionAportacion == 'MIXTA':
                    totalComision = totalPlanillaBruta * 0.027             
                totalPrima = totalPlanillaBruta * 0.027
                totalAporte = totalPlanillaBruta * 0.027
            elif entidadAportacion == 'INTEGRA':
                if comisionAportacion == 'FLUJO':
                    totalComision = totalPlanillaBruta * 0.027
                elif comisionAportacion == 'MIXTA':
                    totalComision = totalPlanillaBruta * 0.027                 
                totalPrima = totalPlanillaBruta * 0.027
                totalAporte = totalPlanillaBruta * 0.027
            elif entidadAportacion == 'PRIMA':
                if comisionAportacion == 'FLUJO':
                    totalComision = totalPlanillaBruta * 0.027
                elif comisionAportacion == 'MIXTA':
                    totalComision = totalPlanillaBruta * 0.027             
                totalPrima = totalPlanillaBruta * 0.027
                totalAporte = totalPlanillaBruta * 0.027
            elif entidadAportacion == 'PROFUTURO':
                if comisionAportacion == 'FLUJO':
                    totalComision = totalPlanillaBruta * 0.027
                elif comisionAportacion == 'MIXTA':
                    totalComision = totalPlanillaBruta * 0.027             
                totalPrima = totalPlanillaBruta * 0.027
                totalAporte = totalPlanillaBruta * 0.027

            if totalPlanillaBruta > 1025:
                totalEssalud = totalPlanillaBruta * 0.09
            else:
                totalEssalud = 1025 * 0.09


            self.tre3.insert('', END, text=id, values=(index, nombreCompleto, sueldoPlanilla, asignacionFamiliar, sueldoMovilidad,
                                                    diasLaborados, diasFaltas, round(planillaBruta, 2), round(movilidadBruta, 2),
                                                    diasVacaciones, round(totalVacaciones, 2), diasCompraVacaciones, round(totalCompraVacaciones, 2), 
                                                    diasDescansoMedico, round(totalDescansoMedico, 2), diasFeriados, round(totalFeriados, 2),
                                                    round(totalPlanillaBruta, 2), round(totalOnp, 2), round(totalComision, 2), round(totalPrima, 2),
                                                    round(totalAporte, 2), '', round(totalDescuentos, 2), round(totalApoyos, 2), round(totalIngresos, 2),
                                                    '', '', '', round(totalEssalud, 2)))
        
        self.tre3.insert('', END, values=('100', 'OROPEZA INCA JEANCARLOS ALBERTO', '1,900.00', '102.50', '350.00',
                                                    '30', '10', '1,900.00', '350.00', '30', '1,900.00', '30', '1,900.00', 
                                                    '30', '1,900.00','2', '250.00',
                                                    '1,900.00', '320.00', '100.00', '100.00',
                                                    '100.00', '100.00', '500.00', '600.00', '200.00',
                                                    '', '', '', '125.00'))

    def Menu4(self):
            
            # Creamos los elementos del menu 1      
            menu = Frame(self)

            Button(menu, text='SALIR'    , bg='#DF2F2F', command=lambda:menu.destroy()).place(x=890, y=125, width=90, height=30)

            # Posicionamos la ventana principal
            menu.place(width=1000, height=600)

    def Menu5(self):
            
        # Creamos los elementos del menu 1      
        menu = Frame(self)

        Button(menu, text='SALIR'    , bg='#DF2F2F', command=lambda:menu.destroy()).place(x=890, y=125, width=90, height=30)

        # Posicionamos la ventana principal
        menu.place(width=1000, height=600)

    def Menu6(self):
        
        # Creamos los elementos del menu 1      
        menu = Frame(self)
        
        Label(menu, anchor='center', bg='#DDDDDD', text='Entidad\nAFP'                ).place(x= 20, y=20, width=100, height=48)
        Label(menu, anchor='center', bg='#DDDDDD', text='Comision\nFlujo        Mixta').place(x=121, y=20, width=121, height=48)       
        Label(menu, anchor='center', bg='#DDDDDD', text='Prima\nSeguro'               ).place(x=243, y=20, width= 60, height=48)        
        Label(menu, anchor='center', bg='#DDDDDD', text='Aporte\nMensual'             ).place(x=304, y=20, width= 60, height=48)        
        Label(menu, anchor='center', bg='#DDDDDD', text='Sueldo\nMaximo'              ).place(x=365, y=20, width= 60, height=48)      
        
        Label(menu, text=' Habitat'             ).place(x= 20, y= 69, width=100, height=24)
        Label(menu, anchor='e', text='1.47%'    ).place(x=121, y= 69, width= 60, height=24)
        Label(menu, anchor='e', text='0.23%'    ).place(x=182, y= 69, width= 60, height=24)
        
        Label(menu, text=' Integra'             ).place(x= 20, y= 94, width=100, height=24)
        Label(menu, anchor='e', text='1.55%'    ).place(x=121, y= 94, width= 60, height=24)
        Label(menu, anchor='e', text='0.00%'    ).place(x=182, y= 94, width= 60, height=24)
        
        Label(menu, text=' Prima'               ).place(x= 20, y=119, width=100, height=24)
        Label(menu, anchor='e', text='1.60%'    ).place(x=121, y=119, width= 60, height=24)
        Label(menu, anchor='e', text='0.18%'    ).place(x=182, y=119, width= 60, height=24)
        
        Label(menu, text=' Profuturo'           ).place(x= 20, y=144, width=100, height=24)
        Label(menu, anchor='e', text='1.69%'    ).place(x=121, y=144, width= 60, height=24)
        Label(menu, anchor='e', text='0.28%'    ).place(x=182, y=144, width= 60, height=24)

        Label(menu, anchor='e', text='1.74%'    ).place(x=243, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='10.00%'   ).place(x=304, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='11,002.84').place(x=365, y= 69, width= 60, height=99)

        Label(menu, anchor='center', bg='#DDDDDD', text='Fondo\nOnp'       ).place(x=445, y=20, width= 60, height=48)    
        Label(menu, anchor='center', bg='#DDDDDD', text='Essalud'          ).place(x=506, y=20, width= 60, height=48)    
        Label(menu, anchor='center', bg='#DDDDDD', text='Sueldo\nMinimo'   ).place(x=567, y=20, width= 60, height=48) 
        Label(menu, anchor='center', bg='#DDDDDD', text='Asigna.\nFamiliar').place(x=628, y=20, width= 60, height=48)         
        
        Label(menu, anchor='e', text='13.00%'   ).place(x=445, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='9.00%'    ).place(x=506, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='1,025.00' ).place(x=567, y= 69, width= 60, height=99)
        Label(menu, anchor='e', text='10.00%'   ).place(x=628, y= 69, width= 60, height=99)
        

        Button(menu, text='MODIFICAR').place(x=890, y=20, width=90, height=30)
        Button(menu, text='SALIR'    , bg='#DF2F2F', command=lambda:menu.destroy()).place(x=890, y=125, width=90, height=30)

        # Posicionamos la ventana principal
        menu.place(width=1000, height=600)



if __name__ == '__main__': aplicacion = App()      