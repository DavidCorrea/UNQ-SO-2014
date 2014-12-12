from memory.continuousAssignment.ContinuousAssignment import *
from memory.paging.Paging import *
from memory.Memory import *


class MemoryManager:

    def __init__(self):
        self._memory = Memory(2048)
        self._next_index = 0
        self._policy = None
        self._memory_free_space = self._memory.get_free_space()

    def write(self, pcb):
        policy_result = self._policy.assign_to_memory(pcb)
        aux = policy_result.get_start_index()
        instructions = pcb.get_instructions()
        for inst in instructions:
            self._memory.put(aux, inst)
            aux += 1

    def read(self, mem_dir):
        return self._memory.get(mem_dir)

    def can_serve(self,pcb):
        return self._memory_free_space >= pcb.get_amount_of_instructions()

    def set_as_ca(self, ca_policy):
        self._policy = ContinuousAssignment(self._memory, ca_policy)

    def set_as_paging(self, instructions_per_frame):
        self._policy = Paging(self._memory, instructions_per_frame)


