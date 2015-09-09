import path
import twitter
import os

class swapper:
    def __init__(self, debug=False):
        self.DEBUG = debug
        self.PATH = path.path()
        self.lobby = 'none'
        self.game = 'none'
        self.mapA = 'none'
        self.mapB = 'none'
        self.mapAPath = 'none'
        self.mapBPath = 'none'

    def run(self):
        self.checkTwitter()
        self.prepMap("A", self.mapA)
        self.prepMap("B", self.mapB)
        self.swapMaps(self.mapAPath, self.mapBPath)
        self.setText(self.game)
        return

    def checkTwitter(self):
        #set lobby, game, mapA, mapB
        self.lobby, self.game, self.mapA, self.mapB = twitter.getRecent()
        #print "FOUND:", self.lobby, self.game, self.mapA, self.mapB
        return

    def prepMap(self, ab, map):
        words = map.split()
        filename = words[0].lower() + words[1] + ".png"
        if "A" not in ab:
            self.mapBPath = filename
        else:
            self.mapAPath = filename

    def swapMaps(self, mapA, mapB):
        #swap the map files so they're current
        self.setMap("A", mapA)
        self.setMap("B", mapB)
        return

    def setMap(self, ab, map):
        changeMap = "a.png"        
        if "A" not in ab:
            changeMap = "b.png"
        #cp <map.png> <aorb.png>
        cmd = "cp " + self.PATH.MAP_DIR + "/" + map + " "
        cmd = cmd + self.PATH.CURRENT_DIR + "/" + changeMap
        os.system(cmd)
        #setting an individual map file
        
        return

    def setText(self, txt):
        #overwrite the current.txt file with self.game
        f = open( self.PATH.CURRENT_DIR + "/" + self.PATH.TXT , 'w')
        f.write(txt)
        f.close
        return

if __name__ == "__main__":
    s = swapper()
    s.run()    
