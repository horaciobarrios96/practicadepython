"""Calculador de comportamiento P-v-T 
para ecuaciones cúbicas de estado de sustancias puras
1. Ecuación de Van der Waals
2. Ecuación de Redlich-Kwong
3. Ecuación de Soave-Redlich-Kwong
4. Ecuación de Peng-Robinson"""

def ecuacion_de_estado():
    contador = 1
    while contador == 1:
        texto = """
        Calculadora de ecuaciones de estado cúbicas
        Seleccione una opción para calcular con la EdE:
        1. Van der Waals
        2. Redlich-Kwong
        3. Soave-Redlich-Kwong
        4. Peng-Robinson
        """
        print(texto)
        opcion = input("Ingrese opción válida: ")
        
        match opcion:
            case 1:
                
            case 2:
                
            case 3:
                
            case 4:
                
            case _:
                print("")