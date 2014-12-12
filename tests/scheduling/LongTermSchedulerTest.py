__author__ = 'robot'
import unittest
from scheduling.LongTermScheduler import LTScheduler
from scheduling.Scheduler import Scheduler
from memory.MemoryManager import MemoryManager
from process.PCB import PCB


class LongTermSchedulerTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.memory = MemoryManager()
        self.STS = Scheduler()
        self.STS.set_as_fifo()
        self.LTS = LTScheduler(self.STS, self.memory)
        self.pcb = PCB(0, 2049, None)
        self.pcb2 = PCB(0, 1, None)

    def test_trying_to_init_process_and_it_pass(self):
        self.LTS.init_process(self.pcb2)
        self.assertEquals(self.LTS.amount_programs_waiting(), 0, "Process SHOULD pass")

    def test_trying_to_init_process_and_it_pass(self):
        self.LTS.init_process(self.pcb)
        self.assertEquals(self.LTS.amount_programs_waiting(), 1, "Process SHOULD NOT pass")

    def releasing_process_from_waiting_queue(self):
        self.LTS.init_pending_process(2049)
        self.assertEquals(self.LTS.amount_programs_waiting(), 0, "Process SHOULD pass")

suite = unittest.TestLoader().loadTestsFromTestCase(LongTermSchedulerTest)
unittest.TextTestRunner(verbosity=2).run(suite)

