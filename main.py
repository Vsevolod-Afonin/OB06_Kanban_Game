
class Hero():
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f'{self.name} атаковал {other.name}')

    def info(self):
        print(f" Имя - {self.name}")
        print(f" Здоровье - {self.health}")
        print(f" Сила атаки - {self.attack_power}")

    def is_alive(self):
        if self.health > 0:
            print(True)

class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer