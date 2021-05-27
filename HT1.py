#Ejercicio 1 

n = int(input("Introduce un numero entero positivo:   "))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")

#Fin Ejercicio 1


#Ejercicio 2

n = int(input("Ingrese un numero positivo: "))

num = n
for i in range(1,num+1):
       print(num-i, end=", ")


#Fin Ejercicio 2


#Ejercicio 3

n = int(input("Introduce un numero entero positivo mayar a 2: "))
i = 2
while n % i != 0:
    i +=1
if i ==n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")