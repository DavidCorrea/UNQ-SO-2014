__author__ = 'David'
from Frame import *

class Paging:

    def __init__(self, memory, instructions_per_frame):
        self._memory = memory
        self._memory_size = len(self._memory._cells)
        self._frames = []
        self._free_frames = []
        self.generate_frames(instructions_per_frame)

    def get_amount_of_frames(self):
        return len(self._frames) # Done this way to make sure there are pages created.

    def generate_frames(self, instructions_per_frame):
        can_create = self._memory_size % instructions_per_frame == 0
        if can_create:
            index = 0
            for split in xrange(0, len(self._memory._cells), instructions_per_frame):
                self._frames.append(Frame(index, self._memory._cells.keys()[split:split+instructions_per_frame]))
                index += 1