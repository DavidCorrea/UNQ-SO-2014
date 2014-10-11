import unittest
from model.Scheduler import *
from model.PCB import *


class TestScheduler(unittest.TestCase):
    # Arrange
    def setUp(self):
        self.pcb1 = PCB(3, 5, 10)
        self.pcb2 = PCB(2, 5, 10)
        self.pcb3 = PCB(1, 5, 10)
        self.scheduler = Scheduler()

    def test_whenISetTheSchedulerPolicyAsFifo_thenIThePCBsAsThePriorityStates(self):
        self.scheduler.set_as_fifo()
        self.scheduler.add(self.pcb1)
        self.scheduler.add(self.pcb2)
        self.scheduler.add(self.pcb3)
        self.assertEquals(self.scheduler.next(), self.pcb1)
        self.assertEquals(self.scheduler.next(), self.pcb2)
        self.assertEquals(self.scheduler.next(), self.pcb3)

    def test_whenISetTheSchedulerPolicyAsPriority_thenIThePCBsAsThePriorityStates(self):
        self.scheduler.set_as_pq()
        self.pcb1.setPriority(PCBPriorities().getPriorities().LOW)
        self.pcb2.setPriority(PCBPriorities().getPriorities().MEDIUM)
        self.pcb3.setPriority(PCBPriorities().getPriorities().HIGH)
        self.scheduler.add(self.pcb1)
        self.scheduler.add(self.pcb2)
        self.scheduler.add(self.pcb3)
        self.assertEquals(self.scheduler.next(), self.pcb3)
        self.assertEquals(self.scheduler.next(), self.pcb2)
        self.assertEquals(self.scheduler.next(), self.pcb1)

    def test_whenISetTheSchedulerPolicyAsRR_thenIThePCBsAsThePriorityStates(self):
        self.scheduler.set_as_rr(5)
        self.scheduler.add(self.pcb1)
        self.scheduler.add(self.pcb2)
        self.scheduler.add(self.pcb3)
        self.assertEquals(self.scheduler.next(), self.pcb1)
        self.assertEquals(self.scheduler.next(), self.pcb2)
        self.assertEquals(self.scheduler.next(), self.pcb3)


suite = unittest.TestLoader().loadTestsFromTestCase(TestScheduler)
unittest.TextTestRunner(verbosity=2).run(suite)