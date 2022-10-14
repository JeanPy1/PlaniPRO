from tkinter import Button, Frame, Label

class Menu6(Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)
        
        Label(self, anchor='center', bg='#DDDDDD', text='Entidad\nAFP'                ).place(x= 20, y=20, width=100, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Comision\nFlujo        Mixta').place(x=121, y=20, width=121, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Prima\nSeguro'               ).place(x=243, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Aporte\nMensual'             ).place(x=304, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Sueldo\nMaximo'              ).place(x=365, y=20, width= 60, height=48)
        Label(self, text=' Habitat'             ).place(x= 20, y= 69, width=100, height=24)
        Label(self, anchor='e', text='1.47%'    ).place(x=121, y= 69, width= 60, height=24)
        Label(self, anchor='e', text='0.23%'    ).place(x=182, y= 69, width= 60, height=24)
        Label(self, text=' Integra'             ).place(x= 20, y= 94, width=100, height=24)
        Label(self, anchor='e', text='1.55%'    ).place(x=121, y= 94, width= 60, height=24)
        Label(self, anchor='e', text='0.00%'    ).place(x=182, y= 94, width= 60, height=24)
        Label(self, text=' Prima'               ).place(x= 20, y=119, width=100, height=24)
        Label(self, anchor='e', text='1.60%'    ).place(x=121, y=119, width= 60, height=24)
        Label(self, anchor='e', text='0.18%'    ).place(x=182, y=119, width= 60, height=24)
        Label(self, text=' Profuturo'           ).place(x= 20, y=144, width=100, height=24)
        Label(self, anchor='e', text='1.69%'    ).place(x=121, y=144, width= 60, height=24)
        Label(self, anchor='e', text='0.28%'    ).place(x=182, y=144, width= 60, height=24)
        Label(self, anchor='e', text='1.74%'    ).place(x=243, y= 69, width= 60, height=99)
        Label(self, anchor='e', text='10.00%'   ).place(x=304, y= 69, width= 60, height=99)
        Label(self, anchor='e', text='11,002.84').place(x=365, y= 69, width= 60, height=99)
        Label(self, anchor='center', bg='#DDDDDD', text='Fondo\nOnp'       ).place(x=445, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Essalud'          ).place(x=506, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Sueldo\nMinimo'   ).place(x=567, y=20, width= 60, height=48)
        Label(self, anchor='center', bg='#DDDDDD', text='Asigna.\nFamiliar').place(x=628, y=20, width= 60, height=48)
        Label(self, anchor='e', text='13.00%'   ).place(x=445, y= 69, width= 60, height=99)
        Label(self, anchor='e', text='9.00%'    ).place(x=506, y= 69, width= 60, height=99)
        Label(self, anchor='e', text='1,025.00' ).place(x=567, y= 69, width= 60, height=99)
        Label(self, anchor='e', text='10.00%'   ).place(x=628, y= 69, width= 60, height=99)
        Button(self, text='MODIFICAR').place(x=890, y=20, width=90, height=30)
        Button(self, text='SALIR'    , bg='#DF2F2F', command=lambda:self.destroy()).place(x=890, y=125, width=90, height=30)

        # Posicionamos la ventana principal
        self.place(width=1000, height=600)