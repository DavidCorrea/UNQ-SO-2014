__author__ = 'David'

import unittest
from memory.CAPolicies import *
from process.PCB import *
from memory.Block import *

class TestCAPolicies(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.pcb = PCB(0, 0, 5)
        self.block1 = Block(0, 0, 3)   # 4  Not enough size.
        self.block2 = Block(1, 4, 11)  # 6  First Fit.
        self.block3 = Block(2, 10, 12) # 3  Just another block with not enough size.
        self.block4 = Block(3, 13, 23) # 11 Worst Fit.
        self.block5 = Block(3, 24, 29) # 6  Another block.
        self.block6 = Block(4, 30, 34) # 5  Best Fit.
        self.blocks = [self.block1, self.block2, self.block3, self.block4, self.block5, self.block6] # This list is a list of Free Blocks.

    def test_whenISetFirstFit_thenIGetTheFirstBlockFoundByThePolicy(self):
        caPolicy = FirstFit()
        self.assertEqual(caPolicy.find_block(self.blocks, self.pcb), self.block2)

    def test_whenISetWorstFit_thenIGetTheFirstBlockFoundByThePolicy(self):
        caPolicy = WorstFit()
        self.assertEqual(caPolicy.find_block(self.blocks, self.pcb), self.block4)

    def test_whenISetBestFit_thenIGetTheFirstBlockFoundByThePolicy(self):
        caPolicy = BestFit()
        self.assertEqual(caPolicy.find_block(self.blocks, self.pcb), self.block6)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCAPolicies)
unittest.TextTestRunner(verbosity=2).run(suite)
