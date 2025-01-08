"""Calculador de comportamiento P-v-T 
para ecuaciones cúbicas de estado de sustancias puras
1. Ecuación de Van der Waals
2. Ecuación de Redlich-Kwong
3. Ecuación de Soave-Redlich-Kwong
4. Ecuación de Peng-Robinson"""

"""Referencia: 
Introduction to Chemical Engineering Thermodynamics, 
by J.M. Smith, H.C. Van Ness, M.M. Abott"""
       

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
    while contador >= 1:
        #Lectura de opciones, se evaluará en 4 casos, uno por cada ecuación de estado cúbica
        opcion = int(input("Ingrese opción válida: \n"))
        
        match opcion:
            case 1:
                print("Ecuación de van der Waals seleccionada\n")
                #Inicialización de parámetros 'a' y 'b' de la ecuación cúbica de estado
                a = (27/64)*R**2*Tc**2/Pc
                b = (1/8)*R*Tc/Pc
                
                
            case 2:
                print("Ecuación de Redlich-Kwong seleccionada\n")
                #Inicialización de parámetros 'a' y 'b' de la ecuación cúbica de estado
                a = 0.42748*((T/Tc)**-0.5)*R**2*Tc**2/Pc
                b = 0.08664*R*Tc/Pc
                
            case 3:
                print("Ecuación de Soave-Redlich-Kwong seleccionada\n")
                #Inicialización de parámetros 'a' y 'b' de la ecuación cúbica de estado
                alfa = (1+(0.480+1.574*omega-0.176*omega**2)*(1-(T/Tc)**0.5))**2
                a = 0.42748*alfa*R**2*Tc**2/Pc
                b = 0.08664*R*Tc/Pc
                
            case 4:
                print("Ecuación de Peng-Robinson seleccionada\n")
                #Inicialización de parámetros 'a' y 'b' de la ecuación cúbica de estado
                alfa = (1+(0.37464+1.5422*omega-0.26992*omega**2)*(1-(T/Tc)**0.5))**2
                a = 0.45724*alfa*R**2*Tc**2/Pc
                b = 0.07780*R*Tc/Pc
                eps = 1 - 2**0.5
                sig = 1 + 2**0.5
                
            case _:
                print("Entrada inválida, intente de nuevo\n")
                

