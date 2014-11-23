__author__ = 'David'


class Frame:

    def __init__(self, index, starting_index, ending_index):
        self._index = index
        self._starting_index = starting_index
        self._ending_index = ending_index
        self._in_use = False

    def is_in_use(self):
        return self._in_use

    def set_in_use(self):
        self._in_use = True

    def set_not_in_use(self):
        self._in_use = False