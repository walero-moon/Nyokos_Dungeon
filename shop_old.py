from hero import Hero

class Shop():
    def __init__(self):
        self._available_items = [
            SmallHealingPotion(),
            SmallHealingPotion(),
            SmallHealingPotion(),
            BigHealingPotion(),
            WeaponUpgrade()
        ]

    @property
    def available_items(self):
        return self._available_items


    def buy(self, item: int):
        if isinstance(self.available_items[item], WeaponUpgrade):
            return self.available_items[item]
        else:
            return self.available_items.pop(item)


class BigHealingPotion():
    def __init__(self):
        self.price = 3
        self.name = 'Big Healing Potion | +50 ❤, 3 gold'


    def change(self, hero: object):
        hero.health += 50
        hero.gold -= self.price


class SmallHealingPotion():
    def __init__(self):
        self.price = 1
        self.name = 'Small Healing Potion | +10 ❤, 1 gold'

    def change(self, hero: object):
        hero.health += 10
        hero.gold -= self.price


class WeaponUpgrade():
    def __init__(self):
        self.price = 1
        self.name = 'Weapon Upgrade | +5% ⚔, 1 gold'
        
    def change(self, hero: object):
        hero.power += hero.power * 0.05
        hero.gold -= self.price


if __name__ == '__main__':
    hero = Hero('Hati')
    hero.gold = 10
    shop = Shop()