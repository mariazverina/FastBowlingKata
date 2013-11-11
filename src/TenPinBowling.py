'''
Created on Nov 11, 2013

@author: maria
'''
import unittest


class Game(object):
    
    def __init__(self):
        self._rolls = []
        self._firstFrame = Frame()
        self._lastFrame = self._firstFrame
    
    def roll(self, pins):
        self._rolls.append(pins)
        self._lastFrame = self._lastFrame.roll(pins)
        return self

    
    def score(self):
        if sum(self._rolls[-3:-1]) == 10:
            return sum(self._rolls) + self._rolls[-1]
        frame = self._firstFrame
        
        return frame.totalScore()

    
    def rollMany(self, rolls):
        for roll in rolls:
            self.roll(roll)


class Frame(object):
    def __init__(self, first=None, second=None):
        self._rolls = []
        self._isClosed = False
        self._next = None
        
        if first != None:
            self.roll(first)
        if second != None:
            self.roll(second)
    
    def roll(self, pinCount):
        if self.isClosed():
            self._next = Frame(pinCount)
            return self._next
        
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

    
    def twoRollScore(self):
        return self.rawScore()

    
    def firstRoll(self):
        return self._rolls[0]

    
    def next(self):
        return self._next

    
    def totalScore(self):
        score = self.rawScore()
        if self.next():
            score += self.next().totalScore()
        return score
    
    
    
    
    
    
    


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
        frame = Frame(5, 4)
        self.assertTrue(frame.isClosed())
    
    def testNewFrameIsOpen(self):
        frame = Frame()
        self.assertFalse(frame.isClosed())
        
        
    def testFrameStaysOpenIfFirstRollsIsNotTen(self):
        frame = Frame()
        frame.roll(3)
        self.assertFalse(frame.isClosed())

    def testFrameIsSpareIfRollsSumUpTo10(self):
        frame = Frame(3, 7)
        self.assertTrue(frame.isSpare())

    def testFrameIsNotSpareWhenLessThan10(self):
        frame = Frame(3, 3)
        self.assertFalse(frame.isSpare())
        
    def testFrameIsAStrikeIfFirstRollsIs10(self):
        frame = Frame()
        frame.roll(10)
        self.assertTrue(frame.isStrike())
        
    def testSpareIsNotStrike(self):
        frame = Frame(4,6)
        self.assertFalse(frame.isStrike())

    def testStrikeFrameIsClosedAfterFirstRoll(self):
        frame = Frame(10)
        self.assertTrue(frame.isClosed())

    def testFrameBaseScoreIsSumOfRolls(self):
        frame = Frame(3, 2)
        self.assertEqual(5, frame.rawScore())
    
    def testNormalFrameCanProvideTwoRollScore(self):
        frame = Frame(3, 5)
        self.assertEquals(8, frame.twoRollScore())
        
    def testNormalFrameCanProvideFirstRoll(self):
        frame = Frame(3, 5)
        self.assertEquals(3, frame.firstRoll())
        
    def testRollOnClosedFrameWillCreateNewFrame(self):
        frame = Frame(3, 5)
        frame.roll(5).roll(2)
        self.assertEquals(7, frame.next().twoRollScore())
    
    def testFrameCanCalculateTotalScore(self):
        frame = Frame(2,3)
        frame.roll(4).roll(5)
        self.assertEquals(14, frame.totalScore())
        
    def testTotalScoreForSimpleFrame(self):
        frame = Frame(2,3)
        self.assertEquals(5, frame.totalScore())
    
    def testThreeFrameTotalScore(self):
        frame = Frame(3, 5)
        frame.roll(1).roll(2).roll(3).roll(4)
        self.assertEquals(18, frame.totalScore())
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFirstRolScoreIsPinCount']
    unittest.main()