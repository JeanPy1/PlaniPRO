from tkinter import Button, Entry, Frame, Label
from scripts.sql import select, update

class Menu6(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)        

        Label(self, anchor='center', bg='#DDDDDD', text='Entidad\nAFP'                ).place(x= 20, y=20, width=100, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Comision\nFlujo        Mixta').place(x=121, y=20, width=121, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Prima\nSeguro'               ).place(x=243, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Aporte\nMensual'             ).place(x=304, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Sueldo\nMaximo'              ).place(x=365, y=20, width= 60, height=48)
        Label(self, text=' Habitat').place(x= 20, y= 69, width=100, height=24)
        self.habitatF = Label(self, anchor='e')
        self.habitatM = Label(self, anchor='e')
        Label(self, text=' Integra').place(x= 20, y= 94, width=100, height=24)
        self.integraF = Label(self, anchor='e')
        self.integraM = Label(self, anchor='e')
        Label(self, text=' Prima').place(x= 20, y=119, width=100, height=24)
        self.primaF = Label(self, anchor='e')
        self.primaM = Label(self, anchor='e')
        Label(self, text=' Profuturo').place(x= 20, y=144, width=100, height=24)
        self.profuturoF = Label(self, anchor='e')
        self.profuturoM = Label(self, anchor='e')
        self.primaS = Label(self, anchor='e')
        self.aporteO = Label(self, anchor='e')
        self.remuneracionM = Label(self, anchor='e')
        Label(self, anchor='center', bg='#DDDDDD', text='Fondo\nOnp'       ).place(x=445, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Essalud'          ).place(x=506, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Sueldo\nMinimo'   ).place(x=567, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Asigna.\nFamiliar').place(x=628, y=20, width= 60, height=48)
        self.onpA = Label(self, anchor='e')
        self.essaludA = Label(self, anchor='e')
        self.sueldoM = Label(self, anchor='e')
        self.asignacionF = Label(self, anchor='e')
        Button(self, text='MODIFICAR', command=self.Modificar).place(x=890, y=20, width=90, height=30)
        Button(self, text='SALIR', bg='#DF2F2F', command=lambda:self.destroy()).place(x=890, y=125, width=90, height=30)

        self.habitatF.place(x=121, y= 69, width= 60, height=24)
        self.habitatM.place(x=182, y= 69, width= 60, height=24)
        self.integraF.place(x=121, y= 94, width= 60, height=24)
        self.integraM.place(x=182, y= 94, width= 60, height=24)
        self.primaF.place(x=121, y=119, width= 60, height=24)
        self.primaM.place(x=182, y=119, width= 60, height=24)
        self.profuturoF.place(x=121, y=144, width= 60, height=24)
        self.profuturoM.place(x=182, y=144, width= 60, height=24)
        self.primaS.place(x=243, y= 69, width= 60, height=99)
        self.aporteO.place(x=304, y= 69, width= 60, height=99)
        self.remuneracionM.place(x=365, y= 69, width= 60, height=99)
        self.onpA.place(x=445, y= 69, width= 60, height=99)
        self.essaludA.place(x=506, y= 69, width= 60, height=99)
        self.sueldoM.place(x=567, y= 69, width= 60, height=99)
        self.asignacionF.place(x=628, y= 69, width= 60, height=99)

        self.CargarDatos()       
        self.place(width=1000, height=600)

    def CargarDatos(self):
        opciones = select(f'SELECT * FROM OPCIONES', False)  
        habitatF = round(opciones[0] * 100, 2)
        habitatM = round(opciones[1] * 100, 2)
        integraF = round(opciones[2] * 100, 2)
        integraM = round(opciones[3] * 100, 2)
        primaF = round(opciones[4] * 100, 2)
        primaM = round(opciones[5] * 100, 2)
        profuturoF = round(opciones[6] * 100, 2)
        profuturoM = round(opciones[7] * 100, 2)
        primaS = round(opciones[8] * 100, 2)
        aporteO = round(opciones[9] * 100, 2)
        remuneracionM = round(opciones[10], 2)
        onpA = round(opciones[11] * 100, 2)
        essaludA = round(opciones[12] * 100, 2)
        sueldoM = round(opciones[13], 2)
        asignacionF = round(opciones[14] * 100, 2)

          
        self.habitatF['text'] = f'{habitatF:.2f}%'
        self.habitatM['text'] = f'{habitatM:.2f}%'
        self.integraF['text'] = f'{integraF:.2f}%'
        self.integraM['text'] = f'{integraM:.2f}%'
        self.primaF['text'] = f'{primaF:.2f}%'
        self.primaM['text'] = f'{primaM:.2f}%'
        self.profuturoF['text'] = f'{profuturoF:.2f}%'
        self.profuturoM['text'] = f'{profuturoM:.2f}%'
        self.primaS['text'] = f'{primaS:.2f}%'
        self.aporteO['text'] = f'{aporteO:.2f}%'
        self.remuneracionM['text'] = f'{remuneracionM:.2f}'
        self.onpA['text'] = f'{onpA:.2f}%'
        self.essaludA['text'] = f'{essaludA:.2f}%'
        self.sueldoM['text'] = f'{sueldoM:.2f}'
        self.asignacionF['text'] = f'{asignacionF:.2f}%'
    
    def Modificar(self):

        contenedor = Frame(self)

        Label(contenedor, anchor='center', bg='#DDDDDD', text='Entidad\nAFP'                ).place(x= 20, y=20, width=100, height=48)
        Label(contenedor, anchor='center', bg='#DDDDDD', text='Comision\nFlujo        Mixta').place(x=121, y=20, width=121, height=48)
        Label(contenedor, anchor='center', bg='#DDDDDD', text='Prima\nSeguro'               ).place(x=243, y=20, width= 60, height=48)
        Label(contenedor, anchor='center', bg='#DDDDDD', text='Aporte\nMensual'             ).place(x=304, y=20, width= 60, height=48)
        Label(contenedor, anchor='center', bg='#DDDDDD', text='Sueldo\nMaximo'              ).place(x=365, y=20, width= 60, height=48)
        Label(contenedor, text=' Habitat').place(x= 20, y= 69, width=100, height=24)
        self.habitatFlujo = Entry(contenedor, justify='right')
        self.habitatMixta = Entry(contenedor, justify='right')
        Label(contenedor, text=' Integra').place(x= 20, y= 94, width=100, height=24)
        self.integraFlujo = Entry(contenedor, justify='right')
        self.integraMixta = Entry(contenedor, justify='right')
        Label(contenedor, text=' Prima').place(x= 20, y=119, width=100, height=24)
        self.primaFlujo = Entry(contenedor, justify='right')
        self.primaMixta = Entry(contenedor, justify='right')
        Label(contenedor, text=' Profuturo').place(x= 20, y=144, width=100, height=24)
        self.profuturoFlujo = Entry(contenedor, justify='right')
        self.profuturoMixta = Entry(contenedor, justify='right')
        self.primaSeguro = Entry(contenedor, justify='right')
        self.aporte = Entry(contenedor, justify='right')
        self.remuneracionMaxima = Entry(contenedor, justify='right')
        Label(contenedor, anchor='center', bg='#DDDDDD', text='Fondo\nOnp'       ).place(x=445, y=20, width= 60, height=48)
        Label(contenedor, anchor='center', bg='#DDDDDD', text='Essalud'          ).place(x=506, y=20, width= 60, height=48)
        Label(contenedor, anchor='center', bg='#DDDDDD', text='Sueldo\nMinimo'   ).place(x=567, y=20, width= 60, height=48)
        Label(contenedor, anchor='center', bg='#DDDDDD', text='Asigna.\nFamiliar').place(x=628, y=20, width= 60, height=48)
        self.onp = Entry(contenedor, justify='right')
        self.essalud = Entry(contenedor, justify='right')
        self.sueldoMinimo = Entry(contenedor, justify='right')
        self.asignacionFamiliar = Entry(contenedor, justify='right')
        Button(contenedor, text='GRABAR', command=self.Grabar).place(x=890, y=20, width=90, height=30)
        Button(contenedor, text='SALIR'    , bg='#DF2F2F', command=lambda:contenedor.destroy()).place(x=890, y=125, width=90, height=30)
       
        self.habitatFlujo.place(x=121, y= 69, width= 60, height=24)
        self.habitatMixta.place(x=182, y= 69, width= 60, height=24)
        self.integraFlujo.place(x=121, y= 94, width= 60, height=24)
        self.integraMixta.place(x=182, y= 94, width= 60, height=24)
        self.primaFlujo.place(x=121, y=119, width= 60, height=24)
        self.primaMixta.place(x=182, y=119, width= 60, height=24)
        self.profuturoFlujo.place(x=121, y=144, width= 60, height=24)
        self.profuturoMixta.place(x=182, y=144, width= 60, height=24)
        self.primaSeguro.place(x=243, y= 69, width= 60, height=99)
        self.aporte.place(x=304, y= 69, width= 60, height=99)
        self.remuneracionMaxima.place(x=365, y= 69, width= 60, height=99)
        self.onp.place(x=445, y= 69, width= 60, height=99)
        self.essalud.place(x=506, y= 69, width= 60, height=99)
        self.sueldoMinimo.place(x=567, y= 69, width= 60, height=99)
        self.asignacionFamiliar.place(x=628, y= 69, width= 60, height=99)


        opciones = select(f'SELECT * FROM OPCIONES', False)
        self.habitatFlujo.insert(0, round(opciones[0] * 100, 2))
        self.habitatMixta.insert(0, round(opciones[1] * 100, 2))
        self.integraFlujo.insert(0, round(opciones[2] * 100, 2))
        self.integraMixta.insert(0, round(opciones[3] * 100, 2))
        self.primaFlujo.insert(0, round(opciones[4] * 100, 2))
        self.primaMixta.insert(0, round(opciones[5] * 100, 2))
        self.profuturoFlujo.insert(0, round(opciones[6] * 100, 2))
        self.profuturoMixta.insert(0, round(opciones[7] * 100, 2))
        self.primaSeguro.insert(0, round(opciones[8] * 100, 2))
        self.aporte.insert(0, round(opciones[9] * 100, 2))
        self.remuneracionMaxima.insert(0, round(opciones[10], 2))
        self.onp.insert(0, round(opciones[11] * 100, 2))
        self.essalud.insert(0, round(opciones[12] * 100, 2))
        self.sueldoMinimo.insert(0, round(opciones[13], 2))
        self.asignacionFamiliar.insert(0, round(opciones[14] * 100, 2))        

        self.opciones = contenedor
        contenedor.place(width=1000, height=600)

    def Grabar(self):
        
        habitatFlujo = float(self.habitatFlujo.get()) / 100
        habitatMixta = float(self.habitatMixta.get()) / 100
        integraFlujo = float(self.integraFlujo.get()) / 100
        integraMixta = float(self.integraMixta.get()) / 100
        primaFlujo = float(self.primaFlujo.get()) / 100
        primaMixta = float(self.primaMixta.get()) / 100
        profuturoFlujo = float(self.profuturoFlujo.get()) / 100
        profuturoMixta = float(self.profuturoMixta.get()) / 100
        primaSeguro = float(self.primaSeguro.get()) / 100
        aporte = float(self.aporte.get()) / 100
        remuneracionMaxima = float(self.remuneracionMaxima.get())
        onp = float(self.onp.get()) / 100
        essalud = float(self.essalud.get()) / 100
        sueldoMinimo = float(self.sueldoMinimo.get())
        asignacionFamiliar = float(self.asignacionFamiliar.get()) / 100

        update(f'''UPDATE OPCIONES SET HABITATF={habitatFlujo}, HABITATM={habitatMixta},
                                        INTEGRAF={integraFlujo}, INTEGRAM={integraMixta},
                                        PRIMAF={primaFlujo}, PRIMAM={primaMixta},
                                        PROFUTUROF={profuturoFlujo}, PROFUTUROM={profuturoMixta},
                                        PRIMA={primaSeguro}, APORTE={aporte},
                                        REMUNERACION={remuneracionMaxima}, ONP={onp},
                                        ESSALUD={essalud}, RMV={sueldoMinimo},
                                        ASIGNACION={asignacionFamiliar}''')

        self.CargarDatos()
        self.opciones.destroy()
