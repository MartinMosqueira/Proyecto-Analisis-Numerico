import math
from funcion import Funcion

class cuarto_orden():
    def __init__(self,funcion,x,y,h):
        self.funcion=funcion
        self.x=x
        self.y=y
        self.h=h
        self.k=None

    def k1(self):
        instancia=Funcion(self.funcion,self.x,self.y)
        instancia.generar_funcion()
        instancia.reemplazar_valores()
        self.k=instancia.reemplazar_valores_trigonometria()

    def k2(self,h,x,y):
        x=self.x+h/2
        y=self.y+h/2*self.k

        
instancia=cuarto_orden('-2*y+4*e**-x',0,2,0.2)
instancia.k1()

