# CLase:
#     -> Son abstracciones de las cosas de la vida cotidiana.
#     -> Moldes o plantillas para crear objetos.
# Objeto:
#     -> Un ejemplar de una clase de particular.
#     -> UNa instancia de una clase.

# class Person():
#         def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
# person_1 = Person('Anthony', 23)
# person_2 = Person('Ruben', 'Ricapa', 15)

# print(person_2.name, person_2.last_name)

# print(person_1.name)

class Car():

    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        self.speed = 0
        self.status = 'off'

    def turn_on(self):
        if self.status == 'on':
            print('The car is already on')
        else:
            self.status = 'on'
            print('The car is now turn on')

    def acelerate(self):
        if self.status == 'on':
            self.speed += 10
            print('Now, the speed is ' + str(self.speed))
        else:
            print('The car is turn off')
    
    def brake(self):
        if self.speed == 0:
            print('The car is already stopped')
        else:
            self.speed = 0
            print('The car is now stopped')

    
    def turn_off(self):
        self.status = 'off'
        return 'The car is off'

Mi_carrito = Car('Negro', 0, 'off')

print(Mi_carrito.color, Mi_carrito.speed, Mi_carrito.status)

print(Mi_carrito.turn_on())

print(Mi_carrito.color, Mi_carrito.speed, Mi_carrito.status)