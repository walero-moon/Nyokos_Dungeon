from abc import ABC, abstractmethod, abstractproperty
import time

class ShopItem(ABC):
    @abstractproperty
    def effect(self):
        pass

    @abstractproperty
    def price(self):
        pass

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def change(self, hero):
        pass

    def __str__(self):
        return f"{self.name} ({self.price} gold)"

class BigHealingPotion(ShopItem):
    effect = '+50 HP'
    name = "big healing potion"
    price = 3
    def change(self, hero):
        """ Gives hero 50 health points """
        hero.health = hero.health + 50
        hero.health = 100 if hero.health > 100 else hero.health
    
class SmallHealingPotion(ShopItem):
    effect = '+10 HP'
    name = "small healing potion"
    price = 1
    def change(self, hero):
        """ Gives hero 10 health points """
        hero.health = hero.health + 10

class SuperHealingPotion(ShopItem):
    effect = '+75 HP'
    name = "super healing potion"
    price = 5
    def change(self, hero):
        """ Gives hero 75 health points """
        hero.health = hero.health + 75
        hero.health = 100 if hero.health > 100 else hero.health

class WeaponUpgrade(ShopItem):
    effect = '+5% AP'
    name = "weapon upgrade"
    price = 1
    def change(self, hero):
        """ Increases hero power by 5% """
        hero.power = round(hero.power * 1.05, 2)

class SuperWeaponUpgrade(ShopItem):
    effect = '+15% AP'
    name = "super weapon upgrade"
    price = 3
    def change(self, hero):
        """ Increases hero power by 15% """
        hero.power = round(hero.power * 1.15, 2)

class CriticalDagger(ShopItem):
    effect = '+5% crt'
    name = "critical dagger"
    price = 2
    def change(self, hero):
        """ Increses Hero's critical strike chance by 5% """
        hero.critical_chance += 0.05

class CurvedBlade(ShopItem):
    effect = '+10% crt'
    name = "curved blade"
    price = 4
    def change(self, hero):
        """ Increses Hero's critical strike chance by 10% """
        hero.critical_chance += 0.10