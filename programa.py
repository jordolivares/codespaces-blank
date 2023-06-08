import numpy as np 
nombres=['Luis', 'Sandra', 'Mario']
ventas = np.empty( [4,3], dtype='object')

for i in range(4):
    for j in range(3):
        cant = int(input(f"Ingrese la cantidad vendida en {i} {nombres[j]}: "))
        ventas[i,j]=cant

print(ventas)    

for i in range(4):
    for j in range(3):
        print(ventas[i,j])


