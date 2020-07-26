import math
from funcion import Funcion

class primer_orden():
    def __init__(self,funcion,x,y,h):
        self.funcion=funcion
        self.x=x
        self.y=y
        self.h=h
        self.k_1=None

    def k1(self):
        instancia=Funcion(self.funcion,self.x,self.y)
        self.k_1=instancia.generar_funcion()
        return self.k_1

class segundo_orden():
    def __init__(self,funcion,x,y,h):
        self.funcion=funcion
        self.x=x
        self.y=y
        self.h=h
        self.k_1=None
        self.k_2=None

    def k1(self):
        instancia=Funcion(self.funcion,self.x,self.y)
        self.k_1=instancia.generar_funcion()
        return self.k_1

    def k2(self):
        x=self.x+self.h
        y=self.y+self.h*self.k_1
        instancia=Funcion(self.funcion,x,y)
        self.k_2=instancia.generar_funcion()
        return self.k_2

    def k(self):
        k=1/2*(self.k_1+self.k_2)
        return k 

class tercer_orden():
    def __init__(self,funcion,x,y,h):
        self.funcion=funcion
        self.x=x
        self.y=y
        self.h=h
        self.k_1=None
        self.k_2=None
        self.k_3=None    

    def k1(self):
        instancia=Funcion(self.funcion,self.x,self.y)
        self.k_1=instancia.generar_funcion()
        return self.k_1

    def k2(self):
        x=self.x+1/2*self.h
        y=self.y+1/2*self.h*self.k_1
        instancia=Funcion(self.funcion,x,y)
        self.k_2=instancia.generar_funcion()
        return self.k_2

    def k3(self):
        x=self.x+self.h
        y=self.y-self.h*self.k_1+2*self.h*self.k_2
        instancia=Funcion(self.funcion,x,y)
        self.k_3=instancia.generar_funcion()       
        return self.k_3

    def k(self):
        k=1/6*(self.k_1+4*self.k_2+self.k_3)
        return k 

class cuarto_orden():
    def __init__(self,funcion,x,y,h):
        self.funcion=funcion
        self.x=x
        self.y=y
        self.h=h
        self.k_1=None
        self.k_2=None
        self.k_3=None
        self.k_4=None

    def k1(self):
        instancia=Funcion(self.funcion,self.x,self.y)
        self.k_1=instancia.generar_funcion()
        return self.k_1

    def k2(self):
        x=self.x+self.h/2
        y=self.y+self.h/2*self.k_1
        instancia=Funcion(self.funcion,x,y)
        self.k_2=instancia.generar_funcion()
        return self.k_2

    def k3(self):
        x=self.x+self.h/2
        y=self.y+self.h/2*self.k_2
        instancia=Funcion(self.funcion,x,y)
        self.k_3=instancia.generar_funcion()       
        return self.k_3

    def k4(self):
        x=self.x+self.h
        y=self.y+self.h*self.k_3
        instancia=Funcion(self.funcion,x,y)
        self.k_4=instancia.generar_funcion()
        return self.k_4

    def k(self):
        k=1/6*(self.k_1+2*self.k_2+2*self.k_3+self.k_4)
        return k  

# instancia=cuarto_orden('-2*y+4*e**-x',0,2,0.2)
# instancia.k1()
# instancia.k2()
# instancia.k3()
# instancia.k4()
# instancia.k()

