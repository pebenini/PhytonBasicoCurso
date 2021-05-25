#While
# While -> Mientras 
# Condicion Finita
# Instrucciones

#The while Loop
print("Primer Ejemplo")
i = 1
while i < 10:
  print(i)
  i += 1
  #Aumentar variable
  #i +=1 # infremento
  #i = i +1 
  #i++
print("Fin Primer Ejemplo")

#The break Statement
print("Segundo Ejemplo")
i = 1
while i < 5:
  print(i)
  if i == 3:
    break
  i += 1
print("Fin Segundo Ejemplo")


#The continue Statement
print("3 Ejemplo")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("Fin 3 Ejemplo")

#The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#Tablas de Multiplicar 
i= 9
j = 1
while j < 10 :
  print(i, "*", j, "=", i * j)
  j += 1


  #While anidados
  #while expression/condicione:
  #bloque continuo


  i = 0
  j = 0
  while i < 3 :
      while j < 3 :
          print(i,j)
          j += 1
        i +=1
        j = 0