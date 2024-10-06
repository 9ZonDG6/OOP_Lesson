from time import sleep


class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def _get_damage(self, target):
        return max(0, self.damage - target.armor)

    def attack(self, pres):
        pres.health -= self._get_damage(pres)
        pres.health = max(0, pres.health)


class Player(Person):
    def __init__(self, health, damage, armor):
        super().__init__(health, damage, armor)


class Enemy(Person):
    def __init__(self, health, damage, armor):
        super().__init__(health, damage, armor)


def start_game():
    print(f'Здоровье игрока: {ZonD.health}\n'
          f'Здоровье врага: {Slime.health}\n'
          'Игрок начинает!\n')

    while ZonD.health > 0 and Slime.health > 0:
        ZonD.attack(Slime)
        print(f'Здоровье врага: {Slime.health}')
        sleep(1)

        if Slime.health <= 0:
            print('Враг побежден!')
            break

        Slime.attack(ZonD)
        print(f'Здоровье игрока: {ZonD.health}')
        sleep(1)

        if ZonD.health <= 0:
            print('Игрок потерпел поражение!')
            break


ZonD = Player(100, 15, 15)
Slime = Enemy(50, 20, 5)
start_game()
