mi_numero = 1 + 3
print(mi_numero + mi_numero)
# 'type()' permite saber el tipo de dato de una variable
print(type(mi_numero))
print("\n")

mi_numero2 = 5.8
print(mi_numero2)
print(type(mi_numero2))
mi_numero2 = mi_numero2 + mi_numero2
print(mi_numero2)
print("\n")

mi_numero3 = 5 + 5.8
print(mi_numero3)
print(type(mi_numero3))

num1 = 7.5
num2 = 2.5
res = num1 + num2
print(res)
print(type(res))
# Aunque la suma de numeros decimales de un entero como resultado, el tipo de la variable
# se mantiene como un float

edad = input("Ingresa tu edad: ")
print("Tu edad es: " + edad)
print(type(edad))
# TODO lo ingresado por el usuario es tomado como un STRING
# Si ingresa un número, no se puede sumar directamente con otro
