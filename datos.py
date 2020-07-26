from ordenes import primer_orden,segundo_orden,tercer_orden,cuarto_orden
from terminaltables import AsciiTable

class Datos():
    def __init__(self,funcion,x1,x2,y,h):
        self.funcion=funcion
        self.x1=x1
        self.x2=x2
        self.y=y
        self.h=h
        self.lista1=['X','Y','K1']
        self.lista2=['X','Y','K1','K2','K']
        self.lista3=['X','Y','K1','K2','K3','K']
        self.lista4=['X','Y','K1','K2','K3','K4','K']

    def interfaz_datos_primer_orden(self):
        iteracion=((self.x2-self.x1)/self.h)+1
        for i in range(int(iteracion)):
            self.lista1.append(self.x1)
            self.lista1.append(self.y)          
            instancia=primer_orden(self.funcion,self.x1,self.y,self.h)    
            k=instancia.k1()    
            self.lista1.append(instancia.k1())
            self.x1=self.x1+self.h
            self.y=self.y+self.h*k
        self.lista1=[self.lista1[i:i+3] for i in range(0,len(self.lista1),3)]
        table = AsciiTable(self.lista1)
        print(table.table)

    def interfaz_datos_segundo_orden(self):
        iteracion=((self.x2-self.x1)/self.h)+1
        for i in range(int(iteracion)):
            self.lista1.append(self.x1)
            self.lista1.append(self.y)          
            instancia=segundo_orden(self.funcion,self.x1,self.y,self.h)    
            instancia.k1()
            self.lista2.append(instancia.k1())
            instancia.k2()
            self.lista2.append(instancia.k2())
            k=instancia.k()
            self.lista2.append(instancia.k())
            self.x1=self.x1+self.h
            self.y=self.y+self.h*k
        self.lista2=[self.lista2[i:i+5] for i in range(0,len(self.lista2),5)]
        table = AsciiTable(self.lista2)
        print(table.table)

    def interfaz_datos_tercer_orden(self):
        iteracion=((self.x2-self.x1)/self.h)+1
        for i in range(int(iteracion)):
            self.lista3.append(self.x1)
            self.lista3.append(self.y)
            instancia=tercer_orden(self.funcion,self.x1,self.y,self.h)    
            instancia.k1()
            self.lista3.append(instancia.k1())
            instancia.k2()
            self.lista3.append(instancia.k2())
            instancia.k3()
            self.lista3.append(instancia.k3())
            k=instancia.k()
            self.lista3.append(instancia.k())
            self.x1=self.x1+self.h
            self.y=self.y+self.h*k
        self.lista3=[self.lista3[i:i+6] for i in range(0,len(self.lista3),6)]
        table = AsciiTable(self.lista3)
        print(table.table)

    def interfaz_datos_cuarto_orden(self):
        iteracion=((self.x2-self.x1)/self.h)+1
        for i in range(int(iteracion)):
            self.lista4.append(self.x1)
            self.lista4.append(self.y)
            instancia=cuarto_orden(self.funcion,self.x1,self.y,self.h)    
            instancia.k1()
            self.lista4.append(instancia.k1())
            instancia.k2()
            self.lista4.append(instancia.k2())
            instancia.k3()
            self.lista4.append(instancia.k3())
            instancia.k4()
            self.lista4.append(instancia.k4())
            k=instancia.k()
            self.lista4.append(instancia.k())
            self.x1=self.x1+self.h
            self.y=self.y+self.h*k
        self.lista4=[self.lista4[i:i+7] for i in range(0,len(self.lista4),7)]
        table = AsciiTable(self.lista4)
        print(table.table)

# instancia=Datos('-2*y+4*e**-x',0,1,2,0.2)
# instancia.interfaz_datos_tercer_orden()