__author__ = 'David'

from driveAllocation.HDD import HDD
from process.Program import Program

class Setup:

    def __init__(self):
        self.setup_programs()
        self._hdd = HDD(50)
        self.add_programs_to_filesystem()

    def setup_programs(self):
        self.program1 = Program(range(0,10), "Word")
        self.program2 = Program(range(0,50), "Excel")
        self.program3 = Program(range(0,20), "Powerpoint")

    def add_programs_to_filesystem(self):
        self._file_system = self._hdd.generate_file_system()
        self._file_system.add_file("Word", self.program1)
        self._file_system.add_file("Excel", self.program2)
        self._file_system.add_file("Powerpoint", self.program3)
        self._hdd.serialize_file_system(self._file_system)

    def get_hdd(self):
        return self._hdd

    def get_file_system(self):
        return self._file_system