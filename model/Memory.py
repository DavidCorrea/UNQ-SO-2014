
class Memory:

    def __init__(self, size):
        self._cells = [None] * size

    def get(self, index):
        return self._cells[index]

    def put(self, instruction):
        # self._cells.insert(index, instruction)
        self._cells.append(instruction)
