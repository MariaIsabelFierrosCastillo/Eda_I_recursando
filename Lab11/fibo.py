def recur_fibo(n):
    if n<=1: #se me hace muy inteligente, para elemento 1(más claro primera iteración, donde i vale 0)  de la serie, imprimir 0, para 2 elementos (más claro segunda iteración, donde i vale 1) de la serie imprimir 1
        return n
    else:
        return(recur_fibo(n-1))+ recur_fibo(n-2) #escencialmente aquí esta la instrucción, básicamente significa sumar el elemento anterior(último) con el anterior del anterior(penúltimo)

nterms=13

if nterms<=0:
    print("Por favor ingrese un número entero positivo.")
else:
    print("Secuencia Fibonacci")
    for i in range(nterms): #a caray, por que estamos en una iteración
        print(recur_fibo(i))