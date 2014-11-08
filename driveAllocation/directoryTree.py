__author__ = 'robot'
from BlockCreator import *


class Folder:

    def __init__(self, folder_name):
        self._address = '/' + folder_name + '/'
        self._files = []
        self._siblings = []

    def get_name(self):
        return self._address

    def new_file(self, new_file):
        self._files.append(new_file)

    def new_folder(self, folder_name):
        folder = Folder(self._address + folder_name + "/")
        self._siblings.append(folder)

    def get_file(self, file_name):
        filtered = filter(lambda f: f.get_name is file_name, self._files)
        return filtered[0]

    def get_folder(self, folder_name):
        filtered = filter(lambda f: f.get_name is folder_name, self._siblings)
        return filtered[0]

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