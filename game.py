import random
from art import text2art
import text_utils
from pathlib import Path
import utils
import time
import os
import msvcrt
from hero import Hero
from monster_team import MonsterTeam
from shop import Shop, BigHealingPotion, SmallHealingPotion, WeaponUpgrade
from shop import CriticalDagger, CurvedBlade, SuperWeaponUpgrade, SuperHealingPotion
from monster_custom import Wolf, Giant, Magician

def initialize():
    """ Shows game's start screen. """
    # Sets console window size
    text_utils.clear_console()
    # os.system("mode con cols=100 lines=40")
    title1 = text2art('    NYOKO\'S', font='doom')
    title2 = text2art('    DUNGEON', font='doom')
    nyoko_sleep = Path('art')
    nyoko_sleep = nyoko_sleep / 'nyoko_sleep.txt'
    with nyoko_sleep.open() as n_art:
        nyoko_sleep = n_art.read()
    print("Nyoko's Dungeon.\n\nPlease maximize the window for the best experience")
    time.sleep(2.8)
    text_utils.clear_console()
    title = text_utils.centerfy([title1, title2])
    print(text_utils.centerfy([title, nyoko_sleep, ' ' * 100]))
    print('Enter your hero\'s name: ', end='')
    return input()

def get_art():
    """ Returns all art from text file that will be used in the game """
    aart = Path('art')
    giant = aart / 'giant.txt'
    magician = aart / 'wizard.txt'
    sword = aart / 'sword.txt'
    wolf = aart / 'wolf.txt'
    skeleton = aart / 'skeleton.txt'
    with giant.open() as art:
        giant = art.read()
    with wolf.open() as art:
        wolf = art.read()
    with magician.open() as art:
        magician = art.read()
    with sword.open() as art:
        sword = art.read()
    with skeleton.open() as art:
        skeleton = art.read()
    return giant, wolf, magician, skeleton, sword

def all_monster_art(monster_team: object, art: list):
    """ Returns a string with each monster in the team side by side """
    giant, wolf, magician, skeleton = art
    monsters_ascii = {
        'wolf': wolf,
        'giant': giant,
        'magician': magician,
        'skeleton': skeleton
    }
    all_m_ascii = []
    for index, monster in enumerate(monster_team.alive_monsters):
        bar = f'[{monster.health} HP  |  {monster.power} AP]\n'
        current_monster = f'{monsters_ascii.get(monster.name)}\n'
        m_level = f'Level {monster.level} {monster.name}\n'
        m_number = f'[ {index} ]'
        all_m_ascii.append(text_utils.centerfy([bar, current_monster, m_level, m_number]))
    all_m_ascii = text_utils.side_by_side(*all_m_ascii, space=25)
    return all_m_ascii

def print_main_w_choices(monster_team: object, hero: object):
    """ Prints the choice screen of the game, with hero's information and mosnters """
    giant, wolf, magician, skeleton, sword = get_art()
    main = [f'{str(hero)}\n', all_monster_art(monster_team, [giant, wolf, magician, skeleton])] 
    main.append(f'\n{sword}')
    main_before_choice = main[::]
    main.append("What will you do?")
    main.append("\n[A]ttack    |    [B]lock    |    [S]hop")
    main.append(' ' * 100)
    print(text_utils.centerfy(main))
    return main_before_choice

def main():
    """ Initializes game and runs necessary tasks """
    level = 1
    monsterTeam = MonsterTeam(level)
    shop = Shop()
    hero = Hero(initialize())
    text_utils.clear_console()

    while hero.is_alive:
        # Prints monster and hero info
        main_before_choice = print_main_w_choices(monsterTeam, hero)

        # Gets user action and executes it
        choice = msvcrt.getwch().lower()
        if choice == 'a':
            text_utils.clear_console()
            main_before_choice.append(' ' * 100)
            print(text_utils.centerfy(main_before_choice))
            print(' ' * 28, 'Enter desired monster\'s number (e.g. 0): ', end='')
            attack_choice = input()
            utils.attacking(monsterTeam, attack_choice, hero, main_before_choice)
            time.sleep(2.3)
            text_utils.clear_console()

        elif choice == 'b':
            utils.blocking(monsterTeam, hero, main_before_choice)
        elif choice == 's':
            utils.shopping(shop, hero)
        else:
            text_utils.clear_console()


        if hero.is_alive and not monsterTeam.is_alive:
            utils.defeated_logistics(monsterTeam, hero, level)

            if level > 2:
                shop.available_items.append(SmallHealingPotion())
                shop.available_items.append(SmallHealingPotion())
                shop.available_items.append(SmallHealingPotion())
                shop.available_items.append(BigHealingPotion())
                shop.available_items.append(WeaponUpgrade())
                shop.available_items.append(WeaponUpgrade())
                shop.available_items.append(WeaponUpgrade())
                shop.available_items.append(CriticalDagger())
                shop.available_items.append(CriticalDagger())
            if level > 4:
                shop.available_items.append(SuperHealingPotion())
                shop.available_items.append(SuperWeaponUpgrade())
                shop.available_items.append(CurvedBlade())
            if level > 5:
                shop.available_items.append(SuperHealingPotion())
                shop.available_items.append(SuperWeaponUpgrade())
                shop.available_items.append(CurvedBlade())

            level += 1
            if level == 8:
                aart = Path('./art')
                nyoko_exit = aart / 'nyoko_exit.txt'
                with nyoko_exit.open() as art:
                    nyoko_exit = art.read()
                final = [text2art('YOU   WON', font='doom')]
                final.append(nyoko_exit)
                print(text_utils.centerfy(final))
                print('Thanks for playing!!')
                break
            monsterTeam = MonsterTeam(level)

    print(f"\nYou survived {level} levels! Congratulations")
    quit = input("\nPress enter to quit")


if __name__ == '__main__':
    main()