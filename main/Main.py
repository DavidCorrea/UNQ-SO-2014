__author__ = 'David'

from driveAllocation.HDD import HDD
from process.Program import Program
from model.Kernel import Kernel
from scheduling.Scheduler import PriorityScheduler
from scheduling.Scheduler import RoundRobinScheduler
from memory.continuousAssignment.ContinuousAssignment import ContinuousAssignment
from memory.paging.Paging import Paging
from memory.continuousAssignment.CAPolicies import BestFit
from memory.MemoryManager import MemoryManager


class Main:

    def __init__(self):

        self.program1 = Program(range(0,10), "Word")
        self.program2 = Program(range(0,50), "Excel")
        self.program3 = Program(range(0,20), "Powerpoint")

        self.hdd = HDD(50)

        self.file_system = self.hdd.generate_file_system()
        self.file_system.add_file("Word", self.program1)
        self.file_system.add_file("Excel", self.program1)
        self.file_system.add_file("Powerpoint", self.program1)

        self.hdd.serialize_file_system(self.file_system)

        self.memory_manager = MemoryManager(self.hdd)

    def run_example_1(self):
        self.scheduler_policy = PriorityScheduler()
        self.continuous_assignment_policy = BestFit()
        self.memory_policy = ContinuousAssignment(self.memory_manager.get_memory(), self.continuous_assignment_policy)
        self.kernel = Kernel(self.scheduler_policy, self.hdd, self.memory_policy)
        self.kernel.run("Word")
        self.kernel.run("Excel")
        self.kernel.run("Powerpoint")

    def run_example_2(self):
        self.scheduler_policy = RoundRobinScheduler(3)
        self.memory_policy = Paging(self.memory_manager.get_memory(), 2, self.hdd)
        self.kernel = Kernel(self.scheduler_policy, self.hdd, self.memory_policy)
        self.kernel.run("Word")
        self.kernel.run("Excel")
        self.kernel.run("Powerpoint")

if __name__ == '__main__':
    Main().run_example_2()
