__author__ = 'David'

from Page import *
import math


class PageCreator():

    def __init__(self):
        pass

    def create(self, pcb, instructions_per_frame):
        items = range(0, pcb.get_amount_of_instructions())
        divided_items = []
        for i in xrange(0, len(items), instructions_per_frame):
            divided_items.append(items[i:i+instructions_per_frame])
        pages = []
        index = 0
        for list in divided_items:
            pages.append(Page(index,list[0],list[-1],len(list)))
            index += 1
        pcb.get_info_holder().set_pages(pages)
'''
    def create_two(self, pcb, instructions_per_frame):
        pages = []
        pcb_inst = pcb.get_amount_of_instructions()
        size_full_pages = int(math.floor(pcb_inst / instructions_per_frame))
        size_not_full_pages = pcb_inst % instructions_per_frame
        for i in xrange(0, size_full_pages, instructions_per_frame -1):
            pages.append(Page(0, i))
'''
