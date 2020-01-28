dic = {}
def agregar_contacto(nombre):

    apellido = input('Ingresa apellido: ')
    cell = input('Ingresa celular: ')
    correo = input('Ingresa correo: ')
    dic[nombre] = [apellido, cell, correo]

def buscar_contacto(nombre):
    
    if nombre in dic:
        print(dic[nombre])
    else:
        print('Contacto no encontrado!')

def eliminar_contacto(nombre):
    
    dic.pop(nombre)
    mostrar_contacto()

def mostrar_contacto():

    print('Contactos: ')
    for position, key in enumerate(dic):
        print(position + 1, key, dic[key])
while True:
    print('***Menu***')
    print('1) Añadir contacto')
    print('2) Eliminar contacto')
    print('3) Mostrar contactos')
    print('4) Buscar contactos')
    print('5) Salir')
    number = int(input('Ingrese un numero para elegir una opcion: '))
    if number == 5:
        break
    elif number != 1 and number != 2 and number != 3 and number != 4:
        print('Error! Escoja una opcion valida')
    else:
        if number == 1:
            nombre = input('Ingresa Nombre: ')
            agregar_contacto(nombre)
        elif number == 2:
            nombre = input('Ingresa Nombre: ')
        elif number == 3:
            mostrar_contacto()
        else:
            nombre = input('Ingresa Nombre: ')
            buscar_contacto