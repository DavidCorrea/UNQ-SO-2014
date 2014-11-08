from memory.Block import *
from memory.OutOfMemory import *


class ContinuousAssignment:

    def __init__(self, memory, policy):
        self._memory = memory
        self._memory_last_index = self._memory.get_last_index()
        self._blocks = [Block(0, 0, self._memory_last_index)]
        self._free_blocks = self._blocks
        self._policy = policy

    def create_new_block(self, pcb):
            if self.exists_block_with_space(p):
                block_to_use = self._policy.find_block(self._free_blocks)
                block_to_use.setUsed()
                self._free_blocks.remove(block_to_use)
                new_block_end_index = pcb.amount_of_instructions() - 1
                new_block = Block(0, 0, new_block_end_index)
                self.increase_blocks_ids()
                self._blocks[0].changeStartIndex(self.new_block_end_index + 1)
                self._blocks[0].changePreviousBlock_double(self.new_block)
                self._blocks[0].decrease_size(self.new_block.size())
                self._blocks.insert(0, self.new_block)
                self.update_free_blocks()
            else:
                self.compact()

    ''' ¿Es necesario o alcanza con solo mirar los bloques?'''
    def enough_space_for(self, program):
        return program.amount_of_instructions() < self._memory.get_free_space

    def exists_block_with_space(self, program):
        result = False
        for block in self._blocks:
            if block.isFree() & (block.size() >= program.amount_of_instructions()):
                result = True
        return result

    def increase_blocks_ids(self):
        for block in self._blocks:
            block.increaseId()

    def compact(self):
        return "Not yet implemented"

    def update_free_blocks(self):
        result = []
        for block in self._blocks:
            if block.isFree():
                result.append(block)
        self._free_blocks = result