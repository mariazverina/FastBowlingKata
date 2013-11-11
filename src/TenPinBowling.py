'''
Created on Nov 11, 2013

@author: maria
'''
import unittest


class Game(object):
    
    def __init__(self):
        self.rolls = []
    
    def roll(self, pins):
        self.rolls.append(pins)
        return self

    
    def score(self):
        return sum(self.rolls)

    
    def rollMany(self, rolls):
        for roll in rolls:
            self.roll(roll)


class Test(unittest.TestCase):

    def setUp(self):
        self.game = Game()



    def testFirstRollScoreIsPinCount(self):
        self.game.roll(5)
        self.assertEqual(5, self.game.score())
        

    def testFirstRollScoreWithDifferentCount(self):
        self.game.roll(7)
        self.assertEqual(7, self.game.score())

    def testTwoRollsAddUp(self):
        self.game.roll(7).roll(5)
        self.assertEqual(12, self.game.score())
        
    def testManyRolls(self):
        self.game.rollMany([4] * 10)
        self.assertEqual(40, self.game.score())
        
    def testFiveIncreasingRolls(self):
        self.game.rollMany([1, 2, 3, 4, 5])
        self.assertEqual(15, self.game.score())
        
    def testSpareByItself(self):
        self.game.roll(2).roll(8)
        self.assertEqual(10, self.game.score())
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFirstRolScoreIsPinCount']
    unittest.main()