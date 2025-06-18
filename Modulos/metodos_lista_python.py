
"""
Manual de Métodos de Listas en Python con Ejemplos y Comentarios

Este archivo contiene ejemplos explicativos sobre cómo usar los principales métodos
de las listas en Python. Cada sección incluye comentarios explicativos para cada línea.
"""

# Crear una lista base para los ejemplos
mi_lista = [5, 3, 8, 1, 9, 3]

# 1. append() - Agrega un elemento al final de la lista
mi_lista.append(4)  # Agrega el número 4 al final de la lista
# Resultado: [5, 3, 8, 1, 9, 3, 4]

# 2. extend() - Agrega todos los elementos de una lista a otra
mi_lista.extend([10, 11])  # Agrega 10 y 11 al final
# Resultado: [5, 3, 8, 1, 9, 3, 4, 10, 11]

# 3. insert() - Inserta un elemento en una posición específica
mi_lista.insert(2, 7)  # Inserta el 7 en la posición 2 (tercer elemento)
# Resultado: [5, 3, 7, 8, 1, 9, 3, 4, 10, 11]

# 4. remove() - Elimina la primera ocurrencia de un valor específico
mi_lista.remove(3)  # Elimina el primer 3 que aparece en la lista
# Resultado: [5, 7, 8, 1, 9, 3, 4, 10, 11]

# 5. pop() - Elimina y retorna el último elemento (o uno en una posición específica)
ultimo = mi_lista.pop()  # Elimina el último elemento (11)
# Resultado de pop: 11

# 6. index() - Devuelve el índice del primer elemento que coincide con el valor
indice = mi_lista.index(9)  # Devuelve la posición de la primera aparición de 9
# Resultado: 4

# 7. count() - Cuenta cuántas veces aparece un valor en la lista
cantidad = mi_lista.count(3)  # Cuenta cuántas veces aparece el número 3
# Resultado: 1

# 8. sort() - Ordena la lista en su lugar (modifica la lista)
mi_lista.sort()  # Ordena los elementos de menor a mayor
# Resultado: [1, 3, 4, 5, 7, 8, 9, 10]

# 9. sorted() - Devuelve una nueva lista ordenada sin modificar la original
otra_lista = [8, 2, 6, 4]
ordenada = sorted(otra_lista)  # [2, 4, 6, 8]
# otra_lista sigue siendo [8, 2, 6, 4]

# 10. reverse() - Invierte el orden de los elementos en la lista
otra_lista.reverse()  # [4, 6, 2, 8]

# 11. copy() - Devuelve una copia superficial de la lista
copia = mi_lista.copy()
# copia y mi_lista son listas diferentes con el mismo contenido

# 12. clear() - Elimina todos los elementos de la lista
temporal = [1, 2, 3]
temporal.clear()  # temporal queda como []

# 13. Recorrer una lista
for elemento in mi_lista:
    print("Elemento:", elemento)

# 14. Usar enumerate para obtener índice y valor
for indice, valor in enumerate(mi_lista):
    print(f"Índice {indice} tiene el valor {valor}")

# 15. Búsqueda con operador 'in'
if 5 in mi_lista:
    print("El número 5 está en la lista")
else:
    print("El número 5 no está en la lista")


# 17. Shallow Copy (copia superficial) usando slicing
#secuencia[start:end:step] - Crea una copia superficial de la lista
#start : el indice de inicio (incluido)
#end : el indice de fin (excluido)
#step : el paso entre los indices (opcional, por defecto es 1)
original = [[1, 2], [3, 4]]
original_nueva = [1, 2, 3, 4, 5]
copia_original_nueva = original_nueva[:]  # Crea una copia superficial de la lista
copia_superficial = original[:]  # Crea una nueva lista, pero las sublistas siguen compartidas
copia_superficial[0][0] = 99
print("Original después de modificar copia superficial:", original)
# La sublista interna también se modifica porque la copia es superficial (shallow copy)

# 18. Deep Copy (copia profunda)
import copy
original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(original)
copia_profunda[0][0] = 77
print("Original después de modificar copia profunda:", original)
# En este caso, original no cambia porque la copia es profunda

# 19. del - Eliminar elementos o listas completas
lista_del = [10, 20, 30, 40, 50]
del lista_del[2]  # Elimina el elemento en el índice 2 (30)
print("Lista después de del:", lista_del)
del lista_del[:]  # Elimina todos los elementos (similar a clear)
print("Lista vacía:", lista_del)

# 20. Slicing - Rebanado de listas
frutas = ["manzana", "banana", "cereza", "durazno", "kiwi"]
primeras_tres = frutas[:3]  # ['manzana', 'banana', 'cereza']
ultimas_dos = frutas[-2:]   # ['durazno', 'kiwi']
salteadas = frutas[::2]     # ['manzana', 'cereza', 'kiwi'] (cada dos elementos)
print("Primeras tres:", primeras_tres)
print("Últimas dos:", ultimas_dos)
print("Salteadas:", salteadas)
