x = 6
y = 2
z = 7

print(f"{x} + {y} = {x+y} ")
print(f"{x} - {y} = {x-y} ")
print(f"{x} * {y} = {x*y} ")
print(f"{x} / {y} = {x/y} ")
# Division con redondeo hacia abajo (division al piso) '//'
print(f"{z} dividido al piso entre {2} es igual a {z//2}")
# Modulo de una division
print(f"{z} modulo de {y} es igual a {z%y}")
# Potencia
print(f"{x} elevado a la {y} es igual a {x**y}")
# Raiz cuadrada
print(f"La raiz cuadrada de {x} es {x**0.5}")

# 'round' permite escoger cuantos decimales nos queremos quedar (0 = sin decimales)
valor = round(95.6666666666666666666666)
print(valor)
print(type(valor))

valor = round(95.6666666666666666666666, 3)
print(valor)
print(type(valor))

valor = 95.6666666666666666666666
print(round(valor, 1))
print(type(valor))
print(valor)
