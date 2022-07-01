from tkinter import Button, Entry, Frame, Label, PhotoImage, Scrollbar, Tk, messagebox
from tkinter.constants import END
from tkinter.ttk import Treeview, Style, Combobox
from datetime import datetime
import sqlite3
import pandas as pd
from dateutil.relativedelta import relativedelta
from tkcalendar import Calendar

import logging
import requests

class ApisNetPe:

    BASE_URL = 'https://api.apis.net.pe'

    def __init__(self, token: str = None):
        self.token = token

    def _get(self, path: str, params: dict):

        url = f'{self.BASE_URL}{path}'

        headers = {
            'Authorization': self.token, 
            'Referer': 'https://apis.net.pe/api-tipo-cambio.html'
        }

        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 422:
            logging.warning(f'{response.url} - invalida parameter')
            logging.warning(response.text)
        elif response.status_code == 403:
            logging.warning(f'{response.url} - IP blocked')
        elif response.status_code == 429:
            logging.warning(f'{response.url} - Many requests add delay')
        elif response.status_code == 401:
            logging.warning(f'{response.url} - Invalid token or limited')
        else:
            logging.warning(f'{response.url} - Server Error status_code={response.status_code}')
        return None

    def get_person(self, dni: str):
        return self._get('/v1/dni', {'numero': dni})

    def get_company(self, ruc: str):
        return self._get('/v1/ruc', {'numero': ruc})

    def get_exchange_rate(self, date: str):
        return self._get('/v1/tipo-cambio-sunat', {'fecha': date})

    def get_exchange_rate_today(self):
        return self._get('/v1/tipo-cambio-sunat', {})

    def get_exchange_rate_for_month(self, month: int, year: int):
        return self._get('/v1/tipo-cambio-sunat', {'month': month, 'year': year})


    ''' #print(ApisNetPe().get_company('20511466629'))
    #print(ApisNetPe().get_person('48555618'))
    #print(ApisNetPe().get_exchange_rate('2020-01-01'))
    #print(ApisNetPe().get_exchange_rate_for_month(1, 2020)) '''

class App(Tk):

    def __init__(self):
        super(App, self).__init__()  
      
        # Creamos la ventana principal
        self.title('PlaniPRO')
        self.geometry('1100x600+-8+0')
        self.resizable(0,0)     
        self.iconbitmap('./img/0.ico')  
        self.option_add('*Font', ('Segoe UI Semibold', '10'))   
        self.option_add('*Button*Font', ('Segoe UI Semibold', '8'))  
        
        # Cargamos las imagenes de los botones
        img1 = PhotoImage(file='./img/1.png')
        img2 = PhotoImage(file='./img/2.png')
        img3 = PhotoImage(file='./img/3.png')
        img4 = PhotoImage(file='./img/4.png')
        img5 = PhotoImage(file='./img/5.png')        
        img6 = PhotoImage(file='./img/6.png')

        # Creamos los botones de los menus  
        self.btn1 = Button(self, image=img1, cursor='hand2', border=0, takefocus=False, command=self.Menu1)
        self.btn2 = Button(self, image=img2, cursor='hand2', border=0, takefocus=False, command=self.Menu2)
        self.btn3 = Button(self, image=img3, cursor='hand2', border=0, takefocus=False)
        self.btn4 = Button(self, image=img4, cursor='hand2', border=0, takefocus=False)
        self.btn5 = Button(self, image=img5, cursor='hand2', border=0, takefocus=False)
        self.btn6 = Button(self, image=img6, cursor='hand2', border=0, takefocus=False)
        
        # Pocisionamos los botones de los menus  
        self.btn1.place(       width=100, height=100)        
        self.btn2.place(y=100, width=100, height=100)       
        self.btn3.place(y=200, width=100, height=100)          
        self.btn4.place(y=300, width=100, height=100)             
        self.btn5.place(y=400, width=100, height=100)         
        self.btn6.place(y=500, width=100, height=100)

        # Remuneracion minima vital RVM
        self.rmv = 1025

        # Cargamos base de datos    
        self.CargarDatos()  
        
        # Variable global de menu DesactivarMenu
        self.menu = 0
            
        # Corremos programa
        self.mainloop()  
         

         
    def CargarDatos(self):
        
        # Cargamos base de datos en dataframe de pandas      
        conexion = sqlite3.connect('PlaniPRO.db')        
        self.datos = pd.read_sql_query('SELECT * FROM ACTIVO ORDER BY APAT, AMAT, NOMB ASC', conexion) 
        conexion.close()    
              
    def DesactivarMenu(self):
        
        # Activar y desactivar botones del menu
        if self.menu == 0:
            self.btn1.configure(state='disabled')
            self.btn2.configure(state='disabled')
            self.btn3.configure(state='disabled')
            self.btn4.configure(state='disabled')
            self.btn5.configure(state='disabled')
            self.btn6.configure(state='disabled')             
        else:
            self.btn1.configure(state='normal')
            self.btn2.configure(state='normal')
            self.btn3.configure(state='normal')
            self.btn4.configure(state='normal')
            self.btn5.configure(state='normal')
            self.btn6.configure(state='normal')                     


                 
    def Menu1(self):  
        
        # desactivamos los botones
        self.DesactivarMenu()
        
        # activamos el boton 1
        self.btn1.configure(state='normal')
        
        # Validacion para destruir el menu 1 si esta activo
        if self.menu == 1: 
            self.men1.destroy()      
            self.menu = 0
            return
        
        # Asignamos el numero de menu activo
        self.menu = 1
               
        # Creamos el frame 
        menu = Frame(self, background='#FFFFFF')  
        
        # Creamos y posicionamos encabezados de treeview
        Label(menu, text='N°'                ).place(x= 15, y=15, width= 30, height=30)
        Label(menu, text='APELLIDOS Y NOMBRE').place(x= 45, y=15, width=280, height=30)
        Label(menu, text='DNI'               ).place(x=325, y=15, width= 82, height=30)
    
        # Creamos el treeview
        self.tre1 = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1','#2','#3'), takefocus=False)
        self.tre1.column('#0', width=  0)
        self.tre1.column('#1', width= 30)
        self.tre1.column('#2', width=270)
        self.tre1.column('#3', width= 90)  
            
        # Creamos el scrollbar              
        self.scroll1 = Scrollbar(menu, orient='vertical', command=self.tre1.yview)
        self.tre1.configure(yscrollcommand=self.scroll1.set)  
        
        # Posicionamos el treeview y scrollbar
        self.tre1.place(x= 15, y=45, height=520)
        self.scroll1.place   (x=409, y=15, height=550)
        
        # Cambiar aspecto del treeview
        Style().configure('Treeview', background='#F0F0F0', font=('Segoe UI Semibold', 10))        
        
        # Evento de seleccion en treeview
        self.tre1.bind('<<TreeviewSelect>>', self.Menu1SeleccionarTreeview)
    
        # Creamos cuadros para mostar detalles del treeview al seleccionar
        Label(menu, text=' Fecha de Nacimiento'    , fg='#5B5857', anchor='nw').place(x=437, y= 15, width=200, height=54)
        Label(menu, text=' Fecha de Ingreso'       , fg='#5B5857', anchor='nw').place(x=437, y= 70, width=200, height=54)
        Label(menu, text=' Planilla'               , fg='#5B5857', anchor='nw').place(x=437, y=125, width=200, height=54)
        Label(menu, text=' Asignacion Familiar'    , fg='#5B5857', anchor='nw').place(x=437, y=180, width=200, height=54)
        Label(menu, text=' Movilidad'              , fg='#5B5857', anchor='nw').place(x=437, y=235, width=200, height=54)
        Label(menu, text=' Sueldo Total'           , fg='#5B5857', anchor='nw').place(x=437, y=290, width=200, height=54)
        Label(menu, text=' Cargo Laboral'          , fg='#5B5857', anchor='nw').place(x=437, y=345, width=200, height=54)
        Label(menu, text=' Cuenta Bancaria'        , fg='#5B5857', anchor='nw').place(x=437, y=400, width=200, height=54)
        Label(menu, text=' Entidad Pensionaria'    , fg='#5B5857', anchor='nw').place(x=437, y=455, width=200, height=54)
        Label(menu, text=' Tipo de Comision S.P.P' , fg='#5B5857', anchor='nw').place(x=437, y=510, width=200, height=55)
        Label(menu, text=' Categoria de Licencia'  , fg='#5B5857', anchor='nw').place(x=638, y= 15, width=200, height=54)
        Label(menu, text=' Vencimiento de Licencia', fg='#5B5857', anchor='nw').place(x=638, y= 70, width=200, height=54)
        Label(menu, text=' Area de Labor'          , fg='#5B5857', anchor='nw').place(x=638, y=125, width=200, height=54)
        Label(menu, text=' Numero de Celular'      , fg='#5B5857', anchor='nw').place(x=638, y=180, width=200, height=54)
        Label(menu, text=' Distrito'               , fg='#5B5857', anchor='nw').place(x=638, y=235, width=200, height=54)
        Label(menu, text=' Edad'                   , fg='#5B5857', anchor='nw').place(x=638, y=290, width=200, height=54)
        Label(menu, text=' Tiempo'                 , fg='#5B5857', anchor='nw').place(x=638, y=345, width=200, height=54)
        Label(menu, text=' Entidad Bancaria'       , fg='#5B5857', anchor='nw').place(x=638, y=400, width=200, height=54)
        Label(menu, text=' C.U.S.P.P.'             , fg='#5B5857', anchor='nw').place(x=638, y=455, width=200, height=54)
        Label(menu, text=' Fecha de Baja'          , fg='#5B5857', anchor='nw').place(x=638, y=510, width=200, height=55)
            
        # Creamos los textos que mostraran los detalles
        self.men1_fnac = Label(menu, anchor='e')
        self.men1_fing = Label(menu, anchor='e')
        self.men1_rem1 = Label(menu, anchor='e')
        self.men1_rem2 = Label(menu, anchor='e')
        self.men1_rem3 = Label(menu, anchor='e')
        self.men1_rem4 = Label(menu, anchor='e')
        self.men1_plab = Label(menu, anchor='e')
        self.men1_cban = Label(menu, anchor='e')
        self.men1_apo1 = Label(menu, anchor='e')        
        self.men1_apo2 = Label(menu, anchor='e')
        self.men1_lice = Label(menu, anchor='e')
        self.men1_venc = Label(menu, anchor='e')
        self.men1_area = Label(menu, anchor='e')
        self.men1_celu = Label(menu, anchor='e')
        self.men1_dist = Label(menu, anchor='e')
        self.men1_edad = Label(menu, anchor='e')
        self.men1_tiem = Label(menu, anchor='e')
        self.men1_banc = Label(menu, anchor='e')
        self.men1_cusp = Label(menu, anchor='e')
        self.men1_renu = Label(menu, anchor='e')       
        
        # Posicionamos los textos de los detalles
        self.men1_fnac.place(x=448, y= 40, width=184) 
        self.men1_fing.place(x=448, y= 95, width=184)
        self.men1_rem1.place(x=448, y=150, width=184)
        self.men1_rem2.place(x=448, y=205, width=184)    
        self.men1_rem3.place(x=448, y=260, width=184)
        self.men1_rem4.place(x=448, y=315, width=184)
        self.men1_plab.place(x=448, y=370, width=184)
        self.men1_cban.place(x=448, y=425, width=184) 
        self.men1_apo1.place(x=448, y=480, width=184)        
        self.men1_apo2.place(x=448, y=535, width=184)
        self.men1_lice.place(x=649, y= 40, width=184)
        self.men1_venc.place(x=649, y= 95, width=184)    
        self.men1_area.place(x=649, y=150, width=184)
        self.men1_celu.place(x=649, y=205, width=184)
        self.men1_dist.place(x=649, y=260, width=184)
        self.men1_edad.place(x=649, y=315, width=184) 
        self.men1_tiem.place(x=649, y=370, width=184)
        self.men1_banc.place(x=649, y=425, width=184)
        self.men1_cusp.place(x=649, y=480, width=184) 
        self.men1_renu.place(x=649, y=535, width=184)   
                  
        # Creamos los botones
        Button(menu, text='AGREGAR'  , cursor='hand2', bg='#88C7FF', bd=0, takefocus=False, command= lambda: self.Menu1Agregar('agregar')).place(x=875, y= 15, width=90, height=30)     
        Button(menu, text='MODIFICAR', cursor='hand2', bg='#88C7FF', bd=0, takefocus=False, command=self.Menu1Modificar                  ).place(x=875, y= 50, width=90, height=30)
        Button(menu, text='ELIMINAR' , cursor='hand2', bg='#88C7FF', bd=0, takefocus=False, command=self.Menu1Eliminar                   ).place(x=875, y= 85, width=90, height=30)        
        
        # Cargamos datos al treeview
        self.Menu1CargarDatos()
        
        # Posicionamos la ventana principal
        menu.place(x=110, y=10, width=980, height=578) 
        
        # Asignamos variable para poder destruir el menu 1
        self.men1 = menu
       
    def Menu1Agregar(self, accion):   

        # Ejecutar codigo si se acepta el cuadro de dialogo       
        if accion == 'agregar':
            respuesta = messagebox.askyesno('AGREGAR','Estas seguro de agregar un trabajador ?', icon = 'warning', default='no')       
            if not respuesta:
                return 

        # Creamos el frame 
        menu = Frame(self.men1, background='#FFFFFF')  
        
        # Creamos los titulos de cada campo 
        Label(menu, text='  Buscar Dni'         , fg='#5B5857', anchor='nw').place(x=  0, y=  0, width=200, height=54)
        Label(menu, text='  Numero Dni'         , fg='#5B5857', anchor='nw').place(x=  0, y= 55, width=200, height=54)
        Label(menu, text='  Apellido Paterno'   , fg='#5B5857', anchor='nw').place(x=  0, y=110, width=200, height=54)
        Label(menu, text='  Apellido Materno'   , fg='#5B5857', anchor='nw').place(x=  0, y=165, width=200, height=54)
        Label(menu, text='  Nombres'            , fg='#5B5857', anchor='nw').place(x=  0, y=220, width=200, height=54)
        Label(menu, text='  Fecha de Nacimiento', fg='#5B5857', anchor='nw').place(x=  0, y=275, width=200, height=54)
        Label(menu, text='  Fecha de Ingreso'   , fg='#5B5857', anchor='nw').place(x=  0, y=330, width=200, height=54)
        Label(menu, text='  Planilla'           , fg='#5B5857', anchor='nw').place(x=  0, y=385, width=200, height=54)
        Label(menu, text='  A. Fam.'            , fg='#5B5857', anchor='nw').place(x= 62, y=385)
        Label(menu, text='  Movili.'            , fg='#5B5857', anchor='nw').place(x=123, y=385)
        Label(menu, text='  Cargo Laboral'      , fg='#5B5857', anchor='nw').place(x=  0, y=440, width=200, height=54)
        Label(menu, text='  Cuenta Bancaria'    , fg='#5B5857', anchor='nw').place(x=  0, y=495, width=200, height=55)
        Label(menu, text='  Entidad Pensio.'    , fg='#5B5857', anchor='nw').place(x=201, y=  0, width=200, height=54)
        Label(menu, text='  Comision'           , fg='#5B5857', anchor='nw').place(x=312, y=  0)
        Label(menu, text='  Codigo Unico S.P.P.', fg='#5B5857', anchor='nw').place(x=201, y= 55, width=200, height=54)
        Label(menu, text='  Licencia'           , fg='#5B5857', anchor='nw').place(x=201, y=110, width=200, height=54)
        Label(menu, text='  Vencimi.'           , fg='#5B5857', anchor='nw').place(x=265, y=110)
        Label(menu, text='  Cod.'               , fg='#5B5857', anchor='nw').place(x=351, y=110)
        Label(menu, text='  Area'               , fg='#5B5857', anchor='nw').place(x=201, y=165, width=200, height=54)
        Label(menu, text='  Celular'            , fg='#5B5857', anchor='nw').place(x=297, y=165)
        Label(menu, text='  Distrito'           , fg='#5B5857', anchor='nw').place(x=201, y=220, width=200, height=54)
        Label(menu, text='  Fecha de Baja'      , fg='#5B5857', anchor='nw').place(x=201, y=275, width=200, height=54)
                
        # Creamos los widges a interactuar} 
        self.men1_agregar_buscar_dni = Entry(menu, relief='flat')       
        self.men1_agre_btn1 = Button(menu, text='BUSCAR', bg='#88C7FF', cursor='hand2', bd=0, takefocus=False, command=self.Menu1ValidarDni)
        self.men1_agre_btn1.place(x=136, y=23, width=54, height=24)         
        self.men1_agre_dni  = Label(menu, relief='flat', bg='white', anchor='w')        
        self.men1_agre_apat = Label(menu, relief='flat', bg='white', anchor='w')
        self.men1_agre_amat = Label(menu, relief='flat', bg='white', anchor='w')
        self.men1_agre_nomb = Label(menu, relief='flat', bg='white', anchor='w')
        self.men1_agre_naci = Entry(menu, relief='flat')
        self.men1_agre_ingr = Entry(menu, relief='flat')
        self.men1_agre_plan = Entry(menu, relief='flat')        
        self.men1_agre_asig = Combobox(menu, values=['SI','NO'], state='readonly')       
        self.men1_agre_movi = Entry(menu, relief='flat')
        self.men1_agre_carg = Combobox(menu, values=['INSPECTOR VIAL','OP. DE GRUA LIVIANA','OP. DE GRUA PESADA'], state='readonly')       
        self.men1_agre_cuen = Entry(menu, relief='flat')
        self.men1_agre_apor = Combobox(menu, values=['ONP','HABITAT','INTEGRA','PRIMA','PROFUTURO',''], state='readonly')
        self.men1_agre_comi = Combobox(menu, values=['FLUJO','MIXTA'], state='disable')
        self.men1_agre_cusp = Entry(menu, relief='flat', state='disable')
        self.men1_agre_lice = Combobox(menu, values=['AI','AIIA','AIIB','AIIIA','AIIIB','AIIIC', ''], state='readonly')       
        self.men1_agre_venc = Entry(menu, relief='flat', state='disable')
        self.men1_agre_codi = Entry(menu, relief='flat', state='disable')
        self.men1_agre_area = Combobox(menu, values=['SUR','NORTE','TALLER','OFICINA'], state='readonly')       
        self.men1_agre_celu = Entry(menu, relief='flat')
        self.men1_agre_dist = Combobox(menu, values=['ANCON', 'ATE VITARTE', 'CARABAYLLO', 'CHORRILLOS',
                                                    'COMAS', 'LOS OLIVOS', 'LURIGANCHO', 'LURIN', 'PUCUSANA', 'PUENTE PIEDRA', 'RIMAC', 'SAN BARTOLO',
                                                    'SAN JUAN DE LURIGANCHO', 'SAN JUAN DE MIRAFLORES', 'SAN MARTIN DE PORRES', 'SANTA ANITA',
                                                    'SANTIAGO DE SURCO', 'SURQUILLO', 'VILLA EL SALVADOR', 'VILLA MARIA DEL TRIUNFO'], state='readonly')      
        self.men1_agre_cese = Entry(menu, relief='flat')
                
        # Agregamos evento al cambiar los items del combobox
        self.men1_agre_apor.bind('<<ComboboxSelected>>', self.Menu1ComboboxAporte) 
        self.men1_agre_lice.bind('<<ComboboxSelected>>', self.Menu1ComboboxLicencia)    

        # Posicionamos los widgets
        self.men1_agregar_buscar_dni.place(x= 10, y= 23, width=120, height=24)    
        self.men1_agre_dni.place (x= 10, y= 78, width=180, height=24)
        self.men1_agre_apat.place(x= 10, y=133, width=180, height=24)
        self.men1_agre_amat.place(x= 10, y=188, width=180, height=24)
        self.men1_agre_nomb.place(x= 10, y=243, width=180, height=24)        
        self.men1_agre_naci.place(x= 10, y=298, width=180, height=24)        
        self.men1_agre_ingr.place(x= 10, y=353, width=180, height=24)
        self.men1_agre_plan.place(x= 10, y=408, width= 56, height=24)  
        self.men1_agre_asig.place(x= 72, y=408, width= 56, height=24)      
        self.men1_agre_movi.place(x=134, y=408, width= 56, height=24) 
        self.men1_agre_carg.place(x= 10, y=463, width=180, height=24)        
        self.men1_agre_cuen.place(x= 10, y=518, width=180, height=24)
        self.men1_agre_apor.place(x=211, y= 23, width=105, height=24) 
        self.men1_agre_comi.place(x=322, y= 23, width= 69, height=24) 
        self.men1_agre_cusp.place(x=211, y= 78, width=180, height=24)
        self.men1_agre_lice.place(x=211, y=133, width= 58, height=24)
        self.men1_agre_venc.place(x=275, y=133, width= 80, height=24)
        self.men1_agre_codi.place(x=361, y=133, width= 30, height=24)
        self.men1_agre_area.place(x=211, y=188, width= 90, height=24)
        self.men1_agre_celu.place(x=307, y=188, width= 84, height=24)
        self.men1_agre_dist.place(x=211, y=243, width=180, height=24)
        self.men1_agre_cese.place(x=211, y=298, width=180, height=24)         
            
        # Asignamos ventana a variable para manipular
        self.men1_agre = menu

        # Creamos boton para grabar los datos
        Button(menu, text='GRABAR', cursor='hand2', bd=0, bg='#88C7FF', takefocus=False, command=self.Menu1Guardar                ).place(x=438, y= 0, width=90, height=30)     
        Button(menu, text='SALIR' , cursor='hand2', bd=0, bg='#88C7FF', takefocus=False, command= lambda: self.men1_agre.destroy()).place(x=438, y=35, width=90, height=30)

        # Superponemos la ventana actual y centramos el foco      
        menu.grab_set()

        # Asignamos el foco al boton de registro del dni
        self.men1_agregar_buscar_dni.focus_set()
        
        # Posicionamos la ventana principal
        menu.place(x=437, y=15, width=528, height=550)
           
    def Menu1Modificar(self):        
        
        # Ejecutar codigo de actualizar informacion si se acepta el cuadro de dialogo
        if self.tre1.selection():
            respuesta = messagebox.askyesno('MODIFICAR','Estas seguro de modificar los datos de este trabajador ?', icon = 'warning', default='no')       
            if respuesta: 
                
                # Obtener id del trabajador seleccionado
                seleccion = self.tre1.focus()
                id = int(self.tre1.item(seleccion).get('text'))
                datos = self.datos[self.datos['ID'] == id]  
                
                # Llamamos a la ventana de agregar trabajador nuevo
                self.Menu1Agregar('modificar')                
                
                # Desactivamos la opcion de buscar dni
                self.men1_agregar_buscar_dni.configure(state='disabled')
                self.men1_agre_btn1.configure(state='disabled')

                # Cargamos datos del trabajador selecionado para actualizar
                self.men1_agre_dni ['text'] = datos['NDNI' ].item()
                self.men1_agre_apat['text'] = datos['APAT'].item()
                self.men1_agre_amat['text'] = datos['AMAT'].item()
                self.men1_agre_nomb['text'] = datos['NOMB'].item()
                self.men1_agre_naci.insert(0, datos['FNAC'].item())
                self.men1_agre_ingr.insert(0, datos['FING'].item())
                self.men1_agre_plan.insert(0, datos['SPLA'].item())

                if datos['AFAM'].item() == 0:
                    self.men1_agre_asig.set('NO')
                else:
                    self.men1_agre_asig.set('SI')

                if datos['SMOV'].item() > 0:
                    self.men1_agre_movi.insert(0, datos['SMOV'].item())                

                self.men1_agre_carg.set(datos['PLAB'].item())
                self.men1_agre_cuen.insert(0, datos['NCUE'].item())
                self.men1_agre_apor.set(datos['EAPO'].item())
                
                if len(datos['EAPO'].item()) > 3:                
                    self.men1_agre_comi.configure(state='readonly')
                    self.men1_agre_comi.set(datos['TCOM'].item())
                    self.men1_agre_cusp.configure(state='normal')                     
                    self.men1_agre_cusp.insert(0, datos['NCUS'].item())
                
                if datos['NLIC'].item() != '':
                    self.men1_agre_lice.set(datos['CLIC'].item())
                    self.men1_agre_venc.configure(state='normal')
                    self.men1_agre_venc.insert(0, datos['VLIC'].item())
                    self.men1_agre_codi.configure(state='normal')
                    self.men1_agre_codi.insert(0, datos['NLIC'].item()[:1])
                    
                self.men1_agre_area.set(datos['ALAB'].item())
                self.men1_agre_celu.insert(0, datos['NCEL'].item())
                self.men1_agre_dist.set(datos['DRES'].item())
                self.men1_agre_cese.insert(0, datos['FCES'].item())

        else:
            messagebox.showinfo('Modificar', 'Debes Seleccionar un Trabajador !', icon = 'warning')  
        
    def Menu1Eliminar(self):  

        # Ejecutar codigo si hay seleccion y se acepta el cuadro de dialogo
        if self.tre1.selection():
            respuesta = messagebox.askyesno('ELIMINAR','Estas seguro de eliminar a este trabajador ?', icon = 'warning', default='no')       
            if respuesta: 
                
                # Tomamos la seleccion del treeview para capturar el ID del trabajador
                seleccion = self.tre1.focus()     
                id = int(self.tre1.item(seleccion).get('text')) 
                
                # Tomamos el index del trabajador para poder eliminarlo del dataframe                  
                index = self.datos[self.datos['ID'] == id].index
                self.datos.drop(index, inplace=True)                
                
                # Limpiamos el treeview y los cuadros de informacion
                self.tre1.delete(*self.tre1.get_children())
                
                # Creamos conexion a la base de datos activando el eliminado en cascada
                conexion = sqlite3.connect('PlaniPRO.db')     
                conexion.execute('PRAGMA foreign_keys = 1')
                cursor = conexion.cursor()  

                # Si hay fecha de cese copiar datos a tabla de cesados
                if self.men1_renu['text'] != '':
                    cursor.execute(f'INSERT INTO CESADO SELECT * FROM ACTIVO WHERE ID = {id}') 
                    conexion.commit()      

                # Ejecutamos la consulta sql de eliminacion
                cursor.execute(f'DELETE FROM ACTIVO WHERE ID = {id}') 
                conexion.commit()
                conexion.close()                  
                
                # Llamamos a la funcion de limpiar datos de informacion
                self.Menu1LimpiarDatos()             
                
                # Cargamos nuevamente los datos al treeview
                self.Menu1CargarDatos()   

        else:
            messagebox.showinfo('Eliminar', 'Debes Seleccionar un Trabajador !', icon = 'warning')                      
        
    def Menu1CargarDatos(self):
        
        # Limpiamos el treeview del menu 1
        self.tre1.delete(*self.tre1.get_children())
        
        # Recorremos datos del dataframe
        orden = 0       
        for fila in self.datos.index:            
            orden+=1     
            
            # Extramos datos para insertar en treeview
            id = self.datos['ID'][fila] 
            dni = self.datos['NDNI'][fila] 
            nombre = self.datos['APAT'][fila] + ' ' + self.datos['AMAT'][fila] + ' ' +self.datos['NOMB'][fila]     
            
            # Insertamos datos al treeview
            self.tre1.insert('',END, text=id, values=(orden, nombre, dni))   
    
    def Menu1LimpiarDatos(self):

            # Limpiamos los cuadros de informacion del menu1
            self.men1_fnac['text'] = ''
            self.men1_fing['text'] = ''
            self.men1_rem1['text'] = ''
            self.men1_rem2['text'] = ''
            self.men1_rem3['text'] = ''
            self.men1_rem4['text'] = ''
            self.men1_plab['text'] = ''
            self.men1_cban['text'] = ''
            self.men1_apo1['text'] = ''            
            self.men1_apo2['text'] = ''
            self.men1_lice['text'] = ''
            self.men1_venc['text'] = ''
            self.men1_area['text'] = ''
            self.men1_celu['text'] = ''
            self.men1_dist['text'] = ''
            self.men1_edad['text'] = ''
            self.men1_tiem['text'] = ''
            self.men1_banc['text'] = ''
            self.men1_cusp['text'] = ''
            self.men1_renu['text'] = ''
     
    def Menu1ValidarDni(self):
      
        # Validamos el dni ingresado
        if self.men1_agregar_buscar_dni.get() == '':
            messagebox.showinfo('BUSCAR', 'Registra el dni del trabajador !', icon = 'warning')    
            self.men1_agregar_buscar_dni.focus()       
        elif len(self.men1_agregar_buscar_dni.get()) != 8: 
            messagebox.showinfo('BUSCAR', 'Registra correctamente el dni del trabajador !', icon = 'warning') 
            self.men1_agregar_buscar_dni.focus()
        elif not self.men1_agregar_buscar_dni.get().isdigit(): 
            messagebox.showinfo('BUSCAR', 'Registra correctamente el dni del trabajador !', icon = 'warning') 
            self.men1_agregar_buscar_dni.focus()
        else:
            
            # Buscamos el dni en la api de buscar dni
            APIS_TOKEN = 'apis-token-1.aTSI1U7KEuT-6bbbCguH-4Y8TI6KS73N'
            api_consultas = ApisNetPe(APIS_TOKEN)    
            dni = self.men1_agregar_buscar_dni.get()
            persona = api_consultas.get_person(dni)
            
            # Si encuentra datos extraer a los textbox
            if persona != None:
                self.men1_agre_dni['text'] = persona['numeroDocumento']
                self.men1_agre_apat['text'] = persona['apellidoPaterno']
                self.men1_agre_amat['text'] = persona['apellidoMaterno']
                self.men1_agre_nomb['text'] = persona['nombres']
                
                self.men1_agregar_buscar_dni.delete(0, END)   
                self.men1_agre_naci.focus_set()                
                
            # Si no encuentra enviar mensaje de aviso
            else:                
                messagebox.showinfo('BUSCAR', 'El numero de Dni ingresado no existe !', icon = 'warning')           
                self.men1_agregar_buscar_dni.focus()   
        
    def Menu1ComboboxAporte(self, e):
        
        # Desactivamos y activamos los elementos del combobox
        if self.men1_agre_apor.get() == 'ONP' or self.men1_agre_apor.get() == '':
            self.men1_agre_comi.set('')
            self.men1_agre_comi['state'] = 'disable'
            self.men1_agre_cusp.delete(0, END)
            self.men1_agre_cusp['state'] = 'disable'            
        else:                 
            self.men1_agre_comi['state'] = 'readonly'
            self.men1_agre_cusp['state'] = 'normal'

    def Menu1ComboboxLicencia(self, e):
        
        # Activamos demas detalles si tiene licencia
        if self.men1_agre_lice.get() == '':  
            self.men1_agre_venc.delete(0, END)   
            self.men1_agre_codi.delete(0, END)           
            self.men1_agre_venc['state'] = 'disable' 
            self.men1_agre_codi['state'] = 'disable'                            
        else: 
            self.men1_agre_venc['state'] = 'normal'
            self.men1_agre_codi['state'] = 'normal' 

    def Menu1SeleccionarTreeview(self, e):
                
        # Si seleccionamos un item se ejecutara el codigo
        if self.tre1.selection():
            
            # Limpiamos los cuadros
            self.Menu1LimpiarDatos()
            
            # Tomamos la seleccion del treeview para capturar el ID del trabajador
            seleccion = self.tre1.focus()     
            id = int(self.tre1.item(seleccion).get('text'))
            
            # Tomamos los datos del trabajador
            datos = self.datos[self.datos['ID'] == id]  
            
            # Extraemos datos del trabajador
            nacimiento  = datos['FNAC'].item()
            ingreso     = datos['FING'].item()
            planilla    = datos['SPLA'].item()  
            asignacion  = datos['AFAM'].item()  
            movilidad   = datos['SMOV'].item()
            total       = planilla + asignacion + movilidad
            cargo       = datos['PLAB'].item()       
            cuenta      = datos['NCUE'].item()
            pension     = datos['EAPO'].item()     
            comision    = datos['TCOM'].item()                          
            licencia    = datos['CLIC'].item() 
            vencimiento = datos['VLIC'].item() 
            area        = datos['ALAB'].item()   
            celular     = datos['NCEL'].item() 
            distrito    = datos['DRES'].item() 
            edad        = relativedelta(datetime.now(), datetime.strptime(nacimiento, '%d/%m/%Y'))
            tiempo      = relativedelta(datetime.now(), datetime.strptime(ingreso, '%d/%m/%Y'))        
            
            banco = ''
            if len(cuenta) == 14:                
                banco       = 'BANCO DE CREDITO'
            elif len(cuenta) == 20:                 
                if cuenta[:3] == '018':
                    banco = 'BANCO DE LA NACION' 
                elif cuenta[:3] == '003':
                    banco = 'INTERBANK' 
                elif cuenta[:3] == '009':
                    banco = 'SCOTIABANK' 
                elif cuenta[:3] == '011':
                    banco = 'BBVA CONTINENTAL' 
                
            cusp        = datos['NCUS'].item()    
            baja        = datos['FCES'].item() 
                           
            # Mostramos datos del trabajador en los cuadros
            self.men1_fnac['text'] = nacimiento
            self.men1_fing['text'] = ingreso
            self.men1_rem1['text'] = f'{planilla:,.2f}'
            self.men1_rem2['text'] = f'{asignacion:,.2f}'
            self.men1_rem3['text'] = f'{movilidad:,.2f}'
            self.men1_rem4['text'] = f'{total:,.2f}'
            self.men1_plab['text'] = cargo
            self.men1_cban['text'] = cuenta       
            self.men1_apo1['text'] = pension   
            self.men1_apo2['text'] = comision             
            self.men1_lice['text'] = licencia
            self.men1_venc['text'] = vencimiento       
            self.men1_area['text'] = area 
            self.men1_celu['text'] = celular 
            self.men1_dist['text'] = distrito 
            self.men1_edad['text'] = edad.years
            self.men1_tiem['text'] = f'{tiempo.years} - {tiempo.months} - {tiempo.days}'
            self.men1_banc['text'] = banco
            self.men1_cusp['text'] = cusp            
            self.men1_renu['text'] = baja 
        
    def Menu1Guardar(self):                
        
        # Validacion de dni
        if self.men1_agre_dni['text'] == '':    
            messagebox.showinfo('GRABAR', 'Busca los datos del trabajador !', icon = 'warning')            
            self.men1_agregar_buscar_dni.focus()                      

        # Validacion de fecha de nacimiento
        elif self.men1_agre_naci.get() == '':
            messagebox.showinfo('GRABAR', 'Registra la fecha de nacimiento !', icon = 'warning')  
            self.men1_agre_naci.focus()
        elif len(self.men1_agre_naci.get()) != 10:
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')  
            self.men1_agre_naci.focus()
        elif not self.men1_agre_naci.get().replace('/','').isdigit() or len(self.men1_agre_naci.get().replace('/','')) != 8:
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                     
            self.men1_agre_naci.focus()
        elif self.men1_agre_naci.get()[2] != '/' or self.men1_agre_naci.get()[5] != '/':
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                      
            self.men1_agre_naci.focus()
        elif int(self.men1_agre_naci.get()[6:10]) < (datetime.today().year - 100):                               
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                         
            self.men1_agre_naci.focus()    
        elif int(self.men1_agre_naci.get()[6:10]) > (datetime.today().year - 18):                               
            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                            
            self.men1_agre_naci.focus()  
        else:            
            try:                  
                datetime.strptime(self.men1_agre_naci.get() , '%d/%m/%Y')                                                                                             
            except ValueError:
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de nacimiento !', icon = 'warning')                                 
                self.men1_agre_naci.focus()        
                return

            # Validacion de fecha de ingreso                          
            if self.men1_agre_ingr.get() == '':
                messagebox.showinfo('GRABAR', 'Registra la fecha de ingreso !', icon = 'warning') 
                self.men1_agre_ingr.focus()
            elif len(self.men1_agre_ingr.get()) != 10:
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')  
                self.men1_agre_ingr.focus()
            elif not self.men1_agre_ingr.get().replace('/','').isdigit() or len(self.men1_agre_ingr.get().replace('/','')) != 8:
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')                             
                self.men1_agre_ingr.focus()
            elif self.men1_agre_ingr.get()[2] != '/' or self.men1_agre_ingr.get()[5] != '/':
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')                          
                self.men1_agre_ingr.focus()
            elif int(self.men1_agre_ingr.get()[6:10]) < (datetime.today().year - 50):                                
                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')                              
                self.men1_agre_ingr.focus()                                                          
            else:                
                try:                  
                    datetime.strptime(self.men1_agre_ingr.get() , '%d/%m/%Y')                                                                                             
                except ValueError:
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de ingreso !', icon = 'warning')                             
                    self.men1_agre_naci.focus()        
                    return

                # Validacion de sueldo planilla   
                if self.men1_agre_plan.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la remuneracion de la planilla !', icon = 'warning')  
                    self.men1_agre_plan.focus()
                elif not self.men1_agre_plan.get().isdigit(): 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la remuneracion de la planilla !', icon = 'warning')   
                    self.men1_agre_plan.focus()
                elif int(self.men1_agre_plan.get()) <=0: 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la remuneracion de la planilla !', icon = 'warning')  
                    self.men1_agre_plan.focus()
                    
                # Validacion de asignacion familiar
                elif self.men1_agre_asig.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la asignacion familiar !', icon = 'warning')  
                    self.men1_agre_asig.focus()
                    
                # Validacion de movilidad
                elif self.men1_agre_movi.get() != '' and not self.men1_agre_movi.get().isdigit():
                    messagebox.showinfo('GRABAR', 'Registra correctamente la remuneracion de la movilidad !', icon = 'warning')  
                    self.men1_agre_movi.focus()
                elif self.men1_agre_movi.get() != '' and int(self.men1_agre_movi.get()) <=0: 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la remuneracion de la movilidad !', icon = 'warning')  
                    self.men1_agre_movi.focus()
                    
                # Validacion de cargo laboral
                elif self.men1_agre_carg.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra el cargo laboral !', icon = 'warning')  
                    self.men1_agre_carg.focus()  

                # Validacion de cuenta bancaria                              
                elif self.men1_agre_cuen.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la cuenta bancaria !', icon = 'warning')  
                    self.men1_agre_cuen.focus()
                elif len(self.men1_agre_cuen.get()) != 14 and len(self.men1_agre_cuen.get()) != 20: 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la cuenta bancaria !', icon = 'warning')  
                    self.men1_agre_cuen.focus()
                elif not self.men1_agre_cuen.get().isdigit(): 
                    messagebox.showinfo('GRABAR', 'Registra correctamente la cuenta bancaria !', icon = 'warning')  
                    self.men1_agre_cuen.focus()
                    
                # Validacion de entidad de aportacion
                elif self.men1_agre_apor.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la entidad pensionaria !', icon = 'warning')  
                    self.men1_agre_apor.focus()

                # Validacion de comision de la entidad de aportacion     
                elif self.men1_agre_comi.state()[0] == 'readonly' and self.men1_agre_comi.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la comision de la entidad pensionaria !', icon = 'warning')                                          
                    self.men1_agre_comi.focus()
                elif self.men1_agre_comi.state()[0] == 'focus' and self.men1_agre_comi.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la comision de la entidad pensionaria !', icon = 'warning')                                            
                    self.men1_agre_comi.focus()                                            
               
                # Validacion del cusp de la entidad de aportacion     
                elif self.men1_agre_cusp.get() != '' and len(self.men1_agre_cusp.get()) != 12:
                    messagebox.showinfo('GRABAR', 'Registra correctamente el cusp de la entidad pensionaria !', icon = 'warning')                                           
                    self.men1_agre_cusp.focus()
                elif self.men1_agre_cusp.get() != '' and not self.men1_agre_cusp.get().isalnum():
                    messagebox.showinfo('GRABAR', 'Registra correctamente el cusp de la entidad pensionaria !', icon = 'warning')                                      
                    self.men1_agre_cusp.focus()               
                                     
                # Validacion de vencimiento de la licencia de conducir
                elif self.men1_agre_lice.get() != '' and self.men1_agre_venc.get() == '':
                    messagebox.showinfo('GRABAR', 'Registra la fecha de revalidacion de la licencia !', icon = 'warning')                                          
                    self.men1_agre_venc.focus()    
                elif self.men1_agre_venc.get() != '' and len(self.men1_agre_venc.get()) != 10:
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                                    
                    self.men1_agre_venc.focus()  
                elif self.men1_agre_venc.get() != '' and not self.men1_agre_venc.get().replace('/','').isdigit():
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                        
                    self.men1_agre_venc.focus()
                elif self.men1_agre_venc.get() != '' and len(self.men1_agre_venc.get().replace('/','')) != 8:
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                       
                    self.men1_agre_venc.focus()    
                elif self.men1_agre_venc.get() != '' and self.men1_agre_venc.get()[2] != '/':
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                         
                    self.men1_agre_venc.focus()
                elif self.men1_agre_venc.get() != '' and self.men1_agre_venc.get()[5] != '/':
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                        
                    self.men1_agre_venc.focus()
                elif self.men1_agre_venc.get() != '' and int(self.men1_agre_venc.get()[6:10]) < (datetime.today().year - 100):                               
                    messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                           
                    self.men1_agre_venc.focus()    
                else:
                    if self.men1_agre_lice.get() != '':
                        try:                  
                            datetime.strptime(self.men1_agre_venc.get() , '%d/%m/%Y')                                                                                             
                        except ValueError:
                            messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de revalidacion de la licencia !', icon = 'warning')                               
                            self.men1_agre_venc.focus()        
                            return
                        
                    # Validacion del codigo de la licencia de conducir
                    if self.men1_agre_lice.get() != '' and self.men1_agre_codi.get() == '':   
                        messagebox.showinfo('GRABAR', 'Registra el codigo de la licencia !', icon = 'warning')                           
                        self.men1_agre_codi.focus()  
                    elif self.men1_agre_lice.get() != '' and len(self.men1_agre_codi.get()) != 1:   
                        messagebox.showinfo('GRABAR', 'Registra correctamente el codigo de la licencia !', icon = 'warning')                            
                        self.men1_agre_codi.focus()   
                    elif self.men1_agre_lice.get() != '' and not self.men1_agre_codi.get().isalpha():   
                        messagebox.showinfo('GRABAR', 'Registra correctamente el codigo de la licencia !', icon = 'warning')                             
                        self.men1_agre_codi.focus()           

                    # Validacion del area de labor 
                    elif self.men1_agre_area.get() == '':
                        messagebox.showinfo('GRABAR', 'Registra el area de labor !', icon = 'warning')                                          
                        self.men1_agre_area.focus()

                    # Validacion del numero celular             
                    elif self.men1_agre_celu.get() == '':
                        messagebox.showinfo('GRABAR', 'Registra el numero de celular !', icon = 'warning')                                              
                        self.men1_agre_celu.focus()
                    elif len(self.men1_agre_celu.get()) != 9:
                        messagebox.showinfo('GRABAR', 'Registra correctamente el numero de celular !', icon = 'warning')                                        
                        self.men1_agre_celu.focus()
                    elif not self.men1_agre_celu.get().isdigit():
                        messagebox.showinfo('GRABAR', 'Registra correctamente el numero de celular !', icon = 'warning')                                       
                        self.men1_agre_celu.focus()
                    
                    # Validacion del distrito de residencia
                    elif self.men1_agre_dist.get() == '':                                                    
                        messagebox.showinfo('GRABAR', 'Registra el distrito de residencia !', icon = 'warning')
                        self.men1_agre_dist.focus()
                      
                    # Validacion de fecha del cese
                    elif self.men1_agre_cese.get() != '' and len(self.men1_agre_cese.get()) != 10:
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                                        
                        self.men1_agre_cese.focus()
                    elif self.men1_agre_cese.get() != '' and not self.men1_agre_cese.get().replace('/','').isdigit():
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                            
                        self.men1_agre_cese.focus()
                    elif self.men1_agre_cese.get() != '' and len(self.men1_agre_cese.get().replace('/','')) != 8:
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                             
                        self.men1_agre_cese.focus()    
                    elif self.men1_agre_cese.get() != '' and self.men1_agre_cese.get()[2] != '/':
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                          
                        self.men1_agre_cese.focus()
                    elif self.men1_agre_cese.get() != '' and self.men1_agre_cese.get()[5] != '/':
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                              
                        self.men1_agre_cese.focus()  
                    elif self.men1_agre_cese.get() != '' and int(self.men1_agre_cese.get()[6:10]) != datetime.today().year: 
                        messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                              
                        self.men1_agre_cese.focus() 
                    else:              
                        if self.men1_agre_cese.get() != '':
                            try:                  
                                datetime.strptime(self.men1_agre_cese.get() , '%d/%m/%Y')                                                                                             
                            except ValueError:
                                messagebox.showinfo('GRABAR', 'Registra correctamente la fecha de cese del trabajador !', icon = 'warning')                               
                                self.men1_agre_cese.focus()        
                                return     

                        # Verificacion de dni ya registrado      
                        if self.men1_agre_btn1['state'] == 'normal':
                            if self.men1_agre_dni['text'] in self.datos['NDNI'].values:                                                    
                                messagebox.showinfo('GRABAR', 'El trabajador ya esta registrado !', icon = 'warning')    
                                return

                        # Guardar datos registrados en variables                                                                                                                                                                   
                        dni  = self.men1_agre_dni.cget('text')
                        apat = self.men1_agre_apat.cget('text')
                        amat = self.men1_agre_amat.cget('text')
                        nomb = self.men1_agre_nomb.cget('text')
                        naci = self.men1_agre_naci.get()
                        ingr = self.men1_agre_ingr.get()
                        plan = int(self.men1_agre_plan.get())      

                        if self.men1_agre_asig.get() == 'NO':
                            asig = 0
                        else:
                            asig = self.rmv * 0.1

                        if self.men1_agre_movi.get() == '':
                            movi = 0  
                        else:                            
                            movi = int(self.men1_agre_movi.get())   

                        carg = self.men1_agre_carg.get()
                        cuen = self.men1_agre_cuen.get()
                        apor = self.men1_agre_apor.get()
                        comi = self.men1_agre_comi.get()
                        cusp = self.men1_agre_cusp.get().upper()
                        lice = self.men1_agre_lice.get()
                        venc = self.men1_agre_venc.get()
                        codi = self.men1_agre_codi.get().upper()
                        
                        if self.men1_agre_lice.get() != '':
                            codi = self.men1_agre_codi.get().upper() + dni                       

                        area = self.men1_agre_area.get()
                        celu = self.men1_agre_celu.get()
                        dist = self.men1_agre_dist.get()              
                        cese = self.men1_agre_cese.get()                         
                        
                        # Obtener el id del trabajador seleccionado
                        seleccion = self.tre1.focus()                        
                        if seleccion !='':
                            id = int(self.tre1.item(seleccion).get('text'))   

                        # Si esta activo boton de dni, nuevo registro (consulta sql)
                        if self.men1_agre_btn1['state'] == 'normal':                                            
                            query = f'''INSERT INTO ACTIVO (NDNI, APAT, AMAT, NOMB, FNAC, FING, SPLA, AFAM, SMOV, EAPO, TCOM, NCUS, PLAB, NCUE, ALAB, NLIC, VLIC, CLIC, NCEL, DRES, FCES) VALUES (
                                '{dni}','{apat}','{amat}','{nomb}','{naci}','{ingr}',{plan},'{asig}',{movi},'{apor}','{comi}','{cusp}','{carg}','{cuen}','{area}','{codi}','{venc}','{lice}','{celu}','{dist}','{cese}')'''
                        
                        # Si no esta activo boton de dni, actualizar registro (consulta sql)               
                        else:                            
                            query = f'''UPDATE ACTIVO SET FNAC = '{naci}', FING = '{ingr}', SPLA = {plan}, AFAM = '{asig}', SMOV = {movi}, EAPO = '{apor}' , TCOM = '{comi}', NCUS = '{cusp}', 
                                    PLAB = '{carg}', NCUE = '{cuen}', ALAB = '{area}', NLIC = '{codi}', VLIC = '{venc}', CLIC = '{lice}', NCEL = '{celu}', DRES = '{dist}', FCES = '{cese}' WHERE ID = {id}'''           

                        # Crear conexion con la base de datos y ejecutar sql                                                                                         
                        conexion = sqlite3.connect('PlaniPRO.db')    
                        cursor = conexion.cursor()
                        cursor.execute(query) 
                        conexion.commit()
                        conexion.close()   

                        # Llamar a funciones para actualizar lista                                                  
                        self.CargarDatos()
                        self.Menu1CargarDatos()
                        self.Menu1LimpiarDatos()                        
                        
                        # Volver a poner el selector del treview en el mismo lugar
                        if seleccion !='':
                            for index in self.tre1.get_children():
                                if int(self.tre1.item(index).get('text')) == id:
                                    self.tre1.selection_set(index)
                                    self.tre1.focus(index)    

                        # Cerrar ventana                           
                        self.men1_agre.destroy()
                                                   
                                                   

    def Menu2(self):  

        # Activamos o desactivamos los botones
        self.DesactivarMenu()
        
        # Dejamos DesactivarMenu el boton 1
        self.btn2.configure(state='normal')
        
        # Validacion para destruir el menu 1 si esta DesactivarMenu y detener la ejecucion
        if self.menu == 2: 
            self.men2.destroy()      
            self.menu = 0
            return
        
        # Asignamos el numero de menu DesactivarMenu
        self.menu = 2
               
        # Creamos el frame       
        menu = Frame(self, background='#FFFFFF')  
        
        # Creamos y posicionamos encabezados de treeview        
        Label(menu, text='N°'                , font=('Segoe UI Semibold', 8)).place(x= 15, y=15, width= 46, height=30)
        Label(menu, text='APELLIDOS Y NOMBRE', font=('Segoe UI Semibold', 8)).place(x= 61, y=15, width=271, height=30)
        Label(menu, text='APOYO'             , font=('Segoe UI Semibold', 8)).place(x=332, y=15, width= 51, height=30)             
        Label(menu, text='FALTA'             , font=('Segoe UI Semibold', 8)).place(x=383, y=15, width= 51, height=30)
        Label(menu, text='FERIADO'           , font=('Segoe UI Semibold', 8)).place(x=434, y=15, width= 51, height=30)
        Label(menu, text='INGRESO'           , font=('Segoe UI Semibold', 8)).place(x=485, y=15, width= 81, height=30)     
        Label(menu, text='RECORTE'           , font=('Segoe UI Semibold', 8)).place(x=566, y=15, width= 81, height=30)
        Label(menu, text='D. ME.'            , font=('Segoe UI Semibold', 8)).place(x=647, y=15, width= 51, height=30)        
        Label(menu, text='VACA.'             , font=('Segoe UI Semibold', 8)).place(x=698, y=15, width= 51, height=30)     
        Label(menu, text='C. VA.'            , font=('Segoe UI Semibold', 8)).place(x=749, y=15, width= 51, height=30)
        Label(menu, text='ADELANTO'          , font=('Segoe UI Semibold', 8)).place(x=800, y=15, width= 81, height=30)    
        Label(menu, text='XFUERA'            , font=('Segoe UI Semibold', 8)).place(x=881, y=15, width= 73, height=30)            
      
        # Crear treeview
        self.tre2 = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12'), takefocus=False)
        self.tre2.column('#0',  width=  0)
        self.tre2.column('#1',  width= 30)
        self.tre2.column('#2',  width=268)
        self.tre2.column('#3',  width= 50, anchor='center')  
        self.tre2.column('#4',  width= 50, anchor='center')
        self.tre2.column('#5',  width= 50, anchor='center')
        self.tre2.column('#6',  width= 81, anchor='center') 
        self.tre2.column('#7',  width= 80, anchor='center')
        self.tre2.column('#8',  width= 52, anchor='center')
        self.tre2.column('#9',  width= 50, anchor='center') 
        self.tre2.column('#10', width= 50, anchor='center') 
        self.tre2.column('#11', width= 87, anchor='center')     
        self.tre2.column('#12', width= 87, anchor='center') 
        
        # Crear scrollbar              
        scroll = Scrollbar(menu, orient='vertical', command=self.tre2.yview)
        self.tre2.configure(yscrollcommand=scroll.set)  
        
        # Evento de seleccion en treeview       
        self.tre2.bind('<Double-1>', self.Menu2DetallesMostrar)

        # Posicionamos treeview y scrollbar
        self.tre2.place(x= 15, y=45, height=520)
        scroll.place   (x=950, y=15, height=550)
        
        # Cambiar aspecto de treeview
        Style().configure('Treeview', background='#F0F0F0', font=('Segoe UI Semibold', 10))         

        self.Menu2CargarDatos()

        # Posicionamos la ventana
        menu.place(x=110, y=10, width=980, height=580)   

        # Asignamos variable a la ventana para poder destruirlo
        self.men2 = menu
                
        # Creamos ventana de detalles y lo ocultamos
        self.Menu2Detalles()
        self.Menu2DetallesOcultar()

    def Menu2CargarDatos(self):

         # Crear conexion a base de datos
        conexion = sqlite3.connect('PlaniPRO.db')    
        cursor = conexion.cursor()

        orden = 0  

        # Recorrer datos almacenados en pandas para agregar informacion a treeview            
        for fila in self.datos.index: 

            orden+=1                  
            id      = self.datos['ID'][fila]  
            apat    = self.datos['APAT'][fila]
            amat    = self.datos['AMAT'][fila]
            nomb    = self.datos['NOMB'][fila]
            nombre  = f'{apat} {amat} {nomb}'  

            # Ejecutamos consultas de los detalles de cada trabajador en base de datos
            apoyo       = cursor.execute(F'SELECT COUNT(FECH) FROM APOYO       WHERE IDAC = {id}').fetchone()  
            falta       = cursor.execute(F'SELECT COUNT(FECH) FROM FALTA       WHERE IDAC = {id}').fetchone()           
            feriado     = cursor.execute(F'SELECT COUNT(FECH) FROM FERIADO     WHERE IDAC = {id}').fetchone()              
            ingreso     = cursor.execute(F'SELECT SUM(MONT)   FROM INGRESO     WHERE IDAC = {id}').fetchone()  
            descuento   = cursor.execute(F'SELECT SUM(MONT)   FROM DESCUENTO   WHERE IDAC = {id}').fetchone()  
            dmedico     = cursor.execute(F'SELECT SUM(DTOT)   FROM DMEDICO     WHERE IDAC = {id}').fetchone()  
            vacaciones  = cursor.execute(F'SELECT SUM(DTOT)   FROM VACACIONES  WHERE IDAC = {id}').fetchone()  
            cvacaciones = cursor.execute(F'SELECT SUM(DTOT)   FROM CVACACIONES WHERE IDAC = {id}').fetchone()  
            adelanto    = cursor.execute(F'SELECT SUM(MONT)   FROM ADELANTO    WHERE IDAC = {id}').fetchone()  
            xfuera      = cursor.execute(F'SELECT SUM(MONT)   FROM XFUERA      WHERE IDAC = {id}').fetchone()  
                       
            if ingreso[0] == None:
                ingreso = '0.00'
            else:
                ingreso = f'{ingreso[0]:.2f}'

            if descuento[0] == None:
                descuento = '0.00'
            else:
                descuento = f'{descuento[0]:.2f}'

            if dmedico[0] == None:
                dmedico = '0'
            else:
                dmedico = dmedico[0]

            if vacaciones[0] == None:
                vacaciones = '0'
            else:
                vacaciones = vacaciones[0]

            if cvacaciones[0] == None:
                cvacaciones = '0'
            else:
                cvacaciones = cvacaciones[0]

            if adelanto[0] == None:
                adelanto = '0.00'
            else:
                adelanto = f'{adelanto[0]:.2f}'

            if xfuera[0] == None:
                xfuera = '0.00'
            else:
                xfuera = f'{xfuera[0]:.2f}'
                   
            # Insertamos datos al treeview
            self.tre2.insert('', END, text=id, values=(orden, nombre, apoyo[0], falta[0], feriado[0], ingreso, descuento, dmedico, vacaciones, cvacaciones, adelanto, xfuera)) 

        # Cerramos conexion a base de datos
        conexion.close()        

    def Menu2Detalles(self):                   
        
        # Creamos el frame 
        menu = Frame(self.men2, background='#FFFFFF')          

        # Creamos el widget del calendario
        self.calendario = Calendar(menu, menuselectmode='day', date_pattern='dd/MM/yyyy', cursor='hand2', takefocus=False)
        self.calendario.place(x=15, y=15)

        # Creamos widgets del registro de apoyos
        Button(menu, text='APOYO', command=lambda: self.Menu2DetallesGrabar('APOYO'), cursor='hand2', bd=0, bg='#88C7FF', takefocus=False).place(x=275, y=15, width=94, height=22)
        self.apoyo = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1'), takefocus=False)
        self.apoyo.column('#0', width= 0)
        self.apoyo.column('#1', width=92)          
        self.apoyo.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.apoyo.place(x=275, y=42, height=160)

        # Creamos widgets del registro de faltas
        Button(menu, text='FALTA', command=lambda: self.Menu2DetallesGrabar('FALTA'), cursor='hand2', bd=0, bg='#88C7FF', takefocus=False).place(x=377, y=15, width=94, height=22)
        self.falta = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1'), takefocus=False)
        self.falta.column('#0', width= 0)
        self.falta.column('#1', width=92) 
        self.falta.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion) # Evento de seleccion en treeview
        self.falta.place(x=377, y=42, height=160)

        # Creamos widgets del registro de feriado
        Button(menu, text='FERIADO', command=lambda: self.Menu2DetallesGrabar('FERIADO'), cursor='hand2', bd=0, bg='#88C7FF', takefocus=False).place(x=479, y=15, width=94, height=22)
        self.feriado = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1'), takefocus=False)
        self.feriado.column('#0', width= 0)
        self.feriado.column('#1', width=92) 
        self.feriado.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.feriado.place(x=479, y=42, height=160)

        # Creamos widgets del registro de adelanto
        Button(menu, text='ADELANTO', command=lambda: self.Menu2DetallesGrabar('ADELANTO'), cursor='hand2', bd=0, bg='#88C7FF', takefocus=False).place(x=581, y=15, width=153, height=22)
        Label(menu, text='Importe', bg='white', anchor='w').place(x=609, y=41, height=16)        
        self.adelantoImporte = Entry(menu, relief='flat', bg='#F0F0F0', justify='right')
        self.adelantoImporte.place(x=671, y=42, width=60, height=17)
        self.adelanto = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1', '#2'), takefocus=False)
        self.adelanto.column('#0', width= 0)
        self.adelanto.column('#1', width=80, anchor='w') 
        self.adelanto.column('#2', width=70, anchor='e')
        self.adelanto.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.adelanto.place(x=581, y=62, height=140)        

        # Creamos widgets del registro de ingreso
        Button(menu, text='INGRESO', command=lambda: self.Menu2DetallesGrabar('INGRESO'), cursor='hand2', bd=0, bg='#88C7FF', takefocus=False).place(x=15, y=240, width=255, height=22)
        Label(menu, text='Detalle', bg='white', anchor='w').place(x=15, y=266, height=16)
        Label(menu, text='Monto', bg='white', anchor='w').place(x=217, y=266, height=16)
        self.ingresoDetalle = Entry(menu, relief='flat', bg='#F0F0F0')
        self.ingresoDetalle.place(x=15, y=284, width=198, height=17)
        self.ingresoImporte = Entry(menu, relief='flat', bg='#F0F0F0', justify='right')
        self.ingresoImporte.place(x=217, y=284, width=50, height=17)
        self.ingreso = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1', '#2'), takefocus=False)
        self.ingreso.column('#0', width= 0)
        self.ingreso.column('#1', width=182, anchor='w') 
        self.ingreso.column('#2', width=70, anchor='e') 
        self.ingreso.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.ingreso.place(x=15, y=304, height=60)

        # Creamos widgets del registro de descuento
        Button(menu, text='DESCUENTO', command=lambda: self.Menu2DetallesGrabar('DESCUENTO'), cursor='hand2', bd=0, bg='#88C7FF', takefocus=False).place(x=277, y=240, width=255, height=22)
        Label(menu, text='Detalle', bg='white', anchor='w').place(x=277, y=266, height=16)
        Label(menu, text='Monto', bg='white', anchor='w').place(x=479, y=266, height=16)
        self.descuentoDetalle = Entry(menu, relief='flat', bg='#F0F0F0')
        self.descuentoDetalle.place(x=277, y=284, width=198, height=17)
        self.descuentoImporte = Entry(menu, relief='flat', bg='#F0F0F0', justify='right')
        self.descuentoImporte.place(x=479, y=284, width=50, height=17)
        self.descuento = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1', '#2'), takefocus=False)
        self.descuento.column('#0', width= 0)
        self.descuento.column('#1', width=182, anchor='w') 
        self.descuento.column('#2', width=70, anchor='e') 
        self.descuento.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.descuento.place(x=277, y=304, height=60)

        # Creamos widgets del registro de vacaciones
        Button(menu, text='VACACIONES', command=lambda: self.Menu2DetallesGrabar('VACACIONES'), cursor='hand2', bd=0, bg='#88C7FF', takefocus=False).place(x=539, y=240, width=194, height=22)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('fivacaciones'), bg='red', cursor='hand2', bd=0, takefocus=False).place(x=621, y=268, width=10, height=14)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('ffvacaciones'), bg='red', cursor='hand2', bd=0, takefocus=False).place(x=696, y=268, width=10, height=14)
        Label(menu, text='Inicio', bg='white', anchor='w').place(x=539, y=266, height=16)
        Label(menu, text='Final', bg='white', anchor='w').place(x=633, y=266, height=16)
        Label(menu, text='Dias', bg='white', anchor='w').place(x=708, y=266, height=16)
        self.vacacionesInicial = Entry(menu, relief='flat', bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.vacacionesInicial.place(x=539, y=284, width=92, height=17)
        self.vacacionesFinal = Entry(menu, relief='flat', bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.vacacionesFinal.place(x=633, y=284, width=73, height=17)
        self.vacacionesTotal = Entry(menu, relief='flat', bg='#F0F0F0', justify='right')
        self.vacacionesTotal.place(x=708, y=284, width=24, height=17)
        self.vacaciones = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1', '#2', '#3'), takefocus=False)
        self.vacaciones.column('#0', width= 0)
        self.vacaciones.column('#1', width=74, anchor='w') 
        self.vacaciones.column('#2', width=74, anchor='e') 
        self.vacaciones.column('#3', width=45, anchor='e') 
        self.vacaciones.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.vacaciones.place(x=539, y=304, height=60)

        # Creamos widgets del registro de descanso medico
        Button(menu, text='DESCANSO MEDICO', command=lambda: self.Menu2DetallesGrabar('DMEDICO'), cursor='hand2', bd=0, bg='#88C7FF', takefocus=False).place(x=15, y=402, width=516, height=22)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('fidmedico'), bg='red', cursor='hand2', bd=0, takefocus=False).place(x=97, y=430, width=10, height=14)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('ffdmedico'), bg='red', cursor='hand2', bd=0, takefocus=False).place(x=172, y=430, width=10, height=14)
        Label(menu, text='Inicio', bg='white', anchor='w').place(x=15, y=428, height=16)
        Label(menu, text='Final', bg='white', anchor='w').place(x=109, y=428, height=16)
        Label(menu, text='Detalle', bg='white', anchor='w').place(x=186, y=428, height=16)
        Label(menu, text='Dias', bg='white', anchor='w').place(x=505, y=428, width=60, height=16)
        self.dmedicoInicial = Entry(menu, relief='flat', bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.dmedicoInicial.place(x=15, y=446, width=92, height=17)
        self.dmedicoFinal = Entry(menu, relief='flat', bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.dmedicoFinal.place(x=109, y=446, width=73, height=17)
        self.dmedicoDetalle = Entry(menu, relief='flat', bg='#F0F0F0')
        self.dmedicoDetalle.place(x=186, y=446, width=317, height=17)
        self.dmedicoTotal = Entry(menu, relief='flat', bg='#F0F0F0', justify='right')
        self.dmedicoTotal.place(x=505, y=446, width=25, height=17)
        self.dmedico = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1', '#2', '#3', '#4'), takefocus=False)
        self.dmedico.column('#0', width= 0)
        self.dmedico.column('#1', width=74, anchor='w') 
        self.dmedico.column('#2', width=75, anchor='e') 
        self.dmedico.column('#3', width=321, anchor='w') 
        self.dmedico.column('#4', width=45, anchor='e') 
        self.dmedico.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.dmedico.place(x=15, y=466, height=60)

        # Creamos widgets del registro de compra de vacaciones
        Button(menu, text='COMPRA DE VACACIONES', command=lambda: self.Menu2DetallesGrabar('CVACACIONES'), cursor='hand2', bd=0, bg='#88C7FF', takefocus=False).place(x=539, y=402, width=194, height=22)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('ficvacaciones'), bg='red', cursor='hand2', bd=0, takefocus=False).place(x=621, y=430, width=10, height=14)
        Button(menu, command=lambda: self.Menu2DetallesSeleccionarFecha('ffcvacaciones'), bg='red', cursor='hand2', bd=0, takefocus=False).place(x=696, y=430, width=10, height=14)
        Label(menu, text='Inicio', bg='white', anchor='w').place(x=539, y=428, height=16)
        Label(menu, text='Final', bg='white', anchor='w').place(x=633, y=428, height=16)
        Label(menu, text='Dias', bg='white', anchor='w').place(x=708, y=428, height=16)
        self.cvacacionesInicial = Entry(menu, relief='flat', bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.cvacacionesInicial.place(x=539, y=446, width=92, height=17)
        self.cvacacionesFinal = Entry(menu, relief='flat', bg='#F0F0F0', justify='right', state='readonly', takefocus=False)
        self.cvacacionesFinal.place(x=633, y=446, width=73, height=17)
        self.cvacacionesTotal = Entry(menu, relief='flat', bg='#F0F0F0', justify='right')
        self.cvacacionesTotal.place(x=708, y=446, width=24, height=17)
        self.cvacaciones = Treeview(menu, show='tree', selectmode='browse', padding=-1, columns=('#1', '#2', '#3'), takefocus=False)
        self.cvacaciones.column('#0', width= 0)
        self.cvacaciones.column('#1', width=74, anchor='w') 
        self.cvacaciones.column('#2', width=74, anchor='e') 
        self.cvacaciones.column('#3', width=45, anchor='e') 
        self.cvacaciones.bind('<Button-1>', self.Menu2DetallesQuitarSeleccion)
        self.cvacaciones.place(x=539, y=466, height=60)
            
        # Cambiar aspecto de treeview
        Style().configure('Treeview', background='#F0F0F0', font=('Segoe UI Semibold', 10)) 
                  
        # Asignamos variable a la ventana para poder destruirlo
        self.men2_detalles = menu

        # Creamos los botones
        Button(menu, text='ELIMINAR', cursor='hand2', bd=0, bg='#88C7FF', takefocus=False, command=self.Menu2DetallesEliminar).place(x=875, y= 15, width=90, height=30)     
        Button(menu, text='SALIR', cursor='hand2', bd=0, bg='#88C7FF', takefocus=False, command=self.Menu2DetallesOcultar).place(x=875, y= 50, width=90, height=30)

        # Posicionamos la ventana
        menu.place(x=0, y=0, width=980, height=580) 

    def Menu2DetallesMostrar(self, e):
      
        # Mostramos la ventana detalles
        if self.tre2.selection():
            
            id = int(self.tre2.item(self.tre2.focus()).get('text'))

            # Crear conexion a base de datos
            conexion = sqlite3.connect('PlaniPRO.db')    
            cursor = conexion.cursor()

            # Ejecutamos consultas de los detalles de cada trabajador en base de datos
            apoyo       = cursor.execute(F'SELECT ID, FECH                      FROM APOYO       WHERE IDAC = {id}').fetchall() 
            falta       = cursor.execute(F'SELECT ID, FECH                      FROM FALTA       WHERE IDAC = {id}').fetchall()  
            feriado     = cursor.execute(F'SELECT ID, FECH                      FROM FERIADO     WHERE IDAC = {id}').fetchall()  
            adelanto    = cursor.execute(F'SELECT ID, FECH, MONT                FROM ADELANTO    WHERE IDAC = {id}').fetchall()  
            ingreso     = cursor.execute(F'SELECT ID, DETA, MONT                FROM INGRESO     WHERE IDAC = {id}').fetchall() 
            descuento   = cursor.execute(F'SELECT ID, DETA, MONT                FROM DESCUENTO   WHERE IDAC = {id}').fetchall()  
            vacaciones  = cursor.execute(F'SELECT ID, FINI, FFIN, DTOT          FROM VACACIONES  WHERE IDAC = {id}').fetchall()  
            dmedico     = cursor.execute(F'SELECT ID, FINI, FFIN, DETA, DTOT    FROM DMEDICO     WHERE IDAC = {id}').fetchall() 
            cvacaciones = cursor.execute(F'SELECT ID, FINI, FFIN, DTOT          FROM CVACACIONES WHERE IDAC = {id}').fetchall()  

            for dato in apoyo:
                self.apoyo.insert('', END, text=dato[0], values=(dato[1])) 

            for dato in falta:
                self.falta.insert('', END, text=dato[0], values=(dato[1]))

            for dato in feriado:
                self.feriado.insert('', END, text=dato[0], values=(dato[1]))    

            for dato in adelanto:
                self.adelanto.insert('', END, text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))      

            for dato in ingreso:
                self.ingreso.insert('', END, text=dato[0], values=(dato[1], f'{dato[2]:.2f}'))    

            for dato in descuento:
                self.descuento.insert('', END, text=dato[0], values=(dato[1], f'{dato[2]:.2f}')) 

            for dato in vacaciones:
                self.vacaciones.insert('', END, text=dato[0], values=(dato[1], dato[2], dato[3])) 

            for dato in dmedico:
                self.dmedico.insert('', END, text=dato[0], values=(dato[1], dato[2], dato[3], dato[4])) 

            for dato in cvacaciones:
                self.cvacaciones.insert('', END, text=dato[0], values=(dato[1], dato[2], dato[3]))     
          
            conexion.close()

            self.men2_detalles.place(x=0, y=0, width=980, height=580) 
            self.men2_detalles.grab_set()

    def Menu2DetallesOcultar(self):
        
        # Limpiamos los cuadros de la ventana detalles
        self.apoyo.delete(*self.apoyo.get_children())
        self.falta.delete(*self.falta.get_children())
        self.feriado.delete(*self.feriado.get_children())
        self.adelanto.delete(*self.adelanto.get_children())
        self.ingreso.delete(*self.ingreso.get_children())
        self.descuento.delete(*self.descuento.get_children())
        self.vacaciones.delete(*self.vacaciones.get_children())
        self.dmedico.delete(*self.dmedico.get_children())
        self.cvacaciones.delete(*self.cvacaciones.get_children())
        
        # Ocultamos la ventana detalles
        self.men2_detalles.place_forget() 
        self.men2_detalles.grab_release()   
        
    def Menu2DetallesGrabar(self, widget):  

        # Actualizamos la fila seleccionada y aunmentamos +1 apoyo
        valores = self.tre2.item(self.tre2.focus())['values'] 

        # Crear conexion a base de datos
        conexion = sqlite3.connect('PlaniPRO.db')    
        cursor = conexion.cursor()    

        # Obtener id de trabajador
        id = int(self.tre2.item(self.tre2.focus()).get('text'))

        if widget == 'APOYO':
            
         # Verificamos si se repite la fecha para anular registro       
            for row in self.apoyo.get_children():
                fecha = self.apoyo.item(row)['values'][0]            
                if fecha == self.calendario.get_date():
                    return                   
        
            valores[2] = int(valores[2]) + 1           
        
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'INSERT INTO APOYO (IDAC, FECH) VALUES ({id}, "{self.calendario.get_date()}")')

            idRegistro = cursor.execute(F'SELECT ID FROM APOYO ORDER BY ID DESC').fetchone()  
            
            # Si no esta registrado la fecha agregamos al treeview
            self.apoyo.insert('',END, text=idRegistro[0] ,values=self.calendario.get_date())
                   
        elif widget == 'FALTA':

            # Verificamos si se repite la fecha para anular registro       
            for row in self.falta.get_children():
                fecha = self.falta.item(row)['values'][0]            
                if fecha == self.calendario.get_date():
                    return                   
        
            valores[3] = int(valores[3]) + 1           
        
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'INSERT INTO FALTA (IDAC, FECH) VALUES ({id}, "{self.calendario.get_date()}")')

            idRegistro = cursor.execute(F'SELECT ID FROM FALTA ORDER BY ID DESC').fetchone()  
            # Si no esta registrado la fecha agregamos al treeview
            self.falta.insert('',END, text=idRegistro[0], values=self.calendario.get_date())

        elif widget == 'FERIADO':

            # Verificamos si se repite la fecha para anular registro       
            for row in self.feriado.get_children():
                fecha = self.feriado.item(row)['values'][0]            
                if fecha == self.calendario.get_date():
                    return                   
        
            valores[4] = int(valores[4]) + 1           
        
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'INSERT INTO FERIADO (IDAC, FECH) VALUES ({id}, "{self.calendario.get_date()}")')
            idRegistro = cursor.execute(F'SELECT ID FROM FERIADO ORDER BY ID DESC').fetchone()
            # Si no esta registrado la fecha agregamos al treeview
            self.feriado.insert('',END,text=idRegistro[0], values=self.calendario.get_date())

        elif widget == 'ADELANTO':

            # Verificamos si esta vacio el cuadro de registro de importe
            if self.adelantoImporte.get() == '':
                self.adelantoImporte.focus_set()   
                messagebox.showinfo('ADELANTO', 'Registra el importe del adelanto !', icon = 'warning')    
            else:

                # Verificamos si se repite la fecha para anular registro
                for row in self.adelanto.get_children():         
                    fecha = self.adelanto.item(row)['values'][0]               
                    if fecha == self.calendario.get_date():                
                        return

                # Si no se repite la fecha verificamos que el importe este correctamente escrito 
                if self.adelantoImporte.get().count('.') == 1 or self.adelantoImporte.get().count('.') == 0:          
                    if self.adelantoImporte.get().replace('.','').isnumeric():

                        # Si todo esta ok, registramos en el treeview
                        monto = float(self.adelantoImporte.get())  

                        valores[10] = f'{float(valores[10]) + monto:.2f}'             
        
                        # Ejecutamos la query de grabar dia de apoyo
                        cursor.execute(F'INSERT INTO ADELANTO (IDAC, FECH, MONT) VALUES ({id}, "{self.calendario.get_date()}", {monto})')

                        idRegistro = cursor.execute(F'SELECT ID FROM ADELANTO ORDER BY ID DESC').fetchone()
                        self.adelanto.insert('',END ,text=idRegistro[0], values=(self.calendario.get_date(), f'{monto:.2f}'))
                        self.adelantoImporte.delete(0, END)                    
                
                # Si esta mal la validacion del importe o esta vacio enviamos el foco al cuadro
                    else:
                        self.adelantoImporte.focus_set()   
                        messagebox.showinfo('ADELANTO', 'Registra correctamente el importe del adelanto !', icon = 'warning')                          
                else:
                    self.adelantoImporte.focus_set()
                    messagebox.showinfo('ADELANTO', 'Registra correctamente el importe del adelanto !', icon = 'warning')    

        elif widget == 'INGRESO':

            # Validamos los cuadros de ingreso si estan vacios enviar el foco
            if self.ingresoDetalle.get() == '':
                self.ingresoDetalle.focus_set()
                messagebox.showinfo('INGRESO', 'Registra el detalle del ingreso !', icon = 'warning')
            elif self.ingresoImporte.get() == '':
                self.ingresoImporte.focus_set()    
                messagebox.showinfo('INGRESO', 'Registra el importe del ingreso !', icon = 'warning')  
            else:
                
                # Validamos el importe que este bien escrito 
                if self.ingresoImporte.get().count('.') == 1 or self.ingresoImporte.get().count('.') == 0:          
                    if self.ingresoImporte.get().replace('.','').isnumeric():

                        # Si todo esta ok, registramos en el treeview
                        monto = float(self.ingresoImporte.get())

                        valores[5] = f'{float(valores[5]) + monto:.2f}' 

                        # Ejecutamos la query de grabar dia de apoyo
                        cursor.execute(F'INSERT INTO INGRESO (IDAC, DETA, MONT) VALUES ({id}, "{self.ingresoDetalle.get()}", {monto})')

                        idRegistro = cursor.execute(F'SELECT ID FROM INGRESO ORDER BY ID DESC').fetchone()
                        self.ingreso.insert('', END,text=idRegistro[0], values=(self.ingresoDetalle.get(), f'{monto:.2f}'))

                        self.ingresoDetalle.delete(0, END)
                        self.ingresoImporte.delete(0, END)
                    
                # Si esta mal la validacion del importe o esta vacio enviamos el foco al cuadro
                    else:
                        self.ingresoImporte.focus_set()  
                        messagebox.showinfo('INGRESO', 'Registra correctamente el importe del ingreso !', icon = 'warning')   
                else:
                    self.ingresoImporte.focus_set()
                    messagebox.showinfo('INGRESO', 'Registra correctamente el importe del ingreso !', icon = 'warning')   

        elif widget == 'DESCUENTO':

            # Validamos los cuadros de descuento si estan vacios enviar el foco
            if self.descuentoDetalle.get() == '':
                self.descuentoDetalle.focus_set()
                messagebox.showinfo('DESCUENTO', 'Registra el detalle del descuento !', icon = 'warning')
            elif self.descuentoImporte.get() == '':
                self.descuentoImporte.focus_set()    
                messagebox.showinfo('DESCUENTO', 'Registra el importe del descuento !', icon = 'warning')
            else:
                
                # Validamos el importe que este bien escrito 
                if self.descuentoImporte.get().count('.') == 1 or self.descuentoImporte.get().count('.') == 0:          
                    if self.descuentoImporte.get().replace('.','').isnumeric():
                                                                   
                        # Si todo esta ok, registramos en el treeview
                        monto = float(self.descuentoImporte.get())

                        valores[6] = f'{float(valores[6]) + monto:.2f}' 

                        # Ejecutamos la query de grabar dia de apoyo
                        cursor.execute(F'INSERT INTO DESCUENTO (IDAC, DETA, MONT) VALUES ({id}, "{self.descuentoDetalle.get()}", {monto})')

                        idRegistro = cursor.execute(F'SELECT ID FROM DESCUENTO ORDER BY ID DESC').fetchone()
                        self.descuento.insert('', END,text=idRegistro[0], values=(self.descuentoDetalle.get(), f'{monto:.2f}'))

                        self.descuentoDetalle.delete(0, END)
                        self.descuentoImporte.delete(0, END)
                    
                # Si esta mal la validacion del importe o esta vacio enviamos el foco al cuadro
                    else:
                        self.descuentoImporte.focus_set()    
                        messagebox.showinfo('DESCUENTO', 'Registra correctamente el importe del descuento !', icon = 'warning') 
                else:
                    self.descuentoImporte.focus_set()
                    messagebox.showinfo('DESCUENTO', 'Registra correctamente el importe del descuento !', icon = 'warning')

        elif widget == 'VACACIONES':

            # Validamos los cuadros de vacaciones si estan vacios enviar el foco
            if self.vacacionesInicial.get() == '':
                self.vacacionesTotal.focus_set() 
                messagebox.showinfo('VACACIONES', 'Selecciona la fecha inicial de las vacaciones !', icon = 'warning')
            elif self.vacacionesFinal.get() == '':
                self.vacacionesTotal.focus_set() 
                messagebox.showinfo('VACACIONES', 'Selecciona la fecha final de las vacaciones !', icon = 'warning')
            elif self.vacacionesTotal.get() == '':
                self.vacacionesTotal.focus_set()   
                messagebox.showinfo('VACACIONES', 'Registra el total de dias de las vacaciones !', icon = 'warning')
            else:
                
                # Validamos el total que este bien escrito             
                if self.vacacionesTotal.get().isnumeric():
                    
                    # Si todo esta ok, registramos en el treeview
                    total =int(self.vacacionesTotal.get())                    

                    valores[8] = int(valores[8]) + total

                    # Ejecutamos la query de grabar dia de apoyo
                    cursor.execute(F'INSERT INTO VACACIONES (IDAC, FINI, FFIN, DTOT) VALUES ({id}, "{self.vacacionesInicial.get()}", "{self.vacacionesFinal.get()}",  {total})')

                    idRegistro = cursor.execute(F'SELECT ID FROM VACACIONES ORDER BY ID DESC').fetchone()
                    self.vacaciones.insert('', END,text=idRegistro[0], values=(self.vacacionesInicial.get(), self.vacacionesFinal.get(), total))

                    self.vacacionesInicial.configure(state='normal')
                    self.vacacionesFinal.configure(state='normal')
                    self.vacacionesInicial.delete(0, END)
                    self.vacacionesFinal.delete(0, END)
                    self.vacacionesTotal.delete(0, END)
                    self.vacacionesInicial.configure(state='readonly')
                    self.vacacionesFinal.configure(state='readonly')
                    
                # Si esta mal la validacion del total enviamos el foco al cuadro               
                else:
                    self.vacacionesTotal.focus_set()
                    messagebox.showinfo('VACACIONES', 'Registra correctamente el total de dias de las vacaciones !', icon = 'warning')

        elif widget == 'DMEDICO':
            
            # Validamos los cuadros de descanso medico si estan vacios enviar el foco
            if self.dmedicoInicial.get() == '':
                self.dmedicoDetalle.focus_set() 
                messagebox.showinfo('DESCANSO MEDICO', 'Selecciona la fecha inicial del descanso medico !', icon = 'warning')
            elif self.dmedicoFinal.get() == '':
                self.dmedicoDetalle.focus_set() 
                messagebox.showinfo('DESCANSO MEDICO', 'Selecciona la fecha final del descanso medico !', icon = 'warning')
            elif self.dmedicoDetalle.get() == '':
                self.dmedicoDetalle.focus_set()   
                messagebox.showinfo('DESCANSO MEDICO', 'Registra el detalle del descanso medico !', icon = 'warning')
            elif self.dmedicoTotal.get() == '':
                self.dmedicoTotal.focus_set()   
                messagebox.showinfo('DESCANSO MEDICO', 'Registra el total de dias del descanso medico !', icon = 'warning')
            else:
                
                # Validamos el total que este bien escrito             
                if self.dmedicoTotal.get().isnumeric():
                    
                    # Si todo esta ok, registramos en el treeview
                    total =int(self.dmedicoTotal.get())                    

                    valores[7] = int(valores[7]) + total

                    # Ejecutamos la query de grabar dia de apoyo
                    cursor.execute(F'INSERT INTO DMEDICO (IDAC, FINI, FFIN, DETA, DTOT) VALUES ({id}, "{self.dmedicoInicial.get()}", "{self.dmedicoFinal.get()}", "{self.dmedicoDetalle.get()}",  {total})')

                    idRegistro = cursor.execute(F'SELECT ID FROM DMEDICO ORDER BY ID DESC').fetchone()
                    self.dmedico.insert('', END,text=idRegistro[0], values=(self.dmedicoInicial.get(), self.dmedicoFinal.get(), self.dmedicoDetalle.get(), total))

                    self.dmedicoInicial.configure(state='normal')
                    self.dmedicoFinal.configure(state='normal')
                    self.dmedicoInicial.delete(0, END)
                    self.dmedicoFinal.delete(0, END)
                    self.dmedicoDetalle.delete(0, END)
                    self.dmedicoTotal.delete(0, END)
                    self.dmedicoInicial.configure(state='readonly')
                    self.dmedicoFinal.configure(state='readonly')

                # Si esta mal la validacion del total enviamos el foco al cuadro               
                else:
                    self.dmedicoTotal.focus_set()
                    messagebox.showinfo('DESCANSO MEDICO', 'Registra correctamente el total de dias del descanso medico !', icon = 'warning')

        elif widget == 'CVACACIONES':

             # Validamos los cuadros de compra de vacaciones si estan vacios enviar el foco
            if self.cvacacionesInicial.get() == '':
                self.cvacacionesTotal.focus_set() 
                messagebox.showinfo('COMPRA DE VACACIONES', 'Selecciona la fecha inicial de la compra de vacaciones !', icon = 'warning')
            elif self.cvacacionesFinal.get() == '':
                self.cvacacionesTotal.focus_set() 
                messagebox.showinfo('COMPRA DE VACACIONES', 'Selecciona la fecha final de la compra de vacaciones !', icon = 'warning')
            elif self.cvacacionesTotal.get() == '':
                self.cvacacionesTotal.focus_set()   
                messagebox.showinfo('COMPRA DE VACACIONES', 'Registra el total de dias de la compra de vacaciones !', icon = 'warning')
            else:
                
                # Validamos el total que este bien escrito             
                if self.cvacacionesTotal.get().isnumeric():

                    # Si todo esta ok, registramos en el treeview
                    total =int(self.cvacacionesTotal.get())                    

                    valores[9] = int(valores[9]) + total

                    # Ejecutamos la query de grabar dia de apoyo
                    cursor.execute(F'INSERT INTO CVACACIONES (IDAC, FINI, FFIN, DTOT) VALUES ({id}, "{self.cvacacionesInicial.get()}", "{self.cvacacionesFinal.get()}",  {total})')

                    idRegistro = cursor.execute(F'SELECT ID FROM CVACACIONES ORDER BY ID DESC').fetchone()
                    self.cvacaciones.insert('', END,text=idRegistro[0], values=(self.cvacacionesInicial.get(), self.cvacacionesFinal.get(), total))

                    self.cvacacionesInicial.configure(state='normal')
                    self.cvacacionesFinal.configure(state='normal')
                    self.cvacacionesInicial.delete(0, END)
                    self.cvacacionesFinal.delete(0, END)
                    self.cvacacionesTotal.delete(0, END)
                    self.cvacacionesInicial.configure(state='readonly')
                    self.cvacacionesFinal.configure(state='readonly')

                # Si esta mal la validacion del total enviamos el foco al cuadro               
                else:
                    self.cvacacionesTotal.focus_set()
                    messagebox.showinfo('COMPRA DE VACACIONES', 'Registra correctamente el total de dias de la compra de vacaciones !', icon = 'warning')

        # Grabamos cambios en base de datos y cerramos conexion
        conexion.commit()
        conexion.close()

        self.tre2.item(self.tre2.focus(), values=valores)
 
    def Menu2DetallesEliminar(self):

        valores = self.tre2.item(self.tre2.focus())['values'] 

        # Crear conexion a base de datos
        conexion = sqlite3.connect('PlaniPRO.db')    
        cursor = conexion.cursor()    
                
        if self.apoyo.selection():
            
            valores[2] = int(valores[2]) - 1            

            # Obtener id de trabajador
            id = int(self.apoyo.item(self.apoyo.focus())['text'] )                
            
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM APOYO WHERE ID = {id}')
            
            # Grabamos cambios en base de datos y cerramos conexion     
            self.apoyo.delete(self.apoyo.focus())          
  
        if self.falta.selection():
            
            valores[3] = int(valores[3]) - 1            

            # Obtener id de trabajador
            id = int(self.falta.item(self.falta.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM FALTA WHERE ID = {id}')
            
            self.falta.delete(self.falta.focus())      

        if self.feriado.selection():

            valores[4] = int(valores[4]) - 1            

            # Obtener id de trabajador
            id = int(self.feriado.item(self.feriado.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM FERIADO WHERE ID = {id}')
            
            self.feriado.delete(self.feriado.focus())     

        if self.adelanto.selection():
            
            monto = float(self.adelanto.item(self.adelanto.focus())['values'][1])    
            saldo = float(valores[10]) - monto    
            valores[10] = f'{saldo:.2f}'      

            # Obtener id de trabajador
            id = int(self.adelanto.item(self.adelanto.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM ADELANTO WHERE ID = {id}')
            
            self.adelanto.delete(self.adelanto.focus())     
            
        if self.ingreso.selection():

            monto = float(self.ingreso.item(self.ingreso.focus())['values'][1])    
            saldo = float(valores[5]) - monto    
            valores[5] = f'{saldo:.2f}'      

            # Obtener id de trabajador
            id = int(self.ingreso.item(self.ingreso.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM INGRESO WHERE ID = {id}')
            
            self.ingreso.delete(self.ingreso.focus())     

        if self.descuento.selection():

            monto = float(self.descuento.item(self.descuento.focus())['values'][1])    
            saldo = float(valores[6]) - monto    
            valores[6] = f'{saldo:.2f}'      

            # Obtener id de trabajador
            id = int(self.descuento.item(self.descuento.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM DESCUENTO WHERE ID = {id}')
            
            self.descuento.delete(self.descuento.focus())     

        if self.vacaciones.selection():
            
            total = int(self.vacaciones.item(self.vacaciones.focus())['values'][2])    
            dias = int(valores[8]) - total    
            valores[8] = dias     

            # Obtener id de trabajador
            id = int(self.vacaciones.item(self.vacaciones.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM VACACIONES WHERE ID = {id}')
            
            self.vacaciones.delete(self.vacaciones.focus())     

        if self.dmedico.selection():

            total = int(self.dmedico.item(self.dmedico.focus())['values'][3])    
            dias = int(valores[7]) - total    
            valores[7] = dias     

            # Obtener id de trabajador
            id = int(self.dmedico.item(self.dmedico.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM DMEDICO WHERE ID = {id}')
            
            self.dmedico.delete(self.dmedico.focus())       

        if self.cvacaciones.selection():

            total = int(self.cvacaciones.item(self.cvacaciones.focus())['values'][2])    
            dias = int(valores[9]) - total    
            valores[9] = dias     

            # Obtener id de trabajador
            id = int(self.cvacaciones.item(self.cvacaciones.focus())['text'] )
           
            # Ejecutamos la query de grabar dia de apoyo
            cursor.execute(F'DELETE FROM CVACACIONES WHERE ID = {id}')
            
            self.cvacaciones.delete(self.cvacaciones.focus())       


        self.tre2.item(self.tre2.focus(), values=valores)

        conexion.commit()
        conexion.close()

    def Menu2DetallesQuitarSeleccion(self, e):

        # Obtener el widget que activo el evento, esta en orden de creacion
        widget = str(e.widget).split(".")[-1][1:]   

        # Desactivar foco de los demas treeview
        if widget == 'treeview':                
            print(self.apoyo.item(self.apoyo.focus())['text'])
            self.falta.selection_set('')      
            self.feriado.selection_set('')       
            self.adelanto.selection_set('')        
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview2':
            print(self.falta.item(self.falta.focus())['text'])
            self.apoyo.selection_set('')      
            self.feriado.selection_set('')       
            self.adelanto.selection_set('')        
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview3':
            print(self.feriado.item(self.feriado.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.adelanto.selection_set('')        
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview4':
            print(self.adelanto.item(self.adelanto.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview5':
            print(self.ingreso.item(self.ingreso.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview6':
            print(self.descuento.item(self.descuento.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.ingreso.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview7':
            print(self.vacaciones.item(self.vacaciones.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.dmedico.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview8':
            print(self.dmedico.item(self.dmedico.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.cvacaciones.selection_set('')

        elif widget == 'treeview9':
            print(self.cvacaciones.item(self.cvacaciones.focus())['text'])
            self.apoyo.selection_set('')      
            self.falta.selection_set('')       
            self.feriado.selection_set('')        
            self.adelanto.selection_set('')
            self.ingreso.selection_set('')
            self.descuento.selection_set('')
            self.vacaciones.selection_set('')
            self.dmedico.selection_set('')        
          
    def Menu2DetallesSeleccionarFecha(self, boton):

        if boton == 'fivacaciones':
            # Agregar fecha inicial al cuadro de vacaciones
            self.vacacionesInicial.configure(state='normal')
            self.vacacionesInicial.delete(0, END)
            self.vacacionesInicial.insert(0, self.calendario.get_date())
            self.vacacionesInicial.configure(state='readonly')
        elif boton == 'ffvacaciones':
            # Agregar fecha final al cuadro de vacaciones
            self.vacacionesFinal.configure(state='normal')
            self.vacacionesFinal.delete(0, END)
            self.vacacionesFinal.insert(0, self.calendario.get_date())
            self.vacacionesFinal.configure(state='readonly')
        elif boton == 'fidmedico':  
            # Agregar fecha inicial al cuadro de descanso medico
            self.dmedicoInicial.configure(state='normal')
            self.dmedicoInicial.delete(0, END)
            self.dmedicoInicial.insert(0, self.calendario.get_date())
            self.dmedicoInicial.configure(state='readonly')
        elif boton == 'ffdmedico':  
            # Agregar fecha final al cuadro de descanso medico
            self.dmedicoFinal.configure(state='normal')
            self.dmedicoFinal.delete(0, END)
            self.dmedicoFinal.insert(0, self.calendario.get_date())
            self.dmedicoFinal.configure(state='readonly')
        elif boton == 'ficvacaciones':  
            # Agregar fecha inicial al cuadro de compra de vacaciones
            self.cvacacionesInicial.configure(state='normal')
            self.cvacacionesInicial.delete(0, END)
            self.cvacacionesInicial.insert(0, self.calendario.get_date())
            self.cvacacionesInicial.configure(state='readonly')
        elif boton == 'ffcvacaciones':  
            # Agregar fecha final al cuadro de compra de vacaciones
            self.cvacacionesFinal.configure(state='normal')
            self.cvacacionesFinal.delete(0, END)
            self.cvacacionesFinal.insert(0, self.calendario.get_date())
            self.cvacacionesFinal.configure(state='readonly')






if __name__ == '__main__':   
    aplicacion = App()