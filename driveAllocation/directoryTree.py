__author__ = 'robot'
from BlockCreator import *


class Folder:

    def __init__(self, parent, folder_name):
        self._absolute_address = self.set_absolute_address(parent, folder_name)
        self._relative_address = folder_name
        self._files = []
        self._siblings = []

    def set_absolute_address(self, parent, folder_name):
        if parent != None:
            return parent.get_absolute_address() + "/" + folder_name
        # Root case.
        else:
            return folder_name

    def get_absolute_address(self):
        return self._absolute_address

    def get_relative_address(self):
        return self._relative_address

    def new_file(self, new_file):
        self._files.append(new_file)

    def new_folder(self, folder_name):
        folder = Folder(self, folder_name)
        self._siblings.append(folder)

    def get_file(self, file_name):
        return filter(lambda f: f.get_name() == file_name, self._files)[0]

    def get_folder(self, folder_name):
        return (filter(lambda f: f.get_relative_address() == folder_name, self._siblings))[0]

    def get_files(self):
        return self._files

    def get_folders(self):
        return self._siblings


class File:

    def __init__(self, name, instructions):
        self._name = name
        self._blockCreator = BlockCreator()
        self._diskBlocks = self._blockCreator.convert_into_blocks(instructions)

    def get_name(self):
        return self._name

    def get_disk_block_size(self):
        return len(self._diskBlocks)

    def get_disk_block(self, index):
        try:
            return self._diskBlocks[index]
        except IndexError:
            print("Lo siento, no tengo ese bloque")