from hero import Hero
from shop_item import BigHealingPotion, SmallHealingPotion, WeaponUpgrade
from shop_item import SuperHealingPotion, CriticalDagger, CurvedBlade, SuperWeaponUpgrade
import os.path

class Shop():
    def __init__(self, shop_file='shop.txt'):
        """ Gets the available items from the file and puts it in a list. """

        self._available_items = []
        items = {
            'small healing potion': SmallHealingPotion,
            'big healing potion': BigHealingPotion,
            'super healing potion': SuperHealingPotion,
            'weapon upgrade': WeaponUpgrade,
            'super weapon upgrade': SuperWeaponUpgrade,
            'critical dagger': CriticalDagger,
            'curved blade': CurvedBlade
        }

        if not shop_file == 'arcade':
            with open(shop_file, 'r') as shop:
                all_items = shop.read().splitlines()
                for item in all_items:
                    self._available_items.append(items[item]())

    def __str__(self):
        """ Returns a string containing all items in the shop """
        string = 'Welcome to the shop. The following items are available:'
        for count, item in enumerate(self.available_items, start=1):
            string += f'\n{count} - {item.name} ({item.price} gold)'
        return string

    def __len__(self):
        return len(self.available_items)

    @property
    def available_items(self):
        return self._available_items
    
    @property
    def items_dict(self):
        amount_items = {
            'small healing potion': 0,
            'big healing potion': 0,
            'weapon upgrade': 0,
            'super healing potion': 0,
            'critical dagger': 0,
            'super weapon upgrade': 0,
            'curved blade': 0
        }
        for item in self.available_items:
            amount_items[item.name] += 1
        return amount_items

    def get_by_name(self, name):
        """ Gets the item by name and returns a random object that matches """
        for item in self.available_items:
            if item.name == name:
                return item
    
    def buy(self, item: int):
        """ Returns an item from the shop and removes it from the available
            items list """
        return self.available_items.pop(item)

    def buy_by_name(self, wanted_item):
        """ Identifies the object, returns it and removes it from the shop. """
        for index, item in enumerate(self.available_items):
            if item.name == wanted_item:
                return self.available_items.pop(index)


if __name__ == '__main__':
    hero = Hero('Hati')
    hero.gold = 10
    shop = Shop()
    print(shop)
    item = shop.buy_by_name('small healing potion')
    item.change(hero)
    print(hero.gold)
    print(hero)