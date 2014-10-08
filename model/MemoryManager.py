
class MemoryManager:

    def __init__(self, memory):
        self._memory = memory
        self._next_index = 0

    def write(self, program):
        begin = self._next_index
        for i in program.getInstructions():
            self._memory.put(self._next_index, i.text())
            self._next_index += 1
        return begin

    def read(self, mem_dir):
        return self._memory.get(mem_dir)
