import unittest

from memory.Memory import *
from memory.continuousAssignment.CAPolicies import *
from process.PCB import *


class TestContinuousAssignment(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.pcb1 = PCB(0, 0, 4)
        self.caPolicy = FirstFit()
        self.memory = Memory(20)
        self.policy = ContinuousAssignment(self.memory, self.caPolicy)

    def test_whenICreateThePolicy_thenItHasAnFreeBlock(self):
        self.assertEqual(self.policy._blocks[0].size(), 20)

    def test_whenIAddANewPCB_thenItHasTwoBlocks(self):
        self.policy.create_new_block(self.pcb1)
        self.assertEqual(len(self.policy._blocks), 2)

    def test_whenIAddManyPCBs_thenItHasThatManyBlocks(self):
        pcb2 = PCB(1, 3, 5)
        pcb3 = PCB(2, 7, 3)
        pcb4 = PCB(2, 4, 8)
        self.policy.create_new_block(self.pcb1)
        self.policy.create_new_block(pcb2)
        self.policy.create_new_block(pcb3)
        self.policy.create_new_block(pcb4)
        self.assertEqual(len(self.policy._blocks), 4)

    def test_whenINeedToCompact_thenItCompacts(self):
        pcb1 = PCB(0, 0, 4)
        pcb2 = PCB(1, 3, 5)
        pcb3 = PCB(2, 7, 3)
        pcb4 = PCB(2, 4, 8)
        self.policy.create_new_block(pcb1)
        self.policy.create_new_block(pcb2)
        self.policy.create_new_block(pcb3)
        self.policy.create_new_block(pcb4)
        self.policy.set_block_to_free(pcb3)
        self.policy.set_block_to_free(pcb1)
        pcb5 = PCB(3, 9, 6)
        self.policy.create_new_block(pcb5)
        self.assertEqual(len(self.policy._blocks), 4)


suite = unittest.TestLoader().loadTestsFromTestCase(TestContinuousAssignment)
unittest.TextTestRunner(verbosity=2).run(suite)
