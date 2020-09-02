bloques = int(input("Ingrese el número de bloques:"))
altura=0
edo = 1
while edo>=0:
    altura +=  1
    bloques = bloques - (1*altura)
    edo = bloques - (1*(altura+1))
    print(" "*espacio,"*"*altura)

print("La altura de la pirámide:", altura)
