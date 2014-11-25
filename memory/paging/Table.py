__author__ = 'David'

from Page import *

class Table():

    # Some methods here should be moved to another class: "PageAssignment" or something like that

    def __init__(self, frames):
        self._page_frame = dict(zip(frames, [None] * len(frames)))

    def put_page(self, page):
        frame_to_use = filter(lambda x: not x.in_use(), self._page_frame.keys())[0]
        self.update_frames_life(frame_to_use)
        self._page_frame[frame_to_use] = page

    def update_frames_life(self, frame):
        frames_to_update = filter(lambda x : not x is frame, self._page_frame.keys())
        frame.reset_life()
        for frm in frames_to_update:
            frm.increase_life()