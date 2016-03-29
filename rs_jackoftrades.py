import math
 
class RSExp:
    def equate(self, xp):
        return math.floor(xp + 300 * (2 ** (xp / 7.0)))
 
    def level_to_xp(self, level):
        return math.floor(
            sum((self.equate(lvl) for lvl in xrange(1, level))) / 4)
 
    def xp_to_level(self, xp):
        level = 1
 
        while self.level_to_xp(level) < xp:
            level += 1
 
        return level
rs = RSExp()
 
#for level in xrange(1, 100):
#    print('level %d: %d xp' % (level, rs.level_to_xp(level)))

currentLevel = 82
currentExp = rs.level_to_xp(currentLevel)
count = 0


while currentLevel < 99:
    currentExp = currentExp + (3/2)*(currentLevel*currentLevel - 2*currentLevel + 100)
    count = count + 1
    if currentExp > rs.level_to_xp(currentLevel+1):
        currentLevel = currentLevel + 1
        print "Level " + str(currentLevel) + " after " + str(count) + " globes."
print "Total: " + str(count)