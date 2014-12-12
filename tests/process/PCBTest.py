import unittest
from memory.MemoryManager import MemoryManager
from memory.continuousAssignment.CAPolicies import FirstFit
from process.PCB import *
from driveAllocation.HDD import HDD
from model.Instruction import *
from process.Program import Program

class PCBTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.hdd = HDD(10)
        self.fs = self.hdd.generate_file_system()
        self.instruction1 = InstructionIO()
        self.instruction2 = InstructionCPU()
        self.instructionList1 = [self.instruction1, self.instruction2]
        self.program1 = Program(self.instructionList1, "AProgram")
        self.fs.add_file("AProgram", self.program1)
        self.file1 = self.fs.get_program("AProgram")
        self.pcb = PCB(0, 2, BlockHolder(self.file1))
        self.mm = MemoryManager()
        self.mm.set_as_ca(FirstFit())
        self.mm.write(self.pcb)

    def test_whenIHaveAPCBAndItsIncremented_thenIHaveAPCBWithOneMoreInstructionIndex(self):
        self.pcb.increment()
        self.assertEqual(self.pcb.get_pc(), 3)

    def test_whenIHaveAPCBAndItsPriorityItsChanged_thenItsDifferent(self):
        self.pcb.set_priority(PCBPriorities().getPriorities().LOW)
        self.pcb.increase_priority()
        self.assertEqual(self.pcb._priority, PCBPriorities().getPriorities().MEDIUM)


suite = unittest.TestLoader().loadTestsFromTestCase(PCBTest)
unittest.TextTestRunner(verbosity=2).run(suite)
