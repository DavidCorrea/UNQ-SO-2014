
class MemoryManager:

    def __init__(self, memory):
        self._memory = memory
        self._next_index = 0

    def write(self, program):
        begin = self._next_index
        for i in program.getInstructions():
            # self._memory.put(self._next_index, i.text())
            self._memory.put(i.text())
            self._next_index += 1
        return begin

    def read(self, mem_dir):
        try:
            return self._memory.get(mem_dir)
        except IndexError:
            print "Implementar"