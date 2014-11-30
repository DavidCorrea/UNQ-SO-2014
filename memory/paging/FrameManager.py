__author__ = 'David'
from Table import *


class FrameManager():

    def __init__(self, frames):
        self._frames = frames
        self._free_frames = frames
        self._table = Table()

    def update_free_frames(self):
        self._free_frames = filter(lambda frame: not frame.is_in_use(), self._frames)

    def assign_page_to_frame(self, pcb):
        pcb_pages = pcb.get_info_holder().get_pages()
        page = next(iter(filter(lambda p: not p.has_been_used(), pcb_pages)))
        policy_result = self.assign(page)
        self.update_free_frames()
        return policy_result

    def free_frame_available(self):
        return len(self._free_frames) > 0

    def empty_youngest_frame(self):
        youngest = min(self._frames, key=lambda x: x.get_life())
        # We should get the Page here and save it into the Swap Disk.
        # HDD.get_swap_disk().save(youngest.get_page())
        youngest.set_not_in_use()

    def assign(self, page):
        if self.free_frame_available():
            policy_result = self._table.put_page(page, self._frames, self._free_frames)
            return policy_result
        else:
            self.empty_youngest_frame()
            self.update_free_frames()
            self.assign(page)

    def get_frames(self):
        return self._frames