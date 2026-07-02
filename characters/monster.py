from characters.character import Character
class Monster(Character):
    _exp_reward: int

    def __init__(self, name, _hp, damage, defence, exp_reward):
        super().__init__(name)
        self._hp = _hp
        self.damage = damage
        self.defence = defence
        self.exp_reward = exp_reward

    def get_stats(self):
        if not self.is_alive():
            print(f"{self.name} погиб")

        status = (f"-----------------------\n"
                  f"name: {self.name}\n"
                  f"stats:\n"
                  f"    hp: {self._hp}\n"
                  f"    damage: {self.damage}\n"
                  f"    defence: {self.defence}\n"
                  f"-----------------------\n")
        print(status)

if __name__ == "__main__":
    p = Monster('monster', 10, 1, 1, 5)
    print(p.get_stats())
    p.take_damage(5)
    print(p.get_stats())
    p.take_damage(30)
    print(p.get_stats())