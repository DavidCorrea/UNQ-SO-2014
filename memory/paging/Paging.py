__author__ = 'David'
from Frame import *
from Table import *


class Paging:

    def __init__(self, memory, instructions_per_frame):
        self._memory = memory
        self._memory_size = len(self._memory._cells)
        self._frames = []
        self._free_frames = []
        self.generate_frames(instructions_per_frame)
        self._table = Table()

    def get_amount_of_frames(self):
        return len(self._frames)

    def generate_frames(self, instructions_per_frame):
        can_create = self._memory_size % instructions_per_frame == 0
        if can_create:
            index = 0
            for split in xrange(0, self._memory_size, instructions_per_frame):
                self._frames.append(Frame(index, split, split + instructions_per_frame - 1))
                index += 1

    def assign_to_memory(self, pcb):
        self._table.