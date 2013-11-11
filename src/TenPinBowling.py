'''
Created on Nov 11, 2013

@author: maria
'''
import unittest


class Game(object):
    
    
    def roll(self, pins):
        self.lastScore = pins

    
    def score(self):
        return self.lastScore
    
    
    
    



class Test(unittest.TestCase):


    def testFirstRollScoreIsPinCount(self):
        game = Game()
        game.roll(5)
        self.assertEqual(5, game.score())
        

    def testFirstRollScoreWithDifferentCount(self):
        game = Game()
        game.roll(7)
        self.assertEqual(7, game.score())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFirstRolScoreIsPinCount']
    unittest.main()