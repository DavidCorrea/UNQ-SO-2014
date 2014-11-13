

class HDD:

    sectors = None

    def __init__(self, amount_sectors):
        if self.sectors is None:
            self.sectors = {}
            for n in range(1, amount_sectors):
                self.sectors[n] = []

    def get_blocks(self, token):
        return [map(lambda x: self.sectors[token.get_sector][x], token.get_blocks())]

    def add_block(self, sector, block):
        disk_sector = self.sectors[sector]
        disk_sector.append(block)
        return len(disk_sector)

    def sectors_size(self):
        return len(self.sectors.keys())