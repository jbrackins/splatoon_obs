#CHANGE THESE IF YOU WANT THE OUTPUT FILES TO BE LOCATED SOMEWHERE ELSE.

class path:
    def __init__(self):
        self.CURRENT_DIR = "/home/jubear/workspace/splatoon_obs/current/"
        self.MAP_DIR = "/home/jubear/workspace/splatoon_obs/maps/"
        
        self.MAP_A = "a.png"
        self.MAP_B = "b.png"
        self.TXT = "current.txt"

    def test(self):
        print "'current' Directory (output files here):"
        print "\t", self.CURRENT_DIR
        print "'map' Directory (grab files here):"
        print "\t", self.MAP_DIR

        print "Map A filename:"
        print "\t", self.MAP_A

        print "Map A filename:"
        print "\t", self.MAP_B

        print "Current Game Type filename"
        print "\t", self.TXT
if __name__ == "__main__":
    p = path()
    p.test()
