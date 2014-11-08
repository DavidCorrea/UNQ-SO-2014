import unittest

from process.PCB import *


class PCBTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.pcb = PCB(0, 3, 3)


    def test_whenIHaveAPCBAndItsIncremented_thenIHaveAPCBWithOneMoreInstructionIndex(self):
        self.pcb.increment()
        self.assertEqual(self.pcb.get_pc(), 4)

    def test_whenIHaveAPCBAndItsPriorityItsChanged_thenItsDifferent(self):
        self.pcb.setPriority(PCBPriorities().getPriorities().LOW)
        self.pcb.increase_priority()
        self.assertEqual(self.pcb._priority, PCBPriorities().getPriorities().MEDIUM)

    def test_whenIHaveAPCBAndItsIncrementedTwice_thenItsFinished(self):
        self.pcb.increment()
        self.pcb.increment()
        self.pcb.increment()
        self.assertTrue(self.pcb.has_finished())

suite = unittest.TestLoader().loadTestsFromTestCase(PCBTest)
unittest.TextTestRunner(verbosity=2).run(suite)
