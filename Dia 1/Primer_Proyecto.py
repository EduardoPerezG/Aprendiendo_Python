print("Hola mundo")

# Impresión de comillas "" ó ''
print("Hola 'Mundo'")
print('Hola "Mundo"')

# Impresión de un número
print(100)

# Impresión de un resultado numérico (sin mostrar la operación)
print(50 + 50)

# Impresión de strings y caracteres especiales
print("Me llamo \"Eduardo\"")
print("Esta es una linea\nY esta es otra linea")
print("\tEste es un tabulador")
print('This isn\'t a number')
print('Este signo "/" es una barra invertida\n\n')

# Solamente pide una entrada sin almacenar la info ingresada
input("Ingresa tu nombre: ")

# Ejecuta de adentro hacia afuera. Primero hace el 'input' con su texto correspondiente y después el 'print' de la
# info ingresada
print(input("Ingresa tu nombre: "))

# Ejecuta de adentro hacia afuera y de  izquierda a derecha (primero el 'input' de la izquierda, luego el de la
# 'derecha' y al final el 'print') Se concatena el texto
print("Tu nombre es: " + input("Ingresa tu nombre: "))
print("Tu nombre completo es: " + (input("Ingresa tu nombre: ")) + " " + (input("Ingresa tu apellido: ")))
