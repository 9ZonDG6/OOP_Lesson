class Car:
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


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


my_car = SportCar(180, 'Черный', 'BMW')
my_car.go()
my_car.stop()
print(my_car.name)
