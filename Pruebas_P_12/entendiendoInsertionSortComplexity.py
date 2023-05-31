#%pylab inline

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random #aquí importamos todo random, por que se podía from random import sample y ya usabamos sample en lugar de random.sample

times = 0 #sho pienso que se llama times y no time, pero como vimos, parece que no es necesria declararla

def grafiquitaDeInsertionSort(n_lista): #cada bendito ciclo, le voy a enviar una lista cada vez más grande a esta función
#lista_variable y n_lista representan escencialmente lo mismo
    
    #print("num vale {}".format(num))
    global times #supongo que significa que dentro de la función la voy a cambiar
    #te das cuenta que times es bien inútil, pa' que decir que es global y decir que lo voy a modificar si en digamos el código prinicipal quiero que siga valiendo lo mismo, 0. No lo que pasa es que si te das cuenta, en el digamos main antes de volver a empezar un nuevo ciclo y cambiar times a 0, es asignado a eje_x con un valor que ya tiene desde esta función
    
    for index in range(1, len(n_lista)): #este segundo parámetro de range va a ser desde 1 hasta 100 tocandolo. Entonces este for se va a ajecutar en todo el programa en TOTAL 100 veces, pero esas veces que se va a ajecutar digamos con una duración cada vez más grande
        #print("soy índice {}".format(index))
        times+=1
        actual = n_lista[index] 
        position = index
        while(position > 0 and n_lista[position-1] > actual): #mi pregunta es cuándo va a ser position menor a cero.
            #print("entré")
            times+=1
            n_lista[position] = n_lista[position-1]
            position-=1
            
        n_lista[position] = actual
    return n_lista

TAM = 101
eje_x = list(range(1, TAM, 1)) 

eje_y = []
lista_variable = [] 

for num in eje_x: 
    lista_variable = random.sample(range(0,1000), num) 
    times = 0
    lista_variable = grafiquitaDeInsertionSort(lista_variable) 
    eje_y.append(times) 
    
print(lista_variable) 


fig, ax = plt.subplots(facecolor='c', edgecolor='b') 
ax.plot(eje_x, eje_y, marker="o", color="r", linestyle='None') 

ax.set_xlabel("x me dicen")
ax.set_ylabel("y sere")
ax.grid(True)  
ax.legend(["Soy Insertion Sort"])

plt.title("Me llaman Insertion sort")
plt.show() 

