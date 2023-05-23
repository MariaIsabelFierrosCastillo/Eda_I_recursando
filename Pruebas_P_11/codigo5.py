def decimal_a_binario(n):
    if n == 0:
        return ''
    else:
        return decimal_a_binario(n // 2) + str(n % 2) 

def fibonacci_inverso(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [1, 0]
    else:
        fib = [0, 1]
        for i in range(2, n):#era lo mismo que poner in range(n-2)
            fib.append(fib[-1] + fib[-2])
        return fib[::-1]

if __name__ == '__main__':
    while True:
        print('Bienvenido, puede realizar las siguientes operaciones:\n')
        print('1 Conversion de bases\n')
        print('2 Serie de Fibonacci\n')
        print('3 Salir\n')
        opcion = int(input('Ingrese la opcion: '))
        
        if opcion == 1:
            n = int(input('\nIngrese el número entero N: '))
            print('\n\033[1;32m' + decimal_a_binario(n) + '\033[0m') #pa' imprimir el resultado de verde
        elif opcion == 2:
            n = int(input('\n\033[1;34mIngrese el número entero N: \033[0m'))
            print('\n\033[1;32m' + ' '.join(map(str, fibonacci_inverso(n))) + '\033[0m') #pone verde la salida #para imprimir sin corchetes la lista 
        elif opcion == 3:
            exit()