__author__ = 'David'
from Frame import *
from Table import *

class Paging:

    def __init__(self, memory, instructions_per_frame):
        self._memory = memory
        self._instructions_per_frame = instructions_per_frame
        self._memory_size = len(self._memory._cells)
        self._frames = []
        self.generate_frames()
        self._table = Table(self._frames)

    def get_amount_of_frames(self):
        return len(self._frames)

    def generate_frames(self):
        can_create = self._memory_size % self._instructions_per_frame == 0
        if can_create:
            index = 0
            for split in xrange(0, self._memory_size, self._instructions_per_frame):
                self._frames.append(Frame(index, split, split + self._instructions_per_frame - 1))
                index += 1

    def assign_to_memory(self, pcb):
        self._table.generate_pages_for_pcb(pcb, self._instructions_per_frame)
        self._table.assign_page_to_frame(pcb)
