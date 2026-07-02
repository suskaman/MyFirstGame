from characters.character import Character
# игрок
# есть опыт, хп, сила, ловкость, урон, защита, инвентарь, инициатива
# может наносить урон, получать урон, брать предметы, получать опыт
#
#
#

class Player(Character):
    name: str
    damage: int = 1
    defence: float = 0

    _lvl: int = 0
    _exp: int = 0
    _exp_for_next_lvl: int = 10
    _strength: int = 0 # сила - здоровье/урон
    _dexterity: int = 0 # ловкость - инициатива/защита
    _max_hp: int = 10

    def __init__(self, name = 'player'):
        super().__init__(name)
        self._hp = self._max_hp

    def get_new_lvl(self):
        self._lvl += 1
        self._exp = 0

        self._strength += 1
        self.damage += 1
        self._max_hp += 10
        self._hp = self._max_hp

        self._dexterity += 1
        self.defence += 0.5

    def get_exp(self, exp):
        self._exp += exp
        if self._exp >= self._exp_for_next_lvl:
            self._exp_for_next_lvl *= 1.5
            self.get_new_lvl()

    def get_stats(self):
        if not self.is_alive():
            print(f"{self.name} погиб")

        status = (f"-----------------------\n"
                  f"name: {self.name}\n"
                  f"lvl: {self._lvl}\n"
                  f"exp for next lvl: {self._exp_for_next_lvl - self._exp}\n"
                  f"stats:\n"
                  f"    hp: {self._hp}\n"
                  f"    strength: {self._strength}\n"
                  f"    dexterity: {self._dexterity}\n"
                  f"    damage: {self.damage}\n"
                  f"    defence: {self.defence}\n"
                  f"-----------------------\n")
        print(status)


if __name__ == "__main__":
    p = Player()
    print(p.get_stats())
    p.take_damage(5)
    print(p.get_stats())
    p.get_exp(10)
    print(p.get_stats())
    p.take_damage(10)
    print(p.get_stats())


