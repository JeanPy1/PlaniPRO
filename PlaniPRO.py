from tkinter import Button, Frame, Label, PhotoImage, Scrollbar, Tk
from tkinter.ttk import Treeview, Style
from Menu1 import Menu1
from Menu2 import Menu2
from Menu3 import Menu3

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
        Menu3(self)    
   
    def Menu4(self):
        pass

    def Menu5(self):
        pass

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


if __name__ == '__main__':
    aplicacion = App()      