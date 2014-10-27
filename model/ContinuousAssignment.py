from model.Block import *
from model.OutOfMemory import *

class Continuous_Assignment:

    def __init__(self, memory):
        self._memory = memory
        self._memory_last_index = self._memory.get_last_index()
        self._blocks = [Block(0, 0, self._memory_last_index)]

    def create_new_block(self, program):
        if self.enough_space_for(program):
            if self.exists_block_with_space(program):
                self.new_block_end_index = program.amount_of_instructions() - 1
                self.new_block = Block(0, 0, self.new_block_end_index)
                self.new_block.setUsed()
                self.increase_blocks_ids()
                self._blocks[0].changeStartIndex(self.new_block_end_index + 1)
                self._blocks[0].changePreviousBlock_double(self.new_block)
                self._blocks[0].decrease_size(self.new_block.size())
                self._blocks.insert(0, self.new_block)
            else:
                self.compact()
        else:
            raise OutOfMemory("You don't have free space to load your program in memory.")

    def enough_space_for(self, program):
        return program.amount_of_instructions() < self._memory.get_free_space

    def exists_block_with_space(self, program):
        self.result = False
        for block in self._blocks:
            if block.isFree() & (block.size() >= program.amount_of_instructions()):
                self.result = True
        return self.result

    def increase_blocks_ids(self):
        for block in self._blocks:
            block.increaseId()

    def compact(self):
        return "Implementar"