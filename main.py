import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Здоровье: {self.health})"


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            print(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден. {self.player.name} выиграл!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден. {self.computer.name} выиграл!")
                break


if __name__ == "__main__":
    # Создание героев
    player_name = input("Введите имя вашего героя: ")
    player = Hero(player_name)
    computer = Hero("Компьютер", health=100, attack_power=random.randint(15, 25))

    # Запуск игры
    game = Game(player, computer)
    game.start()

