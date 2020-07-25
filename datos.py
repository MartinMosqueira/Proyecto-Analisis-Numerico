from ordenes import cuarto_orden
from terminaltables import AsciiTable

class Datos():
    def __init__(self,funcion,x1,x2,y,h):
        self.funcion=funcion
        self.x1=x1
        self.x2=x2
        self.y=y
        self.h=h
        self.lista=['X','Y','K1','K2','K3','K4','K']

    
    def interfaz_datos(self):
        iteracion=((self.x2-self.x1)/self.h)+1
        for i in range(int(iteracion)):
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


# instancia=Datos('-2*y+4*e**-x',0,1,2,0.2)
# instancia.interfaz_datos()