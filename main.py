
class Hero():
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f'{self.name} атаковал {other.name}')
        print(f'{other.health}HP осталось у {other.name}')

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

    def start(self):
        while self.player.health > 0 and self.computer.health > 0:
            self.player.attack(self.computer)
            self.computer.attack(self.player)
        if self.player.health < 0:
            print(f'{self.computer.name} победил')
        else:
            print(f'{self.player.name} победил')

hero1 = Hero('Дровосек')
hero2 = Hero('Пекка', 300, 40)
game1 = Game(hero1, hero2)
game1.start()