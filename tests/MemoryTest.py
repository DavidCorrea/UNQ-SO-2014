import unittest

from memory.Memory import *
from model.Instruction import *


class MemoryTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.memory = Memory(5)
        self.instruction1 = InstructionCPU()
        self.instruction2 = InstructionCPU()
        self.instruction3 = InstructionCPU()

    def test_whenTheMemoryAddsAnInstructionAndIAskForIt_thenIGetIt(self):
        self.memory.put(0, self.instruction1)
        self.memory.put(1, self.instruction2)
        self.memory.put(2, self.instruction3)
        self.assertEqual(self.memory.get(0), self.instruction1)
        self.assertEqual(self.memory.get(1), self.instruction2)
        self.assertEqual(self.memory.get(2), self.instruction3)

    def test_whenISetThreeInstructions_thenIGetTwoFreeSpaces(self):
        self.memory.put(0, self.instruction1)
        self.memory.put(1, self.instruction2)
        self.memory.put(2, self.instruction3)
        self.assertEqual(self.memory.get_free_space(), 2)

suite = unittest.TestLoader().loadTestsFromTestCase(MemoryTest)
unittest.TextTestRunner(verbosity=2).run(suite)