import jsonpickle
from FileSystemComponents import *
from FileSystem import FileSystem
from driveAllocation.DriveSaver import DriveSaver


class HDD:

    def __init__(self, amount_sector):
        self._drive_saver = DriveSaver(self)
        self._sectors = dict.fromkeys(range(1, amount_sector), [])
        self._files = []
        self._representation = jsonpickle.encode(FileSystem(self._drive_saver, Folder(None, "/")))

    def get_drive_saver(self):
        return self._drive_saver

    def get_blocks(self, token):
        return [map(lambda x: self._sectors[token.get_sector][x], token.get_blocks())]

    def add_block(self, sector, block):
        self._sectors.get(unicode(sector)).append(block)
        return len(self._sectors[unicode(sector)])

    def sectors_size(self):
        return len(self._sectors.keys())

    def generate_file_system(self):
        return jsonpickle.decode(self._representation)

    def serialize_file_system(self, file_system):
        self._representation = jsonpickle.encode(file_system)
