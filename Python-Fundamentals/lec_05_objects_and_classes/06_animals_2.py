class Animal:
    def __init__(self):
        self.__name = ''
        self.__age = 0
        self.__sound = ''
        self.__parameters = ''

    def set_name(self, name: str):
        self.__name = name

    def set_age(self, age: int):
        self.__age = age

    def set_sound(self, sound: str):
        self.__sound = sound

    def set_parameters(self, parameters: int):
        self.__parameters = parameters

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_parameters(self):
        return self.__parameters

    def get_sound(self):
        return self.__sound


class Dog(Animal):
    parameter = 1

    def __str__(self):
        return f"Dog: {self.get_name()}, Age: {self.get_age()}, Number Of Legs: {self.get_parameters()}"

    def set_from_string(self, data):
        animal_name, animal_age, animal_parameter = data
        self.set_age(animal_age)
        self.set_name(animal_name)
        self.set_parameters(animal_parameter)
        self.set_sound(
            "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")


class Cat(Animal):
    parameter = 2

    def __str__(self):
        return f"Cat: {self.get_name()}, Age: {self.get_age()}, IQ: {self.get_parameters()}"

    def set_from_string(self, data):
        animal_name, animal_age, animal_parameter = data
        self.set_age(animal_age)
        self.set_name(animal_name)
        self.set_parameters(animal_parameter)
        self.set_sound("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")


class Snake(Animal):
    parameter = 3

    def __str__(self):
        return f"Snake: {self.get_name()}, Age: {self.get_age()}, Cruelty: {self.get_parameters()}"

    def set_from_string(self, data):
        animal_name, animal_age, animal_parameter = data
        self.set_age(animal_age)
        self.set_name(animal_name)
        self.set_parameters(animal_parameter)
        self.set_sound("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")


data = input()
animals = []
# Read all animals
while not data == "I'm your Huckleberry":
    data = data.split()
    if data[0] == 'Dog':
        animal = Dog()
        animal.set_from_string(data[1:])
        animals.append(animal)
    elif data[0] == 'Cat':
        animal = Cat()
        animal.set_from_string(data[1:])
        animals.append(animal)
    elif data[0] == 'Snake':
        animal = Snake()
        animal.set_from_string(data[1:])
        animals.append(animal)
    elif data[0] == 'talk':
        # print only sound of the animal with same name
        print(list(filter(lambda k: k.get_name() == data[1], animals))[0].get_sound())
    data = input()
# print all animals list comprehension sorting by parameter
[print(i) for i in sorted(animals, key=lambda k: k.parameter)]
