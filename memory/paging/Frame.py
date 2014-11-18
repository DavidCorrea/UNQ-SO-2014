__author__ = 'David'

class Frame:

    def __init__(self, index, cells):
        self._index = index
        self._cells = cells
        self._in_use = False

    def get_cells(self):
        return self._cells

    def is_in_use(self):
        return self._in_use

    def set_in_use(self):
        self._in_use = True

    def set_not_in_use(self):
        self._in_use = False