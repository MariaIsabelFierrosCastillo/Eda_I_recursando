# Función para agregar un libro
def agregar_libro(books): #no fue necesario usar *args, por que el parámetro siempre va a ser el mismo, aunque la lista cambie.
#en cambio si desde main se enviara una lista (que cambia a lo largo del bucle) de esta manera: ['H', 'O', 'L', 'A'], entonces si se enviaría con * al frente d ela lista y se recibiría como *args
#la variable books en esta función es alias de la variable libros en main
    titulo = input('Ingrese el título del libro: ') #un libro esta representado por su titulo
    books.append(titulo) #de esta manera la variable titulo sería lo mismo que un libro
    print('Libro agregado:', titulo)

# Función para eliminar un libro
def eliminar_libro(books):
    titulo = input('Ingrese el título del libro: ')
    if titulo in books:
        books.remove(titulo)
        print('Libro eliminado:', titulo)
    else:
        print('Libro no encontrado')

# Función para ordenar la biblioteca
def ordenar_biblioteca(books):
    books.sort()
    print('\nLa biblioteca queda con el siguiente orden:\n')
    for libro in books:
        print(libro)

# Función para ver la biblioteca
def ver_biblioteca(books): #el argumento recibido se puede llamar diferente
    print('\nLa biblioteca contiene los siguientes libros:\n')
    for libro in books: #también se podia usar print(libros)
        print(libro)

# Código principal
if __name__ == '__main__':
    libros = [] #lista de libros local #es buena practica usar variables globales para pasar y manipular data
    while True:
        print('\nBienvenido a la biblioteca, puede realizar las siguientes operaciones:\n')
        print('1 Agregar libro')
        print('2 Eliminar libro')
        print('3 Ordenar biblioteca')
        print('4 Ver biblioteca')
        print('5 Salir')
        opcion = input('\nIngrese la opción: ')
        
        if opcion == '1':
            agregar_libro(libros) #a diferencia del lenguaje C, en python no hay apuntadores. 
            """Aquí se puede observar que con enviar la variable libros como parámetro y la funcion recibirla como argumento, la variable books se modifica, en C hubiera sido necesario enviar su dirección"""
        elif opcion == '2':
            eliminar_libro(libros)
        elif opcion == '3':
            ordenar_biblioteca(libros)
        elif opcion == '4':
            ver_biblioteca(libros)
        elif opcion == '5': 
            break

#todo lo que en este programa se llama titulo, pudo haberse llamado mejor book o libro, en mi opinion se entiende mejor
#una lista1 igual a otra lista2, si cambias alguna, cambias la otra
#*args es para tuplas y listas, **kwargs es para diccionarios