def fibonacci_inverso(n): #trabajamos con listas
                          #no usamos recursión
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [1, 0]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[::-1] #al parecer es para regresar la lista al revés

if __name__ == '__main__':
    print('Bienvenido, puede realizar las siguientes operaciones:\n')
    print('1 Serie de Fibonacci\n')
    print('2 Salir\n')
    opcion = int(input('Ingrese la opcion: '))

    if opcion == 1:
        n = int(input('Ingrese el número entero N: '))#regresa N numeros de la serie de Fibonacci
        print(' '.join(map(str, fibonacci_inverso(n)))) 
    elif opcion == 2:
        exit()
    
#nada que ver pero apenas me dí cuenta que no compilamos y ejecutamos en python, weno es solo una sentencia 