class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print('Машина поехала')

    @staticmethod
    def stop():
        print('Машина остановилась')

    @staticmethod
    def turn(direction):
        if direction.isalpha():
            print(f'Машина повернула на {direction}')


class SportCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print('Машина поехала')

    @staticmethod
    def stop():
        print('Машина остановилась')

    @staticmethod
    def turn(direction):
        if direction.isalpha():
            print(f'Машина повернула на {direction}')


class WorkCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print('Машина поехала')

    @staticmethod
    def stop():
        print('Машина остановилась')

    @staticmethod
    def turn(direction):
        if direction.isalpha():
            print(f'Машина повернула на {direction}')


class PoliceCar:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print('Машина поехала')

    @staticmethod
    def stop():
        print('Машина остановилась')

    @staticmethod
    def turn(direction):
        if direction.isalpha():
            print(f'Машина повернула на {direction}')


my_car = SportCar(220,'Белый', 'Audi')
my_car.go()
my_car.stop()
print(my_car.name)
