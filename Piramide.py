'''Lee la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.
La altura se mide por el número de capas completas: si los constructores 
no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques y
no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
'''
bloques = int(input("Ingrese el número de bloques:"))
altura=0
edo = 1
while edo>=0:
    altura +=  1
    bloques = bloques - (1*altura)
    edo = bloques - (1*(altura+1))
    print(" "*espacio,"*"*altura)

print("La altura de la pirámide:", altura)
