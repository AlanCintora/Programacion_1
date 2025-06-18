""" print("SE HACE INTRODUCCION A LAS MATRICES")

matriX = (
    (1, 2, 3),      #fila 0
    (4, 5, 6),      #fila 1
    (7, 8, 9)       #fila 2
)

matriz2 = (
    [10, 20, 30],      #fila 0
    [40, 50, 60],      #fila 1
    )

print(matriX)

for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        print(matriz2[i][j], end=" ")
    print("")    

#Sí quiero imprimir el elemento 1 de la fila y columna 1 hago:
print(matriz2[1][1])

#Sí quiero modificarlo debo hacer lo siguiente:

matriz2[1][1] = 15

print(matriz2[1][1]) #deberia ser 15 ahora

for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        print(matriz2[i][j], end=" ")
    print("")   


###############################################################
###############################################################
###############################################################
print("A CONTINUACION SE REALIZAN EJECICIOS CON LAS MATRICES \
      SE HACEN OPERACIONES")

# Ejercicio 1: Crear una matriz de 3x3 con valores fijos y mostrarla

# Creamos una matriz de 3 filas y 3 columnas con valores definidos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostramos la matriz fila por fila
print("Matriz completa:")
for fila in matriz:
    print(fila)  # Muestra cada fila como una lista


# Ejercicio 2: Mostrar todos los elementos con sus posiciones

print("\nElementos con sus posiciones:")
for i in range(len(matriz)):  # Recorre las filas
    for j in range(len(matriz[i])):  # Recorre las columnas de cada fila
        print(f"Elemento en posición ({i},{j}): {matriz[i][j]}")


# Ejercicio 3: Calcular la suma de todos los elementos de la matriz

suma_total = 0  # Inicializamos la variable para acumular la suma
for fila in matriz:
    for elemento in fila:
        suma_total += elemento  # Sumamos cada elemento al total

print("\nSuma total de elementos:", suma_total)


# Ejercicio 4: Sumar los elementos de la diagonal principal

suma_diagonal = 0
for i in range(len(matriz)):
    suma_diagonal += matriz[i][i]  # Accedemos a los elementos donde fila == columna

print("Suma de la diagonal principal:", suma_diagonal)


# Ejercicio 5: Buscar un número en la matriz e indicar su posición

numero_buscado = 6  # Valor a buscar en la matriz
encontrado = False

for i in range(len(matriz)):  # Recorremos filas
    for j in range(len(matriz[i])):  # Recorremos columnas
        if matriz[i][j] == numero_buscado:  # Comparamos el valor
            print(f"El número {numero_buscado} se encontró en ({i},{j})")
            encontrado = True

if not encontrado:
    print(f"El número {numero_buscado} no está en la matriz")



################################################################
#Ejercicios con matrices definidas
print("" \
"" \
"" \
"" \
"" \
"Definimos la Matriz" \
"" \
"" \
"" \
"")
filas = 3
columnas = 4
#matriz = [[(0 for c in range(columnas))] for f in range(filas)]


def cargar_matriz_secuencialmente(matreiz:list):
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input(f"Ingrese valor en fila {i}, columna {j}: "))

print("Matriz resultante:")
for fila in matriz:
    print(fila) """

# Inicializar la matriz con ceros


def cargar_matriz_aleatoriamente(matriz:list):
    #agregar as validaciones/retorno que sean necesarias
    seguir =  "S"
    while seguir == "S":
        filas = int(input("Cuantas filas desea ingresar: "))
        columnas = int(input("Cuantas columnas desea ingresar: "))

        fila = int(input("indice de filas: "))
        columna =  int(input("Indice de columna:  "))
        for i in range(filas):
            matriz.append([0] * columnas)

        dato = int(input("Ingrese el numero a cargar"))
        matriz[columna][fila] = dato
        seguir = input("desea seguir cargando? S/N")

mi_matriz = []

cargar_matriz_aleatoriamente(mi_matriz)


print("Matriz resultante:")
for i in mi_matriz:
    print(i)