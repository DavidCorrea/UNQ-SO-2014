__author__ = 'David'

from Page import *

class PageCreator():

    def __init__(self):
        pass

    def create(self, pcb, instructions_per_frame):
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
        pcb.get_info_holder().set_pages(pages)