import math

class Funcion():
    def __init__(self,funcion,x,y):
        self.funcion=funcion
        self.x=x
        self.y=y
        self.lista=[]

    def lista_funcion(self):
        for i in self.funcion:
            self.lista.append(i) 
    
    def reemplazar_valores_lista(self):
        for n, i in enumerate(self.lista):
            if i == 'x':
                self.lista[n] = str(self.x)
            if i == 'y':
                self.lista[n] = str(self.y)
    
    def calcular_expresiones_lista(self):
        for n, i in enumerate(self.lista):        
            if i == 'p':
                self.lista.pop(n+1)
                self.lista[n] = 'math.pi'
        StrA = "".join(self.lista)
        print(StrA)




# funcion='3*x+5*y+pi'
# instancia=Funcion(funcion,9,4)
# instancia.lista_funcion()
# instancia.reemplazar_valores_lista()
# instancia.calcular_expresiones_lista()
