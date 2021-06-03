import text_utils

class Monster():
    def __init__(self, level):
        if type(level) is not int:
            raise AttributeError("Level must be a number.")
        self.level = level
        self._max_health = 10 + level * 10
        self.health = 10 + level * 10
        self.power = level * 5
    
    def __str__(self):
        if self.health > 0:
            return f'{type(self).__name__} ({self.health:.2f} health, {self.power:.2f} power)'
        else:
            return f'{type(self).__name__} (DEAD)'

    def __lt__(self, other):
        if not isinstance(other, Monster):
            raise TypeError("Can only compare with type Monster")
        return (self.health, self.power) < (other.health, other.power)

    @property
    def pretty_str(self):
        """ Prettier string for monster """
        if self.health <= 0:
            return f'{type(self).__name__} (DEAD)'

        health_bar = text_utils.health_bar(self.health, total_hashes=10, max_health=30)
        return f'{type(self).__name__} [{health_bar}] {self.health} HP, {self.power} AP'

    @property
    def is_alive(self) -> bool:
        """ Checks if monster is alive or dead """
        return self.health > 0