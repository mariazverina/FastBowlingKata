'''
Created on Nov 11, 2013

@author: maria
'''
import unittest


class Game(object):
    
    
    def roll(self, pins):
        return pins

    
    def score(self):
        return 5
    
    
    
    



class Test(unittest.TestCase):


    def testFirstRolScoreIsPinCount(self):
        game = Game()
        game.roll(5)
        self.assertEqual(5, game.score())
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFirstRolScoreIsPinCount']
    unittest.main()