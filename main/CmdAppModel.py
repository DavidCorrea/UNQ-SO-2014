__author__ = 'David'

from CustomLogger import Logger
from model.Kernel import Kernel
from process.Program import Program

class CmdAppModel:

    def __init__(self):
        self.setup_programs()
        self._kernel = Kernel()
        self.add_programs_to_filesystem()
        Logger.ok("App ready to use. \n")

    def set_scheduler_policy(self, policy):
        self._scheduler_policy = policy

    def set_memory_policy(self, policy):
        self._memory_policy = policy

    def set_continuous_assignment_policy(self, policy):
        self._continuous_assignment_policy = policy

    def get_scheduler_policy(self, policy):
        return self._scheduler_policy

    def get_memory_policy(self, policy):
        return self._memory_policy

    def get_continuous_assignment_policy(self, policy):
        return self._continuous_assignment_policy

    def get_kernel(self):
        return self._kernel

    def run(self, program_name):
        self._kernel.run(program_name)

    def setup_programs(self):
        self._program1 = Program(range(0,150), "Word")
        self._program2 = Program(range(0,200), "Excel")
        self._program3 = Program(range(0,320), "Powerpoint")

    def add_programs_to_filesystem(self):
        self._kernel.get_file_system().add_file("Word", self._program1)
        self._kernel.get_file_system().add_file("Excel", self._program2)
        self._kernel.get_file_system().add_file("Powerpoint", self._program3)
        self._kernel.get_hdd().serialize_file_system(self._kernel.get_file_system())

    def start(self):
        self._kernel.start()