class Character:
    name: str
    _hp: float
    damage: int
    defence: float

    def __init__(self, name):
        self.name = name

    def is_alive(self):
        if self._hp > 0:
            return True
        else:
            return False

    def deal_damage(self):
        return self.damage

    def take_damage(self, damage):
        self._hp -= damage-self.defence
        if not self.is_alive():
            del self

    def take_defence(self):
        self.defence += 1

    def get_stats(self):
        pass