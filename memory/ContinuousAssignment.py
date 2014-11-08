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
                self.update_free_blocks()
            else:
                self.compact()

    # TO DO.
    def set_block_to_free(self, pcb):
        pass
        # pcb.get_assigned_block().setFree();

    def exists_block_with_space(self, pcb):
        result = False
        for block in self._blocks:
            if block.isFree() & (block.size() >= pcb.get_amount_of_instructions()):
                result = True
        return result

    def compact(self):
        return "Not yet implemented"

    def update_free_blocks(self):
        result = []
        for block in self._blocks:
            if block.isFree():
                result.append(block)
        self._free_blocks = result