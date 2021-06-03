import text_utils
import time
from art import text2art
from pathlib import Path
from shop import Shop

def attacking(monster_team: object, choice: int, hero: object, displaying: list):
    """ Performs logistics of attacking a monster """
    alive_monsters = monster_team.alive_monsters
    to_print = displaying
    try:
        choice = int(choice)
        old_health = hero.health
        old_m_health = alive_monsters[choice].health
        critical = hero.attack_specific(alive_monsters[choice])
        damage_taken = old_health - hero.health
        damage_dealt = old_m_health - alive_monsters[choice].health
    except (IndexError, ValueError):
        to_print.append(f'{" " * 28}{choice} is not a valid monster number.')
        return None
    
    if critical:
        to_print.append(f'\nYou dealt critical damage!!')
        to_print.append(f'Attacked for {2 * hero.power} AP and lost {damage_taken} HP')
    else:
        to_print.append(f'\nAttacked for {damage_dealt} AP and lost {damage_taken} HP')
    text_utils.clear_console()
    to_print.append(' ' * 100)
    print(text_utils.centerfy(to_print))
    monster_team.next_turn()

def blocking(monster_team: object, hero: object, displaying: list):
    """ Performs blocking logistics """
    old_hero_health = hero.health
    critical, enemy = hero.block(monster_team)
    main_before_choice = displaying[::]
    damage_taken = round(old_hero_health - hero.health, 2)
    if critical:
        main_before_choice.append('\nYou dealt critical damage!!')
    main_before_choice.append(f"\nYou blocked a {enemy.name} and lost {damage_taken} HP")
    main_before_choice.append(' ' * 100)
    text_utils.clear_console()
    print(text_utils.centerfy(main_before_choice))
    monster_team.next_turn()
    time.sleep(2.3)
    text_utils.clear_console()

def get_shop_art(shop: object, hero: object) -> list:
    """ Parses and returns list of art for the shop """
    folder = Path('art')
    shop_text = folder / 'shop.txt'
    strings = []

    # Get shop sign and Nyoko talking
    with shop_text.open() as shop_art:
        strings.append(shop_art.read())
    strings.append(text_utils.nyoko_talks(['Nyoko has wares if you have coin.', 'Items reset every level.',
    f'I see that you have {hero.health}% HP,', 
    f'{hero.power} AP and {round(hero.critical_chance * 100, 2)}% crit chance']))
    return strings

def get_items_frame(shop) -> list:
    """ Returns 2 lists, one with each item information and the other with the item name """
    # Get items and list them, with cost, effect, amount, and name
    item_list_str = []
    item_list_name = []
    number = 0
    for item, amount in shop.items_dict.items():
        item_obj = shop.get_by_name(item)
        if amount > 0:
            effect = f'({item_obj.effect})'
            capital = item.capitalize()
            item_str = f'|{number}] {capital:<20} {effect:<10}| {item_obj.price} gold |'
            item_str += f' {amount} in stock|'
            item_list_name.append(item)
            number += 1
            item_list_str.append(item_str)

    return item_list_str, item_list_name

def get_choice(shop, hero, item_list_name):
    """ Gets the item the player wants """
    choice = input(f'        So, what item do you want? (Gold: {hero.gold})\t')
    try:
        choice = int(choice)
        choice = item_list_name[choice]
        choice = shop.buy_by_name(choice)
        if hero.gold < choice.price:
            return('\n        You do not have enough gold to purchase this item.')
        hero.gold -= choice.price
        choice.change(hero)
        return(f'\n        You purchased {choice.name.capitalize()}')
    except (ValueError, IndexError):
        return(f'\n        {choice} is not a valid item.')

def shopping(shop: object, hero: object):
    """ Performs logistics of shopping """
    text_utils.clear_console()
    strings = get_shop_art(shop, hero)

    item_list_str, item_list_name = get_items_frame(shop)

    strings.append('\n'.join(item_list_str))
    strings.append('-' * 57)
    strings.append('\n')
    strings.append(' ' * 100)
    print(text_utils.centerfy(strings))

    # Get the item the player wants
    print(get_choice(shop, hero, item_list_name))
    time.sleep(1.8)
    text_utils.clear_console()

def defeated_logistics(monster_team: object, hero: object, level):
    """ Performs defeated logistics """
    level_defeated = text2art(f'LEVEL     {level}', font='doom')
    defeated = text2art('DEFEATED', font='doom')

    gold = sum(monster.gold_drop for monster in monster_team.all_monsters)
    hero.gold += gold
    total_gold = f'Total gold acquired: {gold}'

    health = 10 * level
    hero.health += health
    hero.health = 100 if hero.health > 100 else hero.health
    health_regenerated = f'Health regenerated: {health}'

    print(text_utils.centerfy([level_defeated, defeated, total_gold, health_regenerated]))
    time.sleep(2.5)
    text_utils.clear_console()