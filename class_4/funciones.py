#Funciones
variable = 27

def saludar(nombre, edad):
    global variable
    variable+=2
    print(f'!HOla {nombre} tiene {edad} años!')
    print(variable)

saludar('ANthony', 23)