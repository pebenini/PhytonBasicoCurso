#Ejercicio 1

Contrasena = input("Ingrese su contraseña: ")
Validacion = input("Ingrese nuevamente su contraseña:")

if Contrasena == Validacion:
    print("Su contraseña es correcta")
else:
    print("*****La contraseña ingresada es incorrecta****")




# Ejercicio 2

name = input("¿Como te llamas?: ")
gender = input("¿Cual es tu sexo (M o H)? ")

if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower () > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)
