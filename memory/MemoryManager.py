from memory.continuousAssignment.ContinuousAssignment import *
from memory.paging.Paging import *

class MemoryManager:

    def __init__(self, memory):
        self._memory = memory
        self._next_index = 0
        self._policy = None
        self._memory_free_space = self._memory.get_free_space()

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

    def set_as_CA(self, ca_policy):
        self._policy = ContinuousAssignment(self._memory, ca_policy)

    def set_as_paging(self, instructions_per_frame):
        self._policy = Paging(self._memory, instructions_per_frame)
