def fibonacci_inverso(n): #trabajamos con listas
                          #no usamos recursión
    if n <= 0: #basicamente dice: quiero 0 elementos de la serie de Fibonacci, aunque aquí se le agregó para cuando da un número negativo, ñe
        return []
    elif n == 1: #quiero 1 elemento de la serie de Fibonacci
        return [0]
    elif n == 2: #quiero 2 elementos de la serie de Fibonacci
        return [1, 0] #en caso de que quiera ver dos elementos, dejamos una lista que ya esta en el orden especificado en la practica
    else: #quiero más de 2 elementos de la serie de fibonacci
        fiboncillo = [0, 1] 
        for i in range(2, n):
            print(i)
            print("Hola {}".format(fiboncillo[-1]))#es curioso como las tratamos como la estructura array in C
            print("Adiós {}".format(fiboncillo[-2]))
            fiboncillo.append(fiboncillo[-1] + fiboncillo[-2]) #esta aprte lo que hace es tomar los dos últimos elementos y sumarlos, sin embargo no sabemos que tanto se nos va a extender la lista, así que una forma inteligente de averiguar cuales son los dos últimos elementos es usar índices nengativos, 
        return fiboncillo[::-1] #al parecer es para regresar la lista al revés
        #es para invertir la lista, hay otras formas además de esta, como la función reverse() o reversed() quién sabe

if __name__ == '__main__':
    print('Bienvenido, puede realizar las siguientes operaciones:\n')
    print('1 Serie de Fibonacci\n')
    print('2 Salir\n')
    opcion = int(input('Ingrese la opcion: '))

    if opcion == 1:
        n = int(input('Ingrese el número entero N: '))#regresa N numeros de la serie de Fibonacci
        print(fibonacci_inverso(n)) 
    elif opcion == 2:
        exit()
    
#nada que ver pero apenas me dí cuenta que no compilamos y ejecutamos en python, weno es solo una sentencia 