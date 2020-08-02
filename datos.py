from ordenes import primer_orden,segundo_orden,tercer_orden,cuarto_orden
from terminaltables import AsciiTable
from pylab import *

class Datos():
    def __init__(self,funcion,x1,x2,y,h):
        self.funcion=funcion
        self.x1=x1
        self.x2=x2
        self.y=y
        self.h=h
        self.lista=[]
        self.iteracion=((self.x2-self.x1)/self.h)+1
        self.lista_x=[]
        self.lista_y=[]

    def interfaz_datos_primer_orden(self):
        self.lista=['X','Y','K1']
        for i in range(int(self.iteracion)):
            self.lista.append(self.x1)
            self.lista_x.append(self.x1)
            self.lista.append(self.y)
            self.lista_y.append(self.y)          
            instancia=primer_orden(self.funcion,self.x1,self.y,self.h)    
            k=instancia.k1()    
            self.lista.append(instancia.k1())
            self.x1=self.x1+self.h
            self.y=self.y+self.h*k
        self.lista=[self.lista[i:i+3] for i in range(0,len(self.lista),3)]
        table = AsciiTable(self.lista)
        print(table.table)
        plot(self.lista_x,self.lista_y,'o')
        show()

    def interfaz_datos_segundo_orden(self):
        self.lista=['X','Y','K1','K2','K']
        for i in range(int(self.iteracion)):
            self.lista.append(self.x1)
            self.lista.append(self.y)          
            instancia=segundo_orden(self.funcion,self.x1,self.y,self.h)    
            instancia.k1()
            self.lista.append(instancia.k1())
            instancia.k2()
            self.lista.append(instancia.k2())
            k=instancia.k()
            self.lista.append(instancia.k())
            self.x1=self.x1+self.h
            self.y=self.y+self.h*k
        self.lista=[self.lista[i:i+5] for i in range(0,len(self.lista),5)]
        table = AsciiTable(self.lista)
        print(table.table)

    def interfaz_datos_tercer_orden(self):
        self.lista=['X','Y','K1','K2','K3','K']
        for i in range(int(self.iteracion)):
            self.lista.append(self.x1)
            self.lista.append(self.y)
            instancia=tercer_orden(self.funcion,self.x1,self.y,self.h)    
            instancia.k1()
            self.lista.append(instancia.k1())
            instancia.k2()
            self.lista.append(instancia.k2())
            instancia.k3()
            self.lista.append(instancia.k3())
            k=instancia.k()
            self.lista.append(instancia.k())
            self.x1=self.x1+self.h
            self.y=self.y+self.h*k
        self.lista=[self.lista[i:i+6] for i in range(0,len(self.lista),6)]
        table = AsciiTable(self.lista)
        print(table.table)

    def interfaz_datos_cuarto_orden(self):
        self.lista=['X','Y','K1','K2','K3','K4','K']
        for i in range(int(self.iteracion)):
            self.lista.append(self.x1)
            self.lista.append(self.y)
            instancia=cuarto_orden(self.funcion,self.x1,self.y,self.h)    
            instancia.k1()
            self.lista.append(instancia.k1())
            instancia.k2()
            self.lista.append(instancia.k2())
            instancia.k3()
            self.lista.append(instancia.k3())
            instancia.k4()
            self.lista.append(instancia.k4())
            k=instancia.k()
            self.lista.append(instancia.k())
            self.x1=self.x1+self.h
            self.y=self.y+self.h*k
        self.lista=[self.lista[i:i+7] for i in range(0,len(self.lista),7)]
        table = AsciiTable(self.lista)
        print(table.table)

instancia=Datos('-2*y+4*e**-x',0,1,2,0.2)
instancia.interfaz_datos_primer_orden()