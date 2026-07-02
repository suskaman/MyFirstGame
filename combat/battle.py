from characters.monster import Monster
from characters.player import Player
import random

class Combat:
    player: Player
    monster: Monster

    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def fight(self):
        while self.monster.is_alive() and self.player.is_alive():

            print(f"ход {self.player.name}")
            self.player.get_stats()
            self.player.defence = 0
            match input():
                case "базовая атака":
                    damage = self.player.deal_damage()
                    self.monster.take_damage(damage)
                case "занять оборону":
                    self.player.take_defence()


            print(f"ход {self.monster.name}")
            self.monster.get_stats()
            self.monster.defence = 0
            rand = random.randint(1, 2)
            match rand:
                case 1:
                    print(f"{self.monster.name} наносит урон")
                    damage = self.monster.deal_damage()
                    self.player.take_damage(damage)
                case 2:
                    print(f"{self.monster.name} занимает оборону")
                    self.monster.take_defence()

        if not self.monster.is_alive():
            self.player.get_exp(self.monster.exp_reward)
            self.player.get_stats()
        else:
            self.player.get_stats()


if __name__ == "__main__":
    p = Player()
    m = Monster('monster', 1, 1, 0, 5)
    c = Combat(p, m)
    c.fight()