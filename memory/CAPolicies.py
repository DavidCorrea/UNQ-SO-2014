

class WorstFit:

    def __init__(self):
        self

    def find_block(self, free_blocks):
        return sorted(free_blocks, key=self.getKey())[0]

    def get_key(self, block):
        return block.size()


class BestFit:

    def __init__(self):
        self

    def find_block(self, free_blocks, program):
        blocks = filter((lambda x: x.size() >= program.amount_of_instructions()), free_blocks)
        return sorted(blocks, key=self.getKey(), reverse=True)[0]

    def get_key(self, block):
        return block.size()


class FirstFit:

    def __init__(self):
        self

    def find_block(self, free_blocks, program):
        return next(filter((lambda x: x.size() >= program.amount_of_instructions()), free_blocks), None)
