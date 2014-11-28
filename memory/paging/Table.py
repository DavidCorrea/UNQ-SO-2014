__author__ = 'David'

from Page import *


class Table():

    def __init__(self, frames):
        self._page_frame = frames
        self._free_frames = self.update_free_frames()

    def update_free_frames(self):
        return filter(lambda frame: not frame.in_use(), self._page_frame)

    def put_page(self, page):
        frame_to_use = next(filter(lambda x: not x.in_use(), self._page_frame))
        self.update_frames_life(frame_to_use)
        frame_to_use.set_page(page)

    def update_frames_life(self, frame):
        frames_to_update = filter(lambda x: x is not frame, self._page_frame)
        frame.reset_life()
        for frm in frames_to_update:
            frm.increase_life()

    def get_free_frames(self):
        return self._free_frames

    def get_frames(self):
        return self._page_frame