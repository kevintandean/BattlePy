from ship import Ship

BOARD_HEIGHT = 10
BOARD_WIDTH = 10

def getDefaultShips():
    return [Ship('Carrier', 5),
            Ship('Battleship', 4),
            Ship('Destroyer', 3),
            Ship('Submarine', 3),
            Ship('Patrol Boat', 2)]

