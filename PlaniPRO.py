from tkinter import Button, Frame, Label, PhotoImage, Tk
from tkinter.ttk import  Style
from Menu1 import Menu1
from Menu2 import Menu2
from Menu3 import Menu3
from Menu6 import Menu6

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
        Menu6(self)
        


if __name__ == '__main__':
    aplicacion = App()      