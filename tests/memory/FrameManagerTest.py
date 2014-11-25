__author__ = 'David'

import unittest
from memory.paging.FrameManager import *
from memory.paging.Frame import *
from memory.paging.PageCreator import *
from process.PCB import *

class FrameManagerTest(unittest.TestCase):

    # Arrange
    def setUp(self):
        self.frame1 = Frame(0, 0, 9)
        self.frame2 = Frame(1, 10, 19)
        self.frame3 = Frame(2, 20, 29)
        self.frame4 = Frame(3, 30, 39)
        self.frames = [self.frame1, self.frame2, self.frame3, self.frame4]
        self.frame_manager = FrameManager(self.frames)
        self.page_creator = PageCreator()
        self.pcb = PCB(0, 0, 20)

    def test_whenICreatePagesForPCB_ThenTheInfoHolderHasThemAsItShould(self):
        self.page_creator.create(self.pcb, 5)
        self.frame_manager.assign_page_to_frame(self.pcb)
        # Check Implementation First before Ending Test.

suite = unittest.TestLoader().loadTestsFromTestCase(FrameManagerTest)
unittest.TextTestRunner(verbosity=2).run(suite)