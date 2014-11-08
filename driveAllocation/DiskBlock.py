__author__ = 'robot'


class DiskBlock:

    def __init__(self, data):
        self._instructions = data

    def __len__(self):
        return len(self._instructions)

    def get_data(self, index):
       return self._instructions[index]