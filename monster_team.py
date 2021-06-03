from monster_custom import Wolf, Magician, Giant, Skeleton
from pathlib import Path
from random import randint, choice
import os.path
import operator

class MonsterTeam():
    def __init__(self, level: int):
        if type(level) is not int:
            raise AttributeError("Level must be an integer.")

        folder = Path('levels')
        levels = folder / f'level_{level}.txt'

        self._monsters = []
        with levels.open() as enemies:
            e_types = {
                'wolf': Wolf,
                'giant': Giant,
                'magician': Magician,
                'skeleton': Skeleton,
            }
            enemies = enemies.read().splitlines()
            for enemy in enemies:
                e_type, e_level = enemy.split(':')
                self._monsters.append(e_types[e_type](int(e_level)))

    def __len__(self):
        return len(self._monsters)

    def __str__(self):
        ordered = sorted(self._monsters, reverse=True)
        ordered = [str(monster) for monster in ordered]
        ordered = '\n'.join(ordered)
        first_line = f'{len(self.alive_monsters)}/{len(self._monsters)} monsters:\n'
        return first_line + ordered
    
    @property
    def is_alive(self):
        alive = [monster for monster in self._monsters if monster.is_alive]
        return len(alive) != 0
    
    @property
    def health(self):
        return sum(monster.health for monster in self._monsters)
    
    @property
    def power(self):
        return sum(monster.power for monster in self.alive_monsters)
    
    @property
    def healthiest_monster(self):
        return self.alive_monsters[0]

    @property
    def weakest_monster(self):
        ordered_by_power = sorted(self.alive_monsters, key=operator.attrgetter('power'))
        return ordered_by_power[0]

    @property
    def alive_monsters(self) -> list:
        alive = [monster for monster in self._monsters if monster.is_alive]
        return sorted(alive, reverse=True)

    def get_alive_monster(self) -> object:
        """ Returns a random alive monster """
        alive = [monster for monster in self._monsters if monster.is_alive]
        return choice(alive)
    
    @property
    def alive_types(self) -> list:
        """ Returns the types of monsters alive """
        alive_type = []
        for monster in self.alive_monsters:
            if monster.name not in alive_type:
                alive_type.append(monster.name)
        return alive_type
    
    @property
    def all_monsters(self):
        """ Returns all monsters in the team """
        return self._monsters

    def next_turn(self):
        """ Changes attributes from monsters in team """
        wolf_counter = 0
        for monster in self.alive_monsters:
            if isinstance(monster, Wolf):
                wolf_counter += 1
            elif isinstance(monster, Magician) and monster.is_alive:
                for enemy in self._monsters:
                    if not isinstance(enemy, Magician):
                        enemy.health += enemy.health * 0.1
        for monster in self.alive_monsters:
            if isinstance(monster, Wolf):
                monster.power += wolf_counter if wolf_counter > 1 else 0

if __name__ == '__main__':
    team = MonsterTeam(5)
    print(team.alive_monsters)
    team._monsters[0].health = 0
    team._monsters[1].health = 0
    print(team.power)
    print(team)