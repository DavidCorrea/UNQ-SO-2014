
class Memory:

    def __init__(self):
        self._cells = []

    def get(self, index):
        return self._cells[index]

    def put(self, index, instruction):
        self.cells.insert(instruction, index)