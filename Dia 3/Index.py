mi_texto = "Esta es una prueba"
# Los corchetes junto a una variable que contenga un STRING ayudan a indicar
# que caracter hay en la posicion indicada
# Python puede contar los indices de izquierda a derecha 0 1 2 3 4 ...
# pero tambien puede contarlos de derecha a izquierda con el siguiente formato:  0 ... -4 -3 -2 -1
resultado = mi_texto[0]
print(resultado)
resultado = mi_texto[-1]
print(resultado)

# El metodo 'index' permite buscar en que indice esta un cierto caracter de un string de izquierda a derecha
resultado = mi_texto.index("n")
print(resultado)
# Si se busca una palabra, solamente indica en que indice comienza esa palabra
resultado = mi_texto.index("prueba")
print(resultado)
# Si se busca una letra o palabra que aparezca varias veces, solamente muestra el indice e la primera que encuentre
resultado = mi_texto.index("a")
print(resultado)
# Se puede indicar a partir de cual indice se quiere buscar un caracter/ palabra agregando un segundo parametro:
# index("palabra_o_caracter", indice_inicial)
resultado = mi_texto.index("a", 5)
print(resultado)
# Se puede indicar a partirde cual y hasta cual indice se desea buscar un carater/palabra agregando un tercer parametro:
# Se puede indicar a parti de cual indice se quiere buscar un caracter o palabra:
# index("palabra_o_caracter", indice_inicial)
resultado = mi_texto.index("a", 2, 10)
print(resultado)
# El metodo 'rindex' permite hacer las busquedas pero de derecha a izquierda
resultado = mi_texto.rindex("a")
print(resultado)




