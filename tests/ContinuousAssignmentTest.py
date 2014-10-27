import unittest
from model.Memory import *
from model.ContinuousAssignment import *
from model.Program import *

class TestContinuousAssignment(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.instruction1 = InstructionIO()
        self.instruction2 = InstructionIO()
        self.instruction3 = InstructionIO()
        self.instructions1 = [self.instruction1, self.instruction2, self.instruction3]
        self.instructions2 = [self.instruction3, self.instruction2]

        self.program1 = Program(self.instructions1, "Dummy")
        self.program2 = Program(self.instructions2, "Another Dummy")

        self.memory = Memory(5)
        self.policy = Continuous_Assignment(self.memory)
        self.block = Block(0, 0, 4)

    def test_whenICreateThePolicy_thenItHasAnFreeBlock(self):
        self.assertEqual(self.policy._blocks[0].size(), self.block.size())

    def test_whenICheckIfThereIsEnoughSpaceForProgram_thenItReturnsTrue(self):
        self.assertTrue(self.policy.enough_space_for(self.program1))

    def test_whenICheckIfExistsAFreeBlockForProgram_thenItReturnsTrue(self):
        self.assertTrue(self.policy.exists_block_with_space(self.program1))

    def test_whenICreateANewBlockForProgram_thenPolicyHasTwoBlocks(self):
        self.policy.create_new_block(self.program1)
        self.assertEquals(len(self.policy._blocks), 2)

    def test_whenITryToCreateTwoNewBlocksForProgram_thenItFails(self):
        self.policy.create_new_block(self.program1)
        self.policy.create_new_block(self.program1)
        self.assertRaises(OutOfMemory("Error"))

    def test_whenIAddTwoProgramsAndCompleteTheMemory_ThenIHaveTwoBlocks(self):
        self.policy.create_new_block(self.program1)
        self.policy.create_new_block(self.program2)
        #Deberian ser dos bloques y borrar el último que es obsoleto.
        self.assertEquals(len(self.policy._blocks), 3)

suite = unittest.TestLoader().loadTestsFromTestCase(TestContinuousAssignment)
unittest.TextTestRunner(verbosity=2).run(suite)
