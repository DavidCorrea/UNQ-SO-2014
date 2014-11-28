__author__ = 'David'
from Table import *


class FrameManager():

    def __init__(self, frames):
        self._frames = frames
        self._free_frames = self.update_free_frames()
        self._table = Table(self._frames)

    def update_free_frames(self):
        return filter(lambda frame: not frame.in_use(), self._frames)

    def assign_page_to_frame(self, pcb):
        pcb_pages = pcb.get_info_holder().get_pages()
        for page in filter(lambda p: not p.has_been_used(), pcb_pages):
            self.assign(page)

    def free_frame_available(self):
        return len(self._free_frames) > 0

    def empty_youngest_frame(self):
        youngest = min(self._frames, key=lambda x: x.get_life())
        # We should get the Page here and save it into the Swap Disk.
        # HDD.get_swap_disk().save(youngest.get_page())
        youngest.set_not_in_use()

    def assign(self, page):
        if self.free_frame_available():
            self._table.put_page(page)
        else:
            self.empty_youngest_frame()
            self.assign(page)