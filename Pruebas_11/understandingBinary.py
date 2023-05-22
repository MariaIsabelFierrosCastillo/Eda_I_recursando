def decimal_a_binario(n):
    if n == 0:
        #print(" mama")
        return ' '#lo que pasa es que la función en general tiene que regresar cadena, el n==0 es necesario para saber dónde detenernos, no creo que se pueda quitar
        #' ' no nos sirve realmente, pero tenemos que regresarnos de alguna manera, y solo se acepta regresar cadenas
    else:
        #print("ga {}".format(n//2))
        #print("to {}".format(n%2))
        return decimal_a_binario(n // 2) + str(n % 2) #es como si los 1's y 0's no son números sino cadenas, dejame aclararte que si son números, pero a lo que me refiero es que al ponerles este str los conviertes en cadenas, y el+ pues es complementario para unirlas
        #empezamos regresando '', la cual es una cadena, de ahí puros '0' o '1', termina siendo una cadena todo

if __name__ == '__main__':
    print('Bienvenido, puede realizar las siguientes operaciones:\n')
    print('1 Conversion de bases\n')
    print('2 Salir\n')
    opcion = int(input('Ingrese la opción: '))
    
    if opcion == 1:
        n = int(input('\nIngrese el número entero N: '))
        print(decimal_a_binario(n))#lo que sea que regrese esa función siempre será cadena, y aunque fuese un número no tendrías que usar str()
    elif opcion == 2:
        exit()