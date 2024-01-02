#-*-couding: utf-8-*-
from Entrada import Var_dep

print('''Introducción
         Este es un programa para el cálculo en ejercicios de torsión, el cual funciona con palabras claves que 
         deben ser escritas correctamente para el correcto funcionamiento del programa, así como los datos mínimos necesarios,
         como el radio exterior, la longitud del tramo y/o el radio interior,el torque, el modulo de rigides en caso de ser necesarios.
         Así para el éxito de la solución se requiere un correcto razonamiento que usted como usuario debe hacer.
         
         Consultas y palabaras claves:
         El programa resuelve: deformacion unitaria en un radio dado o el máximo, el esfuerzo en un radio dado o el máximo, el ángulo 
         y la razón de torsión y el torque, así se tienen palabras claves como (respectivamente): 
         
         def_uni
         def_uni_max
         esf_r
         esf_max
         ang_tor
         raz_tor
         torque
         
         Al digitar los valores, asígne 0 si no tiene el valor, no es necesario o es el que desea hallar.
         Los valores decimales se indican con el punto (.).
         Los valores deben ser añadidos en unidades de m, N-m, Pa y radianes, para que el resultado sea 
         dimensinalmente conciso''')

var_Dep=Var_dep()

if var_Dep!=None:
    print(var_Dep)