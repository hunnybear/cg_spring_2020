import sys
import collections
import math

pac_fields = ['pac_id', 'mine', 'x', 'y', 'type_id', 'speed_turns_left', 'ability_cooldown']

Pac = collections.namedtuple('Pac', pac_fields)
Pellet = collections.namedtuple('Pellet', ['x', 'y', 'value'])

class Map(object):

    def __init__(width, height):
        self.width = width
        self.height = height
        self.cleared = set()
        self.pellets = set()

    def process(pacs, pellets):
        

# Grab the pellets as fast as you can!

# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]
for i in range(height):
    row = input()  # one line of the grid: space " " is floor, pound "#" is wall

got_rude = False

def get_islands(pellets):
    islands = set()
    pellets = set(pellets)

    while pellets:
        borders = islan

# game loop
while True:
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())  # all your pacs and enemy pacs in sight
    my_pacs = set()
    their_pacs = set()
    pellets = {}

    command = []

    for i in range(visible_pac_count):
        # pac_id: pac number (unique within a team)
        # mine: true if this pac is yours
        # x: position in the grid
        # y: position in the grid
        # type_id: unused in wood leagues
        # speed_turns_left: unused in wood leagues
        # ability_cooldown: unused in wood leagues
        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
        pac_id = int(pac_id)
        mine = mine != "0"
        x = int(x)
        y = int(y)
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)
        pac = Pac(pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown)
        if mine:
            my_pacs.add(pac)
        else:
            their_pacs.add(pac)
        if any(any(abs(mine.x-theirs.x) <=1 and abs(mine.y-theirs.y) <= 1 for theirs in their_pacs) for mine in my_pacs):
            print("got rude", file=sys.stderr)
            got_rude=True
    visible_pellet_count = int(input())  # all pellets in sight
    for i in range(visible_pellet_count):
        # value: amount of points this pellet is worth
        x, y, val = [int(j) for j in input().split()]
        pellets[(x,y)] = val

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if False and not got_rude and their_pacs:
        their_pacs = list(their_pacs)
        for pac in my_pacs:
            their_pac = their_pacs.pop()
            command.append("MOVE {} {} {}".format(pac.pac_id, their_pac.x, their_pac.y))
            their_pacs.append(their_pac)

    print(pellets, file=sys.stderr)
    # the max(pellets.values()) is super computation-wasteful, but it amuses me to make the silly one liner
    max_pellets = set((pos) for pos, score in pellets.items() if score == max(pellets.values()))
    for pac in my_pacs:
    # just go for the nearest damn high value pellet

        nearest_max = min(max_pellets, key=lambda p: abs(p[0] - pac.x) + abs(p[1] - pac.y))
    
        command.append('MOVE {} {} {}'.format(pac.pac_id, nearest_max[0], nearest_max[1]))
    print('|'.join(command))    
