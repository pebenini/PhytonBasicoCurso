#Sintaxis
#for objetoiteractivo in secuencia :
#declaraciones (ifs, for, while, metodos o funciones)

#Pasoso
#   1. for
#   2. variable que va manejar las iteraciones
#   3. secuencia a iterar o recorrer
#   4. el area declaracion, donde vamos a manejar cada elemento de la secuencia

#Python for loops
fruits = ["apple","banana", "cherry", "watermelon","berry", "peach", "lemon"]

for fruit in fruits:
    print("Hola", fruit)


#Looping through a string
for x in "banana":
    print(x)


#The break Statement
fruits = ["apple","cherry", "banana", "watermelon","berry", "peach", "lemon"]
for x in fruits:
    print(x)
    if x == "banana" :
            break


#The continue statement
print("The continue statement")
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)



#The range() function
for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

print("range con 3 parametros")
for x in range(2,30,3):
    print(x)


#Else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#Nested loops
adj = ["red","big","tasty"]
frutis =["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)




