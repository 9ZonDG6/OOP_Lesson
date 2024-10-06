class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f'{self.name}, {self.color}, {self.toy_type}'


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

        toy = Toy(name, color, toy_type)
        print('Игрушка успешно создана!')
        return toy


factory = ToyFactory()
toys = factory.create('Плюмбус', 'Розовый', 'Предмет из "РиМ"')
print(toys)
