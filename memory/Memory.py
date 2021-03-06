

class Memory:

    def __init__(self, size):
        self._cells = [None] * size

    def get(self, index):
        return self._cells[index]

    def put(self, position, instruction):
        print("Writing in Memory Position " + str(position) + " : [ " + str(instruction) + " ]")
        self._cells[position] = instruction

    def get_last_index(self):
        return len(self._cells) - 1

    def get_free_space(self):
        return len(filter(lambda x: x is None, self._cells))

    def compact(self):
        used_cells = filter(lambda x: not x is None, self._cells)
        self._cells = used_cells + [None] * (len(self._cells) - len(used_cells))

    def size(self):
        return len(self._cells)