from HDD import HDD
__author__ = 'robot'


class Navigator:

    def __init__(self, sector, block_numbers):
        self._sector = sector
        self._block_numbers = block_numbers
        self._hdd = HDD(10)

    def get_sector(self):
        return self._sector

    def get_block_number(self):
        return self._block_numbers

    def fetch_blocks(self):
        return self._hdd.get_blocks(self)