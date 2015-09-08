import path
#import twitter

class swapper:
    def __init__(self, debug=False):
        self.DEBUG = debug
        self.PATH = path.path()
        self.lobby = 'none'
        self.game = 'none'
        self.mapA = 'none'
        self.mapB = 'none'

    def checkTwitter(self):
        #set lobby, game, mapA, mapB
        return

    def swapMaps(self, mapA, mapB):
        #swap the map files so they're current
        self.setMap("A", mapA)
        self.setMap("B", mapB)
        return

    def setMap(self, map):
        #setting an individual map file
        return

    def setText(self, txt):
        #overwrite the current.txt file with self.game
        return

if __name__ == "__main__":
    s = swapper()
