mensaje_bienvenida = """Calculador de comportamiento P-v-T
para ecuaciones cúbicas de estado de sustancias puras\n
Versión 2.0\n
1. Ecuación de Van der Waals\n
2. Ecuación de Redlich-Kwong\n
3. Ecuación de Soave-Redlich-Kwong\n
4. Ecuación de Peng-Robinson\n"""

mensaje_credits = """Referencia: \n
Introduction to Chemical Engineering Thermodynamics, \n
by J.M. Smith, H.C. Van Ness, M.M. Abott\n

Elaborado por: Horacio Enrique Barrios Osorio, Ing. Químico graduado de la UNAH\n
GitHub:https://github.com/horaciobarrios96\n
"""

from sympy import *
#Esta librería nos permitirá resolver la ecuación cúbica dependiendo la variable a calcular (P, v o T)
#Documentación útil: https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html


print(mensaje_bienvenida)
print(mensaje_credits)

#Se crearon funciones para las 4 ecuaciones de estado cúbicas
