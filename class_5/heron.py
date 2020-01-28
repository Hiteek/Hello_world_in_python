#Programa formula de heron
SemiPerimetro = 0
Area = 0
Lado_A=0
Lado_B=0
Lado_C=0
#LECTURA DE NUMEROS
print('Ingrese los lados del triangulo: ')


while True:
    try:
        Lado_A = float(input('A: '))
        if Lado_A < 0:
            print('The number have to be positive')
        else:
            break
    except ValueError:
        print('The number you\'ve just typed is not and integer')



while True:
    try:
        Lado_B = float(input('B: '))
        if Lado_B < 0:
            print('The number have to be positive')
        else:
            break
    except ValueError:
        print('The number you\'ve just typed is not and integer')


while True:
    try:
        Lado_C = float(input('C: '))
        if Lado_C < 0:
            print('The number have to be positive')
        else:
            break
    except ValueError:
        print('The number you\'ve just typed is not and integer')


#EXISTENCIA DEL TRIANGULO Y HERON
if (Lado_A > abs(Lado_B - Lado_C) and Lado_A < Lado_B + Lado_C) and \
    (Lado_B > abs(Lado_A - Lado_C) and Lado_B < Lado_A + Lado_C) and \
    (Lado_C > abs(Lado_A - Lado_B) and Lado_C < Lado_A + Lado_B):
    
    SemiPerimetro = (Lado_A + Lado_B + Lado_C)/2
    Area = (SemiPerimetro*(SemiPerimetro - Lado_A)*(SemiPerimetro - Lado_B)*(SemiPerimetro - Lado_C))**0.5
    
  
    print('El area del triangulo es ' + str(Area))

else:
    print('El triangulo no existe')