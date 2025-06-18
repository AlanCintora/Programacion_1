def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("El factorial de 5 es:", factorial(5))

def cuenta_regresiva(n):
    if n == 0:
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)

cuenta_regresiva(10)