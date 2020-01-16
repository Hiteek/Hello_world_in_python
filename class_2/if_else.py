# x = 'Anthony'
# Pedro tiene x años
# print('Pedro tiene', x, 'años.')
# # print('PEdro tiene {} años'.format(x))
# # print(f'Pedro tiene {x} años')
# print(type(x))

# Operadores aritmeticos
# x = 10
# print(x)
# x = x + 5
# print(x)
# x = x - 7
# print(x)
# x = x*3
# print(x)
# # x = x/5
# # print(x)

# # x += 5
# # x -= 4
# # x *= 3
# name = input('What\'s your name? ')
# print('Hi', name, '\b!')
# age = int(input('How old are you?'))
# # if age >= 18:
# #     print('You are allowed to enter')
# # else:
# #     print('You shall not pass.')
# if age < 0:
#     print('Error! An age can\' be negative')
# elif age < 18: # else if = elif
#     print('You shall not pass.')
# else:
#     print('jumanju kkbrioooo')

print('Este programa va calcular el area de un circulo')
print('Porfavor ingresa un numero :)')
r = float(input())
if r < 0:
    print('El radio de un circulo no puede ser menor a 0')
elif r == 0:
    print('Si el radio es 0 entonces se trata de un punto y el punto no tiene area')
else:
    A = 22/7*(r**2)
    print('El area del circulo es', A)

# x = input()
# if type(x) == 'str':
#     print('holi')