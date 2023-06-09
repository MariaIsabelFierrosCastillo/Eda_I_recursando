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
# donde __name__ es una variable especial, que junto con otras variables especiales fueron lo primero que estableció un interprete de Python cuando se leyó un archivo de Pyhton(o lo que es lo mismo módulo) es decir con al extensión de archivo .py.
#cuando el intérprete ejecute un módulo/archivo principal, la variable espacial __name__ se establecerá como __main__ en ese módulo/archivo
    libros = [] #lista de libros local #es buena practica usar variables locales para pasar y manipular data
    while True:
        print('\nBienvenido a la biblioteca, puede realizar las siguientes operaciones:\n')
        print('1 Agregar libro')
        print('2 Eliminar libro')
        print('3 Ordenar biblioteca')
        print('4 Ver biblioteca')
        print('5 Salir')
        option = input('\nIngrese la opción: ')
        
        if option == '1':
            agregar_libro(libros) #a diferencia del lenguaje C, en python no hay apuntadores. 
            """Aquí se puede observar que con enviar como argumento la variable libros hacia una función, y la variable books al ser modifica en fucnión que no devuelve nada, las modificaciones se ven reflejadas en el main, en C hubiera sido necesario enviar su dirección para que esto ocurriera"""
        elif option == '2':
            eliminar_libro(libros)
        elif option == '3':
            ordenar_biblioteca(libros)
        elif option == '4':
            ver_biblioteca(libros)
        elif option == '5': 
            break

#todo lo que en este programa se llama titulo, pudo haberse llamado mejor book o libro, en mi opinion se entiende mejor
#una lista1 igual a otra lista2, si cambias alguna, cambias la otra
#*args es para tuplas y listas, **kwargs es para diccionarios

#.append(), .remove() y .sort() son funciones integradas