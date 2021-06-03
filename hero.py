from monster import Monster
from monster_team import MonsterTeam
from monster_custom import Wolf
import random
import text_utils

class Hero():
    def __init__(self, name: str, gold: int = 0):
        self.name = name
        self.health = 100.00
        self.power = 50.00
        self.gold = 0
        self.critical_chance = 0.09

    @property
    def is_alive(self) -> bool:
        """ Checks if hero is alive or not """
        return self.health > 0

    def __str__(self) -> str:
        power = f'{self.power} power'
        bar = text_utils.health_bar(self.health)
        name_n_health = f'{self.name:<10} [{bar}] {self.health} HP'
        pwr_crit_gold = f'{power}  |  {round(100 * self.critical_chance, 2)}% crit chance'
        pwr_crit_gold += f'  |  {self.gold} gold'

        return text_utils.nyoko_scroll([name_n_health, pwr_crit_gold])

    def attack_specific(self, enemy: object) -> None:
        """ Attacks a specific enemy, enemy counter attacks """
        if not isinstance(enemy, Monster):
            raise TypeError("Function takes a Monster object")
        
        # Tries for critical damage
        if random.random() < self.critical_chance:
            enemy.health -= (2 * self.power)
            critical = True
        else:
            enemy.health -= self.power
            critical = False
        enemy.health = round(enemy.health, 2)
        
        self.health -= enemy.power
        self.health= round(self.health, 2)
        return critical

    def attack(self, monster_team: object) -> None:
        """ Damages random, hero suffers counter damage"""
        if not isinstance(monster_team, MonsterTeam):
            raise TypeError("function takes a MonsterTeam")
        
        enemy = monster_team.get_alive_monster()
        # Tries for critical strike chance
        return self.attack_specific(enemy)

    def block(self, monster_team: object) -> None:
        """ Counterattacks enemy, hero takes 30% damage """
        if not isinstance(monster_team, MonsterTeam):
            raise TypeError("function takes a MonsterTeam")
        
        enemy = monster_team.get_alive_monster()
        # Tries for critical strike chance
        if random.random() < self.critical_chance:
            enemy.health -= (2 * self.power) * 0.5
            critical = True
        else:
            enemy.health -= self.power * 0.5
            critical = False
        enemy.health = round(enemy.health, 2)

        self.health -= enemy.power * 0.3
        self.health = round(self.health, 2)
        return critical, enemy


if __name__ == "__main__":
    hati = Hero("Hati")
    wolf = Wolf(3)
    print(hati)
    hati.critical_chance = 1
    critical = hati.attack(wolf)
    if critical:
        print(f'You hit {type(wolf).__name__} for critical damage!')

