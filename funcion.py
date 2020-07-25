from sympy import *
import math

class Funcion():
    def __init__(self,funcion,x,y):
        self.funcion=funcion
        self.x=x
        self.y=y

    def obtener_funcion(self): 
        self.funcion=sympify(self.funcion)

    def reemplazar_valores(self):
        x, y = symbols('x y') 
        self.funcion = self.funcion.subs([(x, self.x), (y, self.y)])
    
    def reemplazar_valores_trigonometria(self):
        pin, e = symbols('pin e')
        self.funcion = self.funcion.subs([(pin, math.pi), (e, math.e)])

    def generar_funcion(self):
        self.obtener_funcion()
        self.reemplazar_valores()
        self.reemplazar_valores_trigonometria()
        return self.funcion


# funcion='pin'
# instancia=Funcion(funcion,9,4)
# instancia.generar_funcion()
# instancia.reemplazar_valores()
# instancia.reemplazar_valores_trigonometria()