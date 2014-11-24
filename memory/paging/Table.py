__author__ = 'David'

from Page import *

class Table():

    # Some methods here should be moved to another class: "PageAssignment" or something like that

    def __init__(self, frames):
        self._frames = frames
        self._free_frames = self.update_free_frames()
        self._pages = {}
        self._page_frame = {}

    def update_free_frames(self):
        return filter(lambda frame : frame.is_in_use(), self._frames)

    def generate_pages_for_pcb(self, pcb, instructions_per_frame):
        # I'M PRETTY SURE THIS CAN BE DONE WAY BETTER!
        items = range(0, pcb.get_amount_of_instructions())
        divided_items = []
        for i in xrange(0, len(items), instructions_per_frame):
            divided_items.append(items[i:i+instructions_per_frame])
        pages = []
        index = 0
        for list in divided_items:
            pages.append(Page(index,list[0],list[-1],len(list)))
            index += 1
        self._pages[pcb] = pages

    def remove_pcb(self, pcb):
        del self._pages[pcb]

    def assign_page_to_frame(self, pcb):
        # Check this, please.
        pcb_pages = self._pages.get(pcb)
        page_to_assign = filter(lambda page : page.has_been_used(), pcb_pages)[0]
        if self.table_has_free_frame():
            frame_to_use = self._free_frames[0]
            frame_to_use.set_page(page_to_assign)
            self._page_frame[frame_to_use] = page_to_assign # Necessary?
            self.update_frames_life(frame_to_use)
        else:
            self.empty_oldest_frame()
            self.assign_page_to_frame(pcb)

    def table_has_free_frame(self):
        return len(self._free_frames) > 0

    def update_frames_life(self, frame):
        frames_to_update = filter(lambda x : not x is frame, self._frames)
        frame.reset_life()
        for frm in frames_to_update:
            frm.increase_life()

    def empty_oldest_frame(self):
        oldest_frame = max(self._frames, key=lambda x : x.get_life())
        oldest_frame.set_not_in_use()


