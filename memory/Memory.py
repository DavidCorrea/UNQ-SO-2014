
class Memory:

    def __init__(self, size):
        self._cells = [None] * size

    def get(self, index):
        return self._cells[index]

    def put(self, position, instruction):
        # self._cells.insert(index, instruction)
        self._cells.pop(position)
        self._cells.insert(position, instruction)

    def get_last_index(self):
        return len(self._cells) - 1

    def get_free_space(self):
        self.free_space = 0
        for cell in self._cells:
            if cell == None:
             self.free_space += 1
        return self.free_space

    def compact(self):
        used_cells = filter(lambda x: not x is None, self._cells)
        self._cells = used_cells + [None] * (len(self._cells) - len(used_cells))