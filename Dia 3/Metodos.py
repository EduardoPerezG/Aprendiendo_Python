texto = "Este es el texto de Eduardo"
resultado = texto
print(resultado)

# El metodo 'upper' permite cambiar las letras de un string a mayusculas
resultado = texto.upper()
print(resultado)
# Se puede aplicar especificamente a algun indice o fragmento
# Solo se imprime el indice indicado
resultado = texto[2].upper()
print(resultado)

# El metodo 'lower' permite cambiar las letras de un string a minusculas
resultado = texto.lower()
print(resultado)

# El metodo 'split' permite separar las palabras de un string y las guarda en una lista
# Por defecto, se toma como separador los espacios del string
resultado = texto.split()
print(resultado)
# Si al metodo 'split' se le pasa un parametro, dicho parametro se toma como separador.
# El caracter/caracteres que sean el separador nuevo ya NO se incluyen en la lista que se genere
# split("separador_nuevo")
resultado = texto.split("t")
print(resultado)

# El metodo 'join' permite unir ELEMENTOS DE UNA LISTA con algun caracter/caracteres que se indique
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)
f = "_".join([a, b, c, d])
print(f)

# El metodo 'find' funciona igual al metodo 'index'
# La unica diferencia con 'index' es que 'find' no arroja error si no encuentra el caracter
resultado = texto.find("e")
print(resultado)

# El metodo 'replace' permite remplazar caracteres o fragmentos de un string indicando dos parametros:
# find("caracter_o_texto_a_remplazar", "caarcter_o_texto_nuevo")
resultado = texto.replace("Eduardo", "todos")
print(resultado)
resultado = texto.replace("de Eduardo", "")
print(resultado)
resultado = texto.replace("e", "x")
print(resultado)
