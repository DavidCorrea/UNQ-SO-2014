__author__ = 'David'


class PCBInfoHolder:

    def __init__(self):
        self._block = None
        self._pages = []

    def set_block(self, block):
        self._block = block

    def set_pages(self, pages):
        self._pages = pages

    def get_block(self):
        return self._block

    def get_pages(self):
        return self._pages

    def has_pages(self):
        return len(self._pages) > 0