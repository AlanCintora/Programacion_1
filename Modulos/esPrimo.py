#Pedimos al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

#Verificamos si el número es menor o igual a 1
if numero <= 1:
    print(f"El número {numero} no es primo.")
else:
    # Usamos un bucle for para verificar si el número es divisible por algún otro número que no sea él mismo ni 1
    es_primo = True  # Suponemos que el número es primo
    for i in range(2, numero):  # Comenzamos desde 2 hasta el número-1
        if numero % i == 0:  # Si el número es divisible por i, entonces no es primo
            es_primo = False
            break  # No es necesario seguir verificando, ya sabemos que no es primo

    # Imprimimos el resultado
    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")