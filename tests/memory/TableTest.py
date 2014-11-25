__author__ = 'David'

import unittest
from memory.paging.Table import *
from memory.paging.Frame import *

class TableTest(unittest.TestCase):

    # Arrange
    def setUp(self):
        self.frame1 = Frame(0, 0, 9)
        self.frame2 = Frame(1, 10, 19)
        self.frame3 = Frame(2, 20, 29)
        self.frame4 = Frame(3, 30, 39)
        self.frames = [self.frame1, self.frame2, self.frame3, self.frame4]
        self.table = Table(self.frames)

    def test_whenIAskForFreeFramesInARecentlyCreatedTable_thenIGetAllTheFrames(self):
        self.assertEqual(len(self.table.get_free_frames()), 4)

    def test_whenIPutAPage_ThenItSavesAndFramesLifeIsIncreased(self):
        page = Page(0, 0, 9, 10)
        self.table.put_page(page)
        self.assertEqual(self.frame1.get_life(), 0)
        self.assertEqual(self.frame2.get_life(), 1)
        self.assertEqual(self.frame3.get_life(), 1)
        self.assertEqual(self.frame4.get_life(), 1)

    def test_whenIPutTwoPages_ThenTheyAreSavedAndFramesLifeIsIncreased(self):
        page1 = Page(0, 0, 9, 10)
        page2 = Page(0, 0, 9, 10)
        self.table.put_page(page1)
        self.table.put_page(page2)
        self.assertEqual(self.frame1.get_life(), 1)
        self.assertEqual(self.frame2.get_life(), 0)
        self.assertEqual(self.frame3.get_life(), 2)
        self.assertEqual(self.frame4.get_life(), 2)


suite = unittest.TestLoader().loadTestsFromTestCase(TableTest)
unittest.TextTestRunner(verbosity=2).run(suite)