from driveAllocation.DiskBlock import *

__author__ = 'robot'


class BlockCreator:

    def __init__(self):
        pass

    def convert_into_blocks(self, instructions):
        return map(lambda b: DiskBlock(b), self.split_into_blocks(instructions))

    @staticmethod
    def split_into_blocks(instructions):
        return [instructions[x:x+10] for x in xrange(0, len(instructions), 10)]