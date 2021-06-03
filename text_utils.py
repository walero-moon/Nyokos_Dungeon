import os
import platform
import itertools
from pathlib import Path

def clear_console():
    """ Detects the operating system and clears the console """
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

def health_bar(current_health: int, max_health: int = 100, total_hashes: int = 20,
health_character: str = '█', missing_character: str = '░') -> str:
    """ Returns the entity's health in bar form. """
    convert_hashes = int(max_health / total_hashes)
    health_dashes = int(current_health / convert_hashes)
    remaining_spaces = total_hashes - health_dashes

    # Makes the bar
    existing_health = health_character * health_dashes
    missing_health = missing_character * remaining_spaces

    return f'{existing_health}{missing_health}'

def get_str_length(strings: list, add: int=8):
    """ Returns longest string's length from a list of strings """
    length = 0
    for string in strings:
        length = len(string) if len(string) >= length else length
    length += add
    return length

def scrollify(strings: list, justification: str = '^') -> str:
    """ Makes a pretty string inside a scroll"""
    length = get_str_length(strings)
    line = '-' * (length + 4)
    underline = '_' * (length + 4)
    space = ' ' * (length + 4)
    ending_space = ' ' * (len(space) - 2)
    # Scroll walls
    scroll_ho = '| |'
    scroll_fi = '|-|'
    # Makes scroll's first lines
    string_final = (
        f' _ {space} _ \n'
        f'(@){space}(@)\n'
        f'|-|{line}|-|\n'
        f'{scroll_ho:<{len(space) + 3}}{scroll_ho}\n'
    )
    # Fills the scroll with content
    for string in strings:
        string_final += (
            f'{scroll_ho:<5}{string:{justification}{length}}{scroll_fi:>5}\n'
            f'{scroll_fi:<{len(space) + 3}}{scroll_ho}'
            '\n'
        )
    # Finishes the scroll
    string_final += f'|_|{underline}|_|\n'
    string_final += f'(@){ending_space}`\{scroll_fi}\n'
    string_final += f'   {space}(@)'
    return string_final

def nyoko_scroll(strings: list, justification: str = '^') -> str:
    """ Makes a pretty string inside a scroll with nyoko peeking """
    length = get_str_length(strings)
    # Scroll parts
    line = '-' * (length + 4)
    underline = '_' * (length + 4)
    space = ' ' * (length + 4)
    scroll_ho = '| |'
    scroll_fi = '|-|'
    ending_space = ' ' * (len(space) - 2)

    # Nyoko parts
    ears = '|\_/|(\\'
    face = '(- -) ))'
    paws = 'w---w'
    first_line_space = int((len(space) - 9)) * ' '
    second_line_space = int((len(space) - 11)) * ' '
    third_line_dash = int((len(space) - 8)) * '-'
    # Makes scroll's first lines
    string_final = (
        f' _    {ears}{first_line_space}_\n'
        f'(@)   {face}{second_line_space}(@)\n'
        f'|-|---{paws}{third_line_dash}|-|\n'
        f'{scroll_ho:<{len(space) + 3}}{scroll_ho}\n'
    )
    # Fills scroll with content
    for string in strings:
        string_final += (
            f'{scroll_ho:<5}{string:{justification}{length}}{scroll_fi:>5}\n'
            f'{scroll_fi:<{len(space) + 3}}{scroll_ho}'
            '\n'
        )

    # Finishes scroll
    string_final += f'|_|{underline}|_|\n'
    string_final += f'(@){ending_space}`\{scroll_fi}\n'
    string_final += f'   {space}(@)'
    return string_final

def blockify(strings: list, justification: str = '^', spaced=True) -> str:
    """ Makes a pretty string inside a block"""
    length = get_str_length(strings)
    underline = '_' * (length + 2)
    space = ' ' * (length + 4)
    empty = ' '
    wall = '|'
    # Makes first lines of block
    string_final = (
        f'_{space}    _\n'
        f'\`~.{underline}.~´/\n'
        f' {wall:<5}{empty:<{length}}{wall:>3}\n'
    )
    # Fills block with content
    for string in strings:
        string_final += (
            f' {wall:<5}{string:{justification}{length}}{wall:>3}\n'
        )
        if spaced:
            string_final += f' {wall:<5}{empty:<{length}}{wall:>3}\n'
    # Finishes block
    string_final += f' \\{underline}____/'
    return string_final

def longest_line_len(string: str) -> int:
    """ Returns the length of the longest line in a string """
    length = 0
    for line in string.splitlines():
        length = len(line) if len(line) >= length else length
    return length

def centerfy(strings: list) -> str:
    """ Takes a list of strings and centers them relative to each other """
    # Discovers how long the longest string is
    length = 0
    for string in strings:
        longest = longest_line_len(string)
        length = longest if longest >= length else length

    final_string = ''
    # Checks if current string is longest, fixes it to center if it isn't
    for string in strings:
        longest_sec_str = longest_line_len(string)
        fixed_str = ''
        if longest_sec_str != length:
            space = ' '
            for line in string.splitlines():
                line = f'{line}\n' if not line.endswith('\n') else line
                fixed_str += f'{space * int((length - longest_sec_str)/ 2)}{line}'
            final_string += f'{fixed_str}'
        else:
            for line in string.splitlines():
                line = f'{line}\n' if not line.endswith('\n') else line
                fixed_str += f'{line}'
            final_string += string

    return final_string

def nyoko_talks(lines: list) -> str:
    """ Returns a string with nyoko and a message inside a bubble """
    # Calculates proper amount of white spaces and characters to build the bubble
    length = 0
    for string in lines:
        length = len(string) if len(string) >= length else length
    underline = '_'
    empty = ' '
    reduced_len = length - 6
    folder = Path('art')
    nyoko = folder / 'nyoko.txt'
    amount_of_sentences = len(lines)

    # Builds start of the bubble, which is fixed
    string_final = (
        f'\n {empty:<24}  {underline * reduced_len}________\n'
        f'{empty:<24}  /{(empty * length)}  \\'
    )

    # Builds message part of the bubble
    for index, line in enumerate(lines):
        if index == amount_of_sentences - 1:
            string_final += (
                f'\n _._     _,-\'""`-._       | {line:<{length}} |\n'
            )
        else:
            string_final += (
                f'\n{empty:<24}  | {line:<{length}} |'
        )
        
    # Finishes building the bubble
    string_final += (
        f'(,-.`._,\'(       |\`-/|   |       {underline * reduced_len}_/\n'
    )
    with nyoko.open() as cat:
        string_final += cat.read()
    return string_final

def side_by_side(*strings, space=30):
    # Puts every string's line in its own list, inside another list
    lines = [
        my_string.split("\n")
        for my_string in strings
    ]

    # zip takes the first element of each list here, and puts them together 
    # inside a new list.
    combined = zip(*lines)

    output = []
    for line in combined:
        # Takes every string inside the list, combines it into a single string
        # and appends it to a new list.
        indented = "".join(f"{element:<{space}}" for element in line)
        output.append(indented)
    # Takes every line (which is its own item inside the list) and separates them
    # by new line.
    return "\n".join(output)

if __name__ == '__main__':
    print(blockify(['String1 over here', 'String 2 over here']))
    art = Path('art')
    giant = art / 'giant.txt'
    with giant.open() as g_art:
        giant = g_art.read()
    wolf = art / 'wolf.txt'
    with wolf.open() as w_art:
        wolf = w_art.read()
    
    print(nyoko_scroll(["This is just a text scrollllllllllll", "Nothing more",
    "I wonder how long I can make these strings before it starts to collapse"],
    justification='<'))
    # print(wolf)
    # print(giant)
    # print(side_by_side(wolf, giant, space=10))