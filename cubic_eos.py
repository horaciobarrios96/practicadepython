mensaje_bienvenida = """Calculador de comportamiento P-v-T\n
con ecuaciones cúbicas de estado de sustancias puras\n
Versión 2.0\n
1. Ecuación de Van der Waals\n
2. Ecuación de Redlich-Kwong\n
3. Ecuación de Soave-Redlich-Kwong\n
4. Ecuación de Peng-Robinson\n"""

mensaje_credits = """Referencia: \n
Introduction to Chemical Engineering Thermodynamics, \n
by J.M. Smith, H.C. Van Ness, M.M. Abott 7th Ed.\n

Elaborado por: Horacio Enrique Barrios Osorio, Ing. Químico graduado de la UNAH\n
GitHub:https://github.com/horaciobarrios96\n
"""

from sympy import *
#Esta librería nos permitirá resolver la ecuación cúbica dependiendo la variable a calcular (P, v o T)
#Documentación útil: https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html


print(mensaje_bienvenida)
print(mensaje_credits)

#Se creó una función que recibe las propiedades críticas de la sustancia
#Devuelve el resultado como una lista
def punto_critico():
    T_crit = float(input("Ingrese temperatura crítica de sustancia: \n"))
    P_crit = float(input("Ingrese presión crítica de sustancia: \n"))
    acen_fact = float(input("Ingrese factor acéntrico de sustancia: \n"))
    propiedades = [T_crit, P_crit, acen_fact]
    return propiedades
    
#Mensaje que le dice al usuario que cálculo desea efectuar
#Se registrará la elección del usuario para hacer el cálculo correspondiente
mensaje_eleccion = """
        ¿Qué variable desea calcular?\n
        1. Presión\n
        2. Volumen\n
        3. Temperatura\n
        Ingrese una opción válida\n
        """
#Se registra la elección, este parámetro será una entrada para las funciones de las EOS
#En las funciones de las EOS se utilizarán sentencias if-else para diferenciar los valores de "elección"
eleccion = int(input(mensaje_eleccion))

#Se le permitirá al usuario ingresar el valor de la constante universal de los gases deseado
R = float(input("Ingrese un valor válido de la constante universal de los gases:\n"))

#Se crearán funciones para las 4 ecuaciones de estado cúbicas
def vanderwaals(eleccion,R):
    propiedades = punto_critico()
    a = (27/64)*R**2*propiedades[0]**2/propiedades[1]
    b = (1/8)*R*propiedades[0]/propiedades[1]
    if eleccion == 1:
        vol = float(input("Ingrese V: \n"))
        temp = float(input("Ingrese T: \n"))
        P = symbols('P')
        init_printing(use_unicode=true )
        P = solveset(Eq(P,(R*temp)/(vol - b) - a/vol**2),P)
        solucion = print(f"P = {P}\n")
        return solucion    
    elif eleccion == 2:
        pres = float(input("Ingrese P: \n"))
        temp = float(input("Ingrese T: \n"))
        V = symbols('V')
        init_printing(use_unicode=true )
        V = solveset(Eq(pres,(R*temp)/(vol - b) - a/vol**2),V)
        solucion = print(f"V = {V}\n")
        return solucion 
    elif eleccion == 3:
        pres = float(input("Ingrese P: \n"))
        vol = float(input("Ingrese V: \n"))
        T = symbols('T')
        init_printing(use_unicode=true )
        T = solveset(Eq(pres,(R*T)/(vol - b) - a/vol**2),T)
        solucion = print(f"T = {T}\n")
        return solucion
    else:
        print("Opción no válida\n")
        return

vanderwaals(eleccion,R)