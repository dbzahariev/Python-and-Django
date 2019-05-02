class Dog:
    def __init__(self, Name, Age, Number_of_legs):
        self.Name = Name
        self.Age = int(Age)
        self.Number_of_legs = int(Number_of_legs)
        self.class_animal = 'Dog'
        self.produce_sound = produce_sound

    def __str__(self):
        return f'Dog: {self.Name}, Age: {self.Age}, Number Of Legs: {self.Number_of_legs}'


class Cat:
    def __init__(self, Name, Age, Intelligence_quotient):
        self.Name = Name
        self.Age = int(Age)
        self.Intelligence_quotient = int(Intelligence_quotient)
        self.class_animal = 'Cat'
        self.produce_sound = produce_sound

    def __str__(self):
        return f'Cat: {self.Name}, Age: {self.Age}, IQ: {self.Intelligence_quotient}'


class Snake:
    def __init__(self, Name, Age, Cruelty_coefficient):
        self.Name = Name
        self.Age = int(Age)
        self.Cruelty_coefficient = int(Cruelty_coefficient)
        self.class_animal = 'Snake'
        self.produce_sound = produce_sound

    def __str__(self):
        return f'Snake: {self.Name}, Age: {self.Age}, Cruelty: {self.Cruelty_coefficient}'


def produce_sound(animal):
    if isinstance(animal, Dog):
        return f"I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."
    if isinstance(animal, Cat):
        return f"I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."
    if isinstance(animal, Snake):
        return f"I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."


dogs = []
cats = []
snakes = []

while True:
    data = input().split()
    if data[0] == 'talk':
        for animal in dogs:
            if animal.Name == data[1]:
                print(animal.produce_sound(animal))
        for animal in cats:
            if animal.Name == data[1]:
                print(animal.produce_sound(animal))
        for animal in snakes:
            if animal.Name == data[1]:
                print(animal.produce_sound(animal))
        continue
    elif data[0] == "I'm":
        for animal in dogs:
            print(animal)
        for animal in cats:
            print(animal)
        for animal in snakes:
            print(animal)
        break
    animal_class, animal_name, animal_age, animal_parameter = data
    if animal_class == 'Dog':
        dogs.append(Dog(animal_name, animal_age, animal_parameter))
    elif animal_class == 'Cat':
        cats.append(Cat(animal_name, animal_age, animal_parameter))
    elif animal_class == 'Snake':
        snakes.append(Snake(animal_name, animal_age, animal_parameter))
