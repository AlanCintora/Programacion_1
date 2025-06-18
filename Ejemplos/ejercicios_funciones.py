
#1-Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
""" def ingresar_int ():
    numero = input("Ingrese un numero entero: ")
    return int(numero)

entero = ingresar_int()
print("Número entero ingresado:", entero) """

#2-Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
""" def ingresar_float ():
    flotante = input("Ingrese un numero con decimales: ")
    return float(flotante)

decimal = ingresar_float()
print("Número decimal ingresado:", decimal) """

#3-Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.

""" def ingresar_string ():
    texto = input("Ingrese una cadena de caracteres: ")
    return str(texto)

cadena = ingresar_string()
print("Cadena ingresada:", cadena) """

#4-Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def area_rectangulo (base: float, altura: float) -> float:
    
    area = base * altura
    return float(area)

resultado = area_rectangulo()
print("El area del rectangulo es: ", resultado)