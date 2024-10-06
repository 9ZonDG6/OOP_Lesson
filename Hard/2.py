class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f'{self.name}, {self.color}, {self.toy_type}'


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, "Животное")


class CartoonToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, "Персонаж мультфильма")


class ToyFactory:
    @staticmethod
    def buy_material():
        print('Закупка сырья для игрушки')

    @staticmethod
    def tailoring():
        print('Пошив игрушки')

    @staticmethod
    def coloring(color):
        print(f'Покраска игрушки в {color} цвет')

    def create(self, name, color, toy_type):
        self.buy_material()
        self.tailoring()
        self.coloring(color)

        if toy_type == 'Животное':
            toy = AnimalToy(name, color)
            print('Игрушка успешно создана!')
            return toy
        elif toy_type == 'Персонаж мультфильма':
            toy = CartoonToy(name, color)
            print('Игрушка успешно создана!')
            return toy
        else:
            print('Не верный тип игрушки')


factory = ToyFactory()
animal_toy = factory.create('Волк', 'Серый', 'Животное')
print(animal_toy)
