from BlockManager import *

class ContinuousAssignment:

    def __init__(self, memory, policy):
        self._memory = memory
        self._memory_last_index = self._memory.get_last_index()
        self._blocks = [Block(0, 0, self._memory_last_index)]
        self._free_blocks = self._blocks
        self._policy = policy
        self._blocks_manager = BlocksManager(self._blocks)

    def create_new_block(self, pcb):
            if self.exists_block_with_space(pcb):
                block_to_use = self._policy.find_block(self._free_blocks, pcb)
                self._blocks_manager.divide_block(pcb, block_to_use)
                pcb.set_block(block_to_use)
                self.update_free_blocks()
            else:
                self._memory.compact()
                self.compact()

    @staticmethod
    def set_block_to_free(pcb):
        pcb.get_block().setFree()

    def exists_block_with_space(self, pcb):
        result = False
        for block in self._blocks:
            if block.isFree() & (block.size() >= pcb.get_amount_of_instructions()):
                result = True
        return result

    def compact(self):
        used_blocks = filter(lambda x: not x.isFree(), self._blocks)
        start_index_free_block = sum(map(lambda x: x.size(), used_blocks)) + 1
        complete_free_block = Block(0, start_index_free_block, self._memory_last_index)
        self._blocks = used_blocks.append(complete_free_block)
        self.update_index()
        self.update_references()
        self.update_ids()

    def update_ids(self):
        [block.set_id(id_block) for (block, id_block) in zip(self._blocks, [0..len(self._blocks)])]

    def update_references(self):
        self._blocks[0].changePreviousBlock(None)
        [sndBlock.changePreviousBlock_double(fstBlock) for (fstBlock, sndBlock) in zip(self._blocks[::1], self._blocks[1::1])]
        self._blocks[-1].changeNextBlock(None)
        [sndBlock.changePreviousBlock_double(fstBlock) for (fstBlock, sndBlock) in zip(self._blocks[::-1], self._blocks[-2::-1])]

    def update_index(self):
        next_index = 0
        for block in self._blocks:
            block.changeStartIndex(next_index)
            next_index = next_index + block.size() - 1
            block.changeEndIndex(next_index)
            next_index += 1

    def update_free_blocks(self):
        result = []
        for block in self._blocks:
            if block.isFree():
                result.append(block)
        self._free_blocks = result