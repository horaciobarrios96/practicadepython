comprobante = 1

while comprobante == 1:
    Tc = float(input("Ingrese Tc de la sustancia en K:\n"))
    Pc = float(input("Ingrese Pc de la sustancia en Pa:\n"))
    omega = float(input("Ingrese factor acéntrico de la sustancias:\n"))
    if Tc < 0:
        print("Tc inválida, no existen Temperaturas absolutas negativas\n")
        comprobante = 1
    elif Pc < 0:
        print("Pc inválida, no existen presiones negativas\n")
        comprobante = 1
    else:
        comprobante = 0