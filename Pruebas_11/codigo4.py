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
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[::-1]

if __name__ == '__main__':
    print('Bienvenido, puede realizar las siguientes operaciones:\n')
    print('1 Conversion de bases\n')
    print('2 Serie de Fibonacci\n')
    print('3 Salir\n')
    opcion = int(input('Ingrese la opción: '))

    if opcion == 1:
        n = int(input('\nIngrese el número entero N:'))
        print(' decimal_a_binario(n)')
    elif opcion == 2:
        n = int(input('Ingrese el número entero N: '))
        print(map(str, fibonacci_inverso(n)))
    elif opcion == 3:
        exit()