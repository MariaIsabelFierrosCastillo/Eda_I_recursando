def decimal_a_binario(n): #complex tro understand, but at least not to learn
    if n == 0:
        return ''
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def fibonacci_inverso(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [1, 0]
    else:
        fib = fibonacci_inverso(n-1)
        fib.append(fib[-1] + fib[-2])
        return fib

if __name__ == '__main__':
    print('Bienvenido, puede realizar las siguientes operaciones:')
    print('1 Conversion de bases')
    print('2 Serie de Fibonacci')
    print('3 Salir\n')
    opcion = int(input('Ingrese la opcion: ')) #convertir la entrada a entero

    if opcion == 1:
        n = int(input('\nIngrese un número entero: ')) #another shit to lear is that you can read inputs like that, great
        print(decimal_a_binario(n))

    elif opcion == 2:
        n = int(input('\nIngrese un número entero: '))
        print(fibonacci_inverso(n)[::-1]) #

    elif opcion == 3:
        exit()
