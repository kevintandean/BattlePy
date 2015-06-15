class Player(object):
    def __init__(self, name='player'):
        self.ships = None
        self.name = name
        self.initPlayer()

    def initPlayer(self):
        pass

    def placeShips(self):
        raise NotImplemented

    def isShipPlacedLegally(self, refShip):
        if not refShip.isPlacementValid():
            return False

        for ship in self.ships:
            if refShip == ship:
                continue

            for location in refShip.locations:
                if location in ship.locations:
                    return False

        return True

    def shotHit(self, shot, ship):
        pass

    def shotMissed(self, shot):
        pass

    def shipSunk(self, ship):
        pass

    def getShot(self):
        raise NotImplemented

    def gameWon(self):
        pass

    def gameLost(self):
        pass

    def newGame(self):
        pass

    def opponentShot(self, shot):
        pass

    def _setShips(self, ships):
        self.ships = ships

    def _allShipsPlacedLegally(self):
        if not self.ships:
            return False

        allLocations = set()
        for ship in self.ships:
            if not ship.isPlacementValid():
                return False

            for location in ship.locations:
                if location in allLocations:
                    return False

            allLocations.update(ship.locations)

        return True

    def _checkIsHit(self, shot):
        hit = False
        hitShip = None
        for ship in self.ships:
            if shot in ship.shots and shot not in ship.hits:
                ship.addHit(shot)
                hit = True
                hitShip = ship
                break

        return hit, hitShip

    def _checkAllShipsSunk(self):
        done = True
        for ship in self.ships:
            if not ship.isSunk():
                done = False
                break
        return done

    def getInfo(self):
        print 'Ship Locations'
        for ship in self.ships:
            print '%s: %s Hits: %s' % (ship.name, sorted(list(ship.locations)), sorted(list(ship.hits)))
