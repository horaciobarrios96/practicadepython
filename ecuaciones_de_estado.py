"""Calculador de comportamiento P-v-T 
para ecuaciones cúbicas de estado de sustancias puras
1. Ecuación de Van der Waals
2. Ecuación de Redlich-Kwong
3. Ecuación de Soave-Redlich-Kwong
4. Ecuación de Peng-Robinson"""

"""Referencia: 
Introduction to Chemical Engineering Thermodynamics, 
by J.M. Smith, H.C. Van Ness, M.M. Abott"""
       
import sympy 
from sympy import *

#Esta librería nos permitirá resolver la ecuación cúbica dependiendo la variable a calcular (P, v o T)
#Documentación útil: https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html

def ecuacion_de_estado():
    
    texto = """
        Calculadora de ecuaciones de estado cúbicas\n
        Ecuaciones disponibles:\n
        1. Van der Waals\n
        2. Redlich-Kwong\n
        3. Soave-Redlich-Kwong\n
        4. Peng-Robinson\n
        """
    print(texto) #Mensaje de bienvenida a la función

    R = 8.314 #J/mol-K, constante universal de los gases
    print(f"Constante universal de gases utilizada para cálculos: {R} J/mol-K" ) #Da al usuario la constante R
    print("Ingrese propiedades termodinámicas de la sustancia\n")
    
    comprobante = 1 #Variable que comprueba que los datos ingresados son válidos
    #Tc y Pc no pueden ser negativos, omega es negativo para algunas sustancias
    while comprobante == 1:
        #Ingreso de propiedades de la sustancia
        Tc = float(input("Ingrese Tc de la sustancia en K:\n")) #Tc y Pc se ingresan en unidades acorde a la constante R
        Pc = float(input("Ingrese Pc de la sustancia en Pa:\n"))
        omega = float(input("Ingrese factor acéntrico de la sustancias:\n"))
        
        if Tc < 0: #Comprobación Tc no negativa
            print("Tc inválida, no existen Temperaturas absolutas negativas\n")
            comprobante = 1
        elif Pc < 0: #Comprobación Pc no negativa
            print("Pc inválida, no existen presiones negativas\n")
            comprobante = 1
        else:
            comprobante = 0 #cambio de valor de variable, permite continuar a las siguientes instrucciones
            #Alternativa: utilizar la sentencia 'break' en vez de 'comprobante = 0'
            
    contador = 1 #Se inicializa variable contador que registra el número de cálculos realizados
    while contador == 1:
        #Lectura de opciones, se evaluará en 4 casos, uno por cada ecuación de estado cúbica
        
        mensaje_eleccion = """
        ¿Qué variable desea calcular?\n
        1. Presión (Pa)\n
        2. Volumen (m^3/mol)\n
        3. Temperatura (K)\n
        """
        #Mensaje que le dice al usuario que cálculo desea efectuar
        #Se registrará la elección del usuario para hacer el cálculo correspondiente
        print(mensaje_eleccion)
        opcion = int(input("Ingrese opción válida: \n"))
        
        #Primero, se analiza que opción ingresó el usuario
        match opcion:
            
            case 1: #Ecuación de Van der Waals
                print("Ecuación de van der Waals seleccionada\n")
                eleccion = int(input(mensaje_eleccion))
                a = (27/64)*R**2*Tc**2/Pc
                b = (1/8)*R*Tc/Pc
                if eleccion == 1:
                    vol = float(input("Ingrese V [m^3/mol]: \n"))
                    temp = float(input("Ingrese T [K]: \n"))
                    P = symbols('P')
                    init_printing(use_unicode=true )
                    P = solveset(Eq(P,(R*temp)/(vol - b) - a/vol**2),P)
                    solucion = print(f"P = {P} Pa\n")
                    break
                    return solucion
                elif eleccion == 2:
                    pres = float(input("Ingrese P [Pa]: \n"))
                    temp = float(input("Ingrese T [K]: \n"))
                    V = symbols('V')
                    init_printing(use_unicode=true )
                    V = solveset(Eq(pres,(R*temp)/(V - b) - a/V**2),V)
                    solucion = print(f"V = {V} m^3/mol\n")
                    break
                    return solucion    
                elif eleccion == 3:
                    pres = float(input("Ingrese P [Pa]: \n"))
                    vol = float(input("Ingrese V [m^3/mol]: \n"))
                    T = symbols('T')
                    init_printing(use_unicode=true )
                    T = solveset(Eq(pres,(R*T)/(vol - b) - a/vol**2),T)
                    solucion = print(f"T = {T} K\n")
                    break
                    return solucion                                 
                else:
                    solucion = print("Opción no válida")
                    contador = 1
                    return solucion
                
                
            case 2: #Ecuación de Redlich-Kwong
                print("Ecuación de Redlich-Kwong seleccionada\n")
                
                eleccion = int(input(mensaje_eleccion))
                if eleccion == 1:
                    vol = float(input("Ingrese V [m^3/mol]: \n"))
                    temp = float(input("Ingrese T [K]: \n"))
                    a = 0.42748*((temp/Tc)**-0.5)*R**2*Tc**2/Pc
                    b = 0.08664*R*Tc/Pc
                    P = symbols('P')
                    init_printing(use_unicode=true )
                    P = solveset(Eq(P,(R*temp)/(vol - b) - a/(vol*(vol + b))),P)
                    solucion = print(f"P = {P} Pa\n")
                    break
                    return solucion
                elif eleccion == 2:
                    pres = float(input("Ingrese P [Pa]: \n"))
                    temp = float(input("Ingrese T [K]: \n"))
                    a = 0.42748*((temp/Tc)**-0.5)*R**2*Tc**2/Pc
                    b = 0.08664*R*Tc/Pc
                    V = symbols('V')
                    init_printing(use_unicode=true )
                    V = solveset(Eq(pres,(R*temp)/(V - b) - a/(V*(V + b))),V)
                    solucion = print(f"V = {V} m^3/mol\n")
                    break
                    return solucion    
                elif eleccion == 3:
                    pres = float(input("Ingrese P [Pa]: \n"))
                    vol = float(input("Ingrese V [m^3/mol]: \n"))
                    T = symbols('T')
                    a = 0.42748*((T/Tc)**-0.5)*R**2*Tc**2/Pc
                    b = 0.08664*R*Tc/Pc
                    init_printing(use_unicode=true )
                    T = solveset(Eq(pres,(R*T)/(vol - b) - a/(vol*(vol + b))),T)
                    solucion = print(f"T = {T} K\n")
                    break
                    return solucion                                 
                else:
                    solucion = print("Opción no válida")
                    contador = 1
                    return solucion               
                
                
            case 3: #Ecuación de Soave-Redlich-Kwong
                print("Ecuación de Soave-Redlich-Kwong seleccionada\n")

                eleccion = int(input(mensaje_eleccion))
                if eleccion == 1:
                    vol = float(input("Ingrese V [m^3/mol]: \n"))
                    temp = float(input("Ingrese T [K]: \n"))
                    alfa = (1+(0.480+1.574*omega-0.176*omega**2)*(1-(temp/Tc)**0.5))**2
                    a = 0.42748*alfa*R**2*Tc**2/Pc
                    b = 0.08664*R*Tc/Pc
                    P = symbols('P')
                    init_printing(use_unicode=true )
                    P = solveset(Eq(P,(R*temp)/(vol - b) - a/(vol*(vol + b))),P)
                    solucion = print(f"P = {P} Pa\n")
                    break
                    return solucion
                elif eleccion == 2:
                    pres = float(input("Ingrese P [Pa]: \n"))
                    temp = float(input("Ingrese T [K]: \n"))
                    alfa = (1+(0.480+1.574*omega-0.176*omega**2)*(1-(temp/Tc)**0.5))**2
                    a = 0.42748*alfa*R**2*Tc**2/Pc
                    b = 0.08664*R*Tc/Pc
                    V = symbols('V')
                    init_printing(use_unicode=true )
                    V = solveset(Eq(pres,(R*temp)/(V - b) - a/(V*(V + b))),V)
                    solucion = print(f"V = {V} m^3/mol\n")
                    break
                    return solucion    
                elif eleccion == 3:
                    pres = float(input("Ingrese P [Pa]: \n"))
                    vol = float(input("Ingrese V [m^3/mol]: \n"))
                    T = symbols('T')
                    alfa = (1+(0.480+1.574*omega-0.176*omega**2)*(1-(T/Tc)**0.5))**2
                    a = 0.42748*alfa*R**2*Tc**2/Pc
                    b = 0.08664*R*Tc/Pc
                    init_printing(use_unicode=true )
                    T = solveset(Eq(pres,(R*T)/(vol - b) - a/vol**2),T)
                    solucion = print(f"T = {T} K\n")
                    break
                    return solucion                                 
                else:
                    solucion = print("Opción no válida")
                    contador = 1
                    return solucion               


                
            case 4: #Ecuación de Peng-Robinson
                print("Ecuación de Peng-Robinson seleccionada\n")

                eps = 1 - 2**0.5
                sig = 1 + 2**0.5
                print("Ecuación de Soave-Redlich-Kwong seleccionada\n")

                eleccion = int(input(mensaje_eleccion))
                if eleccion == 1:
                    vol = float(input("Ingrese V [m^3/mol]: \n"))
                    temp = float(input("Ingrese T [K]: \n"))
                    alfa = (1+(0.37464+1.5422*omega-0.26992*omega**2)*(1-(temp/Tc)**0.5))**2
                    a = 0.45724*alfa*R**2*Tc**2/Pc
                    b = 0.07780*R*Tc/Pc
                    P = symbols('P')
                    init_printing(use_unicode=true )
                    P = solveset(Eq(P,(R*temp)/(vol - eps*b) - a/((vol + eps*b)*(vol + sig*b))),P)
                    solucion = print(f"P = {P} Pa\n")
                    break
                    return solucion
                elif eleccion == 2:
                    pres = float(input("Ingrese P [Pa]: \n"))
                    temp = float(input("Ingrese T [K]: \n"))
                    alfa = (1+(0.37464+1.5422*omega-0.26992*omega**2)*(1-(temp/Tc)**0.5))**2
                    a = 0.45724*alfa*R**2*Tc**2/Pc
                    b = 0.07780*R*Tc/Pc
                    V = symbols('V')
                    init_printing(use_unicode=true )
                    V = solveset(Eq(pres,(R*temp)/(V - eps*b) - a/((V + eps*b)*(V + sig*b))),V)
                    solucion = print(f"V = {V} m^3/mol\n")
                    break
                    return solucion    
                elif eleccion == 3:
                    pres = float(input("Ingrese P [Pa]: \n"))
                    vol = float(input("Ingrese V [m^3/mol]: \n"))
                    T = symbols('T')
                    alfa = (1+(0.37464+1.5422*omega-0.26992*omega**2)*(1-(T/Tc)**0.5))**2
                    a = 0.45724*alfa*R**2*Tc**2/Pc
                    b = 0.07780*R*Tc/Pc
                    init_printing(use_unicode=true )
                    T = solveset(Eq(pres,(R*T)/(vol - eps*b) - a/((vol + eps*b)*(vol + sig*b))),T)
                    solucion = print(f"T = {T} K\n")
                    break
                    return solucion                                 
                else:
                    solucion = print("Opción no válida")
                    contador = 1
                    return solucion   

                
            case _:
                print("Entrada inválida, intente de nuevo\n")
                contador = 1
                return 0

                

ecuacion_de_estado()