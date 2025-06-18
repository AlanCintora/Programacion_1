""" Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot """

altura = int(input("Por favor, ingresá tu altura: "))

if altura < 160:
    print("Base.")
elif altura <= 179:
    print("Escolta.")
elif altura <= 199:
    print("Alero.")
else:
    print("Ala-Pívot o Pívot.")
