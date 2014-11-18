

class Memory:

    def __init__(self, size):
        self._size = size
        self._cells = dict(zip(range(0, size), [None] * size))
        # self._cells = [None] * size

    def get(self, index):
        return self._cells[index]
        # return self._cells.get(index)

    def put(self, position, instruction):
        self._cells[position] = instruction
        # self._cells.pop(position)
        # self._cells.insert(position, instruction)

    def get_last_index(self):
        return len(self._cells) - 1

    def get_free_space(self):
        return len(filter(lambda (key, value): value is None,self._cells.items()))
        # return len(filter(lambda x: x is None, self._cells))

    def compact(self):
        used_cells = filter(lambda value: not value is None, self._cells.values())
        non_used_cells = filter(lambda value: value is None, self._cells.values())
        compacted_values = used_cells + non_used_cells
        self._cells = dict(zip(range(0, self._size), compacted_values))
        # used_cells = filter(lambda x: not x is None, self._cells)
        # self._cells = used_cells + [None] * (len(self._cells) - len(used_cells))
