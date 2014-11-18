__author__ = 'David'

import unittest
from memory.Memory import *
from memory.paging.Paging import *

class PagingTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.memory = Memory(50)
        self.policy = Paging(self.memory, 10)

    def test_WhenIWant10PagesInAMemoryOf50Cells_ThenICanMakeThem(self):
        self.assertEqual(self.policy.get_amount_of_frames(), 5)

suite = unittest.TestLoader().loadTestsFromTestCase(PagingTest)
unittest.TextTestRunner(verbosity=2).run(suite)