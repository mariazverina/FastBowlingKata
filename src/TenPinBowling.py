'''
Created on Nov 11, 2013

@author: maria
'''
import unittest


class Game(object):
    
    def __init__(self):
        self._rolls = []
        self.frames = [Frame()]
    
    def roll(self, pins):
        self._rolls.append(pins)
        if self.frames[-1].isClosed():
            self.frames.append(Frame())
        self.frames[-1].roll(pins)
        return self

    
    def score(self):
        if sum(self._rolls[-3:-1]) == 10:
            return sum(self._rolls) + self._rolls[-1]
        score = 0
        for frame in self.frames:
            score += frame.rawScore()
        return score

    
    def rollMany(self, rolls):
        for roll in rolls:
            self.roll(roll)


class Frame(object):
    def __init__(self):
        self._isClosed = False
        self._rolls = []
    
    
    def roll(self, pinCount):
        self._rolls.append(pinCount)
        return self

    
    def isClosed(self):
        return self.isStrike() or len(self._rolls) >= 2

    
    def isSpare(self):
        return sum(self._rolls) == 10

    
    def isStrike(self):
        return len(self._rolls) > 0 and self._rolls[0] == 10

    
    def rawScore(self):
        return sum(self._rolls)
    
    
    
    


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
        
    def testSpareAddsNextRoll(self):
        self.game.rollMany([1,9,3])
        self.assertEqual(16, self.game.score())
    
    def testFrameIsClosedAfterTwoRolls(self):
        frame = Frame()
        frame.roll(5).roll(4)
        self.assertTrue(frame.isClosed())
    
    def testNewFrameIsOpen(self):
        frame = Frame()
        self.assertFalse(frame.isClosed())
        
        
    def testFrameStaysOpenIfFirstRollsIsNotTen(self):
        frame = Frame()
        frame.roll(3)
        self.assertFalse(frame.isClosed())

    def testFrameIsSpareIfRollsSumUpTo10(self):
        frame = Frame()
        frame.roll(3).roll(7)
        self.assertTrue(frame.isSpare())

    def testFrameIsNotSpareWhenLessThan10(self):
        frame = Frame()
        frame.roll(3).roll(3)
        self.assertFalse(frame.isSpare())
        
    def testFrameIsAStrikeIfFirstRollsIs10(self):
        frame = Frame()
        frame.roll(10)
        self.assertTrue(frame.isStrike())
        
    def testSpareIsNotStrike(self):
        frame = Frame().roll(4).roll(6)
        self.assertFalse(frame.isStrike())

    def testStrikeFrameIsClosedAfterFirstRoll(self):
        frame = Frame().roll(10)
        self.assertTrue(frame.isClosed())

    def testFrameBaseScoreIsSumOfRolls(self):
        frame = Frame()
        frame.roll(3).roll(2)
        self.assertEqual(5, frame.rawScore())
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFirstRolScoreIsPinCount']
    unittest.main()