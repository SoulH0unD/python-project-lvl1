from brain_games.games.calc import calc
from brain_games.games.even import even
from brain_games.games.gcd import gcd
from brain_games.games.prime import prime
from brain_games.games.progression import progression

def engine(name_games: str):
    if name_games == 'calc':
        calc()
    elif name_games == 'even':
        even()
    elif name_games == 'gcd':
        gcd()
    elif name_games == 'prime':
        prime()
    elif name_games == 'progression':
        progression()