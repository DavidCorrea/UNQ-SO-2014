from memory.Memory import *
from memory.MemoryManager import *
from process.Program import *
from memory.continuousAssignment.CAPolicies import *

class MemoryManagerTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.instruction1 = InstructionIO()
        self.instruction2 = InstructionCPU()
        self.instruction3 = InstructionIO()
        self.instructionList1 = [self.instruction1, self.instruction2]
        self.instructionList2 = [self.instruction1, self.instruction2, self.instruction3]
        self.program1 = Program(self.instructionList1, "Pindongo")
        self.program2 = Program(self.instructionList2, "Pituto")
        self.memory = Memory(1)
        self.memoryManager = MemoryManager(self.memory)
        self.memoryManager.set_as_CA(FirstFit())

    def test_whenTheMemoryManagerAddsTwoProgramsAndIAskForThe6thPosition_thenIShouldGetException(self):
        self.memoryManager.write(self.program1)
        self.memoryManager.write(self.program2)
        self.assertRaises(IndexError, self.memoryManager.read(5))

suite = unittest.TestLoader().loadTestsFromTestCase(MemoryManagerTest)
unittest.TextTestRunner(verbosity=2).run(suite)