#Ejercicio:
#Escribí un programa en Python que le pida al usuario ingresar su edad.
#Si la edad es menor a 0 o mayor a 120, mostrar un mensaje que diga: "Edad inválida".
#Si la edad es menor a 13, mostrar: "Acceso denegado. Debes tener al menos 13 años para entrar."
#Si la edad está entre 13 y 17 inclusive, mostrar: "Acceso restringido. Estás en modo adolescente."
#Si la edad es 18 o más, mostrar: "Acceso completo concedido."

edad = int(input("Por favor, ingresá tu edad: "))

if edad < 0 or edad > 120:
    print("Edad Invalida.")
elif edad < 13:
    print("Acceso Denegado. Debes tener al menos 13 años para entrar.")
elif 13 <= edad <= 17:
    print("Acceso restringido. Estás en modo adolescente.")
else:
    print("Acceso completo concedido.")
