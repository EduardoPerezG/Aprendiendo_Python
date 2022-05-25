# Proyecto Dia 2
# Programa que permite calcular la comision del 13% de un usuario, desplegado junto con su nombre
nombre = input("Bienvenido/a usuario\nIngresa tu nombre: ")
# Se pide el dato al usuario, se hace el cast a tipo 'float', se redondea a 2 decimales
# y se guarda en la variable 'ventas'
ventas = round(float(input("Ingresa la cantidad de tus ventas ($): ")), 2)
comision = 0.13
resultado = ventas*comision
print(f"\nHola {nombre}, tu comision por tus ventas de ${ventas} es de ${round(resultado, 2)}")
