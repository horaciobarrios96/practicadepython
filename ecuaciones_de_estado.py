"""Calculador de comportamiento P-v-T 
para ecuaciones cúbicas de estado de sustancias puras
1. Ecuación de Van der Waals
2. Ecuación de Redlich-Kwong
3. Ecuación de Soave-Redlich-Kwong
4. Ecuación de Peng-Robinson"""

"""Referencia: 
Introduction to Chemical Engineering Thermodynamics, 
by J.M. Smith, H.C. Van Ness, M.M. Abott"""

texto = """
        Calculadora de ecuaciones de estado cúbicas\n
        Ecuaciones disponibles:\n
        1. Van der Waals\n
        2. Redlich-Kwong\n
        3. Soave-Redlich-Kwong\n
        4. Peng-Robinson\n
        """
print(texto)

R = 8.314 #J/mol-K
print("Constante universal de gases utilizada para cálculos: " + R + " J/mol-K \n" )

print("Ingrese propiedades termodinámicas de la sustancia\n")
while comprobante == 1:
    Tc = input("Ingrese Tc de la sustancia en K:\n")
    Pc = input("Ingrese Pc de la sustancia en Pa:\n")
    omega = input("Ingrese factor acéntrico de la sustancias:\n")
    if Tc < 0:
        print("Tc inválida, no existen Temperaturas absolutas negativas\n")
        comprobante = 1
    elif Pc < 0:
        print("Tc inválida, no existen presiones negativas\n")
        comprobante = 1
    else:
        comprobante = 0
        
        

def ecuacion_de_estado():
    contador = 1
    while contador == 1:
        
        opcion = input("Ingrese opción válida: \n")
        
        match opcion:
            case 1:
                print("Ecuación de van der Waals seleccionada\n")
                
                
            case 2:
                print("Ecuación de Redlich-Kwong seleccionada\n")
                
                
            case 3:
                print("Ecuación de Soave-Redlich-Kwong seleccionada\n")
                
            case 4:
                print("Ecuación de Peng-Robinson seleccionada\n")
                
            case _:
                print("Entrada inválida, intente de nuevo\n")
                
                
ecuacion_de_estado()