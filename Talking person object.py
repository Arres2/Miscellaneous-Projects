class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hola, soy {self.name}')


person1 = Person("Andrés")
person1.talk()
