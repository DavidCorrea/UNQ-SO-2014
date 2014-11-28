from json import *
import json
from FileSystemComponents import *
from FileSystem import FileSystem
from DriveSaver import DriveSaver


class HDD:

    def __init__(self, amount_sector):
        self._drive_saver = DriveSaver(self)
        self._sectors = {}
        self._files = []
        self._representation = json.dumps(Folder(None, "/"))
        for n in range(1, amount_sector):
            self._sectors[n] = []

    def get_blocks(self, token):
        return [map(lambda x: self.sectors[token.get_sector][x], token.get_blocks())]

    def add_block(self, sector, block):
        disk_sector = self.sectors[sector]
        disk_sector.append(block)
        return len(disk_sector)

    def sectors_size(self):
        return len(self.sectors.keys())

    def generate_file_system(self):
        return FileSystem(JSONDecoder(object_hook= Folder).decode(self._representation))

    def serialize_file_system(self, root_folder):
        self._representation = json.dumps(root_folder)