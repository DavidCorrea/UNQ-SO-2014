__author__ = 'David'

from driveAllocation.HDD import HDD
from process.Program import Program
from model.Instruction import InstructionCPU
from model.Instruction import InstructionIO

class Setup:

    def __init__(self):
        self._hdd = HDD(50)
        self._file_system = self._hdd.generate_file_system()
        self.program1 = Program(self.generate_instructions(35, 9), "Word")
        self.program2 = Program(self.generate_instructions(10, 39), "Excel")
        self.program3 = Program(self.generate_instructions(25, 4), "Powerpoint")
        self.add_programs_to_filesystem()

    def add_programs_to_filesystem(self):
        self._file_system.add_file("Word", self.program1)
        self._file_system.add_file("Excel", self.program2)
        self._file_system.add_file("Powerpoint", self.program3)
        self._hdd.serialize_file_system(self._file_system)

    def get_hdd(self):
        return self._hdd

    def get_file_system(self):
        return self._file_system

    def generate_instructions(self, amount_cpu, amount_io):
        cpu = [InstructionCPU()] * amount_cpu
        io = [InstructionIO()] * amount_io
        return cpu + io