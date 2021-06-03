from monster import Monster

class Magician(Monster):
    def __init__(self, level):
        super().__init__(level)
        self.name = 'magician'
        self.health = 20
        self._max_health = 20
        self.power = 0
        self.gold_drop = 1 * level
    
class Wolf(Monster):
    def __init__(self, level):
        self.name = 'wolf'
        super().__init__(level)
        self._max_health = 10 + level * 10
        self.gold_drop = 2 * level

class Giant(Monster):
    def __init__(self, level):
        super().__init__(level)
        self.name = 'giant'
        self.power = self.power * 2
        self.health = self.health / 2
        self._max_health = (10 + level * 10) / 2
        self.gold_drop = 1 * level

class Skeleton(Monster):
    def __init__(self, level):
        super().__init__(level)
        self.name = 'skeleton'
        self.power = round(self.power * 2.5, 2)
        self.health = 10 + level * 5
        self._max_health = 10 + level * 5
        self.gold_drop = 1 * level
