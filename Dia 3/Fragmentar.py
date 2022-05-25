# Fragmentar un texto (Slicing) permite extraer un caracter/palabra de un string
texto = "ABCDEFGHIJKLM"
# El primer parametro indica desde donde se inicia el fragmento y el segundo parametro indica hasta donde termina el
# fragmento SIN INCLUIR el caracter de ese indice
fragmento = texto[2:5]
print(fragmento)
# Si se deja vacio el segundo parametro, se indica que se quiere el fragmento desde el indice indicado hasta el final
fragmento = texto[2:]
print(fragmento)
# Si se deja vacio el primer parametro, se indica que se quiere el fragmento desde el comienzo hasta el indice indicado
fragmento = texto[:5]
print(fragmento)
# Si se incluye un tercer parametro, este indica de cuanto en cuanto se haran los saltos de indices que se tomaran para
# el fragmento
fragmento = texto[2:10:2]
print(fragmento)
# Si en el ultimo parametro se ponen numeros negativos, se invierte el string y hace los saltos correspondientes
# Si el valor del tercer parametro es -1, solamente se invierte el string
fragmento = texto[::-1]
print(fragmento)
fragmento = texto[::-2]
print(fragmento)
