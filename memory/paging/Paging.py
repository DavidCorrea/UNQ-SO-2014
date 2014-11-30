__author__ = 'David'
from Frame import *
from PageCreator import *
from FrameManager import *


class Paging:

    def __init__(self, memory, instructions_per_frame):
        self._memory = memory
        self._instructions_per_frame = instructions_per_frame
        self._memory_size = len(self._memory._cells)
        self._frames = []
        self.generate_frames()
        self._frame_manager = FrameManager(self._frames)
        self._page_creator = PageCreator()

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
        if not pcb.get_info_holder().has_pages():
            self._page_creator.create(pcb, self._instructions_per_frame)
        policy_result = self._frame_manager.assign_page_to_frame(pcb)
        return policy_result

    def get_amount_of_free_frames(self):
        return len(filter(lambda f: not f.is_in_use(), self._frames))