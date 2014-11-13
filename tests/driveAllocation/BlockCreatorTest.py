__author__ = 'robot'
import unittest
from driveAllocation.DriveSaver import *


class BlockCreatorTest(unittest.TestCase):

    def setUp(self):
        self.instructions = range(0, 30)
        self.otherInstructions = range(0, 25)
        self.blockCreator = BlockCreator()

    def test_creating_a_block_with_a_list_of_30_instructions(self):
        blocks = self.blockCreator.convert_into_blocks(self.instructions)
        self.assertEqual(len(blocks), 3)

    def test_creating_a_block_with_a_list_of_25_instructions(self):
        blocks = self.blockCreator.convert_into_blocks(self.instructions)
        self.assertEqual(len(blocks), 3)

    def test_creating_a_block_with_a_list_of_30_instructions_return_3_lists_of_10(self):
        blocks = self.blockCreator.convert_into_blocks(self.instructions)
        self.assertEqual(sum(map(len, blocks)), 30)

    def test_creating_a_block_with_a_list_of_25_instructions_return_3_lists_of_10_and_1_of_5(self):
        blocks = self.blockCreator.convert_into_blocks(self.otherInstructions)
        self.assertEqual(sum(map(len, blocks)), 25)

suite = unittest.TestLoader().loadTestsFromTestCase(BlockCreatorTest)
unittest.TextTestRunner(verbosity=2).run(suite)