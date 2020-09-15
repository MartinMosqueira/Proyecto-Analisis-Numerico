import math
from datos import *

print('\n--------metodo de Runge Kutta--------------\n\n')

print('Ingrese la funcion que desea trabajar: \n')
funcion=input('dy/dx = ')
x1=input('x1 = ')
x2=input('x2 = ')
y=input('y = ')
h=input('h = ')
instancia=Datos(funcion,int(x1),int(x2),int(y),float(h))
orden=input('Ingrese el orden del metodo: \n1°\n2°\n3°\n4°\n')
if orden == str(1):
    instancia.interfaz_datos_primer_orden()
elif orden == str(2):
    instancia.interfaz_datos_segundo_orden()
elif orden == str(3):
    instancia.interfaz_datos_tercer_orden()
elif orden == str(4):
    instancia.interfaz_datos_cuarto_orden()
else:
    print('Ups!...algo ocurrio verifique si ingreso correctamente el orden')