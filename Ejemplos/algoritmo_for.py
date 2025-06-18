# 1. Mostrar los números ascendentes desde el 1 al 10
print("1. Números del 1 al 10:")
for i in range(1, 11):
    print(i)

# 2. Mostrar los números descendentes desde el 10 al 1
print("\n2. Números del 10 al 1:")
for i in range(10, 0, -1):
    print(i)

# 3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado
n = int(input("\n3. Ingresa un número: "))
print(f"Números del 0 al {n}:")
for i in range(n + 1):
    print(i)

# 4. Tabla de multiplicar de un número ingresado
tabla = int(input("\n4. Ingresa un número para ver su tabla de multiplicar: "))
for i in range(11):
    print(f"{tabla} x {i} = {tabla * i}")

# 5. Ingresar hasta 10 números o hasta que el usuario ingrese 0
print("\n5. Ingresar hasta 10 números (0 para detener):")
suma = 0
contador = 0
for i in range(10):
    numero = int(input(f"Ingresá el número #{i+1}: "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron números válidos.")

# 6. Imprimir los múltiplos de 3 entre 1 y 10
print("\n6. Múltiplos de 3 entre 1 y 10:")
for i in range(1, 11):
    if i % 3 == 0:
        print(i)

# 7. Mostrar números pares desde 1 hasta 50
print("\n7. Números pares del 1 al 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# 8. Pirámide de números
altura = int(input("\n8. Ingresa un número para la pirámide: "))
for i in range(1, altura + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 9. Mostrar divisores de un número
num = int(input("\n9. Ingresar un número para ver sus divisores: "))
divisores = []
for i in range(1, num + 1):
    if num % i == 0:
        divisores.append(i)

print(f"Divisores de {num}: {divisores}")
print(f"Cantidad de divisores: {len(divisores)}")

# 10. Determinar si un número es primo
n_primo = int(input("\n10. Ingresar un número para saber si es primo: "))
es_primo = True

if n_primo <= 1:
    es_primo = False
else:
    for i in range(2, n_primo):
        if n_primo % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{n_primo} es un número primo.")
else:
    print(f"{n_primo} NO es un número primo.")

# 11. Mostrar todos los números primos entre 1 y un número ingresado
limite = int(input("\n11. Ingresar un número límite para ver todos los primos hasta ese valor: "))
contador_primos = 0

print("Números primos encontrados:")
for num in range(2, limite + 1):
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)
        contador_primos += 1

print(f"Cantidad total de números primos encontrados: {contador_primos}")
