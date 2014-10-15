import unittest
from model.Memory import *
from model.Instruction import *

class MemoryTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.memory = Memory()
        self.instruction1 = InstructionCPU()
        self.instruction2 = InstructionCPU()
        self.instruction3 = InstructionCPU()

    def test_whenTheMemoryAddsAnInstructionAndIAskForIt_thenIGetIt(self):
        self.memory.put(self.instruction1)
        self.memory.put(self.instruction2)
        self.memory.put(self.instruction3)
        self.assertEqual(self.memory.get(0), self.instruction1)
        self.assertEqual(self.memory.get(1), self.instruction2)
        self.assertEqual(self.memory.get(2), self.instruction3)

suite = unittest.TestLoader().loadTestsFromTestCase(MemoryTest)
unittest.TextTestRunner(verbosity=2).run(suite)